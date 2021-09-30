class Solution:
    # @param A : string
    # @param B : string
    # @param C : string
    # @return an integer
    def solve(A, B, C):
        C_set = set(C)
        for c in A:
            if c in C_set:
                return 1
        return 0
