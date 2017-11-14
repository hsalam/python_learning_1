#!/usr/bin/python
#pgm to enter student names and marks in one subject,
#finding second lowest score and printing corresponding student name(s) in ascending 
n =int(raw_input("Enetr no: of students:"))
if(n>=2 and n<=5):
    list_names = []
    student = [[0 for i in xrange(2)] for j in xrange(n)] 
    for i in xrange(n):
        student[i].insert(0,raw_input("Enter student name :").strip())
        student[i].insert(1,float(raw_input("Enter mark :")))
    small = 100.00
    second_small = 100.00
    for i in xrange(n):
        if(student[i][1]<small):
            second_small = small
            small= student[i][1]
        if(student[i][1]<second_small and student[i][1]>small):
            second_small = student[i][1]
    for i in xrange(n):
        if student[i][1]==second_small:
            list_names.insert(0,student[i][0])
    list_names.sort()
    for i in xrange(len(list_names)):
        print "student "+str(i+1)+" with second lowest score is "+str(list_names[i])