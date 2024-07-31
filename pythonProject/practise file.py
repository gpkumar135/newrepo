'''count = 0;
while count < 5:
    print(count)
    count+=1'''
'''print("this is from \"batch-1\" training")'''

'''mydict = {'python':'class','machine learning':'tensorflow','pk':'kumar','ai':'ml','jeera':'keera'}
print("keys:")

for key in mydict.keys():
    print(key)

print("values:")

for value in mydict.values():
    print(value)'''

'''mydict = {'python':'class','machine learning':'tensorflow','pk':'kumar','ai':'ml','jeera':'keera'}
for key in mydict:
    print(key)
for value in mydict:
    print(mydict[value])'''

'''fruits =["apple",'banana','grape']
for fruit in fruits:
    print(fruit)'''

import requests
'''data = {
    "email": "pk@reqres.in",
    "password": "pkgkumar"
}
res = requests.post("https://reqres.in/api/register", json=data)
print(res.json())
print(res)'''

'''data = {
    "name": "pk",
    "job": "python dev"
}
res = requests.put("https://reqres.in/api/users/2", json=data)
print(res.json())
print(res)'''

'''res = requests.get("https://reqres.in/api/unknown/2")
print(res.json())
print(res)'''
import requests
import json

'''practice functions'''

'''def first(firstname,lastname):
    print("firstname" +" : "+firstname + " " + "lastname" +" : "+lastname)
first("pavan","kumar")

def multiarg(*arg):
    print("arbitary arg" + arg[3])
multiarg("test1","test2","test3","test4")

p = lambda p,k : p%k
print(p(1,3))

def my_function(**names):
  print("His last name is " + names["lname"])

my_function(fname = "pk", lname = "gk")'''

## recursive function ##
'''def fact(n):
    if n== 0:
        return 1
    else:
        return n * fact(n-1)
n = 10
print(fact(n))'''

'''import paramiko
def ssh_connect(host,username,password,port):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=host,username=username,password=password,port=port)

        print("Connection is successful")
    except Exception as e:
        print(f"Error: {e}")
ssh_connect(host ='192.168.29.108',username = 'root',password = 'Pavan@135',port ='22')'''

# practise on 13/7 #
'''string = "pavan kumar guttha"

s = string.split()[::-1]

l = []
for i in s:
    l.append(i)
print(" ".join(l))'''

'''def findlen (str):
    count = 0
    for i in str:
        count +=1
    return count
str = "pavan"
print(findlen(str))'''

'''list1 = [1,3,5,7,9]
list2 =[2,4,6,8,10]
print(str(list1))
print(str(list2))
pk = sorted(list1 + list2)
print(str(pk))'''

'''lis = [[11, 22, 33, 44], [55, 66, 77], [88, 99, 100]]

flatList = [element for innerList in lis for element in innerList]

print('List', lis)

print('Flat List', flatList)'''

'''oops concepts'''

'''class person(object):

    def __init__ (self,name,id):
        self.name = name
        self.id = id

    def display(self):
        print(self.name,self.id,self.salary,self.post)

# child class
class employee(person):
    def __init__(self,name,id,salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self,name,id)


emp = employee("pavankumar",22,20000,"dev")
emp.display()'''

# superclass #

class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self.age)

class student(person):
    def __init__(self,name,age,dob):
        self.sname = name
        self.sage = age
        self.dob = dob
        super().__init__('pavan',age)
    def displayinfo(self):
        print(self.sname,self.sage,self.dob)
obj = student("kumar",24,"1999")
obj.display()
obj.displayinfo()







