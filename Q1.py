#Question 1
#A. We downloaded the data from the World Development Indicators in .csv file.
#B. We use open() to read the data.
#C. We use plot() in matplotlib to plot the data in linechart.
#D. 1)The defination of gross enrollment ratio is
#total enrolment in primary education, 
#regardless of age, 
#expressed as a percentage of the eligible official primary school-age population 
#in a given school-year.
#   2)Some‘strange’ phenomenon in the data may be the result of the goverment's policy, 
#some events happened in the year (such as in 1989) and so on.
#E. According to the data, we can find that the gross enrollment ratio of China
#have been increasing in the 10 years, while the one of Republic of Korea is decreasing.
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(2010,2020,1);
fp=open("Data.csv");
for i in fp:
    a=i.rstrip("\n").split(",");
    for j in range(0,len(a)):
        if(a[j]==".."): continue;
        a[j]=float(int(float(a[j])*100))/100;
    print(a);
    plt.plot(x,a);
    plt.grid(True,color='g',linestyle='--',linewidth='1')
    plt.show();
