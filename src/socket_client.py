import socket

address = ('127.0.0.1', 5000)

while True:
    try:
        string = input('Send: ')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect(address)
        s.send(string.encode('utf-8'))
        response = s.recv(1024)
        print('Received:', response.decode('utf-8'))
    except Exception as e:
        print(e)
        break
    finally:
        s.close()


