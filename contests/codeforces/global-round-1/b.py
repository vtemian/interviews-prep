n, m, k = map(int, input().split())
b = list(map(int, input().split()))


distances = []
start = 0
end = 1

while end < len(b):
    distances.append(b[end] - b[start])
    start += 1
    end += 1

mine = len(distances) - k + 1
distances = sorted(distances)

solo = len(distances) - mine
#print("solo", solo)
#print("mine", mine)
#print("distances", distances)
print(sum(distances[:mine]) + solo + (k - solo))
