'''
                                    ** Homework-2 **
Question: Write a program that includes information about the grades of 5 students in a school.
            - Keep these student's grades in a list.
            - Keep student's name in a list.
            - Create a dictionary named info and put all the information of students in a dictionary.
            - Sort and list the student's grades here in descending order and congratulate the student with the highest score.
            
Coded By: Yasin BİRCAN
Date:     20.02.2021
'''
import operator
namelist=[]
totalgradelist=[]
#info = {}
for i in range(5):
    a=i+1
    a=str(a)
    namelist.append(input(a+". Öğrencinin adını ve soyadını yazınız: "))
#print (namelist)
for j in range(5):
    for k in range(3):
        c=k+1
        c=str(c)
        grade = int(input(namelist[j] + " adlı öğrencinin " + c + ". notunu giriniz:"))
        #grade = int(grade)
        totalgradelist.append(grade)
#print(totalgradelist)
grade1 = float((totalgradelist[0]+totalgradelist[1]+totalgradelist[2]) / 3)
grade2 = float((totalgradelist[3]+totalgradelist[4]+totalgradelist[5]) / 3)
grade3 = float((totalgradelist[6]+totalgradelist[7]+totalgradelist[8]) / 3)
grade4 = float((totalgradelist[9]+totalgradelist[10]+totalgradelist[11]) / 3)
grade5 = float((totalgradelist[12]+totalgradelist[13]+totalgradelist[14]) / 3)
avggradelist=[grade1, grade2, grade3, grade4, grade5]
#print(avggradelist)

info = {avggradelist[0] : namelist[0],
        avggradelist[1] : namelist[1],
        avggradelist[2] : namelist[2],
        avggradelist[3] : namelist[3],
        avggradelist[4] : namelist[4],}

sortedvalues=sorted(info.items(),reverse=True,key=operator.itemgetter(0))
sortedinfo = {key: value for (key, value) in sortedvalues}
print(sortedinfo)
avggradelist.sort()
#print(avggradelist[4])
print("Tebrikler! : " + info[avggradelist[4]])

