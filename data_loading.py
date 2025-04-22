import csv

students_courses = {}

with open("./small-test-set.csv", "r") as f:
    reader = csv.DictReader(f)

    for row in reader:
        student = row["name"]
        course = row["course"]

        if student not in students_courses:
            students_courses[student] = []
        students_courses[student].append(course)

