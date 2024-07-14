# Overview 
Category: [General Skills]()

AUTHOR: THEONESTE BYAGUTANGAZA

# Description
Can you make sense of this file?

# Solution
- **Download file**
- **Decode file** 

┌──(kali㉿kali)-[~/Downloads]
└─$ cat enc_flag | base64 --decode
VjFSQ2EyTXlSblJUV0dSVllrWmFWRmx0TlZOalJtUlhZVVU1YVZKVVZuaFdWekZoWVZkR2NrNVVXbUZTVmtwUVdWUkdibVZXVm5WUgpiSEJzWVRCd2VWVXhXbXBOUlRWSFdqTnNWZ3BYUjFKeVZGZHdWMlZzVWxaVmJFNW9UVVJDTlZaWE1XRlVkM0JUVW14V05GWkhjRXRXCk1rWnlUVWhzVjJGdGVFVlhibTkzVDFWT2JsQlVNRXNLCg==

┌──(kali㉿kali)-[~/Downloads]
└─$ cat enc_flag | base64 --decode | base64 --decode
V1RCa2MyRnRTWGRVYkZaVFltNVNjRmRXYUU5aVJUVnhWVzFhYVdGck5UWmFSVkpQWVRGbmVWVnVRbHBsYTBweVUxWmpNRTVHWjNsVgpXR1JyVFdwV2VsUlZVbE5oTURCNVZXMWFUd3BTUmxWNFZHcEtWMkZyTUhsV2FteEVXbm93T1VOblBUMEsK

┌──(kali㉿kali)-[~/Downloads]
└─$ cat enc_flag | base64 --decode | base64 --decode| base64 --decode
WTBkc2FtSXdUbFZTYm5ScFdWaE9iRTVxVW1aaWFrNTZaRVJPYTFneVVuQlpla0pyU1ZjME5GZ3lVWGRrTWpWelRVUlNhMDB5VW1aTwpSRlV4VGpKV2FrMHlWamxEWnowOUNnPT0K

┌──(kali㉿kali)-[~/Downloads]
└─$ cat enc_flag | base64 --decode | base64 --decode| base64 --decode| base64 --decode
Y0dsamIwTlVSbnRpWVhObE5qUmZiak56ZEROa1gyUnBZekJrSVc0NFgyUXdkMjVzTURSa00yUmZORFUxTjJWak0yVjlDZz09Cg==

┌──(kali㉿kali)-[~/Downloads]
└─$ cat enc_flag | base64 --decode | base64 --decode| base64 --decode| base64 --decode| base64 --decode
cGljb0NURntiYXNlNjRfbjNzdDNkX2RpYzBkIW44X2Qwd25sMDRkM2RfNDU1N2VjM2V9Cg==

┌──(kali㉿kali)-[~/Downloads]
└─$ cat enc_flag | base64 --decode | base64 --decode| base64 --decode| base64 --decode| base64 --decode| base64 --decode
>**picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_4557ec3e}**
