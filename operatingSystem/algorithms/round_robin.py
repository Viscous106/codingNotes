class Solution:
    def solve(self, A, B):
        n = len(A)
        rem_bt = list(A)
        ct = [0] * n
        t = 0
        
        while True:
            done = True
            for i in range(n):
                if rem_bt[i] > 0:
                    done = False
                    if rem_bt[i] > B:
                        t += B
                        rem_bt[i] -= B
                    else:
                        t += rem_bt[i]
                        ct[i] = t
                        rem_bt[i] = 0
            if done:
                break
        return ct
