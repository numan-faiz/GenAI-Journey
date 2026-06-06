# Project---> Retail Sales Data Analysis And Visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')




# setting up visualization
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
print("all libraries imported succesfully")



# now itsa time to load dataset

df=pd.read_csv('retail_sales.csv')
print(df.head(10))


# Replace text anomalies with real NaNs so your fillna() mode calculation catches them
df['Category'] = df['Category'].replace(['NaN?', 'Nan', 'Null'], np.nan)
df['Region'] = df['Region'].replace(['NaN?', 'Nan', 'Null'], np.nan)
# data dimention and datatypes check dataset basic information
print("===dataset basic information===")
print(f"data dimension {df.shape[0]} rows * {df.shape[1]} columns")
print("/n columns names and datatypes ")
print(df.dtypes)


# now check missing values
print("\n missing values")
print(df.isnull().sum())
print("\ndataset summary")
print(df.info())



df[['Sales','Quantity']]=df[['Sales','Quantity']].fillna(df[['Sales','Quantity']].median())
print(df.info())

df[['Category','Region']]=df[['Category','Region']].fillna(df[['Category','Region']].mode().iloc[0])
# print(df.info())
print(df.isnull().sum())



# data types conversion and cleaninig
print("data type conversion and cleaning")

# convert data to datetime format

df['Date']=pd.to_datetime(df['Date'])

# extarctong exra feature
df['month']=df['Date'].dt.month
df['quarter']=df['Date'].dt.quarter
df['dayofweek']=df['Date'].dt.day_name()
df['monthname']=df['Date'].dt.month_name()




# now ensure numeric columns are properly formated
numeric_columns=['Sales','Quantity','Profit']
for col in numeric_columns:
    df[col]=pd.to_numeric(df[col],errors='coerce')

print("datatype after conversion")
print(df.dtypes)
print(f"\n data range: {df['Date'].min()} to df{df['Date'].max()}")




# basic statistical summary
print("=======statistical summary========")
print("descriptivr statistical for numerical colmns:")
print(df[['Sales','Quantity','Profit']].describe())


print("\n category wise-summary")
category_summary=df.groupby('Category').agg({
    'Sales':['count','sum','mean','std'],
    'Profit':['count','sum'],
    'Quantity':['count','sum']

}).round(2)
print(category_summary)





print("\n region-base summary:")
region_summary=df.groupby('Region').agg({
    'Sales':['sum','mean'],
    'Profit':['sum','mean']
}).round(2)

print(region_summary)

# monthly sales trend analysis
print("Monthly sales trend analysis")

# calculate monthly sales
monthly_sales=df.groupby(['month','monthname']).agg({
    'Sales':'sum',
    'Profit':'sum',
    'Quantity':'sum'
}).reset_index()

monthly_sales=monthly_sales.sort_values('month')
print("monthly sales summary")
print(monthly_sales)


# Visualization 1:monthly sales trend
plt.figure(figsize=(12,6))

