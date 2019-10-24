"""
Canadian Computing Competition: 2000 Stage 1, Junior #1
Write a program to print out a calendar for a particular month given the day on which the first of the month occurs
together with the number of days in the month.

Your program should take as input an integer representing the day of the week on which the month begins (1 for Sunday,
2 for Monday, ... , 7 for Saturday), and an integer which is the number of days in the month (between 28 and 31
inclusive). Your program should print the appropriate calendar for the month. You can assume that all input data will be
valid.

DMOJ-specific note: None of the output lines should contain trailing whitespace. The last line must end with a newline.
"""

info = input()
i_space = info.find(' ')

start_on = int(info[:i_space])
num_days = int(info[i_space + 1:])

days = ('Sun', 'Mon', 'Tue', 'Wed', 'Thr', 'Fri', 'Sat')
for d in days:
    if d == 'Sat':
        print(d, end='')
    else:
        print(d, end=' ')

preceding_space = start_on * 4 - 5

if start_on == 1:
    print('\n' + preceding_space * ' ', end=2 * ' ')
else:
    print('\n' + preceding_space * ' ', end=3 * ' ')

# All dates at the end of a week (row) are given by (8 - k)n where k is as defined above and n is the row number (week).
day_at_end = 8 - start_on
row_num = 0

for d in range(1, num_days + 1):
    if d == num_days:
        print(d, end='')

    else:
        if d % (day_at_end + 7 * row_num) == 0:
            print(d)
            if d < 9:
                print(2 * ' ', end='')
            else:
                print(' ', end='')
            row_num += 1

        else:
            if d < 9:
                print(d, end=3 * ' ')
            else:
                print(d, end=2 * ' ')

print()  # This little f*cker really getting on my nerves.
