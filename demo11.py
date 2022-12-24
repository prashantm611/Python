#if else
marks=90
if marks>=90:
    print("allow give me")
elif marks>=70 and marks<90:
    print("study hard")
else:
    print("lathi charge")

a=[500,600,700]
a.sort()
print("largest element is:",a[-1])
#loop highest number
h=[100,200,300,400,500]
largest_number = h[0]
for number in h:
    if number>largest_number:
        largest_number =number
        print(largest_number)

#highest number
a=[2,3,4,5,6,7,8,9]
def b(x,y):
    if x<y:
        return y
    else:
        return x
    a=reduce(b())
    print(a)
