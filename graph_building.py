from data_loading import students_courses
from visualisation import visualise  # Import the visualisation module

# Create the graph
graph = {}

for courses in students_courses.values():
    for i in range(len(courses)):
        for j in range(i + 1, len(courses)):
            course1 = courses[i]
            course2 = courses[j]

            if course1 not in graph:
                graph[course1] = set()
            graph[course1].add(course2)

            if course2 not in graph:
                graph[course2] = set()
            graph[course2].add(course1)

# Call the visualise function to display the graph
visualise(graph)
