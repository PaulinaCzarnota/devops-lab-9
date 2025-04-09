This repository contains my Lab 9 solution for the Introduction to DevOps module in the third year of the Computer Science course at Technological University Dublin (TU Dublin).

# Overview

The goal of this lab is to demonstrate the ability to:

- Implement a working solution to a logic-based puzzle (Sudoku)
- Create comprehensive unit tests to validate program correctness
- Set up and use GitHub Actions for continuous integration (CI) and automated testing

# Key Tasks

- Developed a Sudoku Solver in Python using recursive backtracking
- Wrote unit tests using Python’s `unittest` module to validate multiple puzzle scenarios
- Configured GitHub Actions CI workflow to run tests automatically on every push or pull request to the repository
- Used test cases inspired by:
  - [sudoku.com](https://sudoku.com)
  - [anysudokusolver.com](https://anysudokusolver.com)
  - [RosettaCode - Python Sudoku](https://rosettacode.org/wiki/Sudoku#Python)

# Technologies Used

- Python 3.10+
- unittest module
- Git & GitHub
- GitHub Actions

# CI/CD Pipeline

On every push or pull request to the `main` branch, GitHub Actions will automatically:

- Set up Python 3.10
- Run all unit tests using `python -m unittest discover`
- Validate that the code runs successfully and passes all test cases

This lab highlights the importance of **automated testing** and **CI/CD pipelines** in modern software development workflows.

# How to Run Locally (Optional)

```bash
# Clone the repository
git clone https://github.com/PaulinaCzarnota/devops-lab-9.git
cd devops-lab-9

# Run tests locally
python -m unittest discover