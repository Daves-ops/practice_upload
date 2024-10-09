letters = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E']
nums = list(range(0, 101))

x = int(input('What is your grade percentage? '))

if 94 <= x <= 100:
    print(x, 'is: A')
elif 93 <= x < 94:
    print(x, 'is: A-')
elif 88 <= x < 93:
    print(x, 'is: B+')
elif 84 <= x < 88:
    print(x, 'is: B')
elif 81 <= x < 84:
    print(x, 'is: B-')
elif 78 <= x < 81:
    print(x, 'is: C+')
elif 75 <= x < 78:
    print(x, 'is: C')
elif 72 <= x < 75:
    print(x, 'is: C-')
elif 69 <= x < 72:
    print(x, 'is: D+')
elif 66 <= x < 69:
    print(x, 'is: D')
elif 63 <= x < 66:
    print(x, 'is: D-')
else:
    print(x, 'is: E')

y = input('Do you want to know your GPA?')

z = y.lower()

if z == 'yes':
     print((x / 100)* 4)
