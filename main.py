class Solution:

    def findMinDiff(self, A,N,M):

        # code here
        a=[]
        m=max(A)-min(A)
        A=sorted(A)
        for i in range(N-M+1):
            m=min(m,A[i+M-1]-A[i])
        return m