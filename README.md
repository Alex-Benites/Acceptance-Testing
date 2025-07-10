# Acceptance Testing with BDD

This project demonstrates Behavior-Driven Development (BDD) using the Behave framework for a simple To-Do List Manager application.

## 📋 Project Overview

The To-Do List Manager is a command-line application that allows users to manage their tasks by adding, listing, and marking them as complete. This project focuses on implementing acceptance tests using BDD methodology.

## 🛠️ Requirements

- Python 3.7+
- behave library
- Visual Studio Code (recommended)

## 📦 Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd Acceptance-Testing
```

2. Install the required dependencies:
```bash
pip install behave
```

## 📁 Project Structure

```
Acceptance-Testing/
├── features/
│   ├── everything.feature      # Gherkin scenarios
│   └── steps/
│       └── steps.py           # Step implementations
├── README.md
└── main.py                    # (if applicable)
```

## 🚀 Running Tests

### ⚠️ Important Note
If the command `behave` doesn't work in your terminal, use the following alternative:

```bash
python -m behave
```

### Available Commands

- **Run all tests:**
```bash
python -m behave
```

- **Run tests with verbose output:**
```bash
python -m behave -v
```

- **Dry run (check scenarios without execution):**
```bash
python -m behave --dry-run
```

- **Generate HTML report:**
```bash
python -m behave --format=html --outfile=report.html
```

## 🧪 Test Scenarios

The project includes 6 test scenarios:

### Basic Scenarios (4):
1. **Adding a task** - Add task to empty list
2. **Listing tasks** - Display all existing tasks
3. **Marking a task as complete** - Mark task as completed
4. **Removing a task** - Delete task from list

### Additional Scenarios (2):
5. **Adding a task to non-empty list** - Add task when list already contains items
6. **Attempting to mark non-existent task as complete** - Error handling for invalid operations

## 📊 Test Results

Last execution results:
- ✅ 1 feature passed
- ✅ 6 scenarios passed
- ✅ 19 steps passed
- ⏱️ Execution time: 0.005s

## 🔧 Troubleshooting

### Command Not Found Error
If you get `'behave' is not recognized as an internal or external command`, use:
```bash
python -m behave
```

### No Feature Files Found
Ensure you're running the command from the project root directory (where the `features/` folder is located).

### Path Issues
Make sure your Python installation includes the Scripts directory in your PATH, or use the `python -m behave` approach.

## 📚 Framework Information

- **BDD Framework:** Behave
- **Language:** Gherkin (for scenarios) + Python (for implementation)
- **Test Type:** Acceptance Testing
- **Methodology:** Behavior-Driven Development

## 🎯 Key Features

- **Natural language scenarios** using Gherkin syntax
- **Automated test execution** with detailed reporting
- **Error handling validation** for edge cases
- **Comprehensive coverage** of main functionalities

## 👥 Authors

- [Alex Benites Segura] - ESPOL Software Engineering II

## 📄 License

This project is part of an academic assignment for Software Engineering II course