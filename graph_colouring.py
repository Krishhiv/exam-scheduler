from graph_building import graph
from slots import exam_slots

def greedy_coloring(graph):
    """ Sorting the vertices in descending order of degrees"""
    sorted_courses = sorted(graph.keys(), key=lambda x: len(graph[x]), reverse=True)

    """ Colouring the vertices of the graph """
    course_colors = {}

    """ Iterating over the vertices (courses) """
    for course in sorted_courses:
        """ Find the colours of adjacent (clashing) courses """
        adjacent_colors = set()

        for neighbor in graph[course]:
            if neighbor in course_colors:
                neighbor_color = course_colors[neighbor]
                adjacent_colors.add(neighbor_color)


        """ Assigning the smallest colour possible """
        color = 1
        while color in adjacent_colors:
            color += 1
        course_colors[course] = color

    return course_colors

print()

course_colors = greedy_coloring(graph)

print("Final Slots:")
print()
for course, slot_num in course_colors.items():
    print(f"Course: {course}, Exam Time: {exam_slots[slot_num]}")

print()