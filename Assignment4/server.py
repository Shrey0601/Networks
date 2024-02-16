import socket

serverPort  = 12000
IP_addr = "127.0.0.1"
message  = "Hello Client"
message_bytes = str.encode(message)
bufferSize = 1024

#Establishing contact between client and server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((IP_addr, serverPort))

#Ready to receive message from the client
print ("The server is ready to receive")

#Server runs for infinite time until the client sends messages
while True:
    message_addr = serverSocket.recvfrom(bufferSize)
    address = message_addr[1]
    message = message_addr[0]
    IP_Client =  "Client IP Address: {}".format(address)
    MSG_Client = "Message from Client: {}".format(message)
    print(MSG_Client)
    print(IP_Client)

    serverSocket.sendto(message_bytes, address)
