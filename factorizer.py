import os

while True:
	number = input("Enter a number: ")

	if len(number) == 0:
		quit() # from os
	
	number = int(number)

	if abs(number) <= 1:
		print(str(number) + "\n" + str(number) + "^1\n")
		continue
	
	primeFactorsList = []
	primeFactorsAmountList = []
	allFactorsList = []
	isNegative = False

	if number < 0:
		isNegative = True
		number *= -1

	# get list of all factors
	sqrtNum = int(number**.5)
	divisor = 1

	while divisor <= sqrtNum:
		if number % divisor == 0:
			allFactorsList.append(divisor)
		divisor += 1

	indices = list(range(len(allFactorsList)))
	if sqrtNum == number**.5:
		indices.pop()
	indices = indices[::-1]

	for i in indices:
		allFactorsList.append(int(number/allFactorsList[i]))

	if isNegative:
		print("-1, ", sep='', end='')
	for i in range(len(allFactorsList)-1):
		print(str(allFactorsList[i]) + ", ", sep='', end='')
	print(allFactorsList[-1])

	# get list of all prime factors
	#divisor = 2
	if number % 2 == 0:
		primeFactorsList.append(2)
		primeFactorsAmountList.append(0)
		while (number % 2 == 0) and (number != 1):
			number /= 2
			primeFactorsAmountList[-1] += 1

	divisor = 3
	while number != 1:
		if number % divisor == 0:
			primeFactorsList.append(divisor)
			primeFactorsAmountList.append(0)
			while (number % divisor == 0) and (number != 1):
				number /= divisor
				primeFactorsAmountList[-1] += 1
		divisor += 2

	if isNegative:
		print("-1 * ", sep='', end='')
	for i in range(len(primeFactorsList)-1):
		print(str(primeFactorsList[i]) + "^" + str(primeFactorsAmountList[i]) + " * ", sep='', end='')
	print(str(primeFactorsList[-1]) + "^" + str(primeFactorsAmountList[-1]))

	print()
	