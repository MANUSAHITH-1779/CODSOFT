import random
print("PASSWORD GENERATOR")
def fun():
    j=int(input("Enter the desired length to generate password :"))
    a= [str(i) for i in range(10)]
    b= [chr(i) for i in range(65, 91)]
    f= [chr(i) for i in range (97,123)]
    g=['#','&','@','*','(',')','!','$','%']
    c=a+b+f+g
    d=""
    d=d+random.choice(b)
    for i in range(j-1):
        k=random.choice(c)
        d=d+k
    print(f"The password of length {j} generated is : {d}")
fun()
while(1):
    l=input("\nsatisfied with the password?(Yes/No) :")
    print()
    if(l=='Yes' or l=='yes'):
        print("Thank You! have a Great day.")
        break
    elif(l=='No' or l=='no'):
        fun()
    else:
        print("Enter valid option !!!")