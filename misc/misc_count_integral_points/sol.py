# Python3 program to find Integral
# points inside a triangle
 
# Class to represent an Integral
# point on XY plane.
# nc 14.225.254.58 55555

import socket
from time import sleep

HOST = '14.225.254.58'  
PORT = 55555        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)

class Point:
 
    def __init__(self, x, y):
        self.x = x
        self.y = y
         
# Utility function to find GCD of
# two numbers GCD of a and b
def gcd(a, b):
 
    if (b == 0):
        return a
         
    return gcd(b, a % b)
 
# Finds the no. of Integral points
# between two given points
def getBoundaryCount(p, q):
     
    # Check if line parallel to axes
    if (p.x == q.x):
        return abs(p.y - q.y) - 1
    if (p.y == q.y):
        return abs(p.x - q.x) - 1
 
    return gcd(abs(p.x - q.x),
               abs(p.y - q.y)) - 1
 
# Returns count of points inside the triangle
def getInternalCount(p, q, r):
 
    # 3 extra integer points for the vertices
    BoundaryPoints = (getBoundaryCount(p, q) +
                      getBoundaryCount(p, r) +
                      getBoundaryCount(q, r) + 3)
 
    # Calculate 2*A for the triangle
    doubleArea = abs(p.x * (q.y - r.y) +
                     q.x * (r.y - p.y) +
                     r.x * (p.y - q.y))
 
    # Use Pick's theorem to calculate
    # the no. of Interior points
    return (doubleArea - BoundaryPoints + 2) // 2

def getCount(p, q):
 
    # If line joining p and q is parallel
    # to x axis, then count is difference
    # of y values
    if p.x == q.x:
        return abs(p.y - q.y) - 1
 
    # If line joining p and q is parallel
    # to y axis, then count is difference
    # of x values
    if p.y == q.y:
        return abs(p.x - q.x) - 1
 
    return gcd(abs(p.x - q.x),
               abs(p.y - q.y)) - 1
 
# Driver code
if __name__=="__main__":
    data= s.recv(1024)
    while(1):
        data=s.recv(100)
        if b'chuc mung' in data:
            print(data)
            break
        print(data)
        a = int(data.split(b' ')[0].split(b'=')[1])
        # print(a)
        b= int(data.split(b' ')[1].split(b'=')[1][:-3])
        # print(b)
        p = Point(0, 0)
        q = Point(a, 0)
        r = Point(0, b)
        res1 = getCount(q,r)+a+b+1
        s.send(str(res1).encode())
        s.recv(100)
        res2= getInternalCount(p, q, r)
        s.send(str(res2).encode())
        sleep(3)

    
    s.close()
     
    # print("Number of integral points "
    #       "inside given triangle is ",
    #       getInternalCount(p, q, r))