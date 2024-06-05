# Projekt2_wtyczka_QGIS
Wtyczka do QGIS - PyQGIS
## Opis
Wtyczka Projekt 2 to narzędzie stworzone w środowisku QGIS z wykorzystaniem języka Python. Pozwala na wykonywanie różnych operacji związanych z analizą punktów i wielokątów.

## Funkcje
- **Obliczanie Różnicy Wysokości**: Wtyczka umożliwia obliczanie różnicy wysokości między dwoma wybranymi punktami na mapie. Wysokości muszą być dostępne jako atrybuty punktów.
- **Obliczanie Pola Wielokąta**: Narzędzie umożliwia obliczanie pola powierzchni wielokąta utworzonego na podstawie wybranych punktów na mapie.
- **Rysowanie Poligonów**: Użytkownik może wybrać punkty na mapie i utworzyć na ich podstawie poligon.
- **Wczytanie pliku**: Użytkownik może wczytać plik ze współrzędnymi punktów w układzie PL-1992 lub PL-2000.
- **Czyszczenie otrzymanych wyników**: Użytownik może wyczyścić otrzymany wynik z konsoli.
- **Odznaczenie zaznaczonych punktów**: Użytownik może odznaczyć zaznaczone punkty.
- **Wybór nowych punktów**: Po odznaczeniu punktów, użytkownik może zminimalizować okno wtyczki i następnie zaznaczyć nowe punkty i te punkty za pomocą przycisku "Wybierz punkty", wczytać nowowybrane punkty do wtyczki. 

## W przypadku obliczeń różnicy wysokości oraz pola powierzchi program pozwala na zmianę jednostki wyniku:
- rożnica wysokości: metry
- pole powierzchni: metry kwadratowe, ary, hektary


## Instrukcja Użytkowania
1. **Instalacja Wtyczki**: Wczytaj plik `.zip` zawierający wtyczkę do środowiska QGIS.
2. **Uruchomienie Wtyczki**: Po instalacji, uruchom wtyczkę z menu `Wtyczki > Wtyczka Projekt 2`.
3. **Wybór Warstwy**: Wybierz warstwę, na której chcesz wykonywać operacje.
4. **Wykonaj Operacje**: Wybierz operację (np. Obliczanie Różnicy Wysokości, Obliczanie Pola Wielokąta) i postępuj zgodnie z instrukcjami.
5. **Wczytaj Plik Z Punktami**: Umożliwia wczytanie pliku `.txt` lub `.csv` zawierającego współrzędne punktów do analizy.

## Wymagania Systemowe
- QGIS w wersji 3.36.0
- Python w wersji 3.11
- PyQt5
- PyQt5.QtWidgets
- PyQt5.QtCore
- qgis.PyQt
- qgis.core

## Instrukcja obsługi

## Autorzy
Plugin został stworzony przez [Twoje Imię/Nazwisko/Twórcę].

## Licencja
Ten projekt jest objęty licencją [TUTAJ WPISZ RODZAJ LICENCJI].
