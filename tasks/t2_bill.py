#Ask the user for:
#Total bill amount
#Tip percentage they want to give
#Number of people splitting the bill
#Then calculate and display how much each person should pay.

total_bill = input('Enter total bill amount: ')
tip_percent = input('Enter percent of tip your want to give: ')
total_people = input('With how many people you want to share tips: ')

tip = ((int(tip_percent)/100) * int(total_bill))
bill = (tip + int(total_bill))/ int(total_people)

print('Each man must pay ', bill, 'dollars')