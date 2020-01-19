
def ShowLoadPercent(percent):
	return('loading {}%'.format(percent))
	
	
def BigNumber(x, temp_list):	
	if temp_list[x] != -1:
		return temp_list[x] 
	else:
		temp_list[x] = BigNumber(x-1, temp_list) + BigNumber(x-2, temp_list)
		return temp_list[x]
	
def fab(x):
	temp_list = [-1] * ( x + 1)
	temp_list[0] = 0
	temp_list[1] = 1
	return BigNumber(x, temp_list)
	
	
def Factorial(x):
	if x == 1:
		return str(x)
	else:
		return str(x) + '*' + Factorial(x-1)
		
def Hanoi(n,x,y,z):
	if n == 1:
		z.append(x.pop())
	else:
		Hanoi(n-1, x,z,y)
		z.append(x.pop())
		Hanoi(n-1, y,x,z)
	
	
	
'''
for i in range(0, 100):
	print(ShowLoadPercent(i +1))

temp = range(10)
odds = list(filter(lambda x : x%2, temp))

test_res = list(map(lambda x : x**2, temp))

for i in test_res:
	#print(ShowLoadPercent(i))
for i in range(10):
	print(BigNumber(i))

'''
x = int(input('璇疯緭鍏ヤ竴涓鏁存暟:'))

listx = list(range(1,x + 1))
listx.reverse()
listy = []
listz = []

Hanoi(x, listx, listy, listz)
print(listz)

