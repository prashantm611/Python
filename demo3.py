a=2
print (a ** 3)
#precidence of operators
print(5-8+2)
#string manupulation
str1 ="moolya"
print(len(str1))
print(str1[4])
z=2000
c = str(z)
print(type(c))
#operations in strings
#find()
print(str1.find("l"))
print(str1.find("z"))
print(str1.upper())
print(str1)
print(str1.count("o"))
print(str1.isupper()) #checkcase
str2= " hello "
print(str2)
print(str2.strip()) #removing space
#replace()
print(str1.replace("m","o"))
str3 = " vishakhapattanam "
print(str3.replace("v","b"))
print(str3)
print(str3.replace("i","m").upper())
print(str3.lstrip()) #left side space will remove
print(str3.rstrip())#right side space will remove
str4="Supplementing with selenium may provide a way to enhance your thyroid function in a natural way"
# split operation( dividing the lines)
print(str4.split("selenium"))
str5="prashant\" mishra" # \" escape character (escape the logic)
print(str5)
z="""
vishakhapattnam is in andhra pradesh.it is very beautiful city in south.
"""
print(z)
print('is' in z)


