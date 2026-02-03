# test_calculator.py
import calculator
print(f"\n--- DEBUG: Starting test_calculator.py")
def test_add():
 assert calculator.add(2, 3) == 5
 assert calculator.add(-1, 1) == 0
def test_subtract():
 assert calculator.subtract(5, 3) == 2
