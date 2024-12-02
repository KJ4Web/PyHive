a = [[9, 6, 3],
     [2, 4, 5],
     [5, 7, 9]]

b = [[3, 2, 4],
     [4, 3, 8],
     [7, 4, 5]]

multiResult = [[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]]

for m in range(len(a)):
   for n in range(len(b[0])):
        for o in range(len(b)):
            multiResult[m][n] += a[m][o] * b[o][n]

print("The multiplication result of matrix a and b is:")
for r in multiResult:
   print(r)
