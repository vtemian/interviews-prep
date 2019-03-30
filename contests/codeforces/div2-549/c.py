v = int(input())

need_check = {}
tree = {}

kids = {}

count = 1
while count <= v:
    parent, to_check = map(int, input().split())
    node = count

    tree[node] = parent

    if to_check:
        need_check[node] = 1

    if parent not in kids:
        kids[parent] = []

    kids[parent].append(node)

    count += 1

deletion = []
for node in sorted(need_check.keys()):
    # determine if we'll delete him
    if node in kids and kids[node]:
        to_delete = True

        for kid in kids[node]:
            if kid not in need_check:
                to_delete = False
                break

        if not to_delete:
            continue

        next_parent = tree[node]
        for kid in kids[node]:
            tree[kid] = next_parent

        del kids[node]
    deletion.append(node)

if not deletion:
    print('-1')
else:
    print(' '.join(map(str, deletion)))
