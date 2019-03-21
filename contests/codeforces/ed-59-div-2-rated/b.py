n = int(input())
max_generated = 9
cache = {}
results = {
    nr: [nr]
    for nr in range(1, 10)
}


def generate(x, k):
    global max_generated
    while len(results[x]) < k:
        max_generated += 1
        res = str(sum(map(int, str(max_generated))))
        while len(res) > 1:
            if res in cache:
                res = cache[res]
                break
            res = str(sum(map(int, str(res))))
        cache[max_generated] = res
        results[int(res)].append(max_generated)
        print(max_generated)


while n:
    k, x = map(int, input().split())

    if len(results[x]) < k:
        generate(x, k)

    print(results[x][k-1])

    n -= 1
