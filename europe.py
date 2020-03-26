#!/usr/bin/python3
"""
Plot coronavirus confirmed cases
"""

import requests
import matplotlib.pyplot as plt
import datetime


if __name__ == "__main__":

    countries = ["italy", "spain", "germany", "france", "us", "united-kingdom"]

    for country in countries:
        url = 'https://api.covid19api.com/total/dayone/country/{}/status/confirmed'.format(country)
        data = requests.get(url).json()
        date = []
        cases = []

        for day in data:
            date.append(day['Date'].split('T')[0])
            cases.append(day['Cases'])

        # plotting the points
        plt.plot([datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in date],
                cases,
                label="{}".format(data[0]['Country']))

    plt.xticks(rotation=45)
    plt.xlabel('Reported Cases')
    plt.ylabel('Date')
    plt.title('Europe')
    plt.legend()
    plt.show()
    # lista = [
    #     {'x':["2020-03-01","2020-03-02","2020-03-03"], 'y':[5,7,4], 'label': "First Line"},
    #     {'x':["2020-02-29","2020-03-02","2020-03-03", "2020-03-04"], 'y':[10,14,12,11], 'label': "Second Line"}
    #     ]

    # for elem in lista:
    #     plt.plot([datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in elem['x']],
    #             elem['y'],
    #             label=elem['label'])

    # plt.xlabel('Plot Number')
    # plt.ylabel('Important var')
    # plt.title('Interesting Graph\nCheck it out')
    # plt.legend()
    # plt.show()
