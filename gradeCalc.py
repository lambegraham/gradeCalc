def avg(lst):
    return sum(lst) / len(lst)

numSubjects = input("Please input the amount of subjects you have:")
gradeList = []

for x in range(int(numSubjects)):
    print("Enter your grade for subject " + str(x) + ": ")
    gradeList.append(int(input()))


print("Your average grade is: " + str(avg(gradeList)))