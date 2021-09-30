def solve(A):
    newA = A.replace("010", "0,1,0")
    newA = newA.replace("10", "1,0")
    newA = newA.replace("01", "0,1")
    A_list = newA.split(",")
    if len(A_list) < 3:
        # print(A, ":", A_list)
        return len(A)
    else:
        # p rint(A, "before merging :", A_list)
        A_merged = []
        for i in range(1, len(A_list) - 1):
            if "1" in A_list[i - 1] and "1" in A_list[i + 1]:
                A_merged.append(A_list[i - 1] + A_list[i] + A_list[i + 1])
            if i - 1 == 0 and "0" in A_list[i - 1] and "1" in A_list[i]:
                A_merged.append(A_list[i - 1] + A_list[i])
            if i + 2 == len(A_list) and "1" in A_list[i] and "0" in A_list[i + 1]:
                A_merged.append(A_list[i] + A_list[i + 1])
        max_length = 0
        for bits in A_merged:
            max_length = max(max_length, len(bits))
        return max_length
    


A_inp01 = "0000000"
A_inp02 = "1001000"
A_inp03 = "1111111"
A_inp04 = "1011000"
A_inp05 = "1011110"
A_inp06 = "1011110"
A_inp07 = "0011110"
A_inp08 = "0011111"
A_inp09 = "0000001"
A_inp10 = "1000001"
A_inp11 = "1000000"
A_inp12 = "1111100"
A_inp13 = "0001011"
A_inp14 = "0001010"
print(A_inp01, ":", solve(A_inp01))
print(A_inp02, ":", solve(A_inp02))
print(A_inp03, ":", solve(A_inp03))
print(A_inp04, ":", solve(A_inp04))
print(A_inp05, ":", solve(A_inp05))
print(A_inp06, ":", solve(A_inp06))
print(A_inp07, ":", solve(A_inp07))
print(A_inp08, ":", solve(A_inp08))
print(A_inp09, ":", solve(A_inp09))
print(A_inp10, ":", solve(A_inp10))
print(A_inp11, ":", solve(A_inp11))
print(A_inp12, ":", solve(A_inp12))
print(A_inp13, ":", solve(A_inp13))
print(A_inp14, ":", solve(A_inp14))