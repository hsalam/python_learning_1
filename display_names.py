#Read names and display names having letter count greater than 5

#!/usr/bin/python
names = raw_input("Enter names:")
names_split = names.split()
for split in names_split:
	if(len(split)>5):
		print split