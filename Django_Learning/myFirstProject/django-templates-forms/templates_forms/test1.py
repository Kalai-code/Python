
x = [[1,10],[2,20],[3,30]]
y = zip([1,2,3],[10,20,30])

for a in x:
    for b in a:
        print(b,",")

for a,b in y:
    print(a,b)
    
