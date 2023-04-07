import os
import socket
s = socket.socket()
PORT = 7005
s.bind(('', PORT))
print('Server is running')
print('Welcome to Folk Server!')

s.listen(5)

while True:
    connection, address = s.accept()

# getting the name of all songs present in the folk music directory 

    msg="List of the following songs present in this library of rock music \n"

    with os.scandir('./folk_music') as files:
        for file in files:
            msg=msg+str(file.name)+'\n'

 
    connection.send(msg.encode("ascii"))

# reciving the name of the requested song

    song_name=connection.recv(1024).decode('ascii')
    print("Song requested ::")
    print(song_name)
    print('\n')

    # uploading song to main server 
    try:
        with open(song_name,'rb') as f:
            data=f.read()
            connection.sendall(data)
    except FileNotFoundError:
        print('File not found')
    connection.close()

