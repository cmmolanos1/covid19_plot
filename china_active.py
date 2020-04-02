#!/usr/bin/python3
"""
Plot coronavirus confirmed cases
"""

import requests
import matplotlib.pyplot as plt
import datetime


if __name__ == "__main__":


    url_confirmed = 'https://api.covid19api.com/total/dayone/country/china/status/confirmed'
    url_recovered = 'https://api.covid19api.com/total/dayone/country/china/status/recovered'
    url_deaths = 'https://api.covid19api.com/total/dayone/country/china/status/deaths'
    
    data_conf = requests.get(url_confirmed).json()
    data_rec = requests.get(url_recovered).json()
    data_death = requests.get(url_deaths).json()
    
    date_c = []
    date_r = []
    date_d = []

    confirmed = []
    recovered = []
    deaths = []
    
    for day in data_conf:
        date_c.append(day['Date'].split('T')[0])
        confirmed.append(day['Cases'])
    
    for day in data_rec:
        date_r.append(day['Date'].split('T')[0])
        recovered.append(day['Cases'])

    for day in data_death:
        date_d.append(day['Date'].split('T')[0])
        deaths.append(day['Cases'])

    plt.plot([datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in date_c], confirmed, label="Reported Cases")
    plt.plot([datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in date_r], recovered, label="Recovered")
    plt.plot([datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in date_d], deaths, label="Death")

    dates = []
    dates.extend(date_c)
    dates.extend(date_r)
    dates.extend(date_d)
    date_total = list(set(dates))
    date_total.sort()

    active = []
    for day in date_total:
        confirmed_l = confirmed[date_c.index(day)]
        try:
            deaths_l = deaths[date_d.index(day)]
        except:
            deaths_l = 0
        try:
            recovered_l = recovered[date_r.index(day)]
        except:
            recovered_l = 0
        active.append(confirmed_l - deaths_l - recovered_l)

    plt.plot([datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in date_total], active, label="Active")

    plt.xticks(rotation=45)
    plt.xlabel('Rate')
    plt.ylabel('Reported Cases')
    plt.title('China')
    plt.legend()
    plt.grid()
    plt.show()
