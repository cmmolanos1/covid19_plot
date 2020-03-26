#!/usr/bin/python3
"""
Plot coronavirus confirmed cases
"""

import requests
import matplotlib.pyplot as plt
import datetime


if __name__ == "__main__":

    countries = ["colombia", "venezuela", "ecuador", "peru", "argentina", "brazil", "chile", "panama", "mexico", "uruguay"]

    for country in countries:
        url = 'https://api.covid19api.com/total/dayone/country/{}/status/confirmed'.format(country)
        data = requests.get(url).json()
        day = []
        cases = []
        d = 0
        for elem in data:
            day.append(d)
            cases.append(elem['Cases'])
            d += 1

        # plotting the points
        plt.plot(day, cases, label="{}".format(data[0]['Country']))

    plt.xticks(rotation=45)
    plt.xlabel('Days')
    plt.ylabel('Reported Cases')
    plt.title('Latin America from day-zero')
    plt.legend()
    plt.grid()
    plt.show()
