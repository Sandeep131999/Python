student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores)

#How sum works in python
sum = 0
for studentscore in student_scores :
    sum += studentscore

#PAUSE 1 - Max
#There are also a built-in Python methods called max()
# and min(), which allow you to pass in a List of numbers, and it will give you the highest number or the lowest number.
#print(max(student_scores))

other_Student_scores = [8,65,89,86,55,91,64,89]
#COMPLETE THIS CHALLENGE WITHOUT USING max()
findMax = 0
for Score in other_Student_scores:
    if Score > findMax:
        findMax = Score
print(findMax)