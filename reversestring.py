s=input("enter a string ")
li=s.split(" ")
print(li)
new=[]
for i in range(len(li)-1,-1,-1):
    new.append(li[i])
string=' '.join(new)
print(string)