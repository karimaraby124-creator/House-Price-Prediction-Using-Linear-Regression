import numpy as np

a =np.array([
    [ 1 , 2 , 3 ],
    [4 , 5 , 6 ],
     [7 , 8 , 9 ]])
b =np.array([
    [ 11, 12 , 13 ],
    [14 , 15 , 16 ],
     [17 , 18 , 19 ]])

f = np.array([
    [  15 , 6],
    [ 69 , 2]
])

print('=' * 30)
print(a.T)

print('=' * 30)
c =np.eye(3)
print(c)
print('=' * 30)
d = np.zeros((3,5))
print(d)
print('='*30)
result =np.linalg.det(f)
print(result)
print('='*30)
result =np.linalg.inv(f)
print(result)
print('='*30)
print((np.trace(a)))
print('='*30)

h = np.array([
    [5 , 3],
    [3 , -5]
])

k = np.array([7 , -23])
solution = np.linalg.solve(h , k)
print(solution)
print('='*30)
A = np.array([
    [1, 0],
    [0, 1]
])

dimension = np.linalg.matrix_rank(A)

print(dimension)
print('='*30)
#projection
m = np.array([9 , 8])
l =  np.array([ 7 , 3])
solution2 = (np.dot( m , l ) / np.dot(l , l))*l
print(solution2)
print('=' *30)

engvalue , engvactor = np.linalg.eig(a)
print("envactor:")
print(engvactor)
print('engvalue:')
print(engvalue)
print ('='*30)
