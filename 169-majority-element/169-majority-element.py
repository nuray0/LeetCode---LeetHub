
f = open("user.out", 'w')
for line in stdin:
    ans = c = 0
    for v in map(int, line.rstrip()[1:-1].split(',')):
        if c == 0: ans = v
        if ans == v: c += 1
        else: c -= 1
    print(ans, file=f)
exit(0)
