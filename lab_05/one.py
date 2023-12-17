import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math
import datetime as dt
import csv


def one():
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})
    plt.axis([0, 10, -1.5, 1.5])

    plt.title('Sine & Cosine')
    plt.xlabel('x')
    plt.ylabel('F(x)')

    xs = []
    sin_vals = []
    cos_vals = []

    x = 0.0
    while x < 10.0:
        sin_vals += [math.sin(x)]
        cos_vals += [math.cos(x)]
        xs += [x]
        x += 0.1

    plt.plot(xs, sin_vals, color='blue', linestyle='solid', label='sin(x)')
    plt.plot(xs, cos_vals, color='red', linestyle='dashed', label='cos(x)')

    plt.legend(loc='upper right')
    fig.savefig('trigan.png')


def two():
    dates = []
    values = {}
    with open('ru-newreg.csv', newline='') as f:
        for row in csv.reader(f, delimiter=',', quotechar='"'):
            if dates == []:
                dates = [dt.datetime.strptime("{}-01".format(d), '%Y-%m-%d').date() for d in row[1:]]
                continue
            values[row[0]] = row[1:]
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})
    plt.title('RU New Domain Names Registration')
    plt.xlabel('Year')
    plt.ylabel('Domains')

    ax = plt.axes()
    ax.yaxis.grid(True)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
    ax.xaxis.set_major_locator(mdates.YearLocator())

    for reg in values.keys():
        plt.plot(dates, values[reg], linestyle='solid', label=reg)

    plt.legend(loc='upper left', frameon=False)
    fig.savefig('domains.png')


def three():
    data_names = [
        'cafe', 'pharmacy', 'fuel', 'bank', 'waste_disposal',
        'atm', 'bench', 'parking', 'restaurant', 'place_of_worship'
    ]
    data_values = [9124, 8652, 7592, 7515, 7041, 6487, 6374, 6277, 5092, 3629]
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 10})

    plt.title('OpenStreetMap Point Types')

    ax = plt.axes()
    ax.yaxis.grid(True, zorder=1)
    xs = range(len(data_names))

    plt.bar(
        [x + 0.05 for x in xs],
        [d * 0.9 for d in data_values],
        width=0.2,
        color='red',
        alpha=0.7,
        label='2016',
        zorder=2
    )

    plt.bar(
        [x + 0.3 for x in xs],
        data_values,
        width=0.2,
        color='blue',
        alpha=0.7,
        label='2017',
        zorder=2
    )
    plt.xticks(xs, data_names)
    fig.autofmt_xdate(rotation=25)
    plt.legend(loc='upper right')
    fig.savefig('bars.png')

def four():
    data_names = ['cafe', 'pharmacy', 'fuel', 'bank', 'w.d.', 'atm', 'bench', 'parking', 'restaurant', 'p.o.w.']
    data_values = [9124, 8652, 7592, 7515, 7041, 6487, 6374, 6277, 5092, 3629]

    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 9})

    plt.title('OpenStreetMap Point Types')
    ax = plt.axes()
    ax.xaxis.grid(True, zorder=1)

    xs = range(len(data_names))

    plt.barh(
        [x + 0.3 for x in xs],
        [d * 0.9 for d in data_values],
        height=0.2,
        color='red',
        alpha=0.7,
        label='2016',
        zorder=2
    )

    plt.barh(
        [x + 0.05 for x in xs],
        data_values,
        height=0.2,
        color='blue',
        alpha=0.7,
        label='2017',
        zorder=2
    )

    plt.yticks(xs, data_names, rotation=10)
    plt.legend(loc='upper right')
    fig.savefig('barshoris.png')


def five():
    data_names = [
        'Москва', 'Санкт-Петербург', 'Сочи', 'Архангельск', 'Владимир',
        'Краснодар', 'Курск', 'Воронеж', 'Ставрополь', 'Мурманск'
    ]
    data_values = [1076, 979, 222, 189, 137, 134, 124, 124, 91, 79]
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))
    mpl.rcParams.update({'font.size': 9})

    plt.title('Распределение кафе по городам России (%)')
    xs = range(len(data_names))

    plt.pie(
        data_values,
        autopct='%.1f',
        radius=1.1,
        explode=[0.15] + [0 for _ in range(len(data_names) - 1)]
    )
    plt.legend(
        bbox_to_anchor=(-0.16, 0.45, 0.25, 0.25),
        loc='lower left',
        labels=data_names
    )
    fig.savefig('pie.png')


# if __name__ == '__main__':
    # one()
    # three()
    # five()
