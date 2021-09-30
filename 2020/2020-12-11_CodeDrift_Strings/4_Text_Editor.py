def solve(A):
    count = 0
    editor = ""
    buffer = ""
    i = 0
    while i < len(A) and editor != A:
        if i == 0:
            # append char to editor
            editor += A[i]
            count += 1
            i += 1
        elif i == 1:
            # append char to editor
            editor += A[i]
            count += 1
            i += 1
        else:
            if buffer != "" and A.startswith(buffer, i) and (buffer not in editor or len(buffer) * 2 >= len(editor) or (not A.startswith(editor, i)) and len(editor) >= 3):
                # copy buffer to editor
                editor += buffer
                count += 1
                i += len(buffer)
            elif A.startswith(editor * 2, i):
                # copy string to buffer
                buffer = editor
                count += 1
            elif A.startswith(editor, i) and len(editor) >= 3:
                # copy string to buffer
                buffer = editor
                count += 1
            else:
                # append char to editor
                editor += A[i]
                buffer = ""
                count += 1
                i += 1
        print(count, "String:", A, "Editor:", editor, "Buffer:", buffer, "i =", i)
    return count



A_inp01 = "abababababab"
A_inp02 = "aaaabaaaab"
A_inp03 = "abababab"
A_inp04 = "abcabc"
A_inp05 = "aibaibaaibaibayaibaibaaibaibayai"
print(A_inp01, ":", solve(A_inp01))
print(A_inp02, ":", solve(A_inp02))
print(A_inp03, ":", solve(A_inp03))
print(A_inp04, ":", solve(A_inp04))
print(A_inp05, ":", solve(A_inp05))