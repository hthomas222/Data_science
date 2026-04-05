import pandas as pd
import numpy as np
from rich import print

df = pd.read_csv("grades_data.csv")
student_grade = df[['Student_ID','Test_1', 'Test_2','Test_3']].set_index("Student_ID")

scores = student_grade[["Test_1","Test_2", "Test_3"]]
tot = scores.sum(axis=0)

print("[green]Sum of Test:[/green]")
print(tot.to_string())
print()

print("[green]Sum per student:[/green]")
student = student_grade.sum(axis=1)
print(student.to_string())

print()
print("[green]Mean per student grades:[/green]")
student = student_grade.mean(axis=1)
print(student.to_string())
