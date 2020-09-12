#Kizar Cassiere 889991428
#Michael Housworth 88684313
from socket import *

def main():

    #declare server port
    serverPort=2020
    serverSocket = socket(AF_INET,SOCK_STREAM)

    #Prepare a server socket
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print('the is running at:',serverPort)

    while True:
        #Establish the connection
        print('Ready to serve')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024)
            print (message, '::',message.split()[0],':',message.split()[1])
            filename = message.split()[1]
            print(filename,'||',filename[1:])
            f = open(filename[1:])
            outputdata = f.read()
            print(outputdata)

            #send HTTP request into socket
            connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
            connectionSocket.send(outputdata)
            connectionSocket.close()

        except IOError:
            #IF connection fails throw error
            connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
    serverSocket.close()

if __name__ == "__main__":
    main()

