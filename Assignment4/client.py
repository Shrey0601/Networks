import socket 

serverName = 'localhost'
serverPort =  ("127.0.0.1", 12000)
message  = input("Message to be sent to server: ")
message_bytes = str.encode(message)
bufferSize = 1024

#Establishing contact between client and server
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("The client is ready to send")

#Sending message to the server
clientSocket.sendto(message_bytes, serverPort)

msgFromServer = clientSocket.recvfrom(bufferSize)
msg = "Message from Server: {}".format(msgFromServer[0])

print(msg)

#Close connection
clientSocket.close()