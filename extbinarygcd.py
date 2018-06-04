def ext_binary_gcd(a,b):
    """Extended binary GCD.

    Given input a, b the function returns d, s, t
    such that gcd(a,b) = d = as + bt.
    """
    u, v, s, t, r = 1, 0, 0, 1, 0
    while a & 1 == 0 and b & 1 == 0:
        a, b, r = a>>1, b>>1, r+1
    alpha, beta = a, b
    #
    #  from here on we maintain a = u * alpha + v * beta
    #  and b = s * alpha + t * beta
    #
    while a & 1 == 0:
        a = a>>1
        if (u & 1 == 0) and (v & 1 == 0):
            u, v = u>>1, v>>1
        else:
            u, v = (u + beta)>>1, (v - alpha)>>1
    while a != b:
        if (b & 1 == 0):
            b = b>>1
            #
            #  Commentary: note that here, since b is even,
            #  (i) if s, t are both odd then so are alpha, beta
            #  (ii) if s is odd and t even then alpha must be even, so beta is odd
            #  (iii) if t is odd and s even then beta must be even, so alpha is odd
            #  so for each of (i), (ii) and (iii) s + beta and t - alpha are even
            #
            if (s & 1 == 0) and (t & 1 == 0):
                s, t = s>>1, t>>1
            else:
                s, t = (s + beta)>>1, (t - alpha)>>1
        elif b < a:
            a, b, u, v, s, t = b, a, s, t, u, v
        else:
            b, s, t = b - a, s - u, t - v
    return (2 ** r) * a, s, t

if __name__ == "__main__":
    print(ext_binary_gcd(1234123410000, 12341234210000))