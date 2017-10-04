#Claire Yegian
#10/3/17
#warmUp8.py - finds sum of all numbers less than 100,000 that are divisible by 3,10, and 2017

num = 1
total = 0
while num<100000:
    if num%3==0 and num%10==0 and num%17==00:
        total += num
    num += 1
print(total)
