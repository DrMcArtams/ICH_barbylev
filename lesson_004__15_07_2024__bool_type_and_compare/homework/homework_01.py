"""Даны формулы:
¬((A ∨ B) ∧ (C ∨ D))       и    ((¬A ∧ ¬B) ∨ (¬C ∧ ¬D)).
Используя закон Де Моргана, докажите, что эти формулы эквивалентны.

not((A or B) and (C or D))  и  ((not A and not B) or (not C and not D))

Законы Моргана:
not (A and B) == not A or not B
not (A or B) == not A and not B

Решение:
not((A or B) and (C or D)) == not (A or B) or not (C or D) ==
(not A and not B) or (not C and not D)
"""
