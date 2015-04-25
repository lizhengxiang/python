months = [
	'Jauary',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'Octber',
	'November',
	'December'
]

endigs = ['st' , 'nd', 'rd'] + 17 * ['th'] \
		+['st' , 'nd', 'rd'] + 7 * ['th'] \
		+ ['st']
year = raw_input('Year: ')
month = raw_input('Month(1----12): ')
day = raw_input('Day(1-----31): ')
month_num = int (month)
day_num = int (day)

print months[month_num -1] + ' ' + day + endigs[day_num - 1] + ' ' + year
