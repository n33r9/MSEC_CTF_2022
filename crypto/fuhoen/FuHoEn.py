
import socketserver
import threading
from Crypto.Util.number import *
import tenseal as ts
import time

context = ts.context(ts.SCHEME_TYPE.BFV, poly_modulus_degree=4096, plain_modulus=1012173232936591361)

def get_decrypted(context, msg):
    now = int(time.time())
    x = [msg]
    enc = ts.bfv_vector(context, x)
    return (enc + now).decrypt()[0]

   
#-----------------------------

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def init(self):
        pass

    def handle(self):
        # self.request.settimeout(30)
        rsend = self.request.sendall
        rclose = self.request.close
        rrecv = self.request.recv

        flag = "***{***}"
        f = ["***", "***", "***"]   #f[0] + f[1] + f[2] = flag
        # congratulations = "".encode()
        for i in range(3):
            flag = f[i].encode()
            # rsend(congratulations)
            rsend(b"Welcome to BrainStorm Challenge " + str(i+1).encode() + b"!\n")
            rsend(b"Please enter your choice:\n")
            rsend(b"1. Test.\n")
            rsend(b"2. Get decrypted result.\n")
            rsend(b"3. Submit flag " + str(i+1).encode())
            rsend(b"\n4. Exit.\n")
            
            while(True):
                x = rrecv(4096).decode().rstrip('\n').rstrip('\r')
                option = int(x)
                if option == 1:
                    try:
                        rsend(b"Enter the message you want to encrypt: ")
                        message = rrecv(4096).decode().rstrip('\n').rstrip('\r').encode()
                    except:
                        rsend(b"Enter proper message")
                        exit(0)
                    message = bytes_to_long(message)
                    result = get_decrypted(context, message)
                    rsend(b"Here take your result: " +str(result).encode() + b"\n\n\n")
                
                elif(option == 2):
                    msg = bytes_to_long(flag)
                    decrypted_result = get_decrypted(context, msg)
                    rsend(b"Here take your decrypted result: " + str(decrypted_result).encode() + b"\n")

                elif(option == 3):
                    submited = rrecv(4096).decode().rstrip('\n').rstrip('\r')
                    if(submited == flag.decode()):
                        congratulations = b"Congratulations! You passed challenge " + str(i+1).encode()
                        break
                elif(option == 4):
                    exit(0) 
                else:
                    rsend("Enter a valid option!\n")
        rsend("Please submit the flag!")
        rclose()


HOST, PORT = 'localhost', 1331
while True:
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:"), server_thread.name
    server_thread.join()
    
    