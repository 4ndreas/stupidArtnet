from stupidArtnet import StupidArtnet
import time
import random
import socket
import math
import threading, queue

# # THESE ARE MOST LIKEL5 THE VALUES YOU WILL BE NEEDING
target_ip = '10.39.0.29'		# typically in 2.x or 10.x range
universe = 0					# see docs
packet_size = 510				# it is not necessary to send whole universe


numLEDs = 5 * 48
groupdata = bytearray(numLEDs * 3)

# baseColor = [255,200,000] #FFEA00
# highColor = [255,234,000]
baseColor = [173,141,15] #FFEA00
highColor = [255,0,0]


def sendData():
    for i in range(0,16):
        a = StupidArtnet(target_ip, i, 510,0)
        a.set(groupdata[0:510])
        a.show()

        b = StupidArtnet(target_ip, 16+i, 210,0)
        b.set(groupdata[510:510+210])
        b.show()        


# wheel_ip = "192.168.2.82"
inputPort = 50585
iSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
running = True
alive = 0

def inputBegin():
    iSock.bind(('',inputPort)) 

def inputDataLoop(input_queue, stop_event):
    
    iSock.settimeout(1.0)

    while not stop_event.is_set():
        try:
            (data, addr) = iSock.recvfrom(10240)
            strData = data.decode("utf-8")
            input_queue.put(strData)

        except Exception as e:
            # print.error(traceback.format_exc())
            
            if str(e) != "timed out":
                print(e)
            time.sleep(1)

    print("end input thread")


def createData():
    for i in range(0,numLEDs*3,3):
        groupdata[i] = baseColor[0]
        groupdata[i+1] = baseColor[1]
        groupdata[i+2] = baseColor[2]


def animate(phi, perioden):
    periodenLen = (numLEDs / perioden)
    for i in range(0,numLEDs):
        a = math.sin((i/periodenLen) * (2*math.pi) + phi)
        a = max(a,0)

        groupdata[i*3] = min(int(groupdata[i*3] + highColor[0] * a),255)
        groupdata[i*3+1] = min(int(groupdata[i*3+1] + highColor[1]* a),255)
        groupdata[i*3+2] = min(int(groupdata[i*3+2]  + highColor[2] * a) ,255)


def setBlack():
    for i in range(0,numLEDs*3):
        groupdata[i] = 0


def main():
    inputBegin()
    input_queue =  queue.Queue()
    stop_event = threading.Event() 
    iThread = threading.Thread(target=inputDataLoop,args=(input_queue,stop_event))
    iThread.start()

    running = True
    aniSpeed = 0.5
    state = 1
    tick = 0
    phases = 40
    phi = 0.
    try:
        while(running):
            if not input_queue.empty():
                d = input_queue.get()
                print(d)
                target, value = d.split(':')
                print(target)
                print(value)
                if(target == "speed"):
                    aniSpeed = float(value)
                elif(target == "state"):
                    state = int(value)
                elif(target == "phases"):
                    phases = int(value)                    
                elif(target == "baseColor"):  
                    r,g,b = value.split(',')
                    baseColor[0] = int(r)
                    baseColor[1] = int(g)
                    baseColor[2] = int(b)
                elif(target == "highColor"):  
                    r,g,b = value.split(',')
                    highColor[0] = int(r)
                    highColor[1] = int(g)
                    highColor[2] = int(b)

            if(state == 1):
                createData()
                animate(phi,phases)
                phi+=0.1 * aniSpeed
            else:
                setBlack()

            sendData()
                
            time.sleep(1. / 30.)
            tick+=1
            if(tick >=30):
                print('tick')
                tick = 0
             
    except (KeyboardInterrupt, SystemExit):
        running = False
        stop_event.set()
        iThread.join()
        iSock.close()
        setBlack()
        sendData()
        print("finished gracefully")
    except:
        print("Unexpected error")
        running = False
        stop_event.set()
        iThread.join()
        iSock.close()
        raise   
        

if __name__ == "__main__":
  main()