def grade(m):
    if (m>=80):
        return "A+"
    elif 100<=m>=75:
        return "A"
    elif m>=70:
        return "A-"
    elif m>=65:
        return "B+"
    elif m>=60:
        return "B"
    elif m>=55:
        return "B-"
    elif m>=50:
        return "C+"
    elif m>=45:
        return "C"
    elif m>=40:
        return "D"
    else :
        return "F"
def point(m):
        if 100<=m>= 80:
            return 4.00
        elif m>= 75:
            return 3.75
        elif m>= 70:
            return 3.50
        elif m>= 65:
            return 3.25
        elif m>=60:
            return 3.00
        elif m>= 55:
            return 2.75
        elif m>=50:
            return 2.50
        elif m>=45:
            return 2.25
        elif m>= 40:
            return 2.00
        else:
            return 0
m=int(input("Enter The Marks = ?"))
print("Your Grade =",grade(m),"And poin =",point(m))
            