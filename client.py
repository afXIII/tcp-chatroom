#Program 2 - client.py
# This implements the client of a simple chat room
# Author:

import socket
import sys
import threading

#class to listen for keyboard input
class keyboardThread ( threading.Thread ):
    def __init__( self, ): # define the constructor with appropriate parameters
        threading.Thread.__init__( self )
        # initilize instance fields
        
    def run( self ):
        while True:
            try:
                # get message from user using input
                
                # if first character is ".", add a second "." to the beginning
               
                # send the message to the server

            except:
                # ^d entered, so exit loop
                break
 
        # send a message consisting of "." to server
        
 #class to listen for chat messages from the server       
class chatThread ( threading.Thread ):
    def __init__( self ): #define the constructor with appropriate parameters
        threading.Thread.__init__( self )
        # initialize instance fields
        
    def run( self ):
        while True:
            # get message from server
            
            # if the message has at least one byte of data, print it out
            
            # else break    

#main
# Create a TCP/IP socket

# get command line arguments

# Connect the socket to the port where the server is listening


# send the user's handle to the server

#start threads to handle the communication
kb = keyboardThread( ) #pass parameters defined in the constructor
kb.start()
chat = chatThread ( ) # pass parameters defined in the constructor
chat.start ()

#wait for the threads to end, which indicates that the user has left the room
kb.join()
chat.join()

# close the TCP connection



