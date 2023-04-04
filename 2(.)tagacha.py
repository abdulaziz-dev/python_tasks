a=input()
if ':' in a:
    for i in range(0,len(a)):
        if a[i]==':'and a[0]!=':':
            a=a[0:i]
            print(a)
    else:
        print(': dan oldin belgi yo`q')
else:
    print('satrda : yo`q')
