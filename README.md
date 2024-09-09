[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![License: Apache-2-License](https://img.shields.io/badge/Licence-Apache--2--Licence-green.svg)](https://www.apache.org/licenses/LICENSE-2.0)
[![Platform: Linux](https://img.shields.io/badge/Platform-Linux-yellow.svg)](https://www.linux.org/)
[![Merge Sort Test](https://github.com/CSC510-GROUP-40/Homework_2/actions/workflows/main.yml/badge.svg)](https://github.com/CSC510-GROUP-40/Homework_2/actions/workflows/main.yml)
[![Coverage Status](https://coveralls.io/repos/github/CSC510-GROUP-40/Homework_2/badge.svg?branch=main)](https://coveralls.io/github/CSC510-GROUP-40/Homework_2?branch=main)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
![pylint](https://img.shields.io/badge/PyLint-10.00-brightgreen?logo=python&logoColor=white)
![autopep8](./autopep8.svg)
# Homework 2 - Debugging

## Project Overview
This project focuses on debugging a faulty `mergeSort` implementation in `hw2_debugging.py` and ensuring the code quality through automated tools. 
The following are the tasks that were performed:
- Automatically format python code to conform to the PEP 8 style guide Using AutoPep8.
- Used Pylint to check for programming errors, enforce a coding standard, finds code smells, which are indications of deeper problems in a system.
- Used Bandit to check for common security issues in python code
- Fixed issues based on the analysis tools' recommendations.
- Fix the bug in the mergeSort Implementation.  
- Writing test cases for `mergeSort` to verify its correctness.
- Configuring continuous integration (CI) to automatically run the analysis tools and test cases on every commit.


## Getting Started

### Prerequisites

- Python 3.13
- `pytest` for running the test cases

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CSC510-GROUP-40/Homework_2.git
   cd Homework_2
2. Install Dependencies by running 'pip install -r requirements.txt'

### Execute AutoPep8 and Two (2)Static Analysis Tools
- Use the following tools to analyze the code:
  1. **AutoPep8**: Automatically formats the code to conform with the PEP8 style guide.
  2. **Pylint**: A static analysis tool to identify errors, style issues, and other potential problems in Python code.
  3. **Bandit**: Finds common security issues in python code.
  
To run these tools, use the following commands:
`bash
autopep8 --in-place --aggressive hw2_debugging.py rand.py
pylint hw2_debugging.py rand.py
bandit hw2_debugging.py rand.py
'
### Contributing
Contributions to the Merge Sort Program are welcome! If you have suggestions for improvements or new features, please fork the repository and create a pull request. You can also open an issue to discuss your ideas.

To Contribute
- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes and commit them (git commit -m 'Add some feature').
- Push to the branch (git push origin feature-branch).
- Open a pull request.


### License
This project is licensed under the Apache License 2.0 See the LICENSE file for more details.

### Contact Information
In case of any issues, please raise an issue on this repository.
Our team of developers monitors the issues and would be happy to answer any and all questions you have about this project!