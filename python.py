#Check if two arrays are equal or not

A = [1, 2, 5]
B = [2, 4, 15]
isequal=True
if len(A)==len(B):
    A.sort()
    B.sort()
    for a in range(len(A)):
        if A[a]!=B[a]:
          isequal=False
          break
else:
   isequal=False
print(isequal)           
