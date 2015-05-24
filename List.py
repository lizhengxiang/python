d = "lizhengxiang"
c = "lizhengxiang"
a = [1, d, 3, 4, 5, c, 7, 8, 9]
print(a[0])
print(a[5])
print(a)
a[0] = "lizhengxiang"
a.append("this is a")
b = [4, 5, 6]
a[2] = [1,2,b] 
m = a[2][0:1]
m[0] = 7
print(a[2])
print(m)
print(a)
