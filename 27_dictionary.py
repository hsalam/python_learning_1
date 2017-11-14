#You have a record of  students. Each record contains the student's name, and their percent 
#marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters 
#some integer  followed by the names and marks for  students. You are required to save the 
#record in a dictionary data type. The user then enters a student's name. Output the average 
#percentage marks obtained by that student, correct to two decimal places.
if __name__ == '__main__':
    N = int(raw_input("Enter student count : "))
    percentage = {}
    for i in range(N):
        student = raw_input("Enter student " +str(i+1)+ " name, marks in maths, physics & che (spaces needed) :").strip().split(" ")
        marks = map(float,student[1:])
        percentage[student[0]] = sum(marks)/float(len(marks))
        print percentage
    print "His mark is %.2f"% round(percentage[raw_input("Enter student name :").strip()],2)
    print percentage