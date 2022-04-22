#write a program make a calculator
a=int(input("enter 1 number:-"))



print('''
press  + :-
press  -   :-
press * :-
press  /:-
press  ** :-''')
cal=input("enter your choise:-")
b=int(input("enter 2 number:-"))
if cal=="+":
   print(a+b)
 
if cal=="-" :
 
    print(a-b)
    
if cal=="*" :
  
    print(a*b)
  
if cal=="/" :
    
    
    print(a/b)
    
if cal=="**" :

    print(a**b)
