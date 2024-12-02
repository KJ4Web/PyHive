t = [[5, 4, 3],
    [2, 4, 6],
    [4, 7, 9],
    [8, 1, 3]]

transResult = [[0, 0, 0, 0],
            [0, 0, 0, 0],
             [0, 0, 0, 0]]

for a in range(len(t)):
    for b in range(len(t[0])):
        transResult[b][a] = t[a][b]

print("The transpose of matrix t is: ")
for r in transResult:
   print(r)
