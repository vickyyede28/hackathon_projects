print ("""
1. kelvin 
2. celcis
3. fahrenheit""")
a= int(input('choose your type '))
if a==0:
    print('exist')
t= int(input('enter your temp '))
if a==1:
    F= t*(9/5)+32
    print(F)
    c= 9/5*(t-273.12)+32
    print(c)
elif a==2:
    f=t*(9/5)+32
    print(f)
    k=t+273.15
    print(k)
elif a==3:
    k=5/9*(t+459.67)
    print(k)
    c=5/9*(t-32)
    print(c)
else:
    if a==0:
        print('not exist')