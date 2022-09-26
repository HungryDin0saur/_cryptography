import math

limit = 100000
primes = [False] * limit
sqrt_limit = int( math.sqrt( limit ) )

x_limit = int( math.sqrt( ( limit + 1 ) / 2 ) )
for x in xrange( 1, x_limit ):
    xx = x*x

    for y in xrange( 1, sqrt_limit ):
        yy = y*y

        n = 3*xx + yy
        if n <= limit and n%12 == 7:
                primes[n] = not primes[n]

        n += xx
        if n <= limit and n%12 in (1,5):
                primes[n] = not primes[n]

        if x > y:
            n -= xx + 2*yy
            if n <= limit and n%12 == 11:
                primes[n] = not primes[n]

for n in xrange(5,limit):
    if primes[n]:
        for k in xrange(n*n, limit, n*n):
            primes[k] = False

res = [2,3] + filter(primes.__getitem__, xrange(5, limit))
print(res)    
    #[2,3] + filter(primes.__getitem__, xrange(5, limit))
    
