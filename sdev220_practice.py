# #6.3
guess_me=5

for n in range(10):
    print(n)
    if n < guess_me:
        print('Too low')
    elif n > guess_me:
        print('Oops')
    else:
        print('Found It!')
        break

# 6.2
# guess_me = 7
# number = 1
#
# while number < guess_me:
#     print(number)
#     print('Too low')
#     number = number + 1
# else:
#
#     number == guess_me
#     print(number)
#     print('Found it!')
#     number = number + 1
#
#     number > guess_me
#     print(number)
#     print('Oops')
#     break


# last = input('Please enter students last name: ')
# for name in last:
#     if last == 'ZZZ':
#         break
# first = input('Please enter students first name: ')
# GPA = input('Please enter student GPA?:')
# GPA = float(GPA)
# if GPA >= 3.5:
#     print(f"{first}  {last} has made the Dean's list.")
#
# if GPA >= 3.25 and GPA < 3.4999:
#     print(f"{first}  {last}  has made the Honor Roll.")
#
# if GPA < 3.25:
#     print("You can do better.")
