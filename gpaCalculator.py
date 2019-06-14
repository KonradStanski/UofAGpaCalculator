# Guick little gpa calculator
courses = []
with open("transcript.txt", "r") as transcript:
	lines = transcript.read().splitlines()
	# print(lines)
	courseFlag = False
	for line in lines:
		if line[0:6] == "Course":
			courseFlag = True
		if line[0:12] == "Term Average":
			courses.append(line)
			courseFlag = False
		if courseFlag:
			courses.append(line)
	if courseFlag:
		for line in reversed(courses):
			if line[0:12] != "Term Average":
				courses.pop()
			else:
				break
	remove = []
	for i in range(len(courses)):
		if courses[i][0:6] == "Course":
			remove.append(i)
		if courses[i][0:12] == "Term Average":
			remove.append(i)
		if courses[i][0:12] == "            ":
			remove.append(i)
	for index in sorted(remove, reverse=True):
		del courses[index]



print("                                      Grade  Units   Units   Grade  Class  Class")
print("Course      Description               Remark Taken  Passed  Points    Avg   Enrl")
for line in courses:
	print(line)

grades = []
credits = []
for i in range(len(courses)):
	grades.append(courses[i][38:40].strip())
	credits.append(float(courses[i][55:58].strip()))
	# print(grades[i] + " " + credits[i])

for i in range(len(grades)):
	grade = grades[i]
	if grade == "A+" or grade == "CR" or grade == "A":
		grades[i] = 4
	elif grade == "A-":
		grades[i] = 3.7
	elif grade == "B+":
		grades[i] = 3.3
	elif grade == "B":
		grades[i] = 3
	elif grade == "B-":
		grades[i] = 2.7
	elif grade == "C+":
		grades[i] = 2.3
	elif grade == "C":
		grades[i] = 2
	elif grade == "C-":
		grades[i] = 1.7
	elif grade == "D+":
		grades[i] = 1.3
	elif grade == "D":
		grades[i] = 1
	elif grade == "F":
		grades[i] = 0


# print(grades)
# print(credits)
# print(len(grades), len(credits))
mult = []
for i in range(len(grades)):
	mult.append(float(grades[i]*float(credits[i])))


gpa = sum(mult)/sum(credits)
print("\nYour Final Overall GPA is:", gpa)

