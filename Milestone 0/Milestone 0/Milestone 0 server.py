# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 16:21:03 2022

@author: Hoda
"""

import socket

def is_still_connected(sock):
    try:
        sock.sendall(b"\n")
        return True
    except:
        return False

def server_program():
    server_socket = socket.socket()
    # get the hostname
    host = "127.0.0.1"
    port = 2500
    server_socket.bind((host, port))  

    
    while True:
       
        server_socket.listen(2)
        conn, address = server_socket.accept()  # accept new connection
        print("Connection from: " + str(address))
        

        while True:
            try:
                data = conn.recv(1024).decode()
            except:
                break
            data= str(data.upper());
            if(len(data) > 0):
                print("from connected user: " + str(data))
                conn.send(data.encode())  
        print("connection with client closed")
           
        
server_program()     
        














