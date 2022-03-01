def push_stack(stack, item):
    if stack[1] == len(stack[0]) - 1:
        print("Stack is full. No place for the new element.")
    else:
        stack[0][stack[1] + 1] = item
        stack[1] += 1


def pop_stack(stack):
    if stack[1] != -1:
        stack[0][stack[1]] = ""
        stack[1] -= 1


def head(stack):
    if stack[1] != -1:
        return stack[0][stack[1]]
    else:
        print("Stack is empty")


def to_string(stack):
    if stack[1] == -1:
        print("Stack is empty")
    else:
        return "".join(stack[0]).strip()


def test_stack():

    # push
    stack = [[""] * 5, -1]
    push_stack(stack, 'a')
    push_stack(stack, 'b')
    push_stack(stack, 'c')
    print(to_string(stack))
    push_stack(stack, 'e')
    push_stack(stack, 'f')
    push_stack(stack, 'g')

    # pop
    for i in range(6):
        pop_stack(stack)
        print(to_string(stack))

    # head
    push_stack(stack, 'a')
    print(head(stack))
    push_stack(stack, 'b')
    print(head(stack))
    push_stack(stack, 'c')
    print(head(stack))

    for i in range(6):
        pop_stack(stack)
        print(head(stack))


def print_codes(string):
    if len(string) == 0:
        print("0")  # Case of the one symbol was not specified.

    ans = []
    stack = [[""] * len(string), 0]
    push_stack(stack, "0")
    for i in range(1, len(string)):
        if (string[i - 1] == "D") and (string[i] == "U"):
            ans.append(to_string(stack))
            pop_stack(stack)
            push_stack(stack, "1")
        elif (string[i - 1] == "U") and (string[i] == "U"):
            ans.append(to_string(stack))
            while head(stack) == "1":
                pop_stack(stack)
            pop_stack(stack)
            push_stack(stack, "1")
        else:
            push_stack(stack, "0")

    # Last symbol
    ans.append(to_string(stack))

    return ans


def main():
    with open("input_1.txt", "r") as f:
        n = int(f.readline())
        ans = []
        for i in range(n):
            codes = print_codes(f.readline().strip())
            ans.append(str(len(codes)))
            ans.extend(codes)
        with open("output.txt", "w") as out:
            for i in range(len(ans)):
                out.write(ans[i] + '\n')


main()
