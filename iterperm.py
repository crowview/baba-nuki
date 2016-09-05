def swap(s,a,b):
    if (a != b):
        s[a],s[b] = s[b],s[a]
        return 1
    return 0

def inv_fact(m,n):
    a = 0
    b = 0
    s = [reduce(lambda x,y: x*y,range(1,k+1)) for k in range(1,m+1)]
    for i in s:
        if n % i == 0:
            a += 1
            if i > 2:
                b = (n/i - 1) % (a+1)
    return a,b
    

def iterperm(s):
    f = [i for i in s]
    b = 0
    a = 1
    perms = reduce(lambda x,y: x*y, range(1,len(s)+1))
    k = 1;
    while k < perms:
        swap(s, len(s)-a-1, len(s)-b-1)
        print f
        f = [i for i in s]
        k += 1
        (a,b) = inv_fact(len(s),k)
    print f

iterperm(range(6))
