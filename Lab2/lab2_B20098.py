""" @Author : Garvit Verma
Roll no. : B20098 
Contact no.: 8272840777"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df1=pd.read_csv("landslide_data3_miss.csv")
df2=pd.read_csv("landslide_data3_original.csv")

# Q1
nan_val=dict(df1.isnull().sum())
plt.bar(nan_val.keys(),nan_val.values())
plt.title("No. of values missing")
plt.legend()
plt.show()

# Q2
#part a
df1_2=df1.dropna(axis=0,how='any',subset=["stationid"])    
print("No. of dropped rows: ",df1['stationid'].isnull().sum())      #no. of dropped rows

#part b
df1_3=df1_2.dropna(axis=0,thresh=7,how='any')
print("Total no. of tuples deleted: ",len(df1_2)-len(df1_3))

# Q3
print(df1_3.isnull().sum())                                         #no. of missing values as per attributes
print("Total no. of missing values in file: ",df1_3.isnull().sum().sum())

# Q4
#part a
df1_m=df1.fillna(df1.mean())
# i
#Mean
print("Mean of all columns are as follows:")
mean_col=df1_m[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].mean()
print(mean_col)
#Median
print("Median of all columns are as follows:")
median_col=df1_m[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].median()
print(median_col)
#Mode
print("Mode of all columns are as follows:")
mode_col=df1_m[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].mode()
print(mode_col)
#Std. deviation
print("Std. deviation of all columns are as follows:")
std_col=df1_m[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].std()
print(std_col)

# Original file
#Mean
print("Mean of all columns are as follows:")
mean_col1=df2[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].mean()
print(mean_col1)
#Median
print("Median of all columns are as follows:")
median_col1=df2[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].median()
print(median_col1)
#Mode
print("Mode of all columns are as follows:")
mode_col1=df2[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].mode()
print(mode_col1)
#Std. deviation
print("Std. deviation of all columns are as follows:")
std_col1=df2[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].std()
print(std_col1)

# ii
s1,s2,s3,s4,s5,s6,s7=0,0,0,0,0,0,0
for i in range(len(df2)):
    s1=s1+(df2.loc[i][2]-df1_m.loc[i][2])**2
    s2=s2+(df2.loc[i][3]-df1_m.loc[i][3])**2
    s3=s3+(df2.loc[i][4]-df1_m.loc[i][4])**2
    s4=s4+(df2.loc[i][5]-df1_m.loc[i][5])**2
    s5=s5+(df2.loc[i][6]-df1_m.loc[i][6])**2
    s6=s6+(df2.loc[i][7]-df1_m.loc[i][7])**2
    s7=s7+(df2.loc[i][8]-df1_m.loc[i][8])**2

temperature_e=(s1/(df1['temperature'].isnull().sum()))**.5
humidity_e=(s2/(df1['humidity'].isnull().sum()))**.5
pressure_e=(s3/(df1['pressure'].isnull().sum()))**.5
rain_e=(s4/(df1['rain'].isnull().sum()))**.5
lightavgw_e=(s5/(df1['lightavgw/o0'].isnull().sum()))**.5
lightmax_e=(s6/(df1['lightmax'].isnull().sum()))**.5
moisture_e=(s7/(df1['moisture'].isnull().sum()))**.5

X=['dates','stationid','temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']
Y=[0,0,temperature_e,humidity_e,pressure_e,rain_e,lightavgw_e,lightmax_e,moisture_e]
print(Y)
plt.bar(X,Y)
plt.ylabel("RMSE")
plt.title("Plot of RMSE vs attribute")
plt.show()

# part b
df1_m1=df1.fillna(df1.interpolate())
# i
#Mean
print("Mean of all columns are as follows:")
mean_col=df1_m1[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].mean()
print(mean_col)
#Median
print("Median of all columns are as follows:")
median_col=df1_m1[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].median()
print(median_col)
#Mode
print("Mode of all columns are as follows:")
mode_col=df1_m1[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].mode()
print(mode_col)
#Std. deviation
print("Std. deviation of all columns are as follows:")
std_col=df1_m1[['temperature','humidity','pressure','rain','lightavgw/o0','lightmax','moisture']].std()
print(std_col)

# ii
s1,s2,s3,s4,s5,s6,s7=0,0,0,0,0,0,0
for i in range(len(df2)):
    s1=s1+(df2.loc[i][2]-df1_m1.loc[i][2])**2
    s2=s2+(df2.loc[i][3]-df1_m1.loc[i][3])**2
    s3=s3+(df2.loc[i][4]-df1_m1.loc[i][4])**2
    s4=s4+(df2.loc[i][5]-df1_m1.loc[i][5])**2
    s5=s5+(df2.loc[i][6]-df1_m1.loc[i][6])**2
    s6=s6+(df2.loc[i][7]-df1_m1.loc[i][7])**2
    s7=s7+(df2.loc[i][8]-df1_m1.loc[i][8])**2

temperature_e1=(s1/(df1['temperature'].isnull().sum()))**.5
humidity_e1=(s2/(df1['humidity'].isnull().sum()))**.5
pressure_e1=(s3/(df1['pressure'].isnull().sum()))**.5
rain_e1=(s4/(df1['rain'].isnull().sum()))**.5
lightavgw_e1=(s5/(df1['lightavgw/o0'].isnull().sum()))**.5
lightmax_e1=(s6/(df1['lightmax'].isnull().sum()))**.5
moisture_e1=(s7/(df1['moisture'].isnull().sum()))**.5
Y=[0,0,temperature_e1,humidity_e1,pressure_e1,rain_e1,lightavgw_e1,lightmax_e1,moisture_e1]
print(Y)
plt.bar(X,Y)
plt.ylabel("RMSE")
plt.title("Plot of RMSE vs attributes")
plt.show()

# Q5
# part a

    # Outliers for temp.
Q1_t=df1_m1['temperature'].quantile(.25)
Q3_t=df1_m1['temperature'].quantile(.75)
iqr_t=Q3_t-Q1_t
print("iqr of temp: ",iqr_t)
df1_new1=df1_m1[df1_m1['temperature']>Q3_t+1.5*iqr_t]
print("Outliers Above upper bound \n",df1_new1['temperature'])
df1_new2=df1_m1[df1_m1['temperature']<Q1_t-1.5*iqr_t]
print("Outliers Below lower bound \n",df1_new2['temperature'])
    # Outliers for rain
Q1_r=df1_m1['rain'].quantile(.25)
Q3_r=df1_m1['rain'].quantile(.75)
iqr_r=Q3_r-Q1_r
print("iqr of rain: ",iqr_r)
df1_new3=df1_m1[df1_m1['rain']>Q3_r+1.5*iqr_r]
print("Outliers Above upper bound\n",df1_new3['rain'])
df1_new4=df1_m1[df1_m1['rain']<Q1_r-1.5*iqr_r]
print("Outliers Below lower bound\n",df1_new4['rain'])

plt.boxplot(df1_m1['temperature'])
plt.title("Boxplot for temperature")
plt.show()
plt.boxplot(df1_m1['rain'])
plt.title("Boxplot for rain")
plt.show()

# part b
med_t=df1_m1['temperature'].median()
med_r=df1_m1['rain'].median()
df1_m1['temperature']=np.where(df1_m1['temperature']<Q1_t-1.5*iqr_t,med_t,df1_m1['temperature'])
df1_m1['temperature']=np.where(df1_m1['temperature']>Q3_t+1.5*iqr_t,med_t,df1_m1['temperature'])
plt.boxplot(df1_m1['temperature'])
plt.title('Boxplot for temperature')
plt.show()

df1_m1['rain']=np.where(df1_m1['rain']<Q1_r-1.5*iqr_r,med_r,df1_m1['rain'])
df1_m1['rain']=np.where(df1_m1['rain']>Q3_r+1.5*iqr_r,med_r,df1_m1['rain'])
plt.boxplot(df1_m1['rain'])
plt.title('Boxplot for rain')
plt.show()

Q1_r1=df1_m1['rain'].quantile(.25)
Q3_r1=df1_m1['rain'].quantile(.75)
iqr_r1=Q3_r1-Q1_r1
print("iqr of rain: ",iqr_r1)
df1_new31=df1_m1[df1_m1['rain']>Q3_r1+1.5*iqr_r1]
print("Outliers Above upper bound\n",df1_new31['rain'])
df1_new41=df1_m1[df1_m1['rain']<Q1_r1-1.5*iqr_r1]
print("Outliers Below lower bound\n",df1_new41['rain'])