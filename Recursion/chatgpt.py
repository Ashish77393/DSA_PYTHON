def fibonacci_series(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series


if __name__ == "__main__":
    try:
        n = int(input().strip())
    except Exception:
        n = 10
    print(fibonacci_series(n))
