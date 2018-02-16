data = ()
list = []

number = int(input("Enter the number of students: "))
for i in range(0, number):
	name = input("Enter the name of the student: ")
	roll = int(input("Enter the roll number of the student: "))
	sub1 = int(input("Enter the marks in subject 1: "))
	sub2 = int(input("Enter the marks in subject 2: "))
	sub3 = int(input("Enter the marks in subject 3: "))
	data = (name, roll, sub1, sub2, sub3)
	list.append(data)
print(list)
