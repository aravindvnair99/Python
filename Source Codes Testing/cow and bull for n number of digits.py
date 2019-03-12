import random as ro


def cow_bull(na,n):
    un=input("enter a number you guess")
    ua=list(str(un))
    cow=0
    bull=0
    for i in ua:
        if int(i) in na:
            cow+=1



            
    for i in range(n):
        if na[i]==int(ua[i]):
            bull+=1
            cow-=1


            

    print("cow  :{0},bull  :{1}".format(cow,bull)) 
    return bull



n=int(input("how many digits number you need? "))
na=ro.sample(range(10),n)
a=map(str,na)
answer=''.join(a)
ans=cow_bull(na,n)
while ans!=n:
    ans=cow_bull(na,n)
print("answer",answer)
print("YOU WON!")
