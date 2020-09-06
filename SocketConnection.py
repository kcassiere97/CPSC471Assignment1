#Kizar Cassiere 889991428
#Michael Houseworth


from socket import *

def main():
    #Socket module import
    serverSocket = socket(AF_INET, SOCKET_STREAM)
    #Prepare server socket


# fill in start
   #---------------------------------------------------
    #local host
    serverHost = 'localhost'
    
    #recieve buffer
    recvBuffer = 1024

    #declare a server port
    serverPort = 2020
    
    # binds the serverSocket to the port and address
    serverSocket.bind(('', serverPort))

    #the server socket will listen to one connection
    serverSocket.listen(1)
   #---------------------------------------------------
#Fill in end

while True:
    #Establish the connection
    print ('Ready to serve...')
    
    #Fill in start 
    connectionSocket, addr = serverSocket.accept()
    #we have to accept the connection 

    try:
        message = connectionSocket.recv(1024)
        print (message)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        print (outputdata)
        
        
        
        #Fill in start #Fill in end
        #Send one HTTP header line into socket
        #Fill in start
        #Fill in end


        