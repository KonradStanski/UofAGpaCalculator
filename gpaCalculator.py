# Guick little gpa calculator
# Parse copied text. use: https://regexr.com/ to make the regular expresison
import re

courses = []
with open("transcript.txt", "r") as transcript:
	lines = transcript.read().splitlines()
	for line in lines:
		# https://regexr.com/ is used to edit this regex
		if re.search(r'[\w\s]{6}\d{3}\s{3}.{26}\w[R\+\-\s]\s{7}\d\.\d\s{5}\d.\d\s{3}[\s\d\.]{5}\s{4}[\dX\.]{3}\s{4}[\d\s]{3}', line):
			courses.append(line)

# Print courses
print("                                      Grade  Units   Units   Grade  Class  Class")
print("Course      Description               Remark Taken  Passed  Points    Avg   Enrl")
for line in courses:
	print(line)

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

# Extract grades and credit weights
print("\n           Letter\nCourse:    Grade: Weight: Remark:")
gradeRemark = []
unitsPassed = []

for line in courses:
	letterGrade = line[38:40].strip()
	if letterGrade == "W":
		continue
	print(line[0:10] + " " + letterGrade.ljust(7 , " ") + line[55:58].ljust(8, " ") + str(gradeDict[letterGrade]))
	gradeRemark.append(gradeDict[letterGrade])
	unitsPassed.append(float(line[55:58].strip()))
	# gradePoints.append(float(line[61:66].strip()))

# Get list of multiplied values
mult = []
for i in range(len(gradeRemark)):
	mult.append(float(gradeRemark[i]*float(unitsPassed[i])))

# Formula used is sum(grade*weight)/sum(weights)
gpa = sum(mult)/sum(unitsPassed)
print("\nYour Final Overall GPA is:", gpa)
