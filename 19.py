while True:
    try:
        n = int(input())
        print(n*n-n+2)
    except (EOFError):
        break
