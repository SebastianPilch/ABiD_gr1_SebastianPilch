import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb',
                        password='adb2020');


def film_in_category(category_id: int) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego id kategorii.
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(category_id, int):
        txt = "select film.title ,language.name , category.name from (((film_category inner join film on film_category.film_id = film.film_id)inner join language on language.language_id = film.language_id)inner join category on category.category_id = film_category.category_id)where film_category.category_id in (" + str(
            category_id) + ")  order by title, language.name asc"
        film_list = pd.read_sql(txt, con=connection)
        film_list.columns = ['title', 'languge', 'category']
        return film_list

    return None


def number_films_in_category(category_id: int) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów w zadanej kategori przez id kategorii.
    Przykład wynikowej tabeli:
    |   |category   |count|
    |0	|Action 	|64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(category_id, int):
        txt = "select category.name ,COUNT(category.name) from ((film_category INNER JOIN film ON film_category.film_id  = film.film_id)INNER JOIN category ON category.category_id = film_category.category_id) where category.category_id IN (" + str(
            category_id) + ') GROUP BY category.name'

        film_id_list = pd.read_sql(txt, con=connection)
        film_id_list.columns = ['category', 'count']
        return film_id_list
    return None


def number_film_by_length(min_length: Union[int, float] = 0, max_length: Union[int, float] = 1e6):
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów o dla poszczegulnych długości pomiędzy wartościami min_length a max_length.
    Przykład wynikowej tabeli:
    |   |length     |count|
    |0	|46 	    |64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    min_length (int,float): wartość minimalnej długości filmu
    max_length (int,float): wartość maksymalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if (isinstance(min_length, int) or isinstance(min_length, float)) and (
            isinstance(max_length, int) or isinstance(max_length, float)) and min_length < max_length:

        txt = "select film.length ,COUNT(film.length) from film where film.length BETWEEN "+str(min_length)+ " AND "+ str(max_length) +" GROUP BY film.length"
        film_list = pd.read_sql(txt, con=connection)

        return film_list

    return None


def client_from_city(city: str) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o listę klientów z zadanego miasta przez wartość city.
    Przykład wynikowej tabeli:
    |   |city	    |first_name	|last_name
    |0	|Athenai	|Linda	    |Williams
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    city (str): nazwa miaste dla którego mamy sporządzić listę klientów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''

    if isinstance(city, str):
        txt = "SELECT city.city, customer.first_name,customer.last_name FROM ((customer INNER JOIN address ON customer.address_id = address.address_id) INNER JOIN city ON address.city_id = city.city_id) WHERE city IN ('" + city + "') ORDER BY customer.first_name,customer.last_name ASC"
        customers_ = pd.read_sql(txt, con=connection)

        return customers_


    return None


def avg_amount_by_length(length: Union[int, float]) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o średnią wartość wypożyczenia filmów dla zadanej długości length.
    Przykład wynikowej tabeli:
    |   |length |avg
    |0	|48	    |4.295389
    
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    length (int,float): długość filmu dla którego mamy pożyczyć średnią wartość wypożyczonych filmów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(length, int) or isinstance(length, float):
        txt_avg = "AVG(payment.amount) from (((film inner join inventory on film.film_id = inventory.film_id)inner join rental on inventory.inventory_id = rental.inventory_id )inner join payment on payment.rental_id = rental.rental_id)"
        txt = "SELECT film.length ,"+ txt_avg + "where film.length IN (' "+ str(length)+ "') GROUP BY film.length "
        customers_ = pd.read_sql(txt, con=connection)
        return customers_
    return None


def client_by_sum_length(sum_min: Union[int, float]) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o sumaryczny czas wypożyczonych filmów przez klientów powyżej zadanej wartości .
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |sum
    |0  |Brian	    |Wyman  	|1265
    
    Tabela wynikowa powinna być posortowane według sumy, imienia i nazwiska klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    sum_min (int,float): minimalna wartość sumy długości wypożyczonych filmów którą musi spełniać klient
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(sum_min, int) or isinstance(sum_min, float):
        if sum_min > 0:

            txt = '''select customer.first_name, customer.last_name ,
                     SUM(film.length) FROM (((film  
                     INNER JOIN inventory ON inventory.film_id = film.film_id) 
                     INNER JOIN rental ON inventory.inventory_id = rental.inventory_id) 
                     INNER JOIN customer ON customer.customer_id = rental.customer_id)  
                     GROUP BY customer.first_name, customer.last_name
                     HAVING sum(film.length) >  ''' +  str(sum_min) + ''' ORDER BY sum(film.length),customer.last_name, 
                     customer.first_name  ASC '''

            customers_ = pd.read_sql(txt, con=connection)
            print(customers_.columns)
            return customers_

    return None


def category_statistic_length(name: str) -> pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o statystykę długości filmów w kategorii o zadanej nazwie.
    Przykład wynikowej tabeli:
    |   |category   |avg    |sum    |min    |max
    |0	|Action 	|111.60 |7143   |47 	|185
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    name (str): Nazwa kategorii dla której ma zostać wypisana statystyka
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if isinstance(name, str):
        txt = '''select category.name,AVG(film.length),SUM(film.length), MIN(film.length),MAX(film.length)
                 FROM (( film
                 INNER JOIN film_category ON film_category.film_id = film.film_id) 
                 INNER JOIN category ON film_category.category_id = category.category_id)''' +"WHERE category.name IN ('"+  name +  "') GROUP BY category.name"
        cat_ = pd.read_sql(txt, con=connection)
        cat_.columns = ['category', 'avg','sum','min','max']
        return cat_

    return None
