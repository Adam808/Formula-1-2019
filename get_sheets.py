import pandas as pd
from unidecode import unidecode as ud

#get driver standings > csv
all_drivers = pd.read_html('https://www.formula1.com/en/results.html/2019/drivers.html')
all_drivers = all_drivers[0]
all_drivers = all_drivers.drop(['Unnamed: 0', 'Unnamed: 6'], axis=1)
all_drivers.to_csv('all_drivers.csv')

#create empty DataFrame
f1_2019 = pd.DataFrame()

#get and append individual driver dfs > csv
for i in all_drivers['Driver']:
    name = ud(i).split()
    tag = name[0][:3].upper() + name[1][:3].upper() + '01'
    driver = pd.read_html('https://www.formula1.com/en/results.html/2019/drivers/'
                                      + tag + '/' + name[0].lower() + '-' + name[1].lower() + '.html')
    driver = driver[0].drop(['Unnamed: 0', 'Unnamed: 6'], axis=1)
    driver['Date'] = pd.to_datetime(driver['Date'])
    driver['Name'] = name[1]
    driver['Total PTS'] = driver['PTS'].cumsum()
    f1_2019 = f1_2019.append(driver)
    
f1_2019.to_csv('f1_2019.csv')
    
#get fastest lap df > csv
fastest_lap = pd.read_html('https://www.formula1.com/en/results.html/2019/fastest-laps.html')
fastest_lap = fastest_lap[0].drop(['Unnamed: 0', 'Unnamed: 5'], axis=1)
fastest_lap['Driver'] = fastest_lap['Driver'].str.split().str[1]

fastest_lap.to_csv('fastest_lap.csv')





