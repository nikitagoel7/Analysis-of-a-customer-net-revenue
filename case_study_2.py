# -*- coding: utf-8 -*-
"""
Created on Mon Apr 09 12:05:24 2022

@author: Nikita Goel
"""

import pandas as pd


def total_revenue_calculation(year_data):
    total_revenue = 0
    for i, row in year_data.iterrows():
        total_revenue += row['net_revenue']
    return total_revenue
    

def new_customer_revenue(current_year, prev_year):
    j = 1
    customer_email = []
    revenue = []
    for i, row in current_year.iterrows():
        if row['customer_email'] not in prev_year['customer_email'].tolist():
            j += 1
            customer_email.append(row['customer_email'].strip())
            revenue.append(row['net_revenue'])
        if j == 11:
            break
    dataframe = pd.DataFrame({'customer_email': customer_email, 'revenue': revenue})
    return dataframe
        

def calculate_existing_customer_growth(current_year, prev_year):
    j = 1
    customer_email = []
    revenue_growth = []
    for i, row in current_year.iterrows():
        if row['customer_email'] in prev_year['customer_email'].tolist():
            j += 1
            growth = float(row['net_revenue']) - float(prev_year[prev_year['customer_email'] == row['customer_email']]['net_revenue'])
            customer_email.append(row['customer_email'].strip())
            revenue_growth.append(round(growth, 2))
        if j == 11:
            break
    dataframe = pd.DataFrame({'customer_email': customer_email, 'revenue_growth': revenue_growth})
    return dataframe
        

def calculate_lost_revenue(current_year, prev_year):
    lost = prev_year[~prev_year['customer_email'].isin(current_year['customer_email'].tolist())]
    lost_revenue = 0
    for i, row in lost.iterrows():
        lost_revenue += row['net_revenue']
    return lost_revenue
        

def calculate_customer_rev_cy(current_year, prev_year):
    j = 1
    customer_email = []
    revenue = []
    for i, row in current_year.iterrows():
        if row['customer_email'] in prev_year['customer_email'].tolist():
            j += 1
            customer_email.append(row['customer_email'].strip())
            revenue.append(row['net_revenue'])
        if j == 11:
            break
    dataframe = pd.DataFrame({'customer_email': customer_email, 'revenue': revenue})
    return dataframe


def calculate_customer_rev_py(current_year, prev_year):
    j = 1
    customer_email = []
    revenue = []
    for i, row in current_year.iterrows():
        if row['customer_email'] in prev_year['customer_email'].tolist():
            j += 1
            customer_email.append(prev_year[prev_year['customer_email'] == row['customer_email']]['customer_email'].tolist()[0].strip())
            revenue.append(float(prev_year[prev_year['customer_email'] == row['customer_email']]['net_revenue']))
        if j == 11:
            break
    dataframe = pd.DataFrame({'customer_email': customer_email, 'revenue': revenue})
    return dataframe
    
        
        
