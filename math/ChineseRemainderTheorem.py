"""
Chinese Remainder Theorem : O(NlogmaxM)
calculate an interger x (x ≡ r (mod m)), satisfies following equations
x ≡ b1 (mod m1)
x ≡ b2 (mod m2)
…
x ≡ bn (mod mn)

return : (r,m)
m = -1 iff having no answer
"""

def extgcd(a, b):
    p, q, pre_p, pre_q = 1, 0, 0, 1
    while b:
        m = a//b
        a, b = b, a%b
        p, q, pre_p, pre_q = pre_p, pre_q, p-m*pre_p, q-m*pre_q
    return a, p, q


def crt(equation):
    r, m = equation[0]
    for b, m2 in equation[1:]:
        g, p, q = extgcd(m, m2)
        if (b-r)%g != 0:
            return 0, -1
        m, r = m*(m2//g), r+m*((b-r)//g*p%(m2//g))
        r %= m
    return r, m
