student_score = float(input())
maximum_score = float(input())

percentage = student_score / maximum_score

if 0.9 <= percentage:
    print('A')
elif 0.8 <= percentage:
    print('B')
elif 0.7 <= percentage:
    print('C')
elif 0.6 <= percentage:
    print('D')
else:
    print('F')
