import datetime


def main():
    years = []
    for year in range(1996, 106, -20):  # only leap years 1*6
        if datetime.date(year, 1, 1).weekday() == 3:  # thursday
            years.append(year)
    print 'January 27th ' + str(years[1])


if __name__ == '__main__':
    main()
