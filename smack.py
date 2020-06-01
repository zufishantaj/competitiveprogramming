if __name__ == '__main__':
    yearList = [2010, 2015, 2016, 2017, 2019]
    test = int(input())
    for i in range(test):
        year = int(input())
        if year in yearList:
            print("HOSTED")
        else:
            print("NOT HOSTED")
