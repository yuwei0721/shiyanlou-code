a=1
for a in range(101):
    b=str(a).find('7')
    if a%7 == 0 or b!=-1:
        continue
    print(a)
    a=a+1

