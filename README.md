# Projekt2_wtyczka_QGIS
Wtyczka do QGIS - PyQGIS
## Opis
Wtyczka Projekt 2 to narzędzie stworzone w środowisku QGIS z wykorzystaniem języka Python. Pozwala na wykonywanie różnych operacji związanych z analizą punktów i wielokątów.

## Funkcje
- **Obliczanie Różnicy Wysokości**: Wtyczka umożliwia obliczanie różnicy wysokości między dwoma wybranymi punktami na mapie. Wysokości muszą być dostępne jako atrybuty punktów w postaci kolumnyu o nazwie "wysokosc".

  ![image](https://github.com/weronikaga/Projekt2_wtyczka_QGIS/assets/150865197/d6c90ac4-8c08-4521-9c79-fb1260d60330)
- **Obliczanie Pola Wielokąta**: Narzędzie umożliwia obliczanie pola powierzchni wielokąta utworzonego na podstawie wybranych punktów na mapie. Narzędzie zadziała jedynie, jeśli zostaną wybrane co najmniej 3 punkty.
- **Rysowanie Poligonów**: Użytkownik może wybrać punkty na mapie i utworzyć na ich podstawie poligon. Narysowany poligon utworzy się na nowej wartwie.
- **Wczytanie pliku**: Użytkownik może wczytać plik ze współrzędnymi punktów w układzie PL-1992 lub PL-2000. Rozpoznawane przez program rozszezrzenia plików to: .txt oraz .csv. Plik musi zawierać dwie kolumny, oddzielone od siebie przecinkiem.
- **Czyszczenie otrzymanych wyników**: Użytownik może wyczyścić otrzymany wynik z konsoli.
- **Odznaczenie zaznaczonych punktów**: Użytownik może odznaczyć zaznaczone punkty.
- **Wybór nowych punktów**: Po odznaczeniu punktów, użytkownik może zminimalizować okno wtyczki a następnie zaznaczyć nowe punkty oraz skontrolować ich współrzędne za pomocą przycisku "Wybierz punkty", następnie program wczyta nowowybrane punkty do wtyczki. 

## W przypadku obliczeń różnicy wysokości oraz pola powierzchi program pozwala na zmianę jednostki wyniku:
- rożnica wysokości: metry
- pole powierzchni: metry kwadratowe, ary, hektary


## Instrukcja Użytkowania
1. **Instalacja Wtyczki**: 
   W celu zapewnienia sprawnego działania wtyczki zalecamy zainstalowanie plików znajdujących się w repozytorium w katalogu plugings w folderze QGisa, aby znaleźć dokładną lokalizację tego katalogu, można skorzystać z instrukcji poniżej:
   ![image](https://github.com/weronikaga/Projekt2_wtyczka_QGIS/assets/150865197/934bbf93-c16f-4cd3-8df0-2fb913258fee)
     W wybranym katalogu zalecamy stworzenie folderu z nazwą wtyczki i przekopiowaniu do niego wszystkich plików znajdujących się w repozytorium.
3. **Uruchomienie Wtyczki**: Po instalacji, uruchom wtyczkę z menu `Wtyczki > Wtyczka Projekt 2`. Warto na tym etapie mieć otwarty projekt, na którym będziemy wykonywać dalsze działania związane z wtyczką.
   ![Zrzut ekranu 2024-06-07 120937](https://github.com/weronikaga/Projekt2_wtyczka_QGIS/assets/150865197/b7b52db2-303b-4627-8f43-2a1184ce3346)
  Po wyborze wtyczki wyświetli się nastepujące okno:
![image](https://github.com/weronikaga/Projekt2_wtyczka_QGIS/assets/150865197/c3e78e8d-fa37-4369-a0e3-e7f1073de2db)
5. **Wybór Warstwy**: Wybierz warstwę, na której chcesz wykonywać operacje.
   ![image](https://github.com/weronikaga/Projekt2_wtyczka_QGIS/assets/150865197/8d1ef136-58c3-4391-b826-dbfb0b96f50d)
7. **Wykonaj Operacje**: Wybierz operację (np. "Licz przewyższenie", "Licz powierzchnię") i postępuj zgodnie z instrukcjami. Po wykonaniu wybranej operacji program wyświetli komunikat. w przypadku pomyślnie wykonanego zadania, będzie to wynik w wybranej jednosce. Jeśli zadanie się nie powiedzie, program opublikuje stosowny błąd z intsrukcją, co należy poprawić.

![image](https://github.com/weronikaga/Projekt2_wtyczka_QGIS/assets/150865197/a042c795-3211-4e5a-8a38-ffe8897d6166)

![image](https://github.com/weronikaga/Projekt2_wtyczka_QGIS/assets/150865197/aaa38117-ddd7-4b40-af13-1d6c6ce25318)

## Wymagania Systemowe
- QGIS w wersji 3.36.0
- Python w wersji 3.11
- PyQt5
- PyQt5.QtWidgets
- PyQt5.QtCore
- qgis.PyQt
- qgis.core

## Obsługa znanych błędów:
- Wybór za małej ilości punktów
- Brak atrybutu "wysokosc" na wybranej wartwie
- Brak wyboru aktywnej wartwy
- Zła geometria wybranych obiektów
- Brak mozliwości zmiany typu zmiennej np. str na int
- Wybór pliku o złym rozszerzeniu lub o niewystarczającej liczbie kolumn

## Autorki
Plugin został stworzony przez [@emiliabartnik](https://github.com/emiliabartnik) oraz [@weronikaga](https://github.com/weronikaga).

