# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 16:43:56 2019

@author: Anubhuti Singh
"""

#importing packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#reading the csv file
df = pd.read_csv("Assessment.csv")

#displaying first ten columns of the csv file
df.head(10)

#looking into the details of our dataset
df.describe()
df.info()
df.index.values
#checking columns and rows
df.shape

#adding headers to each column/feature
df.columns = ['Time','Email','Name','Age','Gender','School/College','Class','Year','Headache','Job_Awareness','Academic_Pressure','Vocal_Expression','Unhealhty_Influence','Weather','Workload','Seeking_Help','Anxiety','Faking','Physical_Health','Relationship_at_Work','Decision_Making','Self_Awareness','Screen_Time','Alcohol_Tobacco','Work_Stress','Parental_Pressure','Empathy','Digital_Distraction','Sleep_Hours','Time_Pressure','Financial_Pressure','Rship_Skills','Tech_Obligations']

df.columns.values 

#dropping un-required features 
df.drop(['Time','Name'], axis=1, inplace=True)

#displaying first two rows
df.head(2)

df.columns.values 

# drop duplicate by a column name 
df.drop_duplicates(['Email'],inplace=True)



#changing strings to numeric values of the questions

cleanup_nums = {"Headache":     {"Very often": 5, "Often": 4, "Sometimes":3, "Rarely":2, "Never":1 },
                "Job_Awareness": {"Never": 5, "Seldom": 4, "Sometimes":3, "Often":2, "Always":1 },
                "Academic_Pressure": {"very great extent": 5, "great extent": 4, "some extent":3, "little extent":2, "no impact":1 },
                "Vocal_Expression": {"really bad": 5, "bad": 4, "fair":3, "good":2, "really good":1 },
                "Unhealhty_Influence": {"Always": 5, "Often": 4, "Sometimes":3, "Seldom":2, "Never":1 },
                "Weather": {"Very often": 5, "Often": 4, "Sometimes":3, "Rarely":2, "Never":1 },
                "Workload": {"Always": 5, "Often": 4, "Sometimes":3, "Seldom":2, "Never":1 },
                "Seeking_Help": {"Never": 5, "Very rarely": 4, "Rarely":3, "Often":2, "Very often":1 },
                "Anxiety": {"Always": 5, "Mostly": 4, "Sometimes":3, "Few times":2, "Never":1 },
                "Faking": {"Always": 5, "Often": 4, "Sometimes":3, "Seldom":2, "Never":1 },
                "Physical_Health": {"Never": 5, "rarely": 4, "Sometimes":3, "Often":2, "Always":1 },
                "Relationship_at_Work": {"Always": 5, "Often": 4, "Sometimes":3, "Seldom":2, "Never":1 },
                "Decision_Making": {"negligible": 5, "very little extent": 4, "little extent":3, "great extent":2, "very great extent":1 },
                "Self_Awareness": {"Strongly agreed": 5, "Agreed": 4, "Neutral":3, "Disagreed":2, "Strongly disagree":1 },
                "Screen_Time": {">2.5 hours": 5, "2-2.5 hours": 4, "2 hours":3, "1-1.5 hours":2, "<1 hour":1 },
                "Alcohol_Tobacco": {"Very often": 5, "Often": 4, "Sometimes":3, "Rarely":2, "Never":1 },
                "Work_Stress": {"Very often": 5, "Often": 4, "Sometimes":3, "Rarely":2, "Never":1 },
                "Parental_Pressure": {"Strongly agreed": 5, "Agreed": 4, "Neutral":3, "Disagreed":2, "Strongly Disagreed":1 },
                "Empathy": {"Never": 5, "Rarely": 4, "Sometimes":3, "Often":2, "Always":1 },
                "Digital_Distraction": {"Always": 5, "Often": 4, "Sometimes":3, "Seldom":2, "Never":1 },
                "Sleep_Hours": {"Rarely": 5, "Only weekends": 4, "Three- Four nights a week":3, "Four-Five nights a week":2, "Mostly every night":1 },
                "Time_Pressure": {"Strongly agree": 5, "Agree": 4, "Neutral":3, "Disagree":2, "Strongly disagree":1 },
                "Financial_Pressure": {"Strongly agreed": 5, "Agreed": 4, "Neutral":3, "Disagreed":2, "Strongly disagreed":1 },
                "Rship_Skills": {"Never": 5, "Very rarely": 4, "Sometimes":3, "Often":2, "Always":1 },
                "Tech_Obligations": {"Always": 5, "Often": 4, "Sometimes":3, "Seldom":2, "Never":1 },
            
            }

df.replace(cleanup_nums, inplace=True)
df.head()

#converting our dataset into dataframe
data = pd.DataFrame(df)
data.head()

#Adding the main feature- Result
data['Result'] =  data[['Headache','Job_Awareness','Academic_Pressure','Vocal_Expression','Unhealhty_Influence','Weather','Workload','Seeking_Help','Anxiety','Faking','Physical_Health','Relationship_at_Work','Decision_Making','Self_Awareness','Screen_Time','Alcohol_Tobacco','Work_Stress','Parental_Pressure','Empathy','Digital_Distraction','Sleep_Hours','Time_Pressure','Financial_Pressure','Rship_Skills','Tech_Obligations']].mean(axis=1)

print(data)
data.drop(['Email','School/College'], axis=1, inplace=True)
data.columns.values 
data.shape


def f(row):
    if row['Result']>=1.00 and row['Result']<=2.33:
        val = "Low Stress"
    elif row['Result']>=2.34 and row['Result']<=3.67:
        val = "Medium Stress"
    else:
        val = "High Stress"
    return val

data['Level'] = data.apply(f, axis=1)

data.head(10)
data.drop(data[data['Gender'] == 'Other'].index, inplace = True)


#new plots
ax = data.groupby(['Level','Gender']).size().unstack().plot(kind='bar',stacked=False,figsize=(13,8))
totals = []

# find the values and append to list
for i in ax.patches:
    totals.append(i.get_height())

# set individual bar lables using above list
total = sum(totals)

# set individual bar lables using above list
for i in ax.patches:
    # get_x pulls left or right; get_height pushes up or down
    ax.text(i.get_x(), i.get_height()+3, \
            str(round((i.get_height()/total)*100, 2))+'%', fontsize=14,
                color='black')
plt.show()

data=data.replace('BTEC', 'BTech.')
#data.drop(data[(data.Class != 'BTech.') & (data.Class != 'BCA')].index, inplace=True)
#data.groupby(['Level','Class']).size().unstack().plot(kind='bar',stacked=False,figsize=(15,10))
#plt.show()


#analysis of dataset for null values using heatmap
#sns.heatmap(df.isnull())
# Clearly; Heatmap of isnull indicates that this dataset does not have any null values
data.isnull()

#representation of stress score of different entries
data['Result'].plot(kind='hist', figsize=(8, 5))
plt.title('Lesser Score Means Less Stress') # add a title to the histogram
plt.ylabel('Number of Entries') # add y-label
plt.xlabel('Stress Score') # add x-label
plt.show()

#participation of girls vs boys
data['Gender'].value_counts().sort_index().plot.bar(figsize=(12, 6), color='purple',
    fontsize=16,title='Participation of Girls and Boys')
plt.xlabel('Gender')
plt.ylabel("Frequency")
#participation of various aged students
data['Age'].value_counts().sort_index().plot.bar(figsize=(12, 6), color='green',
    fontsize=16,title='Participation of various aged students')
plt.xlabel('Age')
plt.ylabel("Frequency")


box_plot_data=[data['Age'],data['Result']]
plt.boxplot(box_plot_data)
plt.ylabel("Age")

data.drop(data[data['Age'] > 80].index, inplace = True)
#participation of various students of different courses
data['Class'].value_counts().sort_index().plot.bar(figsize=(12, 6), color='red',
    fontsize=16,title='Participation of various students of different courses')
plt.xlabel('Courses')
plt.ylabel("Frequency")
#participation of college students of various years
data['Year'].value_counts().sort_index().plot.bar(figsize=(12, 6), color='mediumvioletred',
    fontsize=16,title='Participation of college students of various years')
plt.xlabel('Year')
plt.ylabel("Frequency")





#Visualization of different features vs the Stress Score

a=data['Gender']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.show()


a=data['Age']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.show()


a=data['Headache']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('Headache')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Purples")
plt.ylabel('Headache')
plt.xlabel("Stress Score")
plt.show()
#lot of people associated with medium or high stress score suffer from headaches frequently

#Similarly analysis of other features wrt score is done below
a=data['Job_Awareness']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('Job Awareness')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Blues")
plt.ylabel('Job Awareness')
plt.xlabel("Stress Score")
plt.show()

a=data['Academic_Pressure']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('Academic Pressure ')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Greens")
plt.ylabel('Academic Pressure ')
plt.xlabel("Stress Score")
plt.show()

a=data['Vocal_Expression']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('Vocal Expression ')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Oranges")
plt.ylabel('Vocal Expression ')
plt.xlabel("Stress Score")
plt.show()

a=data['Unhealhty_Influence']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('Unhealthy Influence ')
plt.xlabel("Stress Score")
plt.show()
plt.ylabel('Unhealthy Influence')
plt.xlabel("Stress Score")
plt.hexbin(b,a, gridsize=(10,10),cmap="Reds")
plt.show()

a=data['Weather']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('Weather')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="YlOrBr")
plt.ylabel('Weather')
plt.xlabel("Stress Score")
plt.show()

a=data['Workload']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('Workload')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="YlOrRd")
plt.ylabel('Workload')
plt.xlabel("Stress Score")
plt.show()

a=data['Seeking_Help']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('seeking help')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="OrRd")
plt.ylabel('seeking help')
plt.xlabel("Stress Score")
plt.show()

a=data['Anxiety']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('anxiety')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="PuRd")
plt.ylabel('anxiety')
plt.xlabel("Stress Score")
plt.show()

a=data['Faking']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('faking ')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="RdPu")
plt.ylabel('faking ')
plt.xlabel("Stress Score")

plt.show()

a=data['Physical_Health']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('physical health')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="BuPu")
plt.ylabel('physical health')
plt.xlabel("Stress Score")
plt.show()

a=data['Relationship_at_Work']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('relationship at work')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="GnBu")
plt.ylabel('relationship at work')
plt.xlabel("Stress Score")
plt.show()

a=data['Decision_Making']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('decison making')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="PuBu")
plt.ylabel('decison making')
plt.xlabel("Stress Score")
plt.show()

a=data['Self_Awareness']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('self awareness')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="YlGnBu")
plt.ylabel('self awareness')
plt.xlabel("Stress Score")
plt.show()

a=data['Screen_Time']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('screen time')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="PuBuGn")
plt.ylabel('screen time')
plt.xlabel("Stress Score")
plt.show()

a=data['Alcohol_Tobacco']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('Alcohol_Tobacco')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="BuGn")
plt.ylabel('Alcohol_Tobacco')
plt.xlabel("Stress Score")
plt.show()

a=data['Work_Stress']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('Work stress')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Reds")
plt.ylabel('Work stress')
plt.xlabel("Stress Score")
plt.show()

a=data['Parental_Pressure']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('parental pressure')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Oranges")
plt.ylabel('parental pressure')
plt.xlabel("Stress Score")
plt.show()

a=data['Empathy']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('empathy')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Blues")
plt.ylabel('empathy')
plt.xlabel("Stress Score")
plt.show()

a=data['Digital_Distraction']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('digital distraction')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Greens")
plt.ylabel('digital distraction')
plt.xlabel("Stress Score")
plt.show()

a=data['Sleep_Hours']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('sleep cycle')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="YlGn")
plt.ylabel('sleep cycle')
plt.xlabel("Stress Score")
plt.show()

a=data['Time_Pressure']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('time pressure')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="PuRd")
plt.ylabel('time pressure')
plt.xlabel("Stress Score")
plt.show()

a=data['Financial_Pressure']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('financial pressure')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="PuBu")
plt.ylabel('financial pressure')
plt.xlabel("Stress Score")
plt.show()

a=data['Rship_Skills']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('relationship skills')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Reds")
plt.ylabel('relationship skills')
plt.xlabel("Stress Score")
plt.show()

a=data['Tech_Obligations']
b=data['Result']
plt.figure(figsize=(15,10))
plt.scatter(b,a)
plt.ylabel('tech obligations')
plt.xlabel("Stress Score")
plt.show()
plt.hexbin(b,a, gridsize=(10,10),cmap="Greens")
plt.ylabel('tech obligations')
plt.xlabel("Stress Score")
plt.show()

#on the basis of the above visualisations, few features show low impact to high/medium level of stress score
#these features are being dropped below
data.drop(['Decision_Making','Alcohol_Tobacco','Empathy','Rship_Skills'], axis=1, inplace=True)

data.shape

data.to_csv('Updated.csv')

dp = pd.read_csv("Updated.csv")
dp.shape
#IMPLEMENTING RANDOM FOREST ALGORITHM 



#independent variables
X = pd.DataFrame(dp.iloc[:,5:-2])
X
#dependent variable

Y =pd.DataFrame(dp.iloc[:,-2])
Y

#split the dataset into train and test sets
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)


#Build the random forest regression model with random forest regressor function
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train,Y_train)
Y.pred= regressor.predict(X_test)
Y.pred


from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, Y.pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, Y.pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, Y.pred)))



from sklearn.metrics import r2_score
r2=r2_score(Y_test,Y.pred)
r2


from sklearn.feature_selection import RFE
rfe=RFE(regressor,15) #we are selecting the 15 most important features
rfe=rfe.fit(X,Y)
print(rfe.support_) #it will display TRUE for features that are important
print(rfe.ranking_)
X.shape
X


#on the basis of the result of RFE, we are now dropping the features that showed result FALSE in RFE
dp.drop(['Weather','Seeking_Help','Faking','Self_Awareness','Screen_Time','Parental_Pressure'],axis=1,inplace=True)


#checking accuracy again
X = pd.DataFrame(dp.iloc[:,5:-2])
X


Y =pd.DataFrame(dp.iloc[:,-2])
Y

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)
X_train
Y_train
regressor = RandomForestRegressor(n_estimators=20, random_state=0)
regressor.fit(X_train,Y_train)
Y.pred= regressor.predict(X_test)
Y.pred
Y_test.shape

r2=r2_score(Y_test,Y.pred)
r2
#r2=0.8042412442406475 (might differ everytime)

plt.figure(figsize=(20,10))

plt.scatter(Y_test,Y.pred,color="red")
plt.xlabel('Y_test')
plt.ylabel('Y.pred')
#plt.plot(Y_test, Y.pred, color='red', linewidth=2)
plt.show()






#'Headache','Job_Awareness', 'Academic_Pressure', 'Vocal_Expression','Unhealhty_Influence', 'Workload', 'Anxiety', 'Physical_Health',
#'Relationship_at_Work', 'Work_Stress', 'Digital_Distraction',
#'Sleep_Hours', 'Time_Pressure', 'Financial_Pressure',
#'Tech_Obligations'

