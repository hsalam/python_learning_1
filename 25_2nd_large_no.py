#!/usr/bin/python
#logic for finding second largest element
if __name__ == '__main__':
    n = int(raw_input("Enter no: of elements :"))
    if(n>=2 and n<=10):
        arr = map(int, raw_input("Enter numbers with spaces between them :").split())
        biggest = -100
        second_biggest = -100
        for i in xrange(0,n): 
            if arr[i] <= 100 and arr[i] >= -100:
                if arr[i]>biggest:
                    second_biggest = biggest
                    biggest = arr[i]
                if arr[i] < biggest and arr[i] > second_biggest:
                    second_biggest = arr[i]
                
        print "Second biggest element is" 
        print second_biggest