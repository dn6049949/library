"""
Calculate the intersections of 2 lines, l1(xs1,ys1,xt1,yt1) and l1(xs2,ys2,xt2,yt2) : O(1)
"""

def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]

def intersection(l1, l2):
    xs1,ys1,xt1,yt1 = l1
    xs2,ys2,xt2,yt2 = l2
    s1t1 = (xt1-xs1, yt1-ys1)
    s1s2 = (xs2-xs1, ys2-ys1)
    s1t2 = (xt2-xs1, yt2-ys1)
    if cross(s1t1, s1s2)*cross(s1t1, s1t2) >= 0:
        return None
    
    s2t2 = (xt2-xs2, yt2-ys2)
    s2s1 = (xs1-xs2, ys1-ys2)
    s2t1 = (xt1-xs2, yt1-ys2)
    
    crs = cross(s2t2, s2s1)
    crt = cross(s2t2, s2t1)
    if crs*crt >= 0:
        return None
    
    rate = abs(crs)/(abs(crs)+abs(crt))
    x,y = xs1+rate*s1t1[0], ys1+rate*s1t1[1]
    return x,y
