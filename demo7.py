# list (collection of diff data types)
l=[10,'prashant',.59,True]
print(l[3])
s=[10,10,"prashant",'prashant'] #list can accept a duplicate value
print(s[-1])
print(s[0:3:1])
print(type(s))
y=[18,7,6,5,4,3,2,1]
print(y[0:3:5])
#list methods
#append()
s.append(320)
print(s)
s.insert(3,'moolya')
print(s)

s.remove('prashant')
print(s)
a=['shushant','moolya','prashant','india','prashant']
a.sort()
print(a)
b=[9,30,6,80,60,90]
#(reverse=True)
b.sort()
b.reverse()
print(b)
#c=[6,'prashant',87,78,9,7,'moolya']
#c.sort()
#print(c)
b.clear()
print(b)

print(a.count('prashant'))
