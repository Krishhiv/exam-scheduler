# Exam Scheduling System

This Python application automatically generates a conflict-free exam schedule based on student course enrollment data provided as a CSV file.

## Overview

This system analyses student course enrollment data to identify potential exam conflicts (where students are enrolled in multiple courses). It creates an optimal exam schedule that minimises the time slots needed while ensuring no student has overlapping exams.

## Features

- **Data Processing**: It parses CSV files containing student enrollment data and stores it as a dictionary.
- **Conflict Detection**: This builds a graph where the vertices are courses and the edges connect a course to the conflicting courses.
- **Exam Scheduling**: A greedy colouring algorithm is used to assign non-conflicting time slots.
- **Visualisation**: Generates a visual representation of course conflicts using `networkx` and `matplotlib`.

## Requirements

The application requires Python 3.6+ and the following dependencies:
- matplotlib==3.10.1
- networkx==3.4.2
- numpy==2.2.5

You can install all dependencies using:
```
pip install -r requirements.txt
```

## Modules

- **`data_loading.py`**: This module loads and processes the student enrollment data from CSV files.
- **`graph_building.py`**: Constructing a course conflict graph from enrollment data.
- **`graph_colouring.py`**: Implements the greedy colouring algorithm to assign exam slots.
- **`slots.py`**: It generates exam time slots starting from a specified date.
- **`visualisation.py`**: Creates a visual representation of the course conflict graph.
- **`Data/`**: Directory containing different test CSV files.

## How It Works

1. **Data Loading**: The system reads a CSV file containing student enrollment data (student names and their courses).

2. **Conflict Graph Construction**: A graph is created where:
   - Vertices represent courses.
   - Edges connect courses taken by the same student.

3. **Exam Scheduling**: A greedy graph colouring algorithm assigns data and time slots to courses:
   - Courses are sorted by degree (number of edges connected to a vertex).
   - Each course is assigned the lowest-numbered time slot that doesn't conflict with adjacent courses

4. **Output**: The system generates a schedule showing each course and its assigned exam time slot

## Usage

1. Place the student enrollment data in a CSV file with columns: `name` and `course`
2. Update the file path in `data_loading.py` if needed
3. Run the application:

```
python graph_colouring.py
```

4. View the resulting exam schedule in the console output
5. For visualisation of the conflict graph, the script will display a graph showing course relationships

## Example Data Format (small-test-set.csv)

```csv
name,course
Alice,CS101
Alice,MATH201
Bob,CS101
Bob,PHYS301
Charlie,MATH201
Charlie,PHYS301
Charlie,HIST101
```

## Output Example

The system will output the adjacency list first. Then, we see the visualisation of the graph. Finally, we get the exam schedule, which will look as follows for the dataset mentioned above:

```
Course: MATH201, Exam Time: 2025-05-01 09:00 AM - 12:00 PM
Course: PHYS301, Exam Time: 2025-05-01 02:00 PM - 05:00 PM
Course: CS101, Exam Time: 2025-05-02 09:00 AM - 12:00 PM
Course: HIST101, Exam Time: 2025-05-02 09:00 AM - 12:00 PM
```

## Customization

- To change the exam period start date, modify the parameters in `slots.py`
- To use a different dataset, update the file path in `data_loading.py`
- To adjust the graph visualisation, modify parameters in `visualisation.py`

