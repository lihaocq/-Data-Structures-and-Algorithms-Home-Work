## Key points

1. Pay attention to the range for i, when you use

```Python 3
for i in range()
```

2. use a large p. And the acceptable range of x is [0,p-1]

## Code:

```python 3
# python3


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def PreHashes(text, len_p, p, x):
    len_t = len(text)
    H = [0 for i in range(0, len_t-len_p+1)]
    S = text[len_t-len_p: len_t]
    H[len_t-len_p] = PolyHash(S, p, x)
    y = 1
    for i in range(0, len_p):
        y = ((y*x) % p + p) % p

    for i in reversed(range(0, len_t - len_p)):
        H[i] = ((x*H[i+1]+ord(text[i])-y*ord(text[i+len_p])) % p + p) % p
    return H


def PolyHash(S, p, x):

    hash = 0

    for i in reversed(range(0, len(S))):
        hash = ((hash * x + ord(S[i])) % p + p) % p
    return hash


def RabinKarp(pattern, text):
    len_p = len(pattern)
    len_t = len(text)
    p = 100000000007
    x = 20
    result = []
    pHash = PolyHash(pattern, p, x)

    H = PreHashes(text, len_p, p, x)

    for i in range(0, len_t-len_p+1):
        if pHash != H[i]:
            continue

        if text[i:i+len_p] == pattern:
            result.append(i)

    return result


if __name__ == '__main__':
    print_occurrences(RabinKarp(*read_input()))
```

