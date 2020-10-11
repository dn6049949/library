"""
回文全列挙 : O(N)
"""

def manacher(s):
    n = len(s)
    ev = [0]*(n-1) #偶数長回文、中心:iとi+1の間
    od = [1]*n     #奇数長回文、中心:i
    c = 0
    k = 0
    while c < n-1:
        l = c-k
        r = c+k+1
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        rc = (r-l)//2 #cを中心とする回文の極大半径
        ev[c] = rc
        d = 1
        for d in range(1,rc):
            rl = ev[c-d]
            if rl == rc-d:
                k = rl
                break
            ev[c+d] = min(rc-d,rl)
        else:
            k = 0
        c += d

    c = 1
    k = 1
    while c < n:
        l = c-k
        r = c+k
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        rc = (r-l)//2 #cを中心とする回文の極大半径
        od[c] = rc
        d = 1
        for d in range(1,rc):
            rl = od[c-d]
            if rl == rc-d:
                k = rl
                break
            od[c+d] = min(rc-d,rl)
        else:
            k = 1
        c += d
    return ev,od

s = input()
print(manacher(s))
