import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].to_list()
population_mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print("Population Mean = ",population_mean)
print("Std_deviation=",std_deviation)


def random_set_of_means():

    dataset=[]

    for i in range(0,100):
        random_index=random.randint(0,100)
        value=data[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean



def show_fig(mean_list):
    df=mean_list
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()


def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_means()
        mean_list.append(set_of_means)
    mean  = statistics.mean(mean_list)
    print("mean of sampling distribution = ", mean)
        
    show_fig(mean_list)


setup()


def std():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_means()
        mean_list.append(set_of_means)
    std = statistics.stdev(mean_list)
    print("standard deviation of sampling distribution =", std)

std()