from collections import deque

q = deque()

def queue():
	print("===MAIN MENU===")
	print("1. Insert elements to the left of the queue.")
	print("2. Insert elements to the right of the queue.")
	print("3. Delete the first element from the left of the queue.")
	print("4. Delete the first element from the right of the queue.")
	print("5. Display the queue.")
	print("6. Exit.")
	
	while 1:
		print()
		print("Enter your option: ", end = '')
		option = int(input())
		
		if option == 1:
			val = int(input("Enter the element to be added: "))
			q.appendleft(val)
		elif option == 2:
			val = int(input("Enter the element to be added: "))
			q.append(val)
		elif option == 3:
			print("The deleted element is: ", q.popleft())
		elif option == 4:
			print("The deleted element is: ", q.pop())
		elif option == 5:
			print("The queue is: ", end = '')
			print(q)
		else:
			break

queue()

