# Create a python file that asks an insurance company the following inputs:
#- Insurance company name
#- Number of employees
#- location (city, OR country, OR state)
#- Lowest price for a policy
#- The highest price for a policy
#The output will consist of a prompt almost like an ad. For example:
#We are Company LLC located in India. Our 55 employees can help you find the policy that is right for you with policies ranging from $15 to $300 per month! 

# Solution:
company_name = input('Please type the name of the insurance company>> ')
number_employees = input('Please set the number of employees>> ')
company_location = input('Please set the company location>> ')
lowest_price = input('Set the lowest price for a policy>>')
highest_price = input('Set the highest price for a policy>> ')

print(f'We are {company_name} located in {company_location}. Our {number_employees} employees can help you find that is right for you with policies ranging from {lowest_price} to {highest_price} per month!')