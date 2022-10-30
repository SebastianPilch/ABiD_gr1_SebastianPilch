import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category, int):

        txt = ''' select f.title, l.name , c.name 
                  from film f 
                  INNER JOIN language l using(language_id)
                  INNER JOIN film_category fc using(film_id)
                  INNER JOIN category c using(category_id) where category_id IN ''' + "('" + str(category) + "')"
        txt += ''' ORDER BY f.title, l.name asc '''
        df = pd.read_sql(txt, con=connection)
        df.columns = ['title', 'languge', 'category']

        return df

    if isinstance(category, str):
        txt = ''' select f.title, l.name, c.name
                  from film f 
                  INNER JOIN language l using(language_id)
                  INNER JOIN film_category fc using(film_id)
                  INNER JOIN category c using(category_id) where c.name IN ''' + "('" + category + "')"
        txt += ''' ORDER BY f.title, l.name asc '''
        df = pd.read_sql(txt, con=connection)
        df.columns = ['title', 'languge', 'category']

        return df

    return None
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania'''
    if isinstance(category, int):
        txt = ''' select f.title, l.name , c.name 
                  from film f 
                  INNER JOIN language l using(language_id)
                  INNER JOIN film_category fc using(film_id)
                  INNER JOIN category c using(category_id) where category_id IN ''' + "('" + str(category) + "')"
        txt += ''' ORDER BY f.title, l.name asc '''
        df = pd.read_sql(txt, con=connection)
        df.columns = ['title', 'languge', 'category']

        return df

    if isinstance(category, str):


        txt = ''' select f.title, l.name, c.name
                  from film f 
                  INNER JOIN language l using(language_id)
                  INNER JOIN film_category fc using(film_id)
                  INNER JOIN category c using(category_id) where c.name  ~* ''' + "'" + category + "'"
        txt += ''' ORDER BY f.title, l.name asc '''
        df = pd.read_sql(txt, con=connection)
        df.columns = ['title', 'languge', 'category']

        return df

    return None
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(title, str):
        txt = ''' select ac.first_name, ac.last_name
                  from film f 
                  INNER JOIN film_actor fa using(film_id)
                  INNER JOIN actor ac using(actor_id)
                  where f.title IN ''' + "('" + title +"') "
        txt += ''' ORDER BY  ac.last_name asc, ac.first_name '''
        df = pd.read_sql(txt, con=connection)
        return df

    return None
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(words, list):

        words_str = "('{"
        for i in range(len(words)):
            if len(words) -1 != i:
                words_str += '% ' + str(words[i]) + ','
                words_str += '% ' + str(words[i]) + ' %,'
                words_str += '' + str(words[i]) + ' %,'

            else:
                words_str += '% ' + str(words[i]) + ","
                words_str += '' + str(words[i]) + " %,"
                words_str += '% ' + str(words[i]) + " %}')"

        like_str = "WHERE lower(f.title) ~~* ANY " + words_str + ";"

        txt = ''' select f.title
                  from film f '''
        txt += like_str
        df = pd.read_sql(txt, con=connection)
        return df


    return None

