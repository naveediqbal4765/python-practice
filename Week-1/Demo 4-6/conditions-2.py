# 2. Grades. Given marks, print A for 80 and above, B for 65–79, C for 50–64 and Fail below 50.
#  Test with exactly 80, 79, 50 and 49. Boundary values are where bugs hide.

marks = 79

if marks >= 80:
    print ("Grade A")

elif marks > 64:
    print ("Grade B")

elif marks >= 50:
    print ("Grade C")

else:
    print ("fail")