import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def _dfunction(pth):

    tfe=pd.read_csv(pth,header=2)

     #replace this for data cleaning
    tfe.replace('..',0,inplace=True)

     # replace nan vals for computability
    tfe=tfe.fillna(0)

    tfet=tfe

     #setting country name as index in order to transpose
    tfet.set_index('Country Name')  

    #transposition of df
    tfetp=tfet.transpose()
    return tfe, tfetp

dfstata,comp=_dfunction('API_EG.ELC.COAL.ZS_DS2_en_csv_v2_5273035.csv')

dfstata.head()

dfstata['Country Name'].unique()

statdata=dfstata.drop(["Country Name"	, "Country Code", "Indicator Name", "Indicator Code"],axis=1).astype(float)

statdata=statdata.astype(float)
statdata.head()

statdata.describe()

# Sample data
x = dfstata['Country Name'].values[170:190]
y1 = statdata['1990'].values[170:190]
y2 = statdata['2015'].values[170:190]
y3 = statdata['2021'].values[170:190]

# Create multiline plot
fig, ax = plt.subplots()
ax.plot(x, y1, label='1990')
ax.plot(x, y2, label='2015')
ax.plot(x, y3, label='2021')

# Add labels and legend
ax.set_xlabel('Countries')
ax.set_ylabel('years')
ax.set_title('Electricity production from coal sources (% of total)')
plt.xticks(rotation=90)
ax.legend()

# Show the plot
plt.show()

# Plot the bars for each set of y values
x=dfstata['Country Name'].values[90:120]
y1=statdata['1990'].values[90:120]
y2=statdata['2000'].values[90:120]
y3=statdata['2012'].values[90:120]


plt.bar(x, y1, width=0.2, align='center', label='1990')
plt.bar([i + 0.2 for i in range(len(x))], y2, width=0.2, align='center', label='2000')
plt.bar([i + 0.4 for i in range(len(x))], y3, width=0.2, align='center', label='2012')

# Add labels and legend
plt.xlabel('countries')
plt.ylabel('years')
plt.title( 'Electricity production from coal sources (% of total)')
plt.xticks(rotation=90)
plt.legend()

# Show the plot
plt.show()

dfstata2,kr=_dfunction('API_EG.ELC.HYRO.ZS_DS2_en_csv_v2_4912365.csv')

statdata2=dfstata2.drop(["Country Name"	,"Country Code","Indicator Name", "Indicator Code"],axis=1).astype(float)

statdata2=statdata2.astype(float)
statdata2.head()

statdata2.describe()

# Sample data
categories =dfstata2['Country Name'].values[160:170]
sizes = statdata2['2015'].values[160:170]
#print(sizes)
# Create pie chart
fig, ax = plt.subplots()
ax.pie(sizes, labels=categories, autopct='%1.1f%%')

# Add title
ax.set_title('Electricity production from hydroelectric sources (% of total)')

# Show the plot
plt.show()

# Sample data
x = dfstata2['Country Name'].values[50:70]
y1 =statdata2['2012'].values[50:70]
y2 = statdata2['2015'].values[50:70]
y3 = statdata2['2019'].values[50:70]


# Create filled multiline plot
fig, ax = plt.subplots()
ax.fill_between(x, y1, alpha=0.3)
ax.fill_between(x, y1, y2, alpha=0.3)
ax.fill_between(x, y2, y3, alpha=0.3)
ax.plot(x, y1)
ax.plot(x, y2)
ax.plot(x, y3)

# Add labels and legend
ax.set_xlabel('countries')
ax.set_ylabel('2012,2015,2019')
ax.set_title('Electricity production from hydroelectric sources (% of total)')
ax.legend(['2012', '2015', '2019'])
plt.xticks(rotation=90)
# Show the plot
plt.show()

dfstata3,dfst3t=_dfunction('API_EG.ELC.NGAS.ZS_DS2_en_csv_v2_4912366.csv')

statdata3=dfstata3.drop(["Country Name"	,"Country Code","Indicator Name", "Indicator Code"], axis=1)
statdata3=statdata3.astype(float)
statdata3.head()

statdata3.describe()

x = dfstata3['Country Name'].values[100:120]
y = statdata3['2015'].values[100:120]

# Create bar plot
fig, ax = plt.subplots()
ax.bar(x, y)

# Add labels and title
ax.set_xlabel('countries')
ax.set_ylabel('2015')
ax.set_title('Electricity production from natural gas sources (% of total)')
plt.xticks(rotation=90)

# Show the plot
plt.show()

data =statdata3.iloc[20:40,20:40]

# create a heatmap using the 'hot' colormap
heatmap = plt.imshow(data, cmap='bone')

# add a colorbar to the plot
plt.colorbar(heatmap)

# set the x and y axis labels
plt.xlabel('years 1980- 2000')
plt.ylabel('countries')
plt.xticks(np.arange(0.5, 20.5), range(1980,2000), rotation=90)
plt.yticks(np.arange(0.5, 20.5), dfstata3['Country Name'].values[20:40])

# set the plot title
plt.title('Electricity production from natural gas sources (% of total)')

# show the plot
plt.show()