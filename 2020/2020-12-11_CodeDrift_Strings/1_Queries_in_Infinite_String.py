import string


class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(A):
        S = list(string.ascii_lowercase)
        VOWELS = 'aeiou'
        ans = []
        for dim in range(len(A)):
            L = A[dim][0] - 1
            R = A[dim][1] - 1
            count = 0
            i = 0
            abs_i = 0
            cycle = 1
            done = 0
            while True:
                if L <= abs_i <= R:
                    if done != 0:
                        if S[i] in VOWELS:
                            count += 1
                        done += 1
                        if done == cycle * 26:
                            done = 0
                            i = 0
                            cycle += 1
                        elif done % cycle == 0:
                            i += 1
                        abs_i += 1
                    elif cycle * 26 + abs_i <= R:
                        count += 5 * cycle
                        abs_i += 26 * cycle
                        cycle += 1
                    else:
                        if S[i] in VOWELS:
                            count += 1
                        done += 1
                        if done % cycle == 0:
                            i += 1
                        abs_i += 1
                elif abs_i > R:
                    break
                else:
                    done += 1
                    if done == cycle * 26:
                        done = 0
                        i = 0
                        cycle += 1
                    elif done % cycle == 0:
                        i += 1
                    abs_i += 1
            ans.append(count)
        return ans

    A = [[1, 5], [26, 29]]
    print("A", solve(A))
    B = [[79, 85]]
    print("B", solve(B))
    C = [[42, 468]]
    print("C", solve(C))
    D = [[35, 501]]
    print("D", solve(D))
    E = [[70, 725]]
    print("E", solve(E))
    F = [[79, 359]]
    print("F", solve(F))
    G = [[63, 465]]
    print("F", solve(G))
    H = [[6, 146]]
    print("F", solve(H))
    I = [[82, 828]]
    print("F", solve(I))
    J = [[62, 492]]
    print("F", solve(J))
    K = [[96, 943]]
    print("F", solve(K))
    L = [[28, 437]]
    print("F", solve(L))
