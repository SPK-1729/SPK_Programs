def number_guessing():
    pk_num = 143
    while True:
        try:
            number = int(input('Enter the number: '))            
            if number == pk_num:
                print('Congratulations! You nailed it!')
                break  # Exit the loop when the guess is correct
            elif 140 <= number <150:
                print('You are on fire!')
            elif 1 <= number < pk_num:
                print('You are freezing.')
            elif pk_num < number <= 200:
                print('You are getting warmer.')
            else:
                print('You are scorching')        
        except ValueError:
            print('Please enter a valid integer.')
# Call the function
number_guessing()

