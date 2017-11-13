#!/usr/bin/python
if __name__ == '__main__':
    list_n = []
    n = int(raw_input())
    for j in xrange(n):
        operation = raw_input().strip().split()
        if(operation[0]=="insert"):  
            list_n.insert(int(operation[1]),int(operation[2]))
        elif(operation[0]=="print"):
            print str(list_n)
        elif(operation[0]=="remove"):
            list_n.remove(int(operation[1]))
        elif(operation[0]=="append"):
            list_n.append(int(operation[1]))
        elif(operation[0]=="sort"):
            list_n.sort()
        elif(operation[0]=="pop"):
            list_n.pop()              
        elif(operation[0]=="reverse"):
            list_n.reverse()    