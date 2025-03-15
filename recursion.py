def printN_1(i, n):
    if(i>n):
        return
    printN_1(i+1, n)
    print(i)

def main():
    n = int(input('Enter a number: '))
    printN_1(1,n)

if __name__ == '__main__':
    main()