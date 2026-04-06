import numpy as np
from rich.console import Console
from rich.table import Table


prices = np.array([
    [100, 105, 103, 110, 115, 113, 118, 120, 117, 122],  # Stock A
    [50,  48,  52,  55,  53,  50,  56,  58,  54,  60 ],  # Stock B
    [200, 195, 198, 205, 210, 208, 212, 215, 218, 225],  # Stock C
    [80,  82,  81,  85,  83,  87,  86,  88,  85,  90 ],  # Stock D
    [150, 148, 152, 150, 145, 147, 155, 160, 158, 162],  # Stock E
])

console = Console()
returns = prices.mean(axis=1)
count = 1
console.print("[cyan]Average Stock Prices:[/cyan]")
for i in returns:
	console.print(f"[green]stock[/green][blue] {count}[/blue][green] average is:[/green] [blue]{i}[/blue]")
	count += 1
print()

test = np.diff(prices, axis=1) / prices[:, :-1]
console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Stock", style="cyan", no_wrap=True)  # Stock labels column
table.add_column("Day 1", justify="right")
table.add_column("Day 2", justify="right")
table.add_column("Day 3", justify="right")
table.add_column("Day 4", justify="right")
table.add_column("Day 5", justify="right")
table.add_column("Day 6", justify="right")
table.add_column("Day 7", justify="right")
table.add_column("Day 8", justify="right")
table.add_column("Day 9", justify="right")

stocks = ['A', 'B', 'C', 'D', 'E']
for i, row in enumerate(test):
    formatted_row = ["Stock " + stocks[i]] + [f"{x:.2%}" for x in row]  # Add stock label first
    table.add_row(*formatted_row)

console.print(table)
