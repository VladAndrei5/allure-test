import allure

@allure.title("Test that always passes")
@allure.description("This is a simple test that always passes.")
def test_pass():
    assert True

@allure.title("Test that always passes")
@allure.description("This is a simple test that always passes.")
def test_pass_again():
    assert True

@allure.title("Test that always fails")
@allure.description("This test is supposed to fail for demonstration.")
def test_fail():
    assert False, "Intentional failure"

@allure.title("Test with steps")
@allure.description("This test shows how to use Allure steps.")
def test_with_steps():
    with allure.step("Step 1: Setup"):
        x = 1
        y = 2
    with allure.step("Step 2: Execute"):
        result = x + y
    with allure.step("Step 3: Assert"):
        assert result == 3
