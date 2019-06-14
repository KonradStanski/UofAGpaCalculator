# Guick little gpa calculator
# Parse copy texted
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

# Print courses
print("                                      Grade  Units   Units   Grade  Class  Class")
print("Course      Description               Remark Taken  Passed  Points    Avg   Enrl")
for line in courses:
	print(line)

# Extract grades and credit weights
grades = []
credits = []
for i in range(len(courses)):
	grades.append(courses[i][38:40].strip())
	credits.append(float(courses[i][55:58].strip()))

# Convert to numbers for calculation
gradeDict = {
	"CR":4,
	"A+":4,
	"A":4,
	"A-":3.7,
	"B+":3.3,
	"B":3,
	"B-":2.7,
	"C+":2.3,
	"C":2,
	"C-":1.7,
	"D+":1.3,
	"D":1,
	"F":0
}

for i in range(len(grades)):
	grades[i] = gradeDict[grades[i]]

# Get list of multiplied values
mult = []
for i in range(len(grades)):
	mult.append(float(grades[i]*float(credits[i])))

# Calculate and print gpa
# Formula used is sum(grade*weight)/sum(weights)
gpa = sum(mult)/sum(credits)
print("\nYour Final Overall GPA is:", gpa)

