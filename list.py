odd = []
even = []
numbers = 0

def addElements():
	numbers = int(input("Enter how many numbers are to be added to the list: "))
	for i in range(0, numbers):
		if i % 2 == 0:
			even.append(i)
		
		else:
			odd.append(i)
	
	print(odd)
	print(even)
	
def mergeLists():
	if odd == [] or even == []:
		print("The list(s) are empty! Add elements before performing any operation.")
		
	else:
		odd.extend(even)

def sortList():
	if odd == [] or even == []:
		print("The list(s) are empty! Add elements before performing any operation.")
	
	else:
		odd.sort()

def findMinMax():
	if odd == [] or even == []:
		print("The list(s) are empty! Add elements before performing any operation.")
			
	else:
		print("The number with highest value is: ", odd[numbers - 1])
		print("The number with lowest value is: ",  odd[0])
	
def displayList():
	print("The list is: ", end = '')
	print(odd)
	
def mainMenu():
	print()
	print("===MAIN MENU===")
	print("1. Add elements to the list.")
	print("2. Merge the lists.")
	print("3. Sort the list.")
	print("4. Find the minimum and maximum number from the list.")
	print("5. Display the list.")
	print("6. Exit")
	
	while 1:
		print()
		print("Enter your option: ", end = '')
		option = int(input())
		
		if option == 1:
			addElements()
		elif option == 2:
			mergeLists()
		elif option == 3:
			sortList()
		elif option == 4:
			findMinMax()
		elif option == 5:
			displayList()
		else:
			break

mainMenu()
