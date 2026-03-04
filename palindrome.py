class karhik:
    def palindrome(self, n):
        cnt=0
        a=n
        while n > 0:
            lastdigit=n%10
            cnt=cnt*10+lastdigit 
            n=n//10
        if cnt==a:
            return "Palindrome"
        else:
            return "Not a Palindrome"
a=karhik()
print(a.palindrome(8088))