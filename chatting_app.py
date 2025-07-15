import socket
import threading


def receive(sock):
    while True:
        try:
            data=sock.recv(1024)
            if data:
                print("\nReceived:", data.decode())
        except:
            break

def main():
    print("Choose 'y' if you want others to connect to your IP")
    print("Choose 'n' if you are connecting to someone's IP")
    mode = input("Select (y/n): ").strip().lower()

    if mode == 'y':
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("0.0.0.0", 1337))
        sock.listen(1)
        print("Waiting for connection on port 1337...")
        conn, addr = sock.accept()
        print("Connected by", addr)
        chat_socket=conn
    else:
        ip = input("Enter server IP: ").strip()
        chat_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        chat_socket.connect((ip, 1337))
        print("Connected to server.")

    threading.Thread(target=receive, args=(chat_socket,), daemon=True).start()

    while True:
        msg = input("> ")
        if msg.lower() == "exit":
            break
        chat_socket.send(msg.encode())

    chat_socket.close()

if __name__ == "__main__":
    main()
