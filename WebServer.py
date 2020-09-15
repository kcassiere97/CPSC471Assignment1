#Kizar Cassiere 889991428
#Michael Housworth 88684313
from socket import *
import datetime


# Returns an html response header
def html_header(ct: str = None, cl: int = None):
    tz = datetime.timezone(datetime.timedelta(hours=-7))
    dt = datetime.datetime.now(tz)
    dateStr = "Date:" + dt.strftime("%a, %d. %B %Y %H:%M") + "\r\n"
    serverStr = "Server: PythonSocket/0.1\r\n"
    contentTypeStr = ('Content-Type: ' + ct + '\r\n') if ct else ''
    contentLengthStr = ('Content-Type: ' + str(cl) + '\r\n') if ct else ''

    return dateStr + serverStr + contentTypeStr + contentLengthStr + '\r\n'


# Parses Request message, and sends appropriate Response message
def parse_request(connSock: socket, msg: str):
    # Partition the request line from the message
    request, sep, header = msg.partition('\n')
    # print(request)

    # Partition the command from the request
    cmd, sep, part = request.partition(' ')

    if cmd == 'GET':
        # Partition the object/filepath
        obj, sep, part = part.partition(' ')

        # Attempt to read in the file contents
        fileData = bytes()
        contentType = ''
        contentLength = None
        try:
            filetype = obj.rpartition('.')[2]
            if filetype == 'txt':
                f = open('./FileSystem/' + obj)
                fileData = f.read().encode('utf-8')
                contentType = 'text/plain'
            elif filetype == 'png':
                f = open('./FileSystem/' + obj, 'rb')
                fileData = f.read()
                contentType = 'image/png'
                contentLength = fileData.__len__()
        except IOError:
            connSock.send(b'\nHTTP/1.1 404 Not Found\n\n')

        # Build a response message
        response = 'HTTP/1.1 200 OK\r\n' + html_header(ct=contentType, cl=contentLength)
        # Encode and send response message
        connSock.send(response.encode('utf-8')+fileData)
        print('Response Sent')


def main():

    # Declare server port
    serverPort = 2020
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(('', serverPort))
    serverSocket.listen(1)
    serverSocket.settimeout(3)  # Allows keyboard interrupts to occur
    print('Server running on port: ', serverPort)
    print('Ready to accept')

    while True:
        # Attempt to establish connection
        print('waiting...')
        connectionSocket = socket()
        addr = None

        try:
            try:
                connectionSocket, addr = serverSocket.accept()
            except timeout:
                continue
        except KeyboardInterrupt:
            print('Keyboard Interrupt')
            connectionSocket.close()
            print('Server Socket Closed')
            break

        try:
            # Disable server socket timeout
            serverSocket.settimeout(None)
            print('Accepted Connection')

            # Receive and decode message
            message = connectionSocket.recv(1024)
            decoded = message.decode('utf-8')
            print('Message Received')

            # Pass connection socket and message to parser
            parse_request(connectionSocket, decoded)

            # End connection
            connectionSocket.close()
            print('Closed Connection')

            # Enable server socket timeout
            print('Ready to accept')
            serverSocket.settimeout(3)

        except IOError:
            # If connection fails throw error
            connectionSocket.send(b'HTTP/1.1 404 Not Found\r\n')
        except KeyboardInterrupt:
            connectionSocket.close()
            break
    serverSocket.close()


if __name__ == "__main__":
    main()

