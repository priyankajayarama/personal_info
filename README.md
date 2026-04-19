# Personal Information Manager

> My first Python project — a simple program that stores and displays personal information.

**Author:** Priyanka Jayarama
**Week:** 1 — Python Basics

---

## 📖 Project Description

This program demonstrates the fundamentals of Python by storing personal information in variables, collecting additional details from the user, and displaying everything in a nicely formatted output. It's built as the first project in my Python learning journey.

---

## 🎯 What I Learned

- **Variables** — how to store different types of data (strings, integers)
- **Data types** — the difference between text and numbers in Python
- **Input/Output** — using `input()` to collect user data and `print()` to display it
- **String formatting** — using f-strings to cleanly insert variables into text
- **While loops** — repeating a prompt until valid input is received
- **Input validation** — catching empty input and whitespace-only input with `.strip()`
- **String methods** — using `.capitalize()` to format text nicely
- **Comments** — documenting code so it's easy to read later

---

## 🛠️ How to Run

### Prerequisites
- Python 3.8 or higher installed ([download here](https://www.python.org/downloads/))

### Steps
1. Clone or download this repository
2. Open a terminal and navigate to the project folder:
   ---

## 🧪 Testing

The program was tested with the following inputs:

| Test Case | Input | Expected Behavior | Result |
|-----------|-------|-------------------|--------|
| Normal input | `pizza`, `blue` | Displays info correctly | ✅ Pass |
| Empty input | (press Enter) | Re-prompts user | ✅ Pass |
| Whitespace only | `"   "` | Re-prompts user | ✅ Pass |
| Long input | 50+ character string | Displays without breaking | ✅ Pass |
| Numbers/symbols | `123!@#` | Accepts as valid text | ✅ Pass |

See `test_inputs.txt` for the full list of test cases.

---

## 🧩 Challenges & Solutions

**Challenge 1:** The user could press Enter without typing anything, and the program would happily accept empty strings.
**Solution:** Added a `while` loop that keeps asking until the input is not empty.

**Challenge 2:** Even with the empty check, a user could type only spaces and bypass validation.
**Solution:** Used `.strip()` to remove whitespace before checking if the input is empty.

**Challenge 3:** User input came in with inconsistent capitalization (e.g., `PIZZA` vs `pizza`).
**Solution:** Used `.capitalize()` when displaying the values so output always looks tidy.

---
