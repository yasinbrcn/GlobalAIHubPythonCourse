'''
                                    ** Homework-3 **
Question:   Write two functions.
            The name of the first fuction is prime_first.
            The name of the second function is prime_second.
            You must use these two functions inside the for loop. Ensure that the loop takes values between 0-1000.
            Press the prime numbers between 0-500 on the screen with the prime_first function.
            Press the prime numbers between 500-1000 on the screen with the prime_second function.

Coded By:   Yasin BİRCAN
Date:       20.02.2021
'''
pvlist=[]
primefirstlist=[]
primesecondlist=[]
for i in range(0,1001):
    if (i > 1):
        for j in range(2,i):
            if(i%j)==0:
                break
        else:
            pvlist.append(i)
print(pvlist)

def prime_first():
    for pf in pvlist:
        if (pf>0) & (pf<500):
            primefirstlist.append(pf)
    print("'prime_first' Function Result :" ,primefirstlist)

def prime_second():
    for ps in pvlist:
        if(ps>500) & (ps<1000):
            primesecondlist.append(ps)
    print("'prime_second' Function Result :", primesecondlist)
    
prime_first()
prime_second()


                
