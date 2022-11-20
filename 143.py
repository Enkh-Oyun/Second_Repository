a = int(input("too oruulna uu: ")) #15251
b = a%10 #1
c = a//10000 #1
d = (a-c*10000)//1000 #5
e = a%100 #51
p = e//10 #5
if b==c and d==p:
    print (a, "palindrome too bn")
else:
    print (a, "palindrome too bish bn")