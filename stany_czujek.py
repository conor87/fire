import psycopg2
from pandas import DataFrame, read_sql

def pobierz_stany_czujek():
    #połączenie z bazą postgresql na maszynce 10.1.70.201
    connection = psycopg2.connect(user="postgres",
                                    password="602696957Kd1",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="postgres")
    #pobranie stanów czujek
    stan_czujek = read_sql("SELECT * FROM stan_czujek", connection)
    return stan_czujek

if __name__ == "__main__":
    print(pobierz_stany_czujek())