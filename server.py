#Program 2 - server.py
# This implements the server of a simple chat room
# Author:
#
import socket
import sys
import threading

#class to service one client
class serverThread ( threading.Thread ):
    def __init__( self, connection, client_address, handle ): # define a constructor with appropriate parameters
        threading.Thread.__init__( self )
        # initialize other appropriate instance fields
        self.connection = connection
        self.client_address = client_address
        self.handle = handle

    def run( self ):
        # send message to everyone letting them know that we're in the room
        handleWelcome = self.handle + " has joined the chatroom!"
        for host in connections:
            if host != self.connection:
                host.send(handleWelcome.encode())
        while True:
            # read a message from the client
            message = self.connection.recv(1024).decode()
            # if the message is ".":
                # close the connection
                # break
            if message == ".":
                break
            # if the first character is "."
                # remove the first character
            if message[0] == ".":
                message = message[1:]
            # add the user's handle to the front of the message
            # send this message to all other clients
            if message:
                handleMessage = self.handle + ": " + message
                for host in connections:
                    if host != self.connection:
                        host.send(handleMessage.encode())
        # send message to all other clients letting them know this user is leaving the chat room
        handleGoodbye = self.handle + " has left the chatroom!"
        for host in connections:
            if host != self.connection:
                host.send(handleGoodbye.encode())
        # remove this client from any data structures
        connections.remove(self.connection)
        print(self.client_address, " disconnected")
        # close the TCP connection
        self.connection.close()

# main
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# get command line arguments
if len(sys.argv) == 2:
    port = int(sys.argv[1])
else:
    print ("usage: python3 server.py <port>")
    sys.exit()
# Bind the socket to the port
server_address = ('localhost', port)
print ('starting up on {} port {}'.format(server_address[0], server_address[1]))
sock.bind(server_address)
# Listen for incoming connections
sock.listen()
#initialize any data structures
connections = []
while True:
    # Wait for a connection
    print ('waiting for a connection')
    connection, client_address = sock.accept()
    print(client_address, " has connected")
    # read the first message from the client, which will be the user's handle
    handle = connection.recv(1024).decode()
    # add this client to any data structures
    connections.append(connection)
    # create a thread to handle this client and start that thread
    thread = serverThread(connection, client_address, handle) # You'll have to pass whatever parameters you defined in your constructor
    thread.start()

