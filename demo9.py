#print('$')
#print('$','$')
#print('$','$','$')
#dictionary
a={"url1":"google.com","url2":"amazon.com"}
b={1:"prashant",2:"moolya"}
#print(b[1])
print(a["url1"]) #url1(key)
b[3]="flipkart.com"
print(b)
print(b[3])
print(b.get(1)) #get method
print(b.keys())
print(b.items()) #values comes with key
print(b.values()) #only values will appear
print(b.pop(1)) #to remove or delete value
print(b.keys())
print(b.popitem()) # remove the last one key
print(b.keys())
b.update({3:"demoqa.com",4:"orangehrm.com"}) #update the values with keys
print(b)
b.setdefault(5,"youtube.com") #for update the keys and values also
print(b)
b.clear() #empty dictionary
print(b)
