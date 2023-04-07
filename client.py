import socket
import sys
import os
import shutil

s = socket.socket()
HOST = 'localhost'
PORT = 7002
s.connect((HOST, PORT))
msg=s.recv(1024).decode("ascii")
print(msg)

# choosing the genre of song 

sel_song = input('Select ur genre :')
s.send(sel_song.encode('ascii'))

song_list=s.recv(1024).decode("ascii")
print(song_list)

# choosing the song to download at client side 

song_name=input('Enter ur music to download :: ')
s.send(song_name.encode('ascii'))

# reciving the requested song from the central server

with open("client_req/"+song_name,'wb')as f:
    data=s.recv(1024)
while data:
    f.write(data)
    data=s.recv(1024)
print("File downloaded to client")

s.close()