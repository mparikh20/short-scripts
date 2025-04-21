'''
Problem taken from 'Python Functions, Files, and Dictionaries', U Michigan course.
Solution should not use csv module or any pandas etc.
Read in the contents of the file SP500.txt which has monthly data for 2016 and 2017 about the S&P 500 closing prices as well as some other financial indicators, including the “Long Term Interest Rate”, which is interest rate paid on 10-year U.S. government bonds.
Write a program that computes the average closing price (the second column, labeled SP500) and the highest long-term interest rate. Both should be computed only for the period from June 2016 through May 2017. Save the results in the variables mean_SP and max_interest.

'''
from datetime import datetime

with open('SP500.txt', 'r') as file:

    lines = file.readlines()

    header = lines[0].strip().split(',')

    # find the relevant indices
    for index, name in enumerate(header):

        if name == 'SP500':
            sp_index = index

        elif name == 'Date':
            date_index = index

        elif name == 'Long Interest Rate':
            rate_index = index

    sp_vals = []
    rate_vals = []

    # in the date, months 6,7,8,9,10,11,12,1,2,3,4,5 AND years 2016 or 2017
    for row in lines[1:]:

        row = row.strip().split(',')

        # get the date string
        date_str = row[date_index]

        date = datetime.strptime(date_str, '%m/%d/%Y')

        if (date.year == 2016 and date.month >= 6) or (date.year == 2017 and date.month <= 5):

            # get the values
            sp_vals.append(float(row[sp_index]))
            rate_vals.append(float(row[rate_index]))

    mean_SP = sum(sp_vals) / len(sp_vals)
    max_interest = max(rate_vals)
