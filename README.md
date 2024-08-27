# Gauss Jordan Elimination Numerical Method Implementation in Python

This repository contains a Python implementation of the Gauss-Jordan Elimination method for solving systems of linear equations. The code reads coefficients from an Excel file (`read.xls`), performs Gauss-Jordan Elimination to reduce the matrix to reduced row echelon form, and saves the results back into the Excel file.

### Table of Contents
- [Gauss-Jordan Elimination Theory](#gauss-jordan-elimination-theory)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Example](#example)
- [Files in the Repository](#files-in-the-repository)
- [Input Parameters](#input-parameters)
- [Troubleshooting](#troubleshooting)
- [Author](#author)

### Gauss-Jordan Elimination Theory
Gauss-Jordan Elimination is an algorithm to solve systems of linear equations and to invert matrices. It is an extension of Gaussian Elimination. The goal of the procedure is to transform the augmented matrix into reduced row echelon form (RREF) using elementary row operations.

**Steps:**
1. **Forward Elimination**: Transform the system into an upper triangular matrix.
2. **Backward Elimination**: Continue transforming the matrix until it becomes the identity matrix.
3. **Normalization**: Divide each row by the diagonal element to obtain a row of the identity matrix.

### Dependencies
To run this code, you need the following libraries:
- `numpy`
- `xlrd`
- `xlutils`

### Installation
To install the required libraries, you can use `pip`:
```sh
pip install numpy xlrd xlutils
```

### Usage
1. Clone the repository.
2. Ensure the script and the Excel file (`read.xls`) are in the same directory.
3. Run the script using Python:
    ```sh
    python gauss_jordan_elimination.py
    ```
4. The script will read the coefficients from the Excel file, perform Gauss-Jordan Elimination, and write the results back into the Excel file.

### Code Explanation
The code begins by importing the necessary libraries and reading the matrix of coefficients and constants from the Excel file. It then performs Gauss-Jordan Elimination to transform the system into reduced row echelon form and saves the results into the same Excel file.

Below is a snippet from the code illustrating the main logic:

```python
import xlrd
import numpy as np
from xlrd import open_workbook
from xlutils.copy import copy

workbook = xlrd.open_workbook('read.xls')
sheet = workbook.sheet_by_index(0)

arr = np.zeros((sheet.nrows, sheet.ncols))
arr2 = np.zeros((sheet.nrows, sheet.ncols))

# Taking excel data into numpy array
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        arr[i][j] = sheet.cell_value(i, j)
        arr2[i][j] = sheet.cell_value(i, j)

# Calculate Echelon Matrix Forward
for k in range(0, sheet.ncols):
    for i in range(k + 1, sheet.nrows):
        temp = arr2[k][k] / arr2[i][k]
        for j in range(k, sheet.ncols):
            arr2[i][j] = (temp) * arr2[i][j]
            arr2[i][j] = arr2[i][j] - arr2[k][j]

# Calculate Echelon Matrix Backward
for k in range(0, sheet.ncols):
    for i in range(k + 1, sheet.nrows):
        temp = arr2[i][i] / arr2[k][i]
        for j in range(0, sheet.ncols):
            arr2[k][j] = (temp) * arr2[k][j]
            arr2[k][j] = arr2[k][j] - arr2[i][j]

# Calculate Identity
for i in range(sheet.nrows):
    temp = arr2[i][i]
    for j in range(sheet.ncols):
        arr2[i][j] = arr2[i][j] / temp

rb = open_workbook("read.xls")
wb = copy(rb)
sheet1 = wb.get_sheet(1)

# Clearing all data of excel
for i in range(100):
    for j in range(100):
        sheet1.write(i, j, '')

# Write results to Excel
for i in range(sheet.nrows):
    for j in range(sheet.ncols):
        sheet1.write(i, j, arr2[i][j])

wb.save('read.xls')
```

The code completes by saving the final results into the Excel file `read.xls`.

### Example
Below is an example of how to use the script:

1. Prepare the `read.xls` file with the system of equations in matrix form.
2. **Run the script**:
    ```sh
    python gauss_jordan_elimination.py
    ```

3. **Output**:
    - The script will compute the results using the Gauss-Jordan Elimination method and write the intermediate and final results into the Excel file (`read.xls`).

### Files in the Repository
- `gauss_jordan_elimination.py`: The main script for performing the Gauss-Jordan Elimination method.
- `read.xls`: Excel file from which the matrix data is read and into which the results are written.

### Input Parameters
The initial input data is expected to be in the form of a matrix within the `read.xls` file. Each row represents coefficients of the variables in the equations along with the constants.

### Troubleshooting
1. **Excel File**: Ensure that the input matrix is correct and placed in the `read.xls` file.
2. **Matrix Format**: Confirm that the matrix is complete and correctly formatted.
3. **Excel File Creation**: Ensure you have write permissions in the directory where the script is run to save the Excel file.
4. **Python Version**: This script is compatible with Python 3. Ensure you have Python 3 installed.

## Author
Script created by sudipto3331.

---

This documentation should guide you through understanding, installing, and using the Gauss-Jordan Elimination method script. For further issues or feature requests, please open an issue in the repository on GitHub. Feel free to contribute by creating issues and submitting pull requests. Happy coding!
