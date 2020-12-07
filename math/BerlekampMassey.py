"""
Calculate the reduction formula
ref : https://de.wikipedia.org/wiki/Berlekamp-Massey-Algorithmus
"""

import fractions

def berlekamp_massey(a):
    s = list(map(fractions.Fraction, a))
    n = len(s)
    if n == 1:
        return None
    c = [0]*n
    cl = [0]*n
    c[0] = cl[0] = 1
    L = 0
    l = dl = -1
    for i in range(n):
        d = sum([ci*sj for ci,sj in zip(c[:L+1],s[i-L:i+1][::-1])])
        while d != 0:
            tmp = c[:]
            coef = d/dl
            for k in range(n-i+l):
                c[i-l+k] -= coef*cl[k]
            if 2*L <= i:
                l = i
                cl = tmp[:]
                dl = d
                L = i+1-L
            d = sum([ci*sj for ci,sj in zip(c[:L+1],s[i-L:i+1][::-1])])
            
    c0 = c[0]
    res = ["a_n ="]
    for i, ci in enumerate(c):
        if i == 0 or ci == 0:
            continue
        ci /= -c0
        abs_ci = abs(ci)
        if ci < 0:
            sign = "- "
        elif len(res) > 1:
            sign = "+ "
        else:
            sign = ""
        coef = f"{sign}{abs_ci}" if abs_ci != 1 else sign
        res.append(f"{coef}a_(n-{i})")

    if len(res) == 1:
        return None
    return " ".join(res)