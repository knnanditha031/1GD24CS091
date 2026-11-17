marks=int(input("Enter your marks:"))
if marks>=100 or marks<0:
    print("Invalid marks")
elif marks>=90 and marks<=100:
    print("Grade A")
elif marks>=70 and marks<=89:
    print("Grade B")
elif marks>=60 and marks<=74:
    print("Grade c")
elif marks>=50 and marks<59: 
    print("Grade d")
else:
    print("Fail")