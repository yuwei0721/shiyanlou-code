a=1
for a in range(101):
    test=str(a).find('7')
    if a%7 == 0 or test!=-1:
        continue
    print(a)
    a=a+1

