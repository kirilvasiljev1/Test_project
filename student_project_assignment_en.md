# Final Project: Digital Library Management System

## Overview
This project is designed to test your knowledge of Python Basics, Object-Oriented Programming (OOP), Exceptions, Unit Testing, and Version Control (Git/GitHub). You will build a simple command-line Digital Library Management System.

**Estimated Time to Complete:** 3-4 hours

## Part 1: Version Control (Git & GitHub) Requirements
1. **Repository Setup:** Create a new private repository on GitHub.
2. **Collaborator:** Invite your instructor to the repository as a collaborator.
3. **Branching Strategy:**
   - Clone the repository to your local machine.
   - Create a `dev` branch from `main`.
   - Create a new branch called `feature/library-system` from `dev`. You will do all your work on this feature branch.
4. **Commits:** Make at least **10 meaningful commits** as you progress through the project (e.g., "Add Book class", "Implement borrow exception", "Add unit tests").
5. **Pull Request:** Once the project is complete, push your branches to GitHub and open a **Pull Request** from `feature/library-system` to `dev`. 

## Part 2: Python OOP & Basics
Your system must include the following classes and concepts:

### 1. Abstract Base Class (`Item`)
- **Abstraction:** Create an abstract class `Item` using the `abc` module.
- It should have an `__init__` method accepting `title`, `author`, and `year`.
- Include a private attribute `__is_checked_out` (Encapsulation) which defaults to `False`. Provide getter and setter methods or properties to access/modify it safely.
- Define an abstract method `get_details()`.

### 3. Derived Classes (`Book` and `Magazine`)
- **Inheritance:** Both classes should inherit from `Item`.
- `Book` should have an additional attribute `genre`.
- `Magazine` should have an additional attribute `issue_number`.
- **Polymorphism:** Implement the `get_details()` method differently in each class to return a formatted f-string of the item's information.

### 4. The `Library` Class
- Use a **list** or **dictionary** to store the library items.
- Implement methods to:
  - Add an item to the library.
  - List all available items.
  - Borrow an item (changes the checkout status).
  - Return an item.

### 5. User Interface (Basics)
- Create a main script that runs a command-line interface (CLI) using a `while` loop.
- Use `print()`, `input()`, and `if/elif/else` statements to allow the user to choose actions (e.g., 1. View Library, 2. Borrow Item, 3. Return Item, 4. Exit).

## Part 3: Exceptions
- **Custom Exceptions:** Create at least two custom exceptions:
  - `ItemNotAvailableError`: Raised when a user tries to borrow an item that is already checked out.
  - `ItemNotFoundError`: Raised when a user tries to borrow or return an item that doesn't exist in the library.
- **Error Handling:** Use `try/except` blocks in your CLI to handle these custom exceptions, as well as built-in exceptions like `ValueError` (e.g., if a user inputs text instead of a menu number).

## Part 4: Unit Testing
- Create a separate test file (e.g., `test_library.py`).
- Use Python's built-in `unittest` module.
- Write tests for:
  - Successfully adding an item.
  - Successfully borrowing an item.
  - Attempting to borrow an item that is already checked out (verifying that `ItemNotAvailableError` is raised).
  - Attempting to borrow an item that does not exist.

## Submission
- Ensure all code is pushed to your remote `feature/library-system` branch.
- Create the Pull Request to `dev`.
- Submit the link to your Pull Request.
