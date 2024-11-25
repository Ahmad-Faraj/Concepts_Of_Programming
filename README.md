# Python Programs for Daily Steps Tracker, Library Book Borrowing Analysis, and Word Scramble Game

This repository contains solutions to three distinct problems: **Daily Steps Tracker**, **Library Book Borrowing Analysis**, and **Word Scramble Game**. Each program performs data processing and provides meaningful insights based on user input.


## Video Tutorial

For a more detailed explanation, you can check out the video tutorials below:

- [Watch the First Video Tutorial](https://drive.google.com/file/d/1npZM1g5sEDLxwZa0cSkgArQOeeBPGdD7/view?usp=drive_link)
- [Watch the Second Video Tutorial](https://drive.google.com/file/d/1PfS9Q-s70uwQgT0_jET0uEis425I25pZ/view?usp=drive_link)

---

## Problem 1: Daily Steps Tracker

### Description
This program allows users to input the number of steps they take each day over a month and provides the following insights:
1. The highest and lowest step counts.
2. The average daily step count.
3. The list of step counts sorted in descending order.

### Features
- Accepts daily step counts as space-separated input.
- Identifies the day with the highest and lowest steps.
- Calculates the average daily steps.
- Sorts the step counts in descending order for analysis.

### How to Run
1. Run the program in a Python environment.
2. Enter the daily step counts as space-separated values when prompted.
3. The program will display the calculated results.

---
---

## Problem 2: Library Book Borrowing Analysis

### Description
This program analyzes borrowing records from a library for a month. Users input records in the format `"Book Title - Days Borrowed"`, and the program provides the following:
1. The most borrowed and least borrowed books.
2. The average number of days books were borrowed.
3. A list of unique book titles borrowed.
4. The books sorted by borrowing duration in descending order.

### Features
- Parses user input to process borrowing records.
- Handles multiple records for the same book by summing the borrowing days.
- Identifies the book borrowed for the maximum and minimum number of days.
- Sorts the books based on borrowing duration.

### How to Run
1. Run the program in a Python environment.
2. Enter book borrowing records one by one in the format `"Book Title - Days Borrowed"`.
3. Press **Enter** on an empty line to finish input.
4. The program will display the calculated results.

---
---

# Word Scramble Game

This is a Python-based word scramble game where players try to guess the original word from a randomly scrambled version. The game uses a **visited array** technique to ensure a unique, randomized scramble for each word.

---

## Features

1. **Word Scrambling**:
   - Characters are shuffled into random positions using a visited array.
   - Ensures each character is used exactly once.
2. **Interactive Gameplay**:
   - Players have 5 attempts to guess the correct word.
   - Provides feedback after each incorrect guess, including the number of attempts remaining.
3. **Robust Input Handling**:
   - Handles empty inputs gracefully by prompting the user to enter a valid guess.
   - Case-insensitive input comparison.
4. **Random Word Selection**:
   - Words are selected randomly from a predefined list.

---

## How It Works

1. The program starts by selecting a random word from a predefined list.
2. The word is scrambled using the **visited array** technique:
   - A boolean array tracks whether each position has been filled.
   - Characters are placed in random indices until the entire array is filled.
3. The scrambled word is displayed to the player.
4. The player has up to 5 attempts to guess the original word:
   - If the guess is correct, a congratulatory message is displayed.
   - If the attempts run out, the correct word is revealed.

---

