# Issues to create on GitHub (copy each into New Issue)

## Issue #1: average() returns the wrong value
`average([80, 90, 100])` should return 90 but returns 67.5.
Expected: sum divided by number of grades.

## Issue #2: average() crashes on an empty list
`average([])` should return 0 instead of raising an error.

## Issue #3: letter_grade() wrong at boundaries
A score of exactly 90 should be "A", 80 -> "B", 70 -> "C", 60 -> "D".
Currently each boundary drops to the lower grade.

## Issue #4 (feature): add lowest() function
Add `lowest(grades)` to grades.py that returns the minimum grade.
