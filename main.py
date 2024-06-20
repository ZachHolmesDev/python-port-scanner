import sys
import socket
from datetime import datetime


if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("invalid num of args ")
    print("SYNTAX: python3 main.py")

print('-' *50)
print('Scanning target' + target)
print('time started : ' + str(datetime.now()))
print('-' *50)


try:
    for port in range(50, 85):
        skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = skt.connect_ex(target, port)
        if result == 0:
            print(f'Port {port} is open')
        skt.close

except KeyboardInterrupt:
    print('\nExiting prog')
    sys.exit()

except socket.gaierror:
    print('Host name could not be resolved')
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
    