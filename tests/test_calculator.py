import sys
from io import StringIO
from app.calculator import calculator

# Helper function to run the calculator with given inputs
def run_calculator_with_inputs(monkeypatch, inputs):
    inputs_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs_iterator))
    captured_output = StringIO()
    sys.stdout = captured_output

    calculator()

    sys.stdout = sys.__stdout__
    return captured_output.getvalue()


def test_addition_operation(monkeypatch):
    inputs = ['add 2 3', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs)
    assert "The result is: 5.0" in output


def test_subtraction_operation(monkeypatch):
    inputs = ['subtract 5 2', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs)
    assert "The result is: 3.0" in output


def test_multiplication_operation(monkeypatch):
    inputs = ['multiply 3 4', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs)
    assert "The result is: 12.0" in output


def test_division_operation(monkeypatch):
    inputs = ['divide 10 2', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs)
    assert "The result is: 5.0" in output


def test_invalid_operation(monkeypatch):
    inputs = ['modulus 5 3', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs)
    assert "Unknown operation" in output


def test_invalid_input_format(monkeypatch):
    inputs = ['add five three', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs)
    assert "Invalid input" in output


def test_division_by_zero(monkeypatch):
    inputs = ['divide 5 0', 'exit']
    output = run_calculator_with_inputs(monkeypatch, inputs)
    assert "division by zero" in output.lower()
