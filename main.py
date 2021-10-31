import stany_czujek, wywolane_alarmy
from datetime import datetime
from pandas import DataFrame, to_datetime
from wywolaj_alarm import *

# pobranie aktualngo dnia
now = datetime.now().date()

day = '2021-08-11'

now = day

# pobranie stanów czujek
stany_czujek = DataFrame(stany_czujek.pobierz_stany_czujek())
print('Tabela stanow czujek')
print(stany_czujek)

# odfiltrowanie stanów z dnia dzisiejszego / testowo now zamienione na day (powyżej)
dzisiejsze_stany_czujek = stany_czujek.loc[stany_czujek["DATETIMES"] >= to_datetime(now)]
# odfiltrowanie stanów czujek z sygnałem alarmowym
dzisiejsze_stany_czujek_z_alarmem = dzisiejsze_stany_czujek.loc[dzisiejsze_stany_czujek["SVALUE"] == '2']
print('dzisiejsze stany czujek z alarmem')
print(dzisiejsze_stany_czujek_z_alarmem)
# pobranie najnowszego wpisu w tabeli wywolanych alarmow
wywolane_alarmy = DataFrame(wywolane_alarmy.popierz_najnowszy_wpis())
# print(wywolane_alarmy["DATETIMES"])
# przypisz do zmiennej jeżeli stany czujek z dzisiaj sa mlodsze niz zgloszone alarmy w przeszlosci
czy_wywolac_alarm = dzisiejsze_stany_czujek_z_alarmem.loc[dzisiejsze_stany_czujek_z_alarmem["DATETIMES"] >= wywolane_alarmy["DATETIMES"][0]]
print('Alarmowe stany czujek - daty młodsze niż ostatni alarm')
print(czy_wywolac_alarm)

# Jezeli do zmiennej czy_wywolac_alarm przypisano jakies wartosci -> wywolaj alarm
if len(czy_wywolac_alarm) == 0:
    print('Puste alarmy')
else:
    print('ALARM')
    wywolaj_alarm('sex')

