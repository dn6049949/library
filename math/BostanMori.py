"""
Calculate the N-th term of a linear recurrence sequence.
ref: http://q.c.titech.ac.jp/docs/progs/polynomial_division.html


linear recurrence sequence
a_d := c_1*a_{d-1} + c_2*a_{d-2} + ... + c_d*a_0

G(x) = sigma_{i=0} a_i*x^i

Q(x) = 1 - sigma_{i=0}^{d} c_i*x^i

P(x) = G(x)Q(x) (deg(P(X)) == deg(Q(x)-1))

a_n = bostan_mori(P(x), Q(x), n)
"""


def mul(p, q):
    res = [0]*(len(p)+len(q)-1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            res[i+j] += pi*qj
    return res


def mul_even(p, q):
    res = [0]*((len(p)+len(q))>>1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            k = i+j
            if not k&1:
                res[k>>1] += pi*qj
    return res


def mul_odd(p, q):
    res = [0]*((len(p)+len(q))>>1)
    for i, pi in enumerate(p):
        for j, qj in enumerate(q):
            k = i+j
            if k&1:
                res[k>>1] += pi*qj
    return res


def bostan_mori(p, q, n):
    while n:
        q_ = [qi if not i&1 else -qi for i, qi in enumerate(q)]
        q = mul_even(q, q_)
        if not n&1:
            p = mul_even(p, q_)
        else:
            p = mul_odd(p, q_)
        n >>= 1
    return p[0]


def main():
    g = [1,1,2]
    q = [1,-1,-1]
    p = mul(g,q)[:len(q)-1]
    for n in range(11):
        print(n, bostan_mori(p,q,n))


if __name__ == "__main__":
    main()