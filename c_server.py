import os
import socket
import threading
s = socket.socket()
PORT = 7002
s.bind(('', PORT))
print('Server is running')
print('Welcome to Your Server!')

s.listen(5)
flag = True
while flag:
    connection, address = s.accept()

    msg="Select a genre \n1.rock \n2.folk \n3.pop"
    connection.send(msg.encode('ascii'))

    #geting user music genre choice 

    choice = connection.recv(1024).decode('ascii')
    print(choice)

    #selecting the adjecent server 

    #rock server = 7004
    #folk server = 7005
    #pop server = 7006 

    s1=socket.socket()

    if(choice == "rock"):
        s1.connect(('localhost',7004))
    elif(choice == "folk"):
        s1.connect(('localhost',7005))
    elif(choice == "pop"):
        s1.connect(('localhost',7006))
    else:
        connection.send("Invalid input".encode("utf-8"))
        connection.close()
    
    list_song=s1.recv(1024).decode("ascii")
    connection.send(list_song.encode("ascii"))

    song_name=connection.recv(1024).decode('ascii')
    s1.send(song_name.encode('ascii'))

    # downloading song to main server 
    
    with open(song_name,'wb')as f:
        data=s1.recv(1024)
    while data:
        f.write(data)
        data=s.recv(1024)
    print("File downloaded to server")
    s1.close()

    #uploading song to client side

    try:
        with open(song_name,'rb') as f:
            data=f.read()
            connection.sendall(data)
    except FileNotFoundError:
        print('File not found')
    
    # removing song from central server (beacause it is no longer needed)

    os.remove(song_name)
    connection.close()
    
connection.close()

        