def multiplication(array, multiplicator):
    temp = 0
    for j in range(len(array)):
        x = array[j] * multiplicator + temp
        array[j] = x % 10
        temp = int(x / 10)
    while(temp != 0):
        array.append(temp % 10)
        temp = int(temp / 10)

def my_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                break
            else:
                raise
        except:
            print("Input correct value pls!")
    return value