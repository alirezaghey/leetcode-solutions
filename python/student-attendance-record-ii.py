class Solution:
    # bottom up iterative approach with constant space
    def checkRecord(self, n: int) -> int:
        A, P, L = [1, 2], [1, 3], [1, 3]
        noAP, noAL = [1, 2], [1, 2]
        if n < 3:
            return A[n-1]+P[n-1]+L[n-1]
        
        MOD = 10**9+7
        for _ in range(n-2):
            new_A = [A[1], (noAP[1]+noAL[1]) % MOD]
            new_noAP = [noAP[1], (noAP[1]+noAL[1]) % MOD]
            new_noAL = [noAL[1], (noAP[1]+noAP[0]) % MOD]
            
            new_P = [P[1], (A[1]+L[1]+P[1]) % MOD]
            new_L = [L[1], (A[1]+P[1]+A[0]+P[0]) % MOD]
            A, P, L = new_A, new_P, new_L
            noAP, noAL = new_noAP, new_noAL
            
        return (A[1]+P[1]+L[1])%MOD