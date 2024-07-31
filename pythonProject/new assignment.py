'''l =[]
for i in range(2000,3001):
    if (i%7 ==0)and (i%5!= 0):
        l.append(str(i))

print(','.join(l))'''

'''def factorial(n):
    if n==0:
        return 1
    return (n * factorial(n-1))

n = 8
print(factorial(n))'''

'''n = 8
d = dict()
for i in range(1,n+1):
    d[i] = i*i
print(d)'''

'''values = "34,67,55,33,12,98"
l = values.split(",")
t = tuple(l)
print(l)
print(t)'''


'''class InputOutString(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())


strObj = InputOutString()
strObj.getString()
strObj.printString()'''

'''string =  'without,hello,bag,world'
items = [(x for x in string.split(','))]
items.sort()
print(','.join(items))'''

'''import math
c=50
h=30
value = []
items=[x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))'''

'''lines = []
while True:
    s = "hi pk"
    if s:
        lines.append(s.upper())
    else:
        break;

for sentence in lines:
    print(sentence)'''

'''a = "pk kumar"
words = [word for word in a.split(" ")]
print(" ".join(sorted(list(set(words)))))'''

'''values =["0100,0011,1010,1001"]
items = [x for x in values.split(",")]
for p in items:
    input = int(p,2)
    if not input%5:
        values.append(p)

print(','.join(values))'''

'''s = "HI pkg"
d={"UPPER CASE":0, "LOWER CASE":0}
for i in s:
    if i.isupper():
        d["UPPER CASE"]+=1
    elif i.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])'''

'''values = "1,2,3,4,5,6,7,8,9"
num = [x for x in values.split(',') if int(x)%2!=0]
print(",".join(num))'''

'''a = 8
n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" %(a,a,a))
n4 = int("%s%s%s%s" % (a,a,a,a))
print(n1+n2+n3+n4)'''

'''netamount = 0
while True:
    s = "D 100 W 200"
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation == "D":
        netamount += amount
    elif operation == "W":
        netamount -= amount
    else:
        pass
print(netamount)'''

'''values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))'''

'''def square(num):
    return num **2

print(square(2))
print(square(3))'''

'''def sumfunction(number1,number2):
    return number1 + number2
print(sumfunction(10,20))'''

'''def printvalue(str1,str2):
    len1 = len(str1)
    len2 = len(str2)
    if len1 > len2:
        print(str1)
    elif len2 > len1:
        print(str2)
    else:
        print(str1)
        print(str2)

printvalue("one","four")'''

'''def printDict():
    d =dict()
    for i in range(1,21):
        d[i] = i**2
    print(d)
printDict()'''

'''tuple = (1,2,3,4,5,6,7,8,9)
tp1 = tuple[:5]
tp2 = tuple[5:]
print(tp1)
print(tp2)'''

'''list = [1,2,3,4,5,6,7,8,9,10]
evennum = filter(lambda x: x%2== 0, list)
print(evennum)'''







