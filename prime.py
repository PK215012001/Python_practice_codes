#  programme to find whether a given number is prime or not

def get_pos_int(prompt):
    """Function to get a proper positive integer from user"""
    while(True):
        num = input(prompt)
        try:
            num = float(num)
        except ValueError:
            print('Invalid input')
        else:
            if (num <= 0):
                print('Enter positive integers only')
            else:
                if(int(num) == num):
                    return int(num)
                else:
                    print('Enter integers only')

def is_prime(num):
    """Function to know whether a given number is prime or not"""
    if (num == 1):
        print('Neither prime nor composite')
    elif (num == 2):
        print('Prime')
    else:
        for i in range(2, num):
            if (num % i == 0):
                print('Composite')
                break
        else:
            print('Prime')


def main():
    num = get_pos_int('Enter a number: ')
    is_prime(num)

if (__name__ == '__main__'):
    main()