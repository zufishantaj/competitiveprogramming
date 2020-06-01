if __name__ == '__main__':
    test = int(input())
    for i in range(test):
        inputString = input()
        numList = inputString.split(' ')
        num1 = int(numList[0])
        num2 = int(numList[1])
        if num1 > num2:
            print(">")
        elif num1 < num2:
            print("<")
        else:
            print("=")
