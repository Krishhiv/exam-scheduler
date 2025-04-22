# Exam Scheduling System

A Python application that automatically generates conflict-free exam schedules based on student course enrollments.

## Overview

This system analyzes student course enrollment data to identify potential exam conflicts (where students are enrolled in multiple courses) and creates an optimal exam schedule that minimizes the number of time slots needed while ensuring no student has overlapping exams.

## Features

- **Data Processing**: Parses CSV files containing student enrollment data
- **Conflict Detection**: Builds a graph representing course conflicts
- **Exam Scheduling**: Uses a greedy graph coloring algorithm to assign non-conflicting time slots
- **Visualization**: Generates a visual representation of course conflicts

## Requirements

The application requires Python 3.6+ and the following dependencies:
- matplotlib==3.10.1
- networkx==3.4.2
- numpy==2.2.5

You can install all dependencies using:
```
pip install -r requirements.txt
```

## Project Structure

- **`data_loading.py`**: Loads and processes student enrollment data from CSV files
- **`graph_building.py`**: Constructs a course conflict graph from enrollment data
- **`graph_colouring.py`**: Implements the greedy coloring algorithm to assign exam slots
- **`slots.py`**: Generates exam time slots starting from a specified date
- **`visualisation.py`**: Creates a visual representation of the course conflict graph
- **`Data/`**: Directory containing CSV files with student enrollment data

## How It Works

1. **Data Loading**: The system reads a CSV file containing student enrollment data (student names and their courses).

2. **Conflict Graph Construction**: A graph is created where:
   - Nodes represent courses
   - Edges connect courses taken by the same student (potential conflicts)

3. **Exam Scheduling**: A greedy graph coloring algorithm assigns time slots to courses:
   - Courses are sorted by degree (number of conflicts)
   - Each course is assigned the lowest-numbered time slot that doesn't conflict with adjacent courses

4. **Output**: The system generates a schedule showing each course and its assigned exam time slot

## Usage

1. Place your student enrollment data in a CSV file with columns: `name` and `course`
2. Update the file path in `data_loading.py` if needed
3. Run the application:

```
python graph_colouring.py
```

4. View the resulting exam schedule in the console output
5. For visualization of the conflict graph, the script will display a graph showing course relationships

## Example Data Format

```csv
name,course
Alice,CS101
Alice,MATH201
Bob,CS101
Bob,PHYS301
Charlie,MATH201
```

## Output Example

The system will output something like:

```
Course: CS101, Exam Time: 2025-05-01 09:00 AM - 12:00 PM
Course: MATH201, Exam Time: 2025-05-01 02:00 PM - 05:00 PM
Course: PHYS301, Exam Time: 2025-05-01 09:00 AM - 12:00 PM
Course: HIST101, Exam Time: 2025-05-01 09:00 AM - 12:00 PM
```

## Customization

- To change the exam period start date, modify the parameters in `slots.py`
- To use a different dataset, update the file path in `data_loading.py`
- To adjust the graph visualization, modify parameters in `visualisation.py`

## License

[Insert your chosen license here]

## Contributors

[Add contributor information if applicable]
