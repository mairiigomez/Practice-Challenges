"""You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n."""

x = int(input())
y = int(input())
z = int(input())
n = int(input())
s = [[x1,y1,z1] for x1 in range (x+1) for y1 in range(y+1) for z1 in range(z+1) if x1+y1+z1 != n ]
print(s)
