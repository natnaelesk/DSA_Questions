if __name__ == '__main__':
    n = int(input())
    phone_book = {}

    # Read phone book entries
    for _ in range(n):
        name, number = input().split()
        phone_book[name] = number

    # Read queries until EOF
    while True:
        try:
            query = input()
            if query in phone_book:
                print(f"{query}={phone_book[query]}")
            else:
                print("Not found")
        except EOFError:
            break
