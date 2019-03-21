from collections import Counter


n, m = map(int, input().split())
a = list(map(int, input().split()))
c = [0] * (m + 1)


for aa in a:
    c[aa] += 1

print(c)
triples = 0
idx = 0
while idx < len(c):
    while c[idx] and idx + 1 < len(c) and c[idx + 1] and idx + 2 < len(c) and c[idx + 2]:
        c[idx] -= 1
        c[idx + 1] -= 1
        c[idx + 2] -= 1
        triples += 1

    print(idx, triples, c)

    if c[idx] // 3 > 0:
        triples += c[idx] // 3
        print(c[idx] // 3)
        c[idx] = c[idx] % 3
    idx += 1

print(triples)
