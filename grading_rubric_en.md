# Grading Rubric: Digital Library Management System

| # | Requirement Category | Task Description | Max Points |
|---|---|---|:---:|
| **Part 1** | **Version Control (Git & GitHub)** | | |
| 1 | GitHub Setup | Created a new private repository on GitHub | 1 |
| 2 | Collaboration | Invited the instructor as a collaborator | 1 |
| 3 | Branching (dev) | Cloned the repo and created the `dev` branch from `main` | 1 |
| 4 | Branching (feature) | Created the `feature/library-system` branch from `dev` | 1 |
| 5 | Commits | Made at least 10 meaningful commits with clear messages | 3 |
| 6 | Pull Request | Pushed all branches and opened a PR from `feature/library-system` to `dev` | 2 |
| **Part 2** | **Python OOP & Basics** | | |
| 7 | Abstract Base Class | `Item` class created correctly using the `abc` module | 2 |
| 8 | Initialization | `Item` class correctly initializes `title`, `author`, and `year` | 1 |
| 9 | Encapsulation | Private attribute `__is_checked_out` implemented with getter/setter | 2 |
| 10 | Abstract Method | `get_details()` defined as an abstract method in `Item` class | 1 |
| 11 | Inheritance | Derived classes `Book` and `Magazine` properly inherit from `Item` | 1 |
| 12 | Class Attributes | Derived classes implement additional attributes (`genre`, `issue_number`) | 1 |
| 13 | Polymorphism | `get_details()` is overridden in derived classes and returns an f-string | 2 |
| 14 | Library Data Structure | `Library` class uses a list or dictionary to store items | 1 |
| 15 | Library Methods | Logic to add, list, borrow, and return items works as intended | 3 |
| 16 | User Interface (CLI) | CLI implemented using a `while` loop, `input()`, `print()`, and conditionals | 3 |
| **Part 3** | **Exceptions** | | |
| 17 | Custom Exceptions | Created `ItemNotAvailableError` and `ItemNotFoundError` exceptions | 2 |
| 18 | Error Handling | `try/except` blocks effectively handle both custom and built-in exceptions | 2 |
| **Part 4** | **Unit Testing** | | |
| 19 | Test Setup | Test file exists and properly utilizes the built-in `unittest` module | 1 |
| 20 | Test Cases | Tests cover adding, borrowing, and verifying proper exceptions are raised | 4 |
| | | **Total Maximum Points** | **35** |
