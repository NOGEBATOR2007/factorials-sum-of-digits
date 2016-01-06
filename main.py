import functions as func

TESTS = func.my_input("Input number of tests: ")

for test in range(TESTS):
    print("Test number ", test + 1)

    N = func.my_input("Input factorial to calculate digits: ")
    digits = [1]
    for i in range(1, N + 1):
        func.multiplication(digits, i)
    print(sum(digits))