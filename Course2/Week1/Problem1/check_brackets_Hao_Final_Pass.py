# python3

# has been accepted to the grader. And it passed the grader check.

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append([next, i])
        if next in ")]}":
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:   # First Situation: no '(' before ')'
                return i+1
            top = opening_brackets_stack.pop()
            top = top[0]
            # 2nd Situation: wrong close bracket
            if (next == ")" and top != "(") or (next == "}" and top != "{") or (next == "]" and top != "["):
                return i+1

    if len(opening_brackets_stack) == 0:
        return "Success"
    else:
        return opening_brackets_stack[0][1]+1


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
