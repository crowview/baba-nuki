

## left rotation for positive n
## right rotation for negative n
##
def rotate(s, n): # list -> list
    return s[n:] + s[:n]

## list all rotations of a list
## 
def rotations(s): # list -> list of list
    return [rotate(s,-n) for n in range(len(s))]


## list the permutations of lst
##
def rotperms(s): # list -> list of list
    if s == []:
        return [[]]
    perms = []
    for p in rotperms(s[1:]):
        perms += rotations([s[0]] + p)
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
    for p in rotperms(range(N)): # edit this line to try with rotperms
        block += str(p) + '\n'
        i += 1
        if i % N == 0:
            print block
            block = ''
    print "Printed", i, "permutations."

## let her rip
print_perms(3)

