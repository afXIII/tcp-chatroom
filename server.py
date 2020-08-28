#Program 2 - server.py
# This implements the server of a simple chat room
# Author:
#
import socket
import sys
import threading

#class to service one client
class serverThread ( threading.Thread ):
    def __init__( self ): # define a constructor with appropriate parameters
        threading.Thread.__init__( self )
        # initialize other appropriate instance fields
               
    def run( self ):
        # send message to everyone letting them know that we're in the room
        
        while True:
            # read a message from the client
            
            # if the message is ".":
                # close the connection
                # break
            # if the first character is "."
                # remove the first character
            # add the user's handle to the front of the message
            # send this message to all other clients
        
        # send message to all other clients letting them know this user is leaving the chat room
            
        # remove this client from any data structures
        
        # close the TCP connection
        

# main
# Create a TCP/IP socket

# get command line arguments

# Bind the socket to the port

# Listen for incoming connections

#initialize any data structures

while True:
    # Wait for a connection
    
    # read the first message from the client, which will be the user's handle
    
    # add this client to any data structures
    
    # create a thread to handle this client and start that thread
    thread = serverThread(  ) # You'll have to pass whatever parameters you defined in your constructor
    thread.start()

