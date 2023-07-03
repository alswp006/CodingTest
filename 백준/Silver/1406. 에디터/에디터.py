import sys

def main():
    get = open(0).read().split().__iter__().__next__

    left = list(get())
    right = []

    for _ in range(int(get())):
        command = get()
        if command == "L":
            if left:
                right.append(left.pop())
        elif command == "D":
            if right:
                left.append(right.pop())
        elif command == "B":
            if left:
                left.pop()
        else:
            left.append(get())

    print("".join(left), end="")
    print("".join(right[::-1]))


if __name__ == "__main__":
    sys.exit(main())