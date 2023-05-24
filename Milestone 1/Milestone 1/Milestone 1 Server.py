# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 17:18:29 2022

@author: Hoda and Omar
"""

import socket
import threading 

host = "127.0.0.1"
port = 2500
address= (host, port)
disconect_message ='close socket'



def handle_client(conn, address):
    print(f"[NEW CONNECTION] {address} connected.")
    
    
    while True:
        try:
            data = conn.recv(1024).decode()
            
        except:
            break
        data= str(data.upper());
        if(len(data) > 0):
            print("from connected user: " + str(address) + str(data))
            conn.send(data.encode())  
    print("connection with client closed")
       
    
def main ():
    print("[STARTING] Server is starting..")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))  
    server.listen()
    count = 0

    
    while True:
      
        conn, address = server.accept()  
        print("Connection from: " + str(address))
        thread = threading.Thread(target=handle_client, args = (conn, address))
        count = count + 1 
        thread.start()
        #print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} ")
        print (count)
main()
    
if __name__== "main__":
    main()