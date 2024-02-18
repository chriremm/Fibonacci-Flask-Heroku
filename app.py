from functools import lru_cache
from multiprocessing import Process, Queue

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
CALCULATION_TIMEOUT = 3


@lru_cache(maxsize=1000)
def calculate_fibonacci_1(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return calculate_fibonacci_1(n - 1) + calculate_fibonacci_1(n - 2)


@lru_cache(maxsize=1000)
def calculate_fibonacci_2(n: int) -> int:
    fib = [0] * n
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n - 1]


@lru_cache(maxsize=1000)
def calculate_fibonacci_3(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


@lru_cache(maxsize=1000)
def calculate_fibonacci_4(n: int) -> int:
    v1, v2, v3 = 1, 1, 0
    for rec in bin(n)[3:]:
        calc: int = v2 * v2
        v1, v2, v3 = v1 * v1 + calc, (v1 + v3) * v2, calc + v3 * v3
        if rec == '1':
            v1, v2, v3 = v1 + v2, v1, v2
    return v2


@lru_cache(maxsize=1000)
def calculate_fibonacci_5(n) -> tuple[int, int]:
    if n == 0:
        return 0, 1
    else:
        a, b = calculate_fibonacci_5(n // 2)
        c = a * (b * 2 - a)
        d = a * a + b * b
        if n % 2 == 0:
            return c, d
        else:
            return d, c + d


@lru_cache(maxsize=1000)
def schreibe_zahl_iterativ(zahl: int) -> str:
    if zahl == 0:
        return ""

    result = ""

    while zahl > 0:
        result = str(zahl % (10 ** 4000)) + result
        zahl = zahl // (10 ** 4000)

    return result


def calculation_process(n: int, queue: Queue) -> None:
    queue.put(calculate_fibonacci_4(n))


def response_process(queue: Queue) -> None:
    queue.put(schreibe_zahl_iterativ(queue.get()))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    queue: Queue = Queue()
    n: int = request.args.get('n', default=1, type=int)

    if n < 0:
        return jsonify({"Fibonacci Number": "Error: n must be a positive integer"})

    calculation = Process(target=calculation_process, args=(n, queue))
    calculation.start()

    calculation.join(timeout=CALCULATION_TIMEOUT)

    if calculation.is_alive():
        calculation.terminate()
        print("Calculation terminated due to timeout")
        return jsonify({"Fibonacci Number": "Error: Calculation took too long"})

    response = Process(target=response_process, args=(queue,))
    response.start()

    response.join(timeout=CALCULATION_TIMEOUT)

    if response.is_alive():
        response.terminate()
        print("Response terminated due to timeout")
        return jsonify({"Fibonacci Number": "Error: Response took too long"})

    result: str = queue.get()

    return jsonify({"Fibonacci Number": result})


if __name__ == '__main__':
    app.run()
