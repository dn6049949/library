# 円R1(x1,y1,r1), 円R2(x2,y2,r2)の交点を求める(O(1))
"https://shogo82148.github.io/homepage/memo/geometry/circle-cross.html"

# 2円の中心間の距離の2乗
def D2(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2

# 2円が交点を持つか
def check(R1,R2):
    x1,y1,r1 = R1
    x2,y2,r2 = R2
    d2 = D2(x1,y1,x2,y2)
    if (r1-r2)**2 <= d2 <= (r1+r2)**2:
        return 1
    else:
        return 0

# 2円の交点を出力
def point(R1,R2):
    if not check(R1,R2):
        return []
    else:
        x1,y1,r1 = R1
        x2,y2,r2 = R2
        x2 -= x1
        y2 -= y1
        r = x2**2+y2**2
        a = (r+r1**2-r2**2)/2
        d = (r*r1**2-a**2)**0.5
        X,Y = a*x2/r, a*y2/r
        k = d/r
        X1,Y1 = X+y2*k+x1, Y-x2*k+y1
        X2,Y2 = X-y2*k+x1, Y+x2*k+y1
        return [(X1,Y1),(X2,Y2)]
