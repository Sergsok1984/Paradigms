def multiplication_table(n):
    for i in range(1, n + 1):
        for j in range(1, 10):
            print(f"{i} * {j} = {i * j}", end="\n")
        print()


def main():
    n = int(input("Enter a number: "))
    multiplication_table(n)


if __name__ == "__main__":
    main()