plt.plot(monthly_sales['monthname'],monthly_sales['Sales'],marker='o',linewidth=2,markersize=8,label='Total Sales')
plt.plot(monthly_sales['monthname'],monthly_sales['Profit'],marker='o',linewidth=2,markersize=8,label='Total Profit')
plt.title('monthly sales and profit trend',fontsize=16,fontweight='bold')
plt.xlabel('month',fontsize=12)
plt.ylabel('amount($)',fontsize=12)
plt.legend()
plt.grid(True,alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# category_performance analysis
print("=======category performance analysis========")
category_performance=df.groupby('Category').agg({
    'Sales':'sum',
    'Profit':'sum',
    'Quantity':'sum'

}).sort_values('Sales',ascending=False)
print("category performace (sorted by sales: ")
print(category_performance)

# visulization:top categries by monthly_sales
plt.figure(figsize=(10,6))
colors=plt.cm.Set3(np.linspace(0,1,len(category_performance)))
bars=plt.bar(category_performance.index,category_performance['Sales'],color=colors,alpha=0.8)

#  add value labels on bars
for bar in bars:
    height=bar.get_height()
    plt.text(bar.get_x()+bar.get_width()/2.,height,f'${height:,.0f}',ha='center',va='bottom')

plt.title('total sales by product category',fontsize=16,fontweight='bold')
plt.xlabel('product category',fontsize=12)
plt.ylabel('total sales($)',fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y',alpha=0.3)
plt.tight_layout()
plt.show()

#  Regional Performance Analysis
print("=== REGIONAL PERFORMANCE ANALYSIS ===")

regional_performance = df.groupby('Region').agg({
    'Sales': ['sum', 'mean', 'count'],
    'Profit': ['sum', 'mean']
}).round(2)

print("Regional Performance:")
print(regional_performance)


# Visualization 3: Regional Sales Distribution
plt.figure(figsize=(10, 6))
regional_data = df.groupby('Region')['Sales'].sum()
plt.pie(regional_data, labels=regional_data.index, autopct='%1.1f%%',
        startangle=90, colors=sns.color_palette("pastel"))
plt.title('Sales Distribution by Region', fontsize=16, fontweight='bold')
plt.axis('equal')
plt.tight_layout()
plt.show()


# Day of Week Analysis
print("=== DAY OF WEEK ANALYSIS ===")

# Define proper order for days
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['dayofweek'] = pd.Categorical(df['dayofweek'], categories=day_order, ordered=True)
daily_performance = df.groupby('dayofweek').agg({
    'Sales': 'mean',
    'Profit': 'mean',
    'Quantity': 'mean'
}).round(2)

print("Average Performance by Day of Week:")
print(daily_performance)


# Visualization 4: Daily Sales Pattern
plt.figure(figsize=(10, 6))
plt.plot(daily_performance.index, daily_performance['Sales'],
         marker='o', linewidth=2, markersize=8, label='Average Sales')
plt.plot(daily_performance.index, daily_performance['Profit'],
         marker='s', linewidth=2, markersize=8, label='Average Profit')

plt.title('Average Sales and Profit by Day of Week', fontsize=16, fontweight='bold')
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Amount ($)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# Correlation Analysis
print("=== CORRELATION ANALYSIS ===")

# Select numerical columns for correlation
numerical_df = df[['Sales', 'Quantity', 'Profit', 'month']]
correlation_matrix = numerical_df.corr()

print("Correlation Matrix:")
print(correlation_matrix)

# Heatmap Visualization
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=0.5)
plt.title('Correlation Matrix of Numerical Variables', fontsize=16, fontweight='bold')
plt.tight_layout()
plt.show()



# 4-Chart Mini Dashboard
print("=== 4-CHART RETAIL SALES DASHBOARD ===")

# Create a 2x2 dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 12))
fig.suptitle('Retail Sales Analysis Dashboard', fontsize=20, fontweight='bold')

# Chart 1: Monthly Sales Trend (Top-Left)
axes[0,0].plot(monthly_sales['monthname'], monthly_sales['Sales'],
               marker='o', linewidth=2, color='blue', label='Sales')
axes[0,0].plot(monthly_sales['monthname'], monthly_sales['Profit'],
               marker='s', linewidth=2, color='red', label='Profit')
axes[0,0].set_title('Monthly Sales & Profit Trend', fontweight='bold')
axes[0,0].set_xlabel('Month')
axes[0,0].set_ylabel('Amount ($)')
axes[0,0].legend()
axes[0,0].grid(True, alpha=0.3)
axes[0,0].tick_params(axis='x', rotation=45)

# Chart 2: Top Categories (Top-Right)
colors = plt.cm.viridis(np.linspace(0, 1, len(category_performance)))
bars = axes[0,1].bar(category_performance.index, category_performance['Sales'], color=colors)
axes[0,1].set_title('Sales by Product Category', fontweight='bold')
axes[0,1].set_xlabel('Category')
axes[0,1].set_ylabel('Total Sales ($)')
plt.tight_layout()
plt.show()



#Key Insights and Business Recommendations
print("=== KEY INSIGHTS AND RECOMMENDATIONS ===")

print("\n📊 KEY FINDINGS:")
print("1. Top Performing Category:", category_performance.index[0])
print("2. Best Performing Region:", regional_data.idxmax())
print("3. Highest Sales Month:", monthly_sales.loc[monthly_sales['Sales'].idxmax(), 'monthname'])
print("4. Best Day of Week:", daily_performance['Sales'].idxmax())
print("5. Total Annual Sales: ${:,.2f}".format(df['Sales'].sum()))
print("6. Total Annual Profit: ${:,.2f}".format(df['Profit'].sum()))

print("\n💡 BUSINESS RECOMMENDATIONS:")
print("1. Focus marketing efforts on", category_performance.index[0], "category")
print("2. Investigate performance in lower-performing regions")
print("3. Plan promotions around", daily_performance['Sales'].idxmax(), "to maximize sales")
print("4. Allocate inventory based on monthly trend patterns")
print("5. Monitor correlation between quantity and profit for pricing strategy")

print("\n📈 PROFITABILITY ANALYSIS:")
profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100
print(f"Overall Profit Margin: {profit_margin:.2f}%")

print("\n💡 BUSINESS RECOMMENDATIONS:")
print("1. Focus marketing efforts on", category_performance.index[0], "category")
print("2. Investigate performance in lower-performing regions")
print("3. Plan promotions around", daily_performance['Sales'].idxmax(), "to maximize sales")
print("4. Allocate inventory based on monthly trend patterns")
print("5. Monitor correlation between quantity and profit for pricing strategy")

print("\n📈 PROFITABILITY ANALYSIS:")
profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100
print(f"Overall Profit Margin: {profit_margin:.2f}%")

