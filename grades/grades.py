import pandas as pd
import numpy as np
from rich.console import Console
from rich.table import Table
df = pd.read_csv("grades_data.csv")
student_grade = df[['Student_ID','Test_1', 'Test_2','Test_3']].set_index("Student_ID")

scores = student_grade[["Test_1","Test_2", "Test_3"]]
tot = scores.sum(axis=0)


console = Console()
print()

table = Table(title="[green]Sum of Test[/green]", show_header=True, header_style="bold cyan")
table.add_column("Test", style="bold dark_orange")
table.add_column("Sum", style="orchid2", justify="right")

for test_name, value in tot.items():
    table.add_row(test_name, str(value))

console.print(table)


student = student_grade.sum(axis=1)
console = Console()
table = Table(title="[green]Sum per student:[/green]", show_header=True, header_style="bold cyan")
table.add_column("Test", style="bold dark_orange")
table.add_column("Sum", style="orchid2", justify="right")

for test_name, value in student.items():
    table.add_row(test_name, str(value))

console.print(table)


student = student_grade.mean(axis=1)
console = Console()
table = Table(title="[green]Mean per student grades:[/green]", show_header=True, header_style="bold cyan")
table.add_column("Test", style="bold dark_orange")
table.add_column("Sum", style="orchid2", justify="right")

for test_name, value in student.items():
    value = f"{value:.2f}"
    table.add_row(test_name, str(value))
console.print(table)


top_student = student.idxmax()
top_mean = student.max()
console.print(f"[bold green]Highest performing student: [/bold green]\n[bright_cyan]{top_student}[/bright_cyan][bold green] with a grade of[/bold green] [bright_cyan] {top_mean:.2f}[/bright_cyan]")
print()

bottom_student = student.idxmin()
bottom_mean = student.min()
console.print(f"[bold green]Lowest performing student: [/bold green]\n[bright_cyan]{bottom_student}[/bright_cyan][bold green] with a grade of[/bold green] [bright_cyan] {bottom_mean:.2f}[/bright_cyan]")
