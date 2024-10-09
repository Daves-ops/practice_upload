letters = ['A', 'A-','B+','B', 'B-','C+','C','C-','D+','D','D-','E']
nums = list(range(0,101))
x = int(input())

if x >= 94 and x <=100:
     print(x, 'Is: A')
elif x >= 93:
    print(x, 'Is: A-')
elif x >= 88:
     print(x, 'Is: B+')
elif x >= 84:
    print(x, 'Is: B')
elif x >= 81:
    print(x, 'Is: B-')
elif x >= 78:
     print(x, 'Is: C+')
elif x >= 75:
     print(x, 'Is: C')
elif x >= 72:
     print(x, 'Is: C-')
elif x >= 69:
     print(x, 'Is: D+')
elif x >= 66:
    print(x, 'Is: D')
elif x >= 63:
     print(x, 'Is: D-')
else:
    print(x, 'Is: E')
