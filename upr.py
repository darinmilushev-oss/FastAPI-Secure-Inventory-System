score = int(input("Score:"))
if score <= 100 and score >= 90:
    print("Grade A")
elif score < 90 and score >= 80:
    print("grade B")
elif score < 80 and score >= 70:
    print("grade C")
else:
    print("Error")