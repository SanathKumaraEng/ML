import numpy as np
a = np.array([4, 5, 6])
#print(a[0])
#b = np.array([[1,2],[3,4]])
#print(a.ndim)
#print(a.itemsize)
#print(a.dtype)
#print(a.size) 

a = np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print(a.itemsize)
print(a.size)

b = np.array([[1,2],[3,4],[5,6]], dtype=complex)
print(b)

c = np.zeros((3,4), dtype=complex)
print(c)

l = range(5)
print(l)

m = np.arange(1,5)
print(m)

print(c.shape)
n = c.reshape(4,3)
p = c.ravel()
print(p)

sum = a.sum()
print(sum)

min = a.min()
print(min)

max = a.max()
print(max)

sum_a0 = a.sum(axis=0)
print(sum_a0)

sum_a1 = a.sum(axis=1)
print(sum_a1)