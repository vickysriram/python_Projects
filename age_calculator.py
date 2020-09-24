# claculate the age based on the given birth date and current date 
# need to pass teh birthdate details along with current date details 
def age_cal(current_date,current_month,current_year,birth_date,birth_month,birth_year):

# the below month tuple represent the no of days for each month in a year 
	month=[31,28,31,30,31,30,31,31,30,31,30,31]

#if the birthdate is more than the current date dont count this month , add the 30 days to the current date 
# and subtract the one month from current month so we can calulate the diferrence 
	if (birthdate > current_date):
		current_date = current_date + month[birth_month -1]
		current_month = current_month -1

#if the birthmonth is greater than the current month then subtract a year from cuurent year and add 12 months to cuuurent month 
# so we can calculate the difference 
	if (birth_month > current_month):
		current_year = current_year - 1
		current_month = current_month + 12

# calculate the date , month and year and print them 
	calculated_date = current_date - birth_date
	calculated_month = current_month - birth_month
	calculated_year = current_year - birth_year

	
	print ('no of years :' , calculated_year , ' no of months :' , calculated_month ,' no of days :', calculated_date)
