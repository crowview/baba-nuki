## please only use positive numbers for these
def swap_0(s, n): # list -> list
    if n == 0: return s
    return [s[n]] + s[1:n] + [s[0]] + s[n+1:]

def swap_last(s,n): # list -> list
    if (n == len(s)-1): return s
    return s[:n] + [s[-1]] + s[n+1:len(s)-1] + [s[n]]

def swaps(s): # list -> list of list
    return [swap_0(s,n) for n in range(len(s))]


## list the permutations of lst
##
def swpperms(s): # list -> list of list
    if s == []:
        return [[]]
    perms = []
    for p in swpperms(s[1:]):
        perms += swaps([s[0]] + p)
    return perms



## print permutations of list of size N
## faster and more readable printing for large outputs
##
def print_perms(N): # pos int -> None
    if N > 10:
        print "no."
        return 
    block = ''
    i = 0
    for p in swpperms(range(N)): 
        block += str(p) + '\n'
        i += 1
        if i % N == 0:
            print block
            block = ''
    print "Printed", i, "permutations."

## let her rip
print_perms(3)
