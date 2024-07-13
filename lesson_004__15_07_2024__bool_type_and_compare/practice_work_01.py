"""Даны формулы: ¬(A ∧ (B ∨ C)) и ((¬A ∨ ¬B) ∧ (¬A ∨ ¬C)).
Докажите эквивалентность этих формул, применяя закон Де Моргана.


Формулы: ¬(A ∧ (B ∨ C)) и ((¬A ∨ ¬B) ∧ (¬A ∨ ¬C))

Применяем закон Де Моргана к первой формуле:
¬(A ∧ (B ∨ C)) ≡ (¬A ∨ ¬(B ∨ C))

Согласно закону дистрибутивности  A ∨ ( B ∧ C )  ↔  ( A ∨ B ) ∧ ( A ∨ C )    получаем:

(¬A ∨ (¬B ∧ ¬C)) ≡ (¬A ∨ ¬B) ∧ (¬A ∨ ¬C)

Таким образом, левая часть (¬A ∨ ¬B) ∧ (¬A ∨ ¬C) равняется правой части  ((¬A ∨ ¬B) ∧ (¬A ∨ ¬C))

Что и требовалось доказать!

"""