import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# seaborn style
sns.set(context='notebook')

# driver point totals
all_drivers = pd.read_csv('all_drivers.csv').drop('Unnamed: 0', axis=1)
_ = sns.barplot(x='Driver', y='PTS', data=all_drivers)
plt.ylabel('Total points')
plt.xticks(rotation=90)
plt.show()


# fastest lap bar chart
fastest_lap = pd.read_csv('fastest_lap.csv').drop('Unnamed: 0', axis=1)
_ = sns.countplot(x='Driver', data=fastest_lap)
_.set_ylabel('# of fastest laps')
_.set_xticklabels(_.get_xticklabels(), rotation=45)
plt.show()

# team points graphs
f1 = pd.read_csv('f1_2019.csv').drop('Unnamed: 0', axis=1)
f1['Date'] = pd.to_datetime(f1['Date'])

teams = pd.unique(f1['Car'])

for i in range(len(teams)):
    plt.figure()
    _ = sns.lineplot(x='Date', y='Total PTS', data=f1[f1['Car'] == teams[i]], hue='Name')
    _.set_title(teams[i])
    plt.ylabel('Total points') 
    plt.xticks(rotation=45)     
plt.show()


