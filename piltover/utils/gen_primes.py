# https://langui.sh/2009/03/07/generating-very-large-primes/

import math
import json
import secrets


from cryptography.hazmat.primitives.asymmetric import dh


RNG = secrets.SystemRandom()

# avoid black formatter to wrap the line
LOW_PRIMES = json.loads(
    "[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]",
)


def rabin_miller(n):
    s = n - 1
    t = 0
    while s & 1 == 0:
        s = s // 2
        t += 1
    k = 0
    while k < 128:
        a = RNG.randrange(2, n - 1)
        # a^s is computationally infeasible.  we need a more intelligent approach
        # v = (a**s)%n
        # python's core math module can do modular exponentiation
        v = pow(a, s, n)  # where values are (num,exp,mod)
        if v != 1:
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v**2) % n
        k += 2
    return True


def is_prime(n):
    # lowPrimes is all primes (sans 2, which is covered by the bitwise and operator)
    # under 1000. taking n modulo each lowPrime allows us to remove a huge chunk
    # of composite numbers from our potential pool without resorting to Rabin-Miller

    if n >= 3:
        if n & 1 != 0:
            for p in LOW_PRIMES:
                if n == p:
                    return True
                elif n % p == 0:
                    return False
            return rabin_miller(n)
    return False


def generate_large_prime(k: int) -> int:
    # k is the desired bit length
    r = 100 * (math.log(k, 2) + 1)  # number of attempts max
    # r_ = r

    while r > 0:
        n = RNG.randrange(2 ** (k - 1), 2 ** (k))
        r -= 1
        if is_prime(n):
            return n
    return -1


CURRENT_DH_PRIME = int(
    "C71CAEB9C6B1C9048E6C522F70F13F73980D40238E3E21C14934D037563D930F"
    "48198A0AA7C14058229493D22530F4DBFA336F6E0AC925139543AED44CCE7C37"
    "20FD51F69458705AC68CD4FE6B6B13ABDC9746512969328454F18FAF8C595F64"
    "2477FE96BB2A941D5BCD1D4AC8CC49880708FA9B378E3C4F3A9060BEE67CF9A4"
    "A4A695811051907E162753B56B0F6B410DBA74D8A84B2A14B3144E0EF1284754"
    "FD17ED950D5965B4B9DD46582DB1178D169C6BC465B0D6FF9CA3928FEF5B9AE4"
    "E418FC15E83EBEA0F87FA9FF5EED70050DED2849F47BF959D956850CE929851F"
    "0D8115F635B105EE2E4E15D04B2454BF6F4FADF034B10403119CD8E3B92FCC5B",
    16
)


def gen_safe_prime(size: int = 2048) -> tuple[int, int]:
    """
    parameters = dh.generate_parameters(generator=2, key_size=size)
    numbers = parameters.parameter_numbers()
    return (numbers.p, numbers.g)
    """

    # Cached integer
    return (CURRENT_DH_PRIME, 2)


if __name__ == "__main__":
    p = generate_large_prime(32)
    q = generate_large_prime(32)

    safe = gen_safe_prime()
    print(safe.p, safe.g)

    assert p != -1
    assert q != -1

    print(f"{p=}")
    print(f"{q=}")
    print(f"{p*q = }")
