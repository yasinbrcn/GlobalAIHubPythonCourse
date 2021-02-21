'''
                    ** HOMEWORK-1 **
Question:  Generating a 3x3 matrix with 9 random prime numbers.
            (You have to do it using the for loop.)

Coded By:  Yasin BİRCAN
Date:      20.02.2021
'''
 
import random
list1 =[]
for pv in range(2,100):
    for j in range(2, pv):
        if (pv % j) == 0:
            break
    else:
        list1.append(pv)
for k in range(9):
    pvx = random.choice(list1)
    if(k==0):
        v1 = pvx
    elif (k==1):
        v2 = pvx
    elif (k==2):
        v3 = pvx
    elif (k==3):
        v4 = pvx
    elif (k==4):
        v5 = pvx
    elif (k==5):
        v6 = pvx
    elif (k==6):
        v7 = pvx
    elif (k==7):
        v8 = pvx
    elif (k==8):
        v9 = pvx 
 
print("",v1,v2,v3,'\n',
      v4,v5,v6,'\n',
      v7,v8,v9)
