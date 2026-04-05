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
print()

top_student = student.idxmax()
top_mean = student.max()
print(f"[bold green]Highest performing student: [/bold green]\n[bright_cyan]{top_student}[/bright_cyan][bold green] with a grade of[/bold green] [bright_cyan] {top_mean:.2f}[/bright_cyan]")
print()

bottom_student = student.idxmin()
bottom_mean = student.min()
print(f"[bold green]Lowest performing student: [/bold green]\n[bright_cyan]{bottom_student}[/bright_cyan][bold green] with a grade of[/bold green] [bright_cyan] {bottom_mean:.2f}[/bright_cyan]")
