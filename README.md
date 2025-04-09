This repository contains my Lab 9 - Software Unit Testing solution for the Introduction to DevOps module in the third year of the Computer Science course at TU Dublin.

# Overview

The purpose of this lab is to demonstrate the ability to:
- Implement a working solution to a logic-based puzzle (Sudoku)
- Create comprehensive unit tests to validate program correctness
- Set up and use GitHub Actions for continuous integration and automated testing

# Key Tasks

- Developed a Sudoku Solver using Python with recursive backtracking
- Wrote Unit Tests using Python’s unittest module to test various puzzle conditions
- Configured GitHub Actions CI (.github/workflows/sudoku-tests.yml) to run tests automatically on every push or pull request
- Used test cases inspired by:
  - sudoku.com
  - anysudokusolver.com
  - RosettaCode Python Sudoku

# Technologies Used

- Python 3.10+
- unittest module
- Git and GitHub
- GitHub Actions

# CI/CD Pipeline

On every push to the main branch, GitHub Actions will:
- Set up Python 3.10
- Run all test cases using python -m unittest discover
- Confirm the code is valid and all tests pass

This lab highlights the importance of automated testing and CI/CD in modern software engineering workflows.