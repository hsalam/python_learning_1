#!/usr/bin/python
n = input("Enter number of medicines : ")
medicine_names = []
prices = []
for i in range(n):
	medicine = raw_input("Enter medicine name %d : " %(i+1))
	medicine_names.insert(i,medicine) 
	price = input("Enter price :")
	prices.insert(i,price)
search_medicine = raw_input("Enter medicine name to be searched :")
for i in range(n):
	if(medicine_names[i]==search_medicine):
		print "Medicine "+medicine_names[i]+" found. \n Its price is, %f" %prices[i]
