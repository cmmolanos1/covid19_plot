#!/usr/bin/python3
"""
Plot coronavirus confirmed cases
"""

import requests
import matplotlib.pyplot as plt
import datetime


if __name__ == "__main__":

    url_col = 'https://api.covid19api.com/total/dayone/country/colombia/status/confirmed'
    col_days = len(requests.get(url_col).json())


    countries = ["italy", "spain", "germany", "france", "united-kingdom", "colombia"]

    for country in countries:
        url = 'https://api.covid19api.com/total/dayone/country/{}/status/confirmed'.format(country)
        data = requests.get(url).json()
        day = []
        cases = []
        d = 0
        for elem in data:
            if d < col_days:
                day.append(d)
                cases.append(elem['Cases'])
                d += 1
            else:
                break

        # plotting the points
        plt.plot(day, cases, label="{}".format(data[0]['Country']))

    plt.xticks(rotation=45)
    plt.xlabel('Days')
    plt.ylabel('Reported Cases')
    plt.title('Europe vs. Colombia from day-zero')
    plt.legend()
    plt.show()