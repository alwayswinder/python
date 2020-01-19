import random

answer = random.randint(0,100)
guess = -1
times = 0

while guess != answer:
	temp = input("请输入一个数字！\n")
	if temp.isdigit():
		guess = int(temp)
		if guess > answer:
			print("big")
		else:
			if guess < answer:
				print("small")	
		times = times + 1
	else:
		print("你输入的不是数字！")
print('你用了{}次'.format(times))
 
