def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for _ in range(2, n + 1):
        former_a = a
        a = b
        b = former_a + a
    return b

def is_positive_integer(text):
    try:
        return int(text) > 0
    except:
        pass
    return False

if __name__ == "__main__":
    import time
    while True:
        text = input("Please enter a positive integer: ")
        if not is_positive_integer(text):
            continue
        start = time.perf_counter()
        result = fibonacci(int(text))
        end = time.perf_counter()
        print(f"fibonacci({int(text)}) = {result}, calculating this took {end - start:.4e} seconds.")
