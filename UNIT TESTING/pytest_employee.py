import os
import sys
import pytest

# 1. FIX THE PATH FIRST: Find the directory where THIS file is located
current_file_directory = os.path.dirname(os.path.abspath(__file__))
# and add it to Python's search path before doing any other imports.
sys.path.append(current_file_directory)

# 2. Now you can safely import your module from anywhere
from employee_class import Employee

# --- YOUR FIXTURES ---
@pytest.fixture(scope="module", autouse=True)
def module_setup_teardown():
    print('setupClass')
    yield
    print('teardownClass')

@pytest.fixture
def current_employees():
    print('setUp')
    emp_1 = Employee('Corey', 'Schafer', 50000)
    emp_2 = Employee('Sue', 'Smith', 60000)
    yield emp_1, emp_2
    print('tearDown\n')

# --- YOUR TEST CASES ---
def test_email(current_employees):
    print('test_email')
    emp_1, emp_2 = current_employees
    assert emp_1.email == 'Corey.Schafer@email.com'
    assert emp_2.email == 'Sue.Smith@email.com'

def test_fullname(current_employees):
    print('test_fullname')
    emp_1, emp_2 = current_employees
    assert emp_1.fullname == 'Corey Schafer'
    assert emp_2.fullname == 'Sue Smith'

def test_apply_raise(current_employees):
    print('test_apply_raise')
    emp_1, emp_2 = current_employees
    emp_1.apply_raise()
    emp_2.apply_raise()
    assert emp_1.pay == 52500
    assert emp_2.pay == 63000

def test_monthly_schedule(current_employees, monkeypatch):
    emp_1, emp_2 = current_employees
    class MockResponse:
        def __init__(self, ok, text):
            self.ok = ok
            self.text = text

    called_url = None
    def mock_get(url):
        nonlocal called_url
        called_url = url
        return MockResponse(mock_get.ok, mock_get.text)

    monkeypatch.setattr("employee_class.requests.get", mock_get)

    mock_get.ok = True
    mock_get.text = 'Success'
    schedule = emp_1.monthly_schedule('May')
    assert called_url == 'http://company/Schafer/May.com'
    assert schedule == 'Success'

    mock_get.ok = False
    mock_get.text = 'Success'
    schedule = emp_2.monthly_schedule('June')
    assert called_url == 'http://company/Smith/June.com'
    assert schedule == 'Bad Response!'


# 3. UNIVERSAL RUNNER BLOCK (Just like unittest)
if __name__ == '__main__':
    # Automatically injects the correct file name and the '-s' print flag
    sys.exit(pytest.main(["-s", __file__]))