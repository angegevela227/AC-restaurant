#recursion function 
def arithmetic_seq(n, a1, d):#defining the variable in the sequence
    if n == 1:
        return a1
    else:
        return arithmetic_seq(n-1, a1, d) + d#calculating the quadratic sequence

grpseq = []

n = int(input("Enter the number of terms: "))
a1 = int(input("Enter the first term: "))
d = int(input("Enter the common difference: "))

for i in range(1, n+1):
    grpseq.append(arithmetic_seq(i, a1, d))

print("The group of number inside the sequence is ",grpseq)