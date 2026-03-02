class karthik:
    def kar(self, N):
        for i in range(0, N+1):
            for j in range(N-i):
                print(chr(65+j), end=" ")   
            print()
a=karthik()
a.kar(7)

class karthik2:
    def kar2(self, N):
        for i in range(N):
            for j in range(i+1):
                print(chr(65 + i), end=" ")
            print()

a2 = karthik2()
a2.kar2(5)
