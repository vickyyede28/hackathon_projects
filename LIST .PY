# list = ['king','queen','gulam','1233','23.33']
# print(len(list))


# list1 = ["abc", 34, True, 40, "male"]
# print(type(list1))

# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))

# a = list(('apple','bananan','stawberry'))
# print (type(a))

# a=['23','fish','fruit','mahiya']
# print(a[2:4:-1])

# list = ['human','being','person','man','women','king','ben']
# if 'jhon' in list:
#     print('yes it is present in a list')
# else:
#     print('sorry you are informed wrong')

# thing = ['mango','apple','watermelon']
# thing[0:2]=['banana','cherry','funnel cake','meethi']
# print(thing)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon",'king']      # in len we don't count from 0 count from 1
# print(len(thislist))
# print(thislist)

# to insert in a specific index we use insert
# list = ["apple", "banana", "cherry"]
# list.insert(5,'choco')
# print(list)
# print(len(list))

# thislist = ["apple", "banana", "cherry"]
# thislist.append("orange")
# print(thislist)

#extend add two list 
# list =['apple','baanana','mango','pomogrante','cheeku']
# triple =['basebal','crircket','football']
# triple.extend(list)
# print(triple)
# list.extend(triple)
# print(list)

# list =['apple','baanana','mango','pomogrante','cheeku']
# list.remove('mango')
# print(list)
# list.pop(3)
# print(list)
# it removes the last item of list
# list.pop()      
# print(list)
# del list[0:2]
# print(list)
# del list
# print(list)
# list.clear()
# print(list)


# list =['apple','baanana','mango','pomogrante','cheeku']
# for i in list:
#     print(i,end='')
#     print()

# thislist = ["apple", "banana", "cherry"]
# for i in range(len(thislist)):
#   print(thislist[i])


# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i <len(thislist):
#   print(thislist[i])
#   i = i + 1

# thislist = ["apple", "banana", "cherry"]
# [print(x)for x in thislist]


# fruits = ["apple", "banana", "cherry", "kiwi", "mango",'amdfj','adkf']
# newlist = []

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print(newlist)


# thislist = ["apple", "banana", "cherry",'man','king']
# mylist = thislist.copy()
# print(mylist)

# can copy with help of list also
# thislist = ["apple", "banana", "cherry",'isjih','wdewfw']
# mylist = list(thislist)
# print(mylist)


# list joining types
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list2.append(list1)
# print(list2)

# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]

# list3 = list1 + list2
# print(list3)


# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)


#########################################################################################


# list =[23,43,44,42,7,77,877,74,43,5,64,5]
# count=0
# for i in list:
#     count=count+1
#     print(count)

# list =[23,24,44,42,7,77,87,76,43,5,64,5]
# sum = 0
# for i in list:
#     if i>20 and i<40:
#         print(i)
#         sum = sum + i
# print(sum)

# maximum
# a= [10,12,31,23,45,50]
# max=a[0]
# for i in a:
#     if i>max:
#         max=i
# print(max)


# 2 maximun
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# numbers.sort()
# print(numbers)
# print(numbers[-2])


# reverse order
# state=['goa','mumbai','pune','delhi','banglore']
# a=len(state)
# while a>0:
#     a=a-1
#     # print(state[::-1])
# print(state[::-1])

# palimdrome
# name=[ 'n', 'i', 't', 'i', 'n' ]
# a=['n','i','t','i','n']
# b = (name[::-1])
# if b==a:
#   print('it is palimdrome')
# else :
#     print('it is not a palimdrome')

#REVERSE ORDER 
# state=['goa','mumbai','pune','delhi','banglore']
# for i in range(len(state)):
#     b=len(state)-(i+1)
#     print(state[b])


# we can make list from string
# string= "king,man,ijf,khifj,krfk,khfkj"
# list= string.split(',')
# print(list)

# converting string int into list .
# int='123456789'
# print(list(int))

#DIFFERENCE OF MERAKI
# list1 = [1,2,3,4,5,6]
# list2 = [2,3,1,0,6,7]
# list3=[]
# for i in list1:
#     if i not in list2:
#         list3.append(i)
# print(list3)


#REPOT CARD
# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# a=marks[0]+marks[1]+marks[2]
# sum=0
# for i in a:
#     sum = sum+i
# print(sum)

#question no 2
# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78]
# ]
# a=marks[0]+marks[1]+marks[2]
# sum=0
# for i in a:
#      sum = sum+i
# print(sum)

