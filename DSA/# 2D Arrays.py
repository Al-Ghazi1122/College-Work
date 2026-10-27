# the items written backwards

''''''
#2D arrays (lists)


Two2Dy = [[1,2,3],
          [4,5,6],
          [7,8,9,],
            ["string"] ]

print (Two2Dy[2],[1])
print(Two2Dy[1])

for row in Two2Dy:
    print(row)

for row in Two2Dy:
    for item in row:
        print(row)

Two2Dy[0][1] = 600

print(Two2Dy)
