# PyTutor

An interactive, terminal-based application designed to help users learn the fundamentals of Python programming step-by-step.

![Screenshot 2025-04-15 133143](https://github.com/user-attachments/assets/0740a7df-c84f-4ca4-a383-19f9bd1f6277)
![Screenshot 2025-04-15 133203](https://github.com/user-attachments/assets/4866cb44-e3b3-4237-bb36-f094b1418bb9)
![Screenshot 2025-04-15 133237](https://github.com/user-attachments/assets/b10bad54-fdee-4c72-ac8d-943ee38beb7b)
![Screenshot 2025-04-15 133259](https://github.com/user-attachments/assets/76f955f5-b512-4c05-a6d5-e0c5d1ec1057)


## Features

*   **Interactive Learning:** Learn Python directly within your terminal.
*   **Modular Content:** Lessons are organized into modules covering various Python topics (Basics, Variables, Strings, Conditionals, Loops, Data Structures, Functions, File I/O, Error Handling, Modules, OOP, etc.).
*   **Multiple Lesson Types:**
    *   **Explanations:** Clear descriptions of concepts with code examples.
    *   **Quizzes:** Multiple-choice questions to test understanding.
    *   **Coding Challenges:** Hands-on exercises where you write Python code directly in the terminal, with automatic output verification.
*   **Progress Tracking:** The application saves your completed lessons in `progress.json` so you can pick up where you left off.
*   **Enhanced UI:** Uses the `rich` library for a visually appealing and user-friendly terminal interface (with a basic fallback if `rich` is not installed).
*   **Easy Navigation:** Simple menu system to select modules and lessons.

## Requirements

*   Python 3.x
*   `rich` library (for the best experience)

## Installation

1.  Clone this repository or download the source files (`main.py`, `content.py`, `.gitignore`, `README.md`).
2.  Install the required `rich` library using pip:

> ```bash
> pip install rich
> ```

## Usage

1.  Navigate to the project directory in your terminal.
2.  Run the main script:

```bash
python main.py
