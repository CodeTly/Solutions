def primePalindrome(self, n: int) -> int:
    def isPalindrome (i):
        temp = str(i)
        if(str(i)==temp[::-1]):
            return isPrime(i)
        else:
            return 0

    def isPrime(num):
        for i in range(2, num) :          
            if(num%i==0):
                return 0
        else:
            return(num)

    if n==1:
        return 2
    else:    

        for i in range(n, (n+1)**5):
            if isPalindrome(i)!=0 :
                return i

        else:
            return 0
        
if __name__=="__main__":
    
    n=int(input("Enter limit"))
    print(primePalindrome(0, n))