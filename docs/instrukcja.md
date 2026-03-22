# Instrukcja krok po kroku — praca z szablonem repozytorium ALF

## Spis treści

1. [Wymagania wstępne](#1-wymagania-wstępne)
2. [Tworzenie nowego repozytorium z szablonu](#2-tworzenie-nowego-repozytorium-z-szablonu)
3. [Konfiguracja środowiska lokalnego](#3-konfiguracja-środowiska-lokalnego)
4. [Tworzenie zgłoszenia (issue)](#4-tworzenie-zgłoszenia-issue)
5. [Tworzenie gałęzi roboczej (branch)](#5-tworzenie-gałęzi-roboczej-branch)
6. [Implementacja funkcjonalności](#6-implementacja-funkcjonalności)
7. [Testowanie w symulatorze](#7-testowanie-w-symulatorze)
8. [Tworzenie Pull Request](#8-tworzenie-pull-request)
9. [Proces code review](#9-proces-code-review)
10. [Testowanie na fizycznym robocie](#10-testowanie-na-fizycznym-robocie)
11. [Scalanie zmian (merge)](#11-scalanie-zmian-merge)
12. [Typowe problemy i rozwiązania](#12-typowe-problemy-i-rozwiązania)

---

## 1. Wymagania wstępne

Przed rozpoczęciem pracy upewnij się, że masz zainstalowane i skonfigurowane:

- **Git** — system kontroli wersji
- **ROS2** (Humble lub nowszy) — framework robotyczny
- **Python 3.10+** — wymagany przez pakiety ROS2
- **Konto GitHub** — z dostępem do organizacji `ALF1-RZIT`
- **Klucz SSH** skonfigurowany dla konta GitHub (lub token HTTPS)

Weryfikacja instalacji:

```bash
git --version
ros2 --version
python3 --version
```

---

## 2. Tworzenie nowego repozytorium z szablonu

### Krok 2.1 — Otwórz szablon na GitHub

1. Przejdź do repozytorium szablonu: `https://github.com/ALF1-RZIT/repo-template`
2. Kliknij zielony przycisk **„Use this template"** w prawym górnym rogu strony.
3. Wybierz opcję **„Create a new repository"**.

### Krok 2.2 — Skonfiguruj nowe repozytorium

Wypełnij formularz tworzenia repozytorium:

| Pole | Zalecana wartość |
|------|-----------------|
| **Owner** | `ALF1-RZIT` (organizacja) |
| **Repository name** | `<obszar>-<nazwa-funkcjonalności>`, np. `percepcja-wykrywanie-obiektow` |
| **Description** | Zwięzły opis funkcjonalności w języku polskim |
| **Visibility** | `Private` (domyślnie dla projektów wewnętrznych) |

4. Kliknij **„Create repository from template"**.

### Krok 2.3 — Skonfiguruj nowe repozytorium

Po utworzeniu repozytorium:

1. Przejdź do **Settings → Collaborators and teams** i dodaj odpowiednie zespoły z właściwymi uprawnieniami.
2. Zaktualizuj plik `CODEOWNERS` — zastąp `@ALF1-RZIT/maintainers` konkretnymi nazwami zespołów lub użytkowników.
3. Zaktualizuj `docs/safety.md` — uzupełnij sekcję **Kontakty awaryjne**.
4. Zaimportuj ruleset ochrony gałęzi `main` — szczegóły w [`docs/ruleset.md`](ruleset.md).

---

## 3. Konfiguracja środowiska lokalnego

### Krok 3.1 — Sklonuj repozytorium

```bash
git clone git@github.com:ALF1-RZIT/<nazwa-repozytorium>.git
cd <nazwa-repozytorium>
```

### Krok 3.2 — Skonfiguruj workspace ROS2

```bash
# Utwórz workspace ROS2 (jeśli jeszcze nie istnieje)
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# Dołącz repozytorium do workspace (symlink lub skopiuj pakiety)
ln -s ~/ścieżka/do/<nazwa-repozytorium>/packages/* .

# Wróć do workspace i zainstaluj zależności
cd ~/ros2_ws
rosdep install --from-paths src --ignore-src -r -y

# Zbuduj workspace
colcon build --symlink-install
```

### Krok 3.3 — Zainicjalizuj środowisko

```bash
source ~/ros2_ws/install/setup.bash
```

> 💡 Dodaj powyższy wiersz do pliku `~/.bashrc`, aby środowisko było inicjalizowane automatycznie przy każdym uruchomieniu terminala.

---

## 4. Tworzenie zgłoszenia (issue)

Każda nowa funkcjonalność lub poprawka musi zaczynać się od issue na GitHubie.

### Krok 4.1 — Otwórz formularz nowego issue

1. Przejdź do zakładki **Issues** w repozytorium.
2. Kliknij **„New issue"**.
3. Wybierz odpowiedni szablon:
   - **„Nowa funkcjonalność"** — dla nowych modułów i rozszerzeń
   - **„Zgłoszenie błędu"** — dla naprawy istniejącego kodu
   - **„Zadanie"** — dla prac niekodowych: refaktoryzacja, konfiguracja, dokumentacja, research

### Krok 4.2 — Wypełnij issue

Uzupełnij wszystkie sekcje szablonu:

- **Tytuł**: `[FEATURE] Krótki opis`, `[BUG] Krótki opis` lub `[TASK] Krótki opis`
- **Opis**: Co ma być zrobione i dlaczego
- **Cel i motywacja**: Jaki problem rozwiązuje dana funkcjonalność
- **Kryteria akceptacji**: Lista mierzalnych warunków ukończenia zadania
- **Zespół / obszar**: Zaznacz właściwy obszar (Kognicja / Percepcja / Akcja)
- **Plan testów**: Opisz jak będzie testowana funkcjonalność

### Krok 4.3 — Przypisz issue

- Przypisz issue do odpowiednich osób (**Assignees**)
- Dodaj właściwe etykiety (**Labels**)
- Przypisz do odpowiedniego milestone lub projektu (jeśli dotyczy)

---

## 5. Tworzenie gałęzi roboczej (branch)

### Krok 5.1 — Pobierz aktualne zmiany

```bash
git checkout main
git pull origin main
```

### Krok 5.2 — Utwórz nową gałąź

Konwencja nazewnictwa gałęzi: `feature/<numer-issue>-<krótki-opis-kebab-case>`

```bash
git checkout -b feature/42-wykrywanie-obiektow
```

Przykłady poprawnych nazw gałęzi:

| Typ | Przykład |
|-----|---------|
| Nowa funkcjonalność | `feature/15-modul-planowania-ruchu` |
| Naprawa błędu | `fix/23-naprawa-bledu-kolizji` |
| Dokumentacja | `docs/8-aktualizacja-readme` |

### Krok 5.3 — Opublikuj gałąź na GitHubie

```bash
git push -u origin feature/42-wykrywanie-obiektow
```

---

## 6. Implementacja funkcjonalności

### Krok 6.1 — Utwórz nowy pakiet ROS2

Skopiuj przykładowy pakiet i dostosuj go do nowej funkcjonalności:

```bash
cp -r packages/alf_example packages/alf_<nazwa_pakietu>
cd packages/alf_<nazwa_pakietu>
```

Zmień nazwy we wszystkich plikach:
- `package.xml` — zmień `<name>`, `<version>`, `<description>`, `<maintainer>`
- `setup.py` — zaktualizuj `name`, `packages`, `entry_points`
- `setup.cfg` — zaktualizuj `[tool:pytest]` i nazwy modułów

### Krok 6.2 — Implementuj kod

Twórz węzły ROS2 w katalogu `packages/alf_<nazwa_pakietu>/alf_<nazwa_pakietu>/`:

```python
# Wzorzec węzła ROS2 — wzoruj się na packages/alf_example/alf_example/example_node.py
```

Przestrzegaj zasad kodowania:
- Każdy plik musi zaczynać się od nagłówka licencji Apache 2.0
- Stosuj styl PEP8 (weryfikowane przez `ament_pep8` i `ament_flake8`)
- Nazwy zmiennych, funkcji i klas w języku angielskim
- Komentarze i docstringi mogą być po polsku lub angielsku

### Krok 6.3 — Commituj zmiany regularnie

```bash
git add .
git commit -m "feat: dodaj węzeł wykrywania obiektów"
git push
```

Konwencja wiadomości commitów:

| Prefix | Zastosowanie |
|--------|-------------|
| `feat:` | Nowa funkcjonalność |
| `fix:` | Naprawa błędu |
| `docs:` | Zmiany w dokumentacji |
| `refactor:` | Refaktoryzacja bez zmiany funkcjonalności |
| `test:` | Dodanie lub modyfikacja testów |
| `chore:` | Zmiany narzędziowe, konfiguracyjne |

---

## 7. Testowanie w symulatorze

> ⚠️ **Obowiązkowo przed każdym testem na fizycznym robocie.**

### Krok 7.1 — Zbuduj pakiet

```bash
cd ~/ros2_ws
colcon build --packages-select alf_<nazwa_pakietu>
source install/setup.bash
```

### Krok 7.2 — Uruchom testy jednostkowe

```bash
cd ~/ros2_ws
colcon test --packages-select alf_<nazwa_pakietu>
colcon test-result --verbose
```

### Krok 7.3 — Uruchom węzeł w symulatorze

```bash
# Uruchom symulator (np. Gazebo lub inny)
ros2 launch <pakiet_symulatora> <plik_launch>

# W osobnym terminalu uruchom węzeł
ros2 run alf_<nazwa_pakietu> <nazwa_węzła>
```

### Krok 7.4 — Weryfikacja działania

- Sprawdź, czy węzeł publikuje oczekiwane wiadomości: `ros2 topic echo /alf/<temat>`
- Sprawdź logi: `ros2 node info /alf_<nazwa_węzła>`
- Upewnij się, że brak niespodziewanych ruchów lub błędów krytycznych w logach

---

## 8. Tworzenie Pull Request

### Krok 8.1 — Upewnij się, że gałąź jest aktualna

```bash
git fetch origin
git rebase origin/main
git push --force-with-lease
```

### Krok 8.2 — Otwórz PR na GitHubie

1. Przejdź do repozytorium na GitHubie.
2. Kliknij **„Compare & pull request"** (pojawi się automatycznie po pushu) lub przejdź do zakładki **Pull requests → New pull request**.
3. Upewnij się, że:
   - **Base branch**: `main`
   - **Compare branch**: Twoja gałąź `feature/...`

### Krok 8.3 — Wypełnij opis PR

Szablon PR jest automatycznie wczytywany. Uzupełnij wszystkie sekcje:

- **Opis zmian**: Co zostało zmienione i dlaczego
- **Closes #<numer>**: Numer powiązanego issue
- **Typ zmiany**: Zaznacz odpowiednie pole
- **Instrukcje testowe**: Dokładne kroki testowania (symulator i/lub fizyczny robot)
- **Checklista bezpieczeństwa**: Wypełnij wszystkie pola checklisty

### Krok 8.4 — Przypisz recenzentów

- Dodaj co najmniej jednego recenzenta z listy **Reviewers** (zgodnie z `CODEOWNERS`)
- Przypisz PR do siebie w **Assignees**

---

## 9. Proces code review

### Dla autora PR

1. **Odpowiadaj na komentarze** recenzentów w ciągu 24 godzin.
2. **Wprowadzaj poprawki** w tej samej gałęzi i pushuj — PR zaktualizuje się automatycznie.
3. **Oznaczaj komentarze jako rozwiązane** po wprowadzeniu zmian.
4. **Nie zamykaj dyskusji** — pozwól recenzentowi samemu zamknąć komentarz po weryfikacji.

### Dla recenzenta

1. **Sprawdź poprawność kodu**: logika, zgodność ze standardami, brak błędów oczywistych.
2. **Sprawdź testy**: czy zostały napisane i czy przechodzą.
3. **Sprawdź checklistę bezpieczeństwa**: czy wszystkie punkty są zaznaczone i realistyczne.
4. **Zaapprove PR** (`Approve`) lub zażądaj zmian (`Request changes`) z konkretnymi uwagami.

> ℹ️ Wymagany jest **co najmniej 1 approval** przed mergem (zgodnie z ustawieniami gałęzi `main`).

---

## 10. Testowanie na fizycznym robocie

> ⚠️ **Wykonuj tylko po pozytywnym wyniku testów w symulatorze i po otrzymaniu approval w PR.**

Przed przystąpieniem do testów fizycznych **obowiązkowo** zapoznaj się z [`docs/safety.md`](safety.md).

### Krok 10.1 — Przygotowanie

- [ ] Kod przetestowany w symulatorze bez błędów
- [ ] PR zaapproved przez co najmniej 1 osobę
- [ ] Co najmniej **dwie osoby** obecne podczas testu
- [ ] Jedna osoba z dostępem do **przycisku awaryjnego (e-stop)**

### Krok 10.2 — Przygotowanie środowiska

```bash
# Na komputerze sterującym lub bezpośrednio na robocie:
source ~/ros2_ws/install/setup.bash

# Ustaw zmienne środowiskowe ROS2 (adres IP robota, domeny itp.)
export ROS_DOMAIN_ID=<numer_domeny>
```

### Krok 10.3 — Uruchomienie testu

```bash
# Uruchom węzeł w trybie testowym (prędkości ograniczone)
ros2 run alf_<nazwa_pakietu> <nazwa_węzła> --ros-args -p test_mode:=true
```

### Krok 10.4 — Obserwacja i dokumentacja

- Obserwuj zachowanie robota przez cały czas trwania testu
- Loguj wszystkie błędy i niespodziewane zachowania
- Nagraj wideo (jeśli możliwe)
- Po teście zatrzymaj robota w bezpiecznej pozycji

### Krok 10.5 — Po teście

```bash
# Zapisz logi do pliku
ros2 bag record -o test_<data>_<nazwa> /alf/<temat>
```

Udokumentuj wyniki w PR lub issue (logi, nagrania, obserwacje).

---

## 11. Scalanie zmian (merge)

### Krok 11.1 — Warunki przed mergem

Upewnij się, że spełnione są wszystkie warunki:

- [ ] Co najmniej 1 approval od recenzenta
- [ ] Wszystkie automatyczne testy (CI) przechodzą
- [ ] Checklisty bezpieczeństwa wypełnione
- [ ] Brak nierozwiązanych komentarzy w PR

### Krok 11.2 — Wykonaj merge

1. Na stronie PR kliknij **„Merge pull request"**.
2. Wybierz metodę: **„Squash and merge"** (zalecane dla czystej historii) lub **„Merge commit"**.
3. Potwierdź mergem klikając **„Confirm squash and merge"**.

### Krok 11.3 — Po mergu

```bash
# Lokalnie zaktualizuj gałąź main
git checkout main
git pull origin main

# Usuń lokalną gałąź roboczą
git branch -d feature/<numer-issue>-<krótki-opis>
```

---

## 12. Typowe problemy i rozwiązania

### Problem: Konflikty przy rebase

```bash
git fetch origin
git rebase origin/main
# Jeśli są konflikty:
# 1. Edytuj pliki z konfliktami
# 2. git add <plik>
# 3. git rebase --continue
```

### Problem: Błędy ament_flake8 lub ament_pep8

```bash
# Sprawdź błędy stylu lokalnie
cd ~/ros2_ws
ament_flake8 src/<nazwa_pakietu>
ament_pep8 src/<nazwa_pakietu>

# Automatyczna naprawa (jeśli dostępna)
autopep8 --in-place --recursive src/<nazwa_pakietu>
```

### Problem: Brakujący nagłówek licencji

Każdy plik Python musi zaczynać się od:

```python
# Copyright 2026 ALF1-RZIT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# ...
```

### Problem: Węzeł ROS2 nie startuje

```bash
# Sprawdź logi
ros2 run alf_<nazwa_pakietu> <nazwa_węzła> --ros-args --log-level DEBUG

# Sprawdź zainstalowane pakiety
ros2 pkg list | grep alf
```

### Problem: Brak uprawnień do merge

Upewnij się, że:
- PR ma wymagany approval od osoby z `CODEOWNERS`
- Wszystkie wymagane testy CI przechodzą
- Nie ma aktywnych żądań zmian (`Request changes`) od recenzentów

---

> 📌 W razie pytań lub problemów skontaktuj się z maintainerami: `@ALF1-RZIT/maintainers`
