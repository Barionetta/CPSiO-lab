### CPSiO-lab - Repozytorium z rozwiązaniami zadań z kursu Cyfrowe Przetwarzanie Sygnałów i Obrazów.
## Spis treści
* [Opis](#opis)
* [Technologie](#technologie)
* [Uruchomienie](#uruchomienie)
* [Autor](#autor)

 ## Opis
Powyższe repozytorium zawiera rozwiązania list zadań z kursu Cyfrowe Przetwarzanie Sygnałów i Obrazów.

 ## Technologie
Projekt został napisany w całości w języku Python 3 z następującymi bibliotekami
* python=3.12.2
* jupyter==1.0.0
* scipy==1.12.0
* seaborn==0.13.2

## Uruchomienie
Aby uruchomić któryś ze skryptów lub notatników, najpierw należy sklonować repozytorium

``` bash
git clone https://github.com/Barionetta/CPSiO-lab.git
```

Następnie utworzyć wirtualne środowisko cpsio

```bash
conda env create -f environment.yml
```

Po utworzeniu i aktywowaniu środowiska można uruchomić dowolny skrypt w repozytorium z wybranymi parametrami, np.

 ```bash
python part_1.py ekg1.txt
```

## Autorzy
Autorami skryptów i notatników są Mateusz Gawłowski i Katarzyna Matuszek.