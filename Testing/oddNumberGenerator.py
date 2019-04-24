def getOddNumbers(a) :
	odd_numbers = []
	for i in range(1, a+1) :
		if i % 2 == 1 :
			odd_numbers.append(i)
	return odd_numbers

target = input("Please enter the limit for odd numbers:\n")

print(getOddNumbers(int(target)))
