#Kizar Cassiere 889991428
#Michael Housworth 88684313
from socket import *


# Checks if messages is just an HTTP header
def is_header(msg: bytes):
    string = msg.decode('utf-8')
    if string.__contains__("HTTP"):
        print("HTTP Header:\n")
        print(string)
        return True


def main():

    # Prepare a client socket
    serverPort = 2020
    clientSocket = socket(AF_INET,SOCK_STREAM)

    # Attempt a file request
    try:
        # Connect to server
        clientSocket.connect(('localhost', serverPort))

        # Send filename
        filename = input('Enter Filename: ')
        clientSocket.send(filename.encode('utf-8'))

        # Deals with request/transfer failures
        clientSocket.settimeout(10)

        # Message handling
        message = bytes()
        while True:
            message = clientSocket.recv(1024)
            if not is_header(message):
                break

        # Creates and writes to file, Downloads folder needs to exist
        f = open('./Downloads/' + filename, 'w')
        f.write(message.decode('utf-8'))

    except IOError:
        print('Failed to connect to server')

    clientSocket.close()


if __name__ == "__main__":
    main()

