import numpy as np
import pandas as pd

num_students = 5
num_tests = 3

grades = np.array([
    [85, 90, 78],
    [70, 82, 75],
    [94, 96, 98],
    [60, 65, 58],
    [88, 82, 85]])

df = pd.DataFrame(
    grades,
    columns=[f'Test_{i+1}' for i in range(num_tests)]
)
df.insert(0, 'Student_ID', [f'Student_{i}' for i in range(num_students)])

df.to_csv('grades_data.csv', index=False)
print("Generated grades_data.csv")
