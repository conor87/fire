from pandas import DataFrame


def wywolaj_alarm(stany_alarmowe):
    print(stany_alarmowe)


if __name__ == '__main__':
    data = {
        "ID": [1],
        "OBJECTNAME": ['T1$3&8'],
        "SVALUE": ['2'],
        "DATETIMES": ['2021-10-15 22:02:01']
    }

    alarm = DataFrame(data)
    wywolaj_alarm(alarm)
