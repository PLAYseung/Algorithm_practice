def solution (A,B):
    A.sort()
    B.sort()
   
    Amax, Amin = A[-1],A[0]
    Bmax, Bmin = B[-1],B[0]
    
    pos = 0
    res = 0
    
    # print(Amax,Amin,Bmax,Bmin)
    
    if Bmin>Amax: return len(B)
    if Amin>Bmax: return 0
    
    for idx in range(len(A)):
        if B[idx] > A[pos]:
            pos += 1
            res += 1
        return res
