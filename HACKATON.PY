# gussing game:

# import random
# a=random.randint(1,10)
# print(a)
# for i in range(5):
#     if i==4:
#         print("This is your last chance.")
#     b=int(input("Enter your guessed number :"))
#     if a>b:
#         print('This numbers is smaller')
#     elif a<b:
#         print(' This  number is greater')
#     elif a==b:
#         print('CONGULATION! Your guess is correct')
#         break
#     if  i==4 and b!=a:
#         print('Your all chances are over',',''You are out of game')


#############################################################


# rolling dice

# import random
# a=random.randint(1,6)
# print(a)
# b=int(input())
# c=int(input())

# sum2=0
# sum1=0
# for i in range(1,11):
#     a=input("enter your choice  ")
#     if a=='y':
#         import random
#         a=random.randint(1,6)
#         if i%2==0:
#             sum1=sum1+a
#             print(a)
#         else:
#             sum2=sum2+i
#             print(a)
#     else:
#         break
# print(sum1)
# print(sum2)
# if sum1<sum2:
#     print(sum2,'this is winner')
# else:
#     print(sum1,'this is winner')



######################################################3

# ADVENTURE GAME

# print("All deserts are dry.Dryness is a part of there Defination. but while all deserts mat be dry,they are not equally dry.")
# print("The derist desert on earth is Atacama desert in chill.")
# print("The Atacama desert gets an average of less than .01 centimeters (.004 inches) of rain every year")
# print("Sometimes years will go by between rain storms. In fact, there are some places in the Atacana desert where it has not rained for over 400 years.")

# a= ["WHERE IS DRIEST DESERT IN THE WORLD","desert are in which condition","how many year rain not happen in atacana","which is a driest desert in the world "]
# b= ['1) usa','1) wet','1) 100','1) sahara']
# c= ['2) brazil','2) dry','2) 200','2) atacana']
# d= ['3) chile','3) hot','3) 300','3) amaan']
# e= ['4) europe','4)cool','4)400','4) nansn']
# f= ['chile','dry','400','atacana']
# g= ['3','2','4','2']
# paisa=0
# for i in range(len(a)):
#     print()
#     print(f'{i+1}]',a[i])
#     print(b[i])
#     print(c[i])
#     print(d[i])
#     print(e[i])
#     print()
#     ans=input("enter your options :")
#     if ans==g[i]:
#         print("your answer is correct .")
#         paisa+=10000
#         print("your won",paisa,"rupees.")
#     else:
#         print("your ans is wrong.")
# print("Totaly you won",paisa,"rupees.")








