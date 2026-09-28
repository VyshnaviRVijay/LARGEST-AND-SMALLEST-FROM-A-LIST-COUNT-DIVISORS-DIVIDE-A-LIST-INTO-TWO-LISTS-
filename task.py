##printing largest and smallest from a list
a=[11,230,3,4000,6,-10,-2,3,999]
largest=0
for i in a:
    if i>largest:
        largest=i
print(largest)


smallest=0
for i in a:
    if i<smallest:
        smallest=i
print(smallest)


#divide the list into two lists
a=[11,12,13,15,15,16,17,18,19,20]
x=[]
y=[]
mid=len(a)//2
for i in range (len(a)):
    if i<mid:
        x.append(a[i])
    else:
        y.append(a[i])
print(x)
print(y)

##convert each word in the  string as an element in a list
data="hello my name is python"
word=''
result=[]
for i in data:
    if i!=" ":
        word=word+i
    else:
        result.append(word)
        word=''
result.append("python")
print(result)


#COUNT DIVISORS
data=" 1 10 2 "
newdata=data.strip()
new=newdata.split()
print(new)
l=int(new[0])
r=int(new[1])
k=int(new[2])
print(l,r,k)
count=0
for i in range(l,r+1):
    if i%k==0:
        count+=1
print(count)



