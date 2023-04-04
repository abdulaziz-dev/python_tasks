#  x 1 ,  x 2 ,  x 3 ,  y 1 ,  y 2 ,  y 3   haqiqiy  sonlar  berilgan  bo‘lsin.
#Koordinatalar  boshi uchlarining koordinatalari (x 1 , y 1 ), (x 2 , y 2 ) va (x 3 , y 3 )
#bo‘lgan uchburchak ichida yotadimi ? 
x1=float(input())
x2=float(input())
x3=float(input())
y1=float(input())
y2=float(input())
y3=float(input())

if(x1>0)and (x2>0)and (x3>0)and (y>0)or(y==0)or(x==0):
    a = true
if(x1<0)and (x2<0)and (x3<0)and (y>0)or(y==0)or(x==0):
    b = true
if(x1>0)and (x2>0)and (x3>0)and (y<0)or(y==0)or(x==0):
    c = true
if(x1<0)and (y2<0)and (y3<0)and (y<0)or(y==0)or(x==0):
    d = true
if(y1>0)and (y2>0)and (y3>0)and (x>0)or(y==0)or(x==0):
    e = true
if(y1<0)and (y2<0)and (y3<0)and (x>0)or(y==0)or(x==0):
    f = true
if(y1>0)and (y2>0)and (y3>0)and (x<0)or(y==0)or(x==0):
    g = true
if(y1<0)and (y2<0)and (y3<0)and (x<0)or(y==0)or(x==0):
    h = true
if a or b or c or d or e or f or g or h:
    print('yotmaydi')
else:
    print('yotadi')
