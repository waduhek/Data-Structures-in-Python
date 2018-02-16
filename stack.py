from collections import deque

s = deque()

def stack():
        while 1:
                print()
                print("1. Push onto the stack.")
                print("2. Pop the topmost element from the stack.")
                print("3. Display the stack.")
                print("4. Exit.")
                
                print()
                print("Enter your option: ", end ='')
                option = int(input())
		
                if option == 1:
                        print("Enter the number that has to pushed onto the stack: ", end = '')
                        number = int(input())
                        s.append(number)
		
                elif option == 2:
                        print("The number popped from the stack is: ", s.pop())

                elif option == 3:
                        print("The elements of the stack are: ", end = '')
                        print(s)
		
                else:
                        break

stack()
