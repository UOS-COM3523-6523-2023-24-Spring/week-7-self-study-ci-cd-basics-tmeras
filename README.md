# Self study for Week 7 (CI/CD Basics)

## Install

```bash
python -m pip install pytest
```

## Task 1

Run the following on the pycharm built-in terminal:

```bash
pytest -v
```

You can see that `test_simple_function2` is failed. Fix the code (line 2 in `main.py`) to make the test case pass.

When it's fixed, push the change to GitHub to see the GitHub Actions in action.

## Task 2

If you uncomment `test_complex_function` in `test_main.py`, you can see that the test case is most likely failed.
This is because the behaviour of `complex_function` is non-deterministic (depending on `random_function`).

Such non-deterministic behaviour is not uncommon in real-world software system.
How can we test such non-deterministic behaviour? Think about this. (No need to implement anything)

### Thoughts on Task 2
Testing such non-deterministic behaviour could be done by:

1. Setting the seed for the random number generation. In the case of `complex_function`, `random.seed(x)` could be called with
a specific value for x before the call to `random.random()` is made. In this way, non-determinism has been eliminated
as the result from calling `random_function` will be the same each time for a particular seed, and a wide range of seed values should be used to 
cover many possible scenarios

2. Replacing the non-deterministic behavior with "equivalent" deterministic behavior for testing purposes. For instance,
the call to `random_function` could be replaced with a call to a function that always returns true or another function which always
returns false, depending on which behavior the test case aims to evaluate. Granted,this is likely not always possible depending on the nature of the system

3. Running the non-deterministic behavior multiple times to cover different scenarios. For instance, `complex_function`
could be called enough times such that both the if and else branches are executed at least once. However, in most cases
it is likely difficult (if not impossible) to determine how many times the non-deterministic behavior should be run