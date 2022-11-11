# Labolatorium 6

Tematem zajęć jest przeanalizowanie bazy opinii na temat zakupionych w województwie Wielkopolskim odkurzaczy.Dane zostały umieszczone w folderze /Original_Data jako plik Wielkopolskie.csv.

Opinie zamieszczone w pliku źródłowym posortowałem i umieściłem w mniejszych bazach, możliwie najbardziej przystępnych zawierających dane które planowałem zwizualizować.Sortowanie i zapis wykonywany jest w pliku Command_files/Lab_6_CommandFiles.ipynb.Posortowane dane zamieściłem w folderze Analysis/, znalazły się tam następujące dane:

  - Rating_for_brand.csv - plik zawiera średnią ocenę wszystkich klientów recenzujących jedną z dostępnych marek. Wyniki zaprezentowałem na wykresie Documents/Ocena_od_Marki.png
  - Mark_rating_to_sex.csv - plik zawiera dane dotyczące średniej opinii klientów z uwzględnieniem płci kupującego. Wyniki przedstawione na grafice Documents/Ocena_od_plci.png 
  - Rating_changes_per_day.csv - plik zawiera dane o średnich opiniach z poszczególnych dni po zakupie, aby zwizualizować jak zmienia się opinia klientów na temat marki po upływie czasu. Wizualizacja danych an wykresie Documents/Ocena_wedlug_dni.png 
  - Buyers_age_histogram.csv - plik ten zawiera liczbę osób w poszczególnym wieku składających opinie o zakupionym urządzeniu. Na podstawie tych danych wyrysuję rozkład wieku kupujących, który zamieszę w grafice Documents/Rozkład_wieku_recenzentow.png 
  - Wielkopolska_rating.csv - originalde dane pozbawione wiersza z indeksami 

Generowanie wykresów dotyczących poszczególnych danych odbywa się w pliku Command_files/Data_Appendix.ipynb
