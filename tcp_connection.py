import socket

target_host="google.com"
target_port=80

# create TCP connection
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# create conenction 
client.connect((target_host,target_port))

#create send request to target host
client.send(b"GET /HTTP/1.1\r\nHOST:google.com\r\n\r\n")

# collecting data send by target
responce = client.recv(4096)

print(responce)
