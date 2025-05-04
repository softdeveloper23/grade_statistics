# Grade Statistics Application Enhanced (MOOC 2024)

A beginner-friendly Python application that collects student exam results and exercise completion data, then calculates grades, averages, pass percentages, and grade distributions.

This project was created to practice fundamental Python concepts including input handling, conditionals, loops, functions, error checking, and basic statistics.

## 📌 Features

- Collects multiple students’ exam and exercise results
- Validates user input with helpful error messages
- Calculates:
  - Exercise points (1 point per 10 exercises)
  - Total course points
  - Course grade (scale 0–5)
  - Average of total points
  - Pass percentage
  - Grade distribution
- Displays individual results for each student
- Modular code with clear, reusable functions and comments
- Beginner-friendly structure and logic

## 🚀 How to Run

Make sure you have Python 3 installed on your machine.

1. Clone or download this repository.
2. Open a terminal and navigate to the project folder.
3. Run the script: python grade_statistics.py

Follow the prompts to enter student data.

## 💡 Example

How many results would you like to enter? 2
(1) Enter the exam points: 25
(1) Enter the exercises completed: 80
(2) Enter the exam points: 10
(2) Enter the exercises completed: 50

Statistics:
Points average: 27.5
Pass percentage: 100.0
Grade distribution:
  5: *
  4: 
  3: 
  2: 
  1: 
  0: *

Individual results:
  Student 1: Exam 25 + Exercises 8 = Total 33 → Grade 5
  Student 2: Exam 10 + Exercises 5 = Total 15 → Grade 1

## 🧠 How Grades Are Calculated
Exercise Points: exercises_completed // 10

Total Points = Exam Points + Exercise Points

Grade Scale:

0–14 → Grade 0 (Fail)

15–17 → Grade 1

18–20 → Grade 2

21–23 → Grade 3

24–27 → Grade 4

28–30+ → Grade 5

## 📂 File Structure

grade_statistics/
grade_statistics.py   # Main Python script

README.md             # This file
            
## 🛠️ Tech Used
Python 3

Standard library only (no external packages required)

## 📚 Lessons Learned
Importance of clear function names

Using try/except for safe input handling

Organizing code with small, focused functions

Handling edge cases and user errors

Iterative refactoring improves readability and maintainability

## ✅ To-Do (Future Ideas)
Save results to a CSV or text file

Add a basic GUI with tkinter

Add colorized terminal output (using colorama)

Add unit tests for functions

## 👤 Author
Brannon Garrett

Python Developer

softdeveloper23 on GitHub
