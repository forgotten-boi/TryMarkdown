def plusOne(A):
    num = 0;
    b = [];

    for i in range(0,len(A)):
        num = num * 10 + A[i];

    num = num + 1;

    print(num)

    while(num > 0):
        r = num % 10;
        num = num // 10;
        b.append(r);
        
    b.reverse();
    return b;
    

A=[1,2,3];
print(plusOne(A));
