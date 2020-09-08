#Kizar Cassiere 889991428
#Michael Housworth 88684313


from socket import *

# Server's host address and port
HOST = 'localhost'
PORT = 2020

# Receive buffer
RECVBUFF = 1024

if __name__ == '__main__':
    # Create socket object
    serverSocket = socket(AF_INET, SOCK_STREAM)
    
    # Binds the serverSocket to the port and address
    serverSocket.bind((HOST, PORT))

    # The server socket will listen to one connection
    serverSocket.listen(1)

    # Accept a connection
    connectionSocket, addr = serverSocket.accept()

    with connectionSocket as conn:
        # Establish the connection
        print('Connected to ', addr)

        try:
            # Receive HTTP request data
            message = conn.recv(RECVBUFF)
            print(message)

            # Echo back message
            conn.sendall(message)

            # filename = message.split()[1]
            # f = open(filename[1:])
            # outputdata = f.read()
            # print (outputdata)

        except ConnectionError:
            conn.close()

