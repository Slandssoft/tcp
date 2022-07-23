import socket
import binascii
from binascii import unhexlify
print("\n")
print('''
 __ _                 _                __ _   
/ _\ | __ _ _ __   __| |___ ___  ___  / _| |_ 
\ \| |/ _` | '_ \ / _` / __/ __|/ _ \| |_| __|
_\ \ | (_| | | | | (_| \__ \__ \ (_) |  _| |_ 
\__/_|\__,_|_| |_|\__,_|___/___/\___/|_|  \__|
                                              
 ''')
print("Tcp in python by @Antiskamsquad")
conn = socket.socket()
handshake = unhexlify(input("Введите хендшейк: "))
hexes = unhexlify(input("Введите хекс: "))
conn.connect((input("Введите ip: "), 2222))
conn.send(handshake)
conn.recv(100)
while True:
    conn.send(hexes)
    conn.recv(100)
    print("Отправлено")

