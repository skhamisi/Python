def convert(avg):
    if avg >= 90 : grade = 'A'
    elif avg < 90 and avg >= 80 : grade = 'B'
    elif avg < 80 and avg >= 70 : grade = 'C'
    elif avg < 70 and avg >= 60 : grade = 'D'
    elif avg < 60 and avg >= 0 : grade = 'F'
    print(grade)

convert(89)

