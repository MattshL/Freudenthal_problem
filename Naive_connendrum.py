"""
Let a and b be two integers (between 2 and 50) with a>b.
Two Mathematicians are discussing.
-The first mathematician (M1) only knows the product (a*b)
-The second mathematician (M2) only knows the sum (a+b)
-They have the following dialog :
	(M1) - "I can't find the two numbers a and b with the information I have."
	(M2) - "I already knew that you couldn't"
	(M1) - "Now I know the answer, what a and b are"
	(M2) - "Now I do too !"
"""










a = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

def isprime(x):
	for a in range(2, x/2+1):
		y = x/a
		z = y*a
		if z == x:
			return False
	return True

def check1(x):
	a = range(2,x-1)
	b = range(x-2,1,-1)
	nres = True
	for i,j in zip(a,b):
		primes = isprime(i) and isprime(j)
		nprimes = not(primes)
		nres = nres and nprimes
	return nres


b = []
for x in a:
	if check1(x):
		b += [x]


def getDivisors(x):
	res = []
	for a in range(2, x/2):
		b = x/a
		if a*b==x:
			res+=[[a,b]]
	res2 = [xx for xx in res if xx[0]<=xx[1]]
	return res2


def check2(x, bl):
	divs = getDivisors(x)
	res = 0
	ress = []
	for div in divs:
		sum = div[0] + div[1]
		if sum in bl:
			res += 1
			ress += [[sum, div[0] * div[1], [div[0], div[1]]]]
	return [res, ress]

c = list(dict.fromkeys([x * y for x in range(2,51) for y in range(2,51)]))

d = []
dd = []
for x in c:
	z = check2(x, b)
	if z[0] == 1:
		d += [z[1]]
		dd += [z[1][0]]


ddd = [x[1] for x in dd]


def getTerms(x):
	res = []
	for a in range(2, x/2+1):
		res += [[a, x-a]]
	return res

def check3(x, dddl):
	terms = getTerms(x)
	res = 0
	ress = []
	for term in terms:
		prod = term[0] * term[1]
		if prod in dddl:
			res += 1
			ress += [[prod, term[0] + term[1], [term[0], term[1]]]]
	return [res, ress]

e = []
for x in b:
	z = check3(x, ddd)
	if z[0] == 1:
		e += [z[1][0]]

def printSolution(z):
	for x in z :
		print("Solution :")
		print("\ta*b = " + str(x[0]))
		print("\ta+b = " + str(x[1]))
		print("\t(a,b) = (" + str(x[2][0]) + "," + str(x[2][1]) + ")")

	

def solve(xxx):
	a0 = range(2, xxx+1)
	a = range(4, xxx*2+1)
	b = []
	for x in a:
		if check1(x):
			b += [x]
	c = list(dict.fromkeys([x * y for x in a0 for y in a0]))
	d = []
	dd = []
	for x in c:
		z = check2(x, b)
		if z[0] == 1:
			d += [z[1]]
			dd += [z[1][0]]
	ddd = [x[1] for x in dd]
	e = []
	for x in b:
		z = check3(x, ddd)
		if z[0] == 1:
			e += [z[1][0]]
	printSolution(e)
	return e


solve(50)

