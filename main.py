#a simple personal budget tracker that can be updated as new expenses occur
#the first input will ask for your known monthly income, the second input will ask for your known expense
#the third and any continuous inputs will be any expenses that occur throughout the month
#the program will finally output the money you will have left over after your total monthly expenses


#setting 3 variables that will be used for the program, 2 inputs 1 set variable
monthly_income = float(input("Please enter your monthly income:"))
fixed_expenses = float(input("Please enter your fixed monthly expenses:"))
variable_expenses = 0

#while loop to handle any unforseen expense to add to the set variable above
while True:
    expense = float(input("Please enter your expense:"))
    expense += variable_expenses

    decision = input("Do you have any more expenses to add? (Y/N)")
    if decision == ("N"):  #Continues the loop until "N" condition is satisfied
        break


#Calculations for the variables
total_expenses = fixed_expenses + variable_expenses
remaining_income = monthly_income - total_expenses

#displays the final remaining income for the month
print(remaining_income)
