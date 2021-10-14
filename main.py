import stany_czujek, wywolane_alarmy
from datetime import date, datetime
from pandas import DataFrame, to_datetime

#pobranie aktualngo dnia
now = datetime.now().date()

day = '2021-08-11'

now = day

#pobranie stanów czujek
stany_czujek = DataFrame(stany_czujek.pobierz_stany_czujek())
print('Tabela stanow czujek')
print(stany_czujek)

#odfiltrowanie stanów z dnia dzisiejszego / testowo now zamienione na day (powyżej)
dzisiejsze_stany_czujek = stany_czujek.loc[stany_czujek["DATETIMES"] >= to_datetime(now)]
#odfiltrowanie stanów czujek z sygnałem alarmowym
dzisiejsze_stany_czujek_z_alarmem = dzisiejsze_stany_czujek.loc[dzisiejsze_stany_czujek["SVALUE"] == '2']

#pobranie najnowszego wpisu w tabeli wywolanych alarmow
wywolane_alarmy = DataFrame(wywolane_alarmy.popierz_najnowszy_wpis())
#print(wywolane_alarmy["DATETIMES"])

# przypisz do zmiennej daty jeżeli stany czujek z dzisiaj sa starsze niz zgloszone alarmy w przeszlosci -> jezeli True to nie ma alarmu
# jezeli False -> zgloszenie z czujki jest nowsze niz ostatni wywołany alarm -> wywolac alarm
czy_wywolac_alarm = dzisiejsze_stany_czujek_z_alarmem["DATETIMES"]<wywolane_alarmy["DATETIMES"][0]
print('Odfiltrowane dane z czujek')
print(czy_wywolac_alarm.values)

if False in czy_wywolac_alarm.values:
    print('Alarm, alarm!')








#jeżeli stan czujek jest nowszy od wywolanego alarmu -> wywolaj alarm
#if dzisiejsze_stany_czujek["DATATIMES"] > wywolane_alarmy["DATEIMES"]:
#    print('ok')