def main_function(data_2015, data_2016, data_2017):
    # Calculation for the year 2015
    print("Calculation for year 2015")
    total_revenue_2015 = total_revenue_calculation(data_2015)
    print("\nTotal revenue for the year 2015: ", total_revenue_2015)
    # Total Customers Current Year
    print("\nTotal customer count for the curent year (2015): ", data_2015.shape[0])
    
    
    
    #Calculation for the year 2016
    print("\n\nCalculation for year 2016")
    total_revenue_2016 = total_revenue_calculation(data_2016)
    print("\nTotal revenue for the year 2016: ", total_revenue_2016)

    #new_customer revenue 
    print("\nNew customer Revenue")
    new_customer_revenue_df = new_customer_revenue(data_2016, data_2015)
    print(new_customer_revenue_df)
            
    # Existing customer growth - nothing
    print("\n\nExisting customer growth\nCustomer Email - Growth")
    customer_growth = calculate_existing_customer_growth(data_2016, data_2015)
    print(customer_growth)
            
    # Revenue lost from attrition
    lost_revenue_2016 = calculate_lost_revenue(data_2016, data_2015)
    print("\n\nLost revenue from attrition: ", total_revenue_2016 - lost_revenue_2016)

    # Existing Customer Revenue Current Year
    print("\n\nExisting customer revenue current year\nCustomer Email - Revenue")
    exist_cust_rev_2016 = calculate_customer_rev_cy(data_2016, data_2015)
    print(exist_cust_rev_2016)
            
    # Existing Customer Revenue Prior Year
    print("\n\nExisting customer revenue prior year\nCustomer Email - Revenue")
    exist_cust_rev_2015 = calculate_customer_rev_py(data_2016, data_2015)
    print(exist_cust_rev_2015)
    
    # Total Customers Current Year
    print("\nTotal customer count for the curent year (2016): ", data_2016.shape[0])

    # Total Customers Previous Year
    print("\nTotal customer count for the previous year (2015): ", data_2015.shape[0])

    # New Customers
    new_customer = data_2016[~data_2016['customer_email'].isin(data_2015['customer_email'].tolist())]
    print("\nTotal number of new customers for the curent year (2016): ", new_customer.shape[0])

    # Lost Customers
    lost_customers = data_2015[~data_2015['customer_email'].isin(data_2016['customer_email'].tolist())]
    print("\nTotal customer lost for the curent year (2016): ", lost_customers.shape[0])
    
    
    
    #Calculation for the year 2017
    print("\n\nCalculation for year 2017")
    total_revenue_2017 = total_revenue_calculation(data_2017)
    print("\nTotal revenue for the year 2017: ", total_revenue_2017)

    #new_customer revenue 
    print("\nNew customer Revenue")
    new_customer_revenue_df = new_customer_revenue(data_2017, data_2016)
    print(new_customer_revenue_df)
            
    # Existing customer growth - nothing
    print("\n\nExisting customer growth\nCustomer Email - Growth")
    customer_growth = calculate_existing_customer_growth(data_2017, data_2016)
    print(customer_growth)
            
    # Revenue lost from attrition
    lost_revenue_2017 = calculate_lost_revenue(data_2017, data_2016)
    print("\n\nLost revenue from attrition: ", total_revenue_2017 - lost_revenue_2017)

    # Existing Customer Revenue Current Year
    print("\n\nExisting customer revenue current year\nCustomer Email - Revenue")
    exist_cust_rev_2017 = calculate_customer_rev_cy(data_2017, data_2016)
    print(exist_cust_rev_2017)
            
    # Existing Customer Revenue Prior Year
    print("\n\nExisting customer revenue prior year\nCustomer Email - Revenue")
    exist_cust_rev_2016 = calculate_customer_rev_py(data_2017, data_2016)
    print(exist_cust_rev_2016)
    
    # Total Customers Current Year
    print("\nTotal customer count for the curent year (2017): ", data_2017.shape[0])

    # Total Customers Previous Year
    print("\nTotal customer count for the previous year (2016): ", data_2016.shape[0])

    # New Customers
    new_customer = data_2017[~data_2017['customer_email'].isin(data_2016['customer_email'].tolist())]
    print("\nTotal number of new customers for the curent year (2017): ", new_customer.shape[0])

    # Lost Customers
    lost_customers = data_2016[~data_2016['customer_email'].isin(data_2017['customer_email'].tolist())]
    print("\nTotal customer lost for the curent year (2017): ", lost_customers.shape[0])
    
    
if __name__ == '__main__':
    dataset = pd.read_csv('customer_orders.csv', index_col=0)
    distinct_year = dataset['year'].unique().tolist()
    data_2015 = dataset[dataset['year'] == 2015]
    data_2016 = dataset[dataset['year'] == 2016]
    data_2017 = dataset[dataset['year'] == 2017]
    main_function(data_2015, data_2016, data_2017)