"""
Create a function that displays all different combinations of three different digits in ascending order, listed by ascending order

ex: 012, 013, 014, 015, 016, 017, 018, 019, 023, ..., 789

notes:   
    987 isn't there because 789 already is
    999 isn't there because the digit 9 is present more than once
"""

def solution():
    combos = []

    x = 0

    while x <= 7:
    y = x + 1
    while y <= 8:
        z = y + 1
        while z <= 9:
        combos.append(f"{x}{y}{z}")
        z += 1
        y += 1
    x += 1

    print(", ".join(combos))

