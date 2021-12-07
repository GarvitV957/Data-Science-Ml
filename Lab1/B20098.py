
""" @Author : Garvit Verma
Roll no. : B20098 
Contact no.: 8272840777"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df=pd.read_csv('pima-indians-diabetes.csv')

# Q1
#Mean
print("Mean of all columns are as follows:")
mean_col=df[['pregs','plas','pres','skin','test','BMI','pedi','Age']].mean()
print(mean_col)
#Median
print("Median of all columns are as follows:")
median_col=df[['pregs','plas','pres','skin','test','BMI','pedi','Age']].median()
print(median_col)
#Mode
print("Mode of all columns are as follows:")
mode_col=df[['pregs','plas','pres','skin','test','BMI','pedi','Age']].mode()
print(mode_col)
#Maximum
print("Maximum of all columns are as follows:")
max_col=df[['pregs','plas','pres','skin','test','BMI','pedi','Age']].max()
print(max_col)
#Minimum
print("Minimum of all columns are as follows:")
min_col=df[['pregs','plas','pres','skin','test','BMI','pedi','Age']].min()
print(min_col)
#Std. deviation
print("Std. deviation of all columns are as follows:")
std_col=df[['pregs','plas','pres','skin','test','BMI','pedi','Age']].std()
print(std_col)

# Q2
df1=df['Age']
df2=df['BMI']
# Part a
plt.scatter(df1,df['pregs'])
plt.ylabel('pregs')
plt.xlabel('Age')
plt.show()
plt.scatter(df1,df['plas'])
plt.ylabel('plas')
plt.xlabel('Age')
plt.show()
plt.scatter(df1,df['pres'])
plt.ylabel('pres')
plt.xlabel('Age')
plt.show()
plt.scatter(df1,df['skin'])
plt.ylabel('skin')
plt.xlabel('Age')
plt.show()
plt.scatter(df1,df['test'])
plt.ylabel('test')
plt.xlabel('Age')
plt.show()
plt.scatter(df1,df['BMI'])
plt.ylabel('BMI')
plt.xlabel('Age')
plt.show()
plt.scatter(df1,df['pedi'])
plt.ylabel('pedi')
plt.xlabel('Age')
plt.show()

# Part b
plt.scatter(df2,df['pregs'])
plt.ylabel('pregs')
plt.xlabel('BMI')
plt.show()
plt.scatter(df2,df['plas'])
plt.ylabel('plas')
plt.xlabel('BMI')
plt.show()
plt.scatter(df2,df['pres'])
plt.ylabel('pres')
plt.xlabel('BMI')
plt.show()
plt.scatter(df2,df['skin'])
plt.ylabel('skin')
plt.xlabel('BMI')
plt.show()
plt.scatter(df2,df['test'])
plt.ylabel('test')
plt.xlabel('BMI')
plt.show()
plt.scatter(df2,df['Age'])
plt.ylabel('Age')
plt.xlabel('BMI')
plt.show()
plt.scatter(df2,df['pedi'])
plt.ylabel('pedi')
plt.xlabel('BMI')
plt.show()

# Q3
# Part a
print("Correlation coefficient between Age and pregs: ",df1.corr(df['pregs']))
print("Correlation coefficient between Age and plas: ",df1.corr(df['plas']))
print("Correlation coefficient between Age and pres: ",df1.corr(df['pres']))
print("Correlation coefficient between Age and skin: ",df1.corr(df['skin']))
print("Correlation coefficient between Age and test: ",df1.corr(df['test']))
print("Correlation coefficient between Age and BMI: ",df1.corr(df['BMI']))
print("Correlation coefficient between Age and pedi: ",df1.corr(df['pedi']))
#Part b
print("Correlation coefficient between BMI and pregs: ",df2.corr(df['pregs']))
print("Correlation coefficient between BMI and plas: ",df2.corr(df['plas']))
print("Correlation coefficient between BMI and pres: ",df2.corr(df['pres']))
print("Correlation coefficient between BMI and skin: ",df2.corr(df['skin']))
print("Correlation coefficient between BMI and test: ",df2.corr(df['test']))
print("Correlation coefficient between BMI and Age: ",df2.corr(df['Age']))
print("Correlation coefficient between BMI and pedi: ",df2.corr(df['pedi']))

# Q4
plt.hist(df['pregs'])
plt.title("Histogram of pregs")
plt.show()
plt.hist(df['skin'])
plt.title("Histogram of skin")
plt.show()

# Q5
df_new1=df[df['class']==0]
df_new2=df[df['class']==1]
plt.hist(df_new1['pregs'])
plt.title("Histogram of preg with class:0")
plt.show()
plt.hist(df_new2['pregs'])
plt.title("Histogram of preg with class:1")
plt.show()

# Q6
plt.boxplot(df['pregs'])
plt.title("Boxplot of pregs")
plt.show()
plt.boxplot(df['plas'])
plt.title("Boxplot of plas")
plt.show()
plt.boxplot(df['pres'])
plt.title("Boxplot of pres")
plt.show()
plt.boxplot(df['skin'])
plt.title("Boxplot of skin")
plt.show()
plt.boxplot(df['test'])
plt.title("Boxplot of test")
plt.show()
plt.boxplot(df['BMI'])
plt.title("Boxplot of BMI")
plt.show()
plt.boxplot(df['pedi'])
plt.title("Boxplot of pedi")
plt.show()
plt.boxplot(df['Age'])
plt.title("Boxplot of Age")
plt.show()
