####################高精度减法实战####################
# Python原生支持大整数减法
####################高精度减法实战####################
def sub(a,b):
    neg = False
    if len(a) < len(b) or (len(a) == len(b) and a < b):
        a,b = b,a
        neg = True
    a=a[::-1]
    b=b[::-1]
    res = []
    borrow = 0
    for i in range(len(a)):
        da = int(a[i]) - borrow
        db = int(b[i]) if i < len(b) else 0
        borrow = 0
        if da < db:
            da += 10
            borrow = 1
        res.append( str(da-db) )
    ans=''.join(res[::-1]).lstrip('0')
    return "-" + ans if neg else (ans or "0")

s1=input().strip()
s2=input().strip()
print(sub(s1,s2))