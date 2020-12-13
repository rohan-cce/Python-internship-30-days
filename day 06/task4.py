num = int(input('Enter a number: '))
num_original=num

def check_armstrong(num):
    sum1 = 0
    num2=num
    cnt=0
    while(num>0):
            cnt=cnt+1
            num=num//10

    while num2>0:
       rem = num2% 10
       sum1 += rem ** cnt
       num2//= 10
    return sum1

sum_1=check_armstrong(num)

if(num_original==sum_1):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')