#question no 3
# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65],
#     [95, 45, 78],
#     [87, 67, 49, 68, 88]
# ]
# a=marks[0]+marks[1]+marks[2]+marks[3]
# sum = 0
# for s in a:
#     sum=sum+s
# print(sum)


# marks = [
#     [78, 76, 94, 86, 88],
#     [91, 71, 98, 65, 76],
#     [95, 45, 78, 52, 49]
# ]
# p= marks
# # b=len(marks[0])
# # a=marks[0]+marks[1]+marks[2]
# # sum=0
# # for i in a:
# #     sum=sum+i
# print(sum/b)
# for i in p:
#     print(sum(i)/len(i))


# iterating list
# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]

# length = len(students) 
# counter = 0
# while counter < length:
#      print ((students[counter]) + str(marks[counter]))
#      counter=counter+1


#kitne aadmi hai
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# count=0
# Counter=0
# for i in elements:
#     if i%2==0:
#         count=count+1
#     else:
#         Counter=Counter+1
# print(count,'even')
# print(Counter,'odd')


# aao jode #lets join the number
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# sum=0
# sum1=0
# for i in elements:
#     if i%2==0:
#         sum=sum+i
#     else:
#         sum1=sum1+i
# print(sum)
# print(sum1)

 

#HOW MUCH IS AVERAGE
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# sum=0
# sum1=0
# counter=0
# counter1=0
# for i in elements:
#     if i%2==0:
#         sum=sum+i
#         counter=counter+1
#     else:
#         sum1=sum1+i
#         counter1=counter1+1
# print(sum/counter,'average score')
# print(sum1/counter1,'average score')





#sab saath mai 
# elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
# sum=0
# sum1=0
# counter=0
# counter1=0
# for i in elements:
#     if i%2==0:
#         sum=sum+i
#         counter=counter+1
#     else:
#         sum1=sum1+i
#         counter1=counter1+1
# print(counter,'even')
# print(counter1,'odd')
# print(sum,'total sum of even no')
# print(sum1,'total sum of odd no')
# print(sum/counter,'average score')
# print(sum1/counter1,'average score')

# HOW MANY CROREPati are there.
# money = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510,4100]
# count=0
# count1=0
# count2=0
# for i in money:
#     if i>=10000000:
#         # print('HE IS A CROREPATI',i)
#         count=count+1
#     elif i>=100000:
#         # print('he is a lakhpati')
#         count1=count1+1
#     else:
#         # print('EVERYONE ARE DIWALIYA')
#         count2=count2+1
# print(count)
# print(count1)
# print(count2)


# list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# him=[]
# for i in list:
#     aasd=[]
#     if i not in him:
#         aasd.append(i)
#         aasd.append(list.count(i))
#     him.append(aasd)
# print(him)


# list=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# him=[]
# for i in list:
#     if i not in him:
#         x=list.count('a')
# x.append([i,x])
# print(x)



# count occurance
# list=["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# him=[]
# count=0
# for s in list:
#     c=list.count(s)
#     count=count+1
#     if [s,c] in him:
#         continue
#     him.append([s,c])
#     print(s,"-",count,"times")
# print(him)



# taking out duplicate
# n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
# a=[]
# b=[]
# for s in n:
#     a.append(s)
#     if s in a:
#         if s in b:
#             continue
#         b.append(s)
# print(b)



question = [
    "How many continents are there?",              
    "What is the capital of India?",           
    "NG mei kaun se course padhaya jaata hai?",
    "WHO WON THE IPL TITLE 2021 "
]
options = [
    #pehle question ke liye options
    [ "a)one","b)three","c)seven","d)hundered"],
    #second question ke liye options
    ["a)Chandigarh", "b)Bhopal", "c)Chennai", "d)Delhi"],
    #third question ke liye options
    ["a)Software Engineering", "b)Counseling", "c)Tourism", "d)Agriculture"],
    # #forth question ke liye option
    ["a)KKR",'b)RCB',"c)CSK","d)DC"]
]
solution = ['c', 'd', 'a', 'c']
for i in range(len(question)):
    print(question[i])
    print(options[i])
    
    a=(input('choose your input -'))
    print('DO YOU WANT TO USE 50 -50')
    if a==solution[i]:
        print('your answer correct')
    else:
        print('your answer is wrong')
        break



