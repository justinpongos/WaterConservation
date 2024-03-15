customer_code = input('Enter a customer code(R, C, or I)): ')

if(customer_code == "R" or customer_code == "C" or customer_code == "I"):
    start_reading = float(input('Enter beginning reading(between 0 and 999999999): '))
    end_reading = float(input('Enter ending reading (between 0 and 999999999): '))
    if(0 <= start_reading <= 999999999 and 0 <= end_reading <= 999999999) and (end_reading>= start_reading):
        used_gallons =  float((end_reading - start_reading) /10 )
        if customer_code == 'R':
            to_bill = float( 5.00 + 0.0005 * used_gallons)
        elif customer_code == 'C':
            if used_gallons <= 4000000.00:
                to_bill = float(1000.00)
            else:
                to_bill = float(1000.00 + 0.00025*(used_gallons - 4000000.00))
        else:
            if used_gallons <= 4000000.00:
                to_bill = float(1000.00)
            elif 4000000.00 < used_gallons < 10000000.00:
                to_bill = float(2000.00)
            else:
                to_bill = float(2000.00 + (0.00025 * (used_gallons - 10000000)))

        print ('Customer code:', customer_code)
        print ('Beginning reading value in gallons and tenths of gallon', (start_reading / 10))
        print ('Ending reading value in gallons and tenths of gallon', (end_reading / 10))
        print ('Gallons of water used:',used_gallons)
        print ('Amount billed:', f'${to_bill:.2f}')
    else:
        print('Invalid input (beginning or ending reading value is out of the range)')
else:
    print('Invalid input (customer code)')
##Code By - Justin Pongos & Tim Mapula
