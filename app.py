from functools import lru_cache

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


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
def schreibe_zahl_rekursiv(zahl: any) -> str:
    if zahl == 0:
        return ""

    try:
        return schreibe_zahl_rekursiv(zahl // (10 ** 4000)) + str(zahl % (10 ** 4000))
    except RecursionError:
        return "Error: Zahl ist zu groß"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    n = request.args.get('n', default=1, type=int)

    if n < 0:
        return jsonify({"Fibonacci Number": "Error: n must be a positive integer"})
    elif n > 1_000_000:
        return jsonify({"Fibonacci Number": "Error: n must be smaller than 100_000"})

    result = calculate_fibonacci_4(n)

    response = schreibe_zahl_rekursiv(result)

    return jsonify({"Fibonacci Number": response})


if __name__ == '__main__':
    app.run()
