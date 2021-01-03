#Fibonacci Search

'''

Prerequistics :
	- Array must be Sorted.

FOR BEST UNDERSTANDING VISIT :
- https://www.geeksforgeeks.org/fibonacci-search/
- Scroll down and understand table.
	
'''


#Fibonacci search
def fibonacci_search(data,search):
	a = 0
	b = 1
	c = 0
	
	#For find fibonacci serie according to length of data.
	while c <= len(data)-1:
		a=b
		b=c
		c = a + b
		
	#Offset value for storing base address to current position
	offset = 0

	#Current value as per index
	i = min(offset+a,len(data)-1)
	
	#Compare for 0th index value
	if data[0] == search:
		return 0
		
	if data[len(data)-1] == search:
		return len(data)-1
		
	#Basically data is sorted so if Search is greater than last data then definitely not found.
	if search > data[len(data)-1]:
		return -1
	if search < data[0]:
		return -1
	
	
	while data[i] != search and c>0:
		if data[i] < search:
			#print("If Confition for lesser")
			c = b
			b = a
			a = c - b
			offset = i
			i = min(offset+a,len(data)-1)
			if a == 0:
				i = min(offset-1,len(data)-1)
			else:
				i = min(offset-a,len(data)-1)
		
		elif data[i] > search:
			#print("We are in else statement")
			c = a
			b = b - a
			a = c - b
			offset = i
			if a == 0:
				i = min(offset-1,len(data)-1)
			else:
				i = min(offset-a,len(data)-1)
		
		else:
			return i
				
	else:
		return i
	
			
		
	#print(f"\n i : { i }")
	#print(f"\n A : { a } B : { b } C : { c } Offset : { offset } i : { i }")
	
	
	
if __name__ == "__main__":
	data = []
	size = int(input("\nHow many elements you want to enter ? : "))
	
	print("\n-----------------INITIALISING--------------------")
	for i in range(size):
		temp = int(input(f"Enter element : { i + 1 } : "))
		data.append(temp)
		
	data.sort()
	
	
	search = int(input("Enter element for search : "))
	print("\n-----------------DATA----------------------")
	print(data)
	print("\n----------------SEARCHED FOR---------------")
	print(search)
	
	print("\n----------------RESULT---------------")
	temp=fibonacci_search(data,search)
	if temp==0:
		print("FOUND At Index  : 0")
	elif temp <0:
		print("OOPS! SERCHED ELEMENT NOT FOUND")
	else:
		print(f"FOUND AT Index : {temp}")
	
		