import stany_czujek
from datetime import date, datetime
from pandas import DataFrame, to_datetime

#pobranie aktualngo dnia
today = date.today()
now = datetime.now()
print(now)

day = '2021-10-12 12:10:01'

#pobranie stanów czujek
stany_czujek = DataFrame(stany_czujek.pobierz_stany_czujek())
print(stany_czujek)

#odfiltrowanie stanów z dnia dzisiejszego
test = stany_czujek.loc[stany_czujek["DATETIMES"] >= to_datetime(day)]
print(test)

