#!/usr/bin/python3
"""
Plot coronavirus confirmed cases
"""

import requests
import matplotlib.pyplot as plt
import datetime


if __name__ == "__main__":


    url = 'https://api.covid19api.com/total/dayone/country/china/status/confirmed'
    data = requests.get(url).json()
    date = []
    cases = []
    daily_cases = [0]
    
    for day in data:
        date.append(day['Date'].split('T')[0])
        cases.append(day['Cases'])

    for i in range(1, len(cases)):
        daily_cases.append(cases[i] - cases[i - 1])

    plt.plot([datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in date], cases, label="Reported Cases")
    plt.plot([datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in date], daily_cases, label="Daily variation")
    plt.xticks(rotation=45)
    plt.xlabel('Rate')
    plt.ylabel('Reported Cases')
    plt.title('China')
    plt.legend()
    plt.grid()
    plt.show()
