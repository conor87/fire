import psycopg2
from pandas import DataFrame, read_sql

def pobierz_wywolane_alarmy():
    #połączenie z bazą postgresql na maszynce 10.1.70.201
    connection = psycopg2.connect(user="postgres",
                                    password="602696957Kd1",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
    #pobranie stanów czujek
    stan_czujek = read_sql("SELECT * FROM wywolane_alarmy", connection)
    return stan_czujek


def pobierz_najnowszy_wpis():
    connection = psycopg2.connect(user="postgres",
                                    password="602696957Kd1",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
    #pobranie najnowszego wpisu
    najnowszy_wpis = read_sql("SELECT * FROM wywolane_alarmy ORDER BY 4 DESC LIMIT 1", connection)
    return najnowszy_wpis

if __name__ == "__main__":
    print(pobierz_wywolane_alarmy())
    print(pobierz_najnowszy_wpis())