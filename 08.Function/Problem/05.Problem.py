def calculate_grade(marks):
    avg = sum(marks) / len(marks)
    
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

marks = [80, 90, 85]
print(calculate_grade(marks))
