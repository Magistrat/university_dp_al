import matplotlib as mpl
import matplotlib.pyplot as plt


def one():
    months = (
        'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль',
        'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
    )
    temperature = (-6.7, -6.1, -0.9, 6.9, 13.2, 17.2, 20, 17.9, 11.8, 5.8, -0.1, -4.4)
    mpl.rcParams.update({'font.size': 10})
    dpi = 80
    fig = plt.figure(dpi=dpi, figsize=(512 / dpi, 384 / dpi))

    plt.style.use('bmh')
    plt.plot(
        months,
        temperature,
        color='green',
        marker='o',
        markersize=4,
        linewidth=2.0
    )
    plt.xlabel('Месяц')
    plt.ylabel('Температура воздуха')
    plt.title('Температура воздуха в в Москве по месяца')

    plt.show()
    fig.savefig('months-temperature.png')


def two():
    months = ('Январь', 'Апрель', 'Июль', 'Октябрь')
    sunny_days = (3, 11, 29, 8)
    plt.style.use('bmh')

    plt.bar(
        months,
        sunny_days,
        color='orange',
    )

    plt.xlabel('Месяц')
    plt.ylabel('Количество солнечных дней')
    plt.show()


def three():
    seasons = ('Зима', 'Весна', 'Лето', 'Осень')
    rains = (1, 18, 15, 63)

    plt.pie(
        rains,
        labels=seasons
    )
    plt.title('Количество дождей по временам года')
    plt.show()


if __name__ == '__main__':
    three()
