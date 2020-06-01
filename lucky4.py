if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        count = 0
        num = input()
        for c in num:
            if c == '4':
                count = count + 1
        print(count)
