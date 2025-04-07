from collections import deque


def is_palindrom(string):
    formatted_string = ''.join(string.lower().split())

    dq = deque(formatted_string)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
    

input_string = "Was it a cAr or acat I saw"
if is_palindrom(input_string):
    print("Рядок є паліндромом.")
else:
    print("Рядок не є паліндромом.")