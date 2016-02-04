def count_inversion(sequence):
   v =  SortCount(list(sequence))
   return v[1]

def SortCount(A):
   l = len(A)
   if l > 1:
      n = l//2
      C = A[:n]
      D = A[n:]
      C, c = SortCount(A[:n])
      D, d = SortCount(A[n:])
      B, b = MergeCount(C,D)
      return B, b+c+d
   else:
      return A, 0


def MergeCount(A,B):
   count = 0
   M = []
   while A and B:
      if A[0] <= B[0]: 
         M.append(A.pop(0)) 
      else: 
         count += len(A)
         M.append(B.pop(0)) 
   M  += A + B     
   return M, count
