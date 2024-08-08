
n = int(input())
for i in range(n):
    try:
        a, b = map(int, input().split())
        print(int(a / b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")
