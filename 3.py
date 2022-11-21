def upsideDownEqual(S):
    for i in range(len(S)):
        if (S[i] not in ('0', '1', '2', '5', '6','8','9')):
            return "No"
    return "Yes"
 
i1 = int(input())
c = 0
for i in range(1,1000):
    if (upsideDownEqual(str(i)) == 'Yes'):
        r = i
        c = c+1
    if c==i1:
        break
print(r)