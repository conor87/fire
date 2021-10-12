import stany_czujek
from datetime import date
from pandas import DataFrame as df

#pobranie aktualngo dnia
today = date.today()
print(today)

day = '2021-10-01'

#pobranie stanów czujek
stany_czujek = stany_czujek.pobierz_stany_czujek()
print(stany_czujek)

#odfiltrowanie stanów z dnia dzisiejszego
test = stany_czujek.loc[stany_czujek['DATETIMES'] == day]
print(test)

#odfiltrowanie stanów z pożarami
test = stany_czujek.loc[stany_czujek['SVALUE'] == '2']
#print(test)
