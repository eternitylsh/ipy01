mtea = 3
while True:
    money = int(input('Please money.') or 300)
    if 300 == money:
        mtea -= 1
        print("Thank you Order. This order Milk Tea here. : " + str(mtea))
    elif 300 < money:
        mtea -= 1
        print(f'Thank you Order. This order Milk Tea here. This change {money - 300}. : {str(mtea)}')
    else:
        print(f'Sorry too hear that.')
        print('leftover milk tea : {0}'.format(mtea))

    if 0 == mtea:
        print('We are closed today because we have run out of milk tea for today.')
        break