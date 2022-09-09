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
        # B의 요소가 이긴 경우에만 다음 A의 값으로 넘어간다
        if B[idx] > A[pos]:  
            pos += 1 
            res += 1
    return res

if __name__=='__main__':
    print(solution([5,1,3,7],[2,2,6,8]))