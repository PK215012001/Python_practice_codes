def is_palindrome(a, i,j):
    if (i>=j):
        return True
    if(a[i]!=a[j]):
        return False
    return is_palindrome(a, i+1,j-1)

def main():
    a = 'TENET'
    print(is_palindrome(a,0,len(a) - 1))
if (__name__ == '__main__'):
    main()
    
    