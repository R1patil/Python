n=[["rahul",1000],["sonam",2000],["anil",3000]]
t=sorted(n, key=lambda x:x[1])
print(t)

dic={'apple':50,'banana':20,'orange':30,'grape':40}
sorted_dic=sorted(dic.items(), key=lambda x:x[1])
print(sorted_dic)


n=[1,2,3,4,5,6,7,8,9,10]
ans=list(filter(lambda x:x%2==0,n))
print(ans)

m=[1,2,3,4,5,6,7,8,9,10]
squared=list(map(lambda x:x%2==0,m))
print(squared)


t=["hello","world","python","is","awesome"]
lengths=list(map(lambda x:len(x),t))
print(lengths)


n=5
factorial=lambda x:1 if x==0 else x*factorial(x-1)
print(factorial(n))

x=lambda a,b:a+b
print(x(5,10))
