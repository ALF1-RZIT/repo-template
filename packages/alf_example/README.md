# alf_example — Przykładowy pakiet ROS2

> **Szablon pakietu ROS2 (Python)** dla projektu ALF — Unitree G1 EDU.
> Skopiuj ten pakiet i dostosuj do swojej funkcjonalności.

---

## Co robi ten pakiet?

Pakiet `alf_example` zawiera minimalny, działający węzeł ROS2 napisany w Pythonie.
Węzeł co sekundę publikuje wiadomość tekstową na topicu `/alf/status`.

Cel pakietu to pokazanie **poprawnej struktury** pakietu ROS2 z narzędziami jakości kodu,
abyś mógł go skopiować i dostosować do własnej funkcjonalności.

---

## Struktura pakietu

```
alf_example/
├── alf_example/
│   ├── __init__.py          # Wymagany przez Python — inicjalizacja modułu
│   └── example_node.py      # Implementacja węzła ROS2
├── resource/
│   └── alf_example          # Znacznik zasobu wymagany przez ament
├── test/
│   ├── test_copyright.py    # Sprawdza nagłówki licencji w plikach
│   ├── test_flake8.py       # Sprawdza styl kodu (flake8)
│   └── test_pep8.py         # Sprawdza zgodność z PEP8
├── package.xml              # Metadane pakietu ROS2 (nazwa, wersja, zależności)
├── setup.cfg                # Konfiguracja instalacji skryptów
└── setup.py                 # Konfiguracja budowania pakietu Python
```

---

## Jak działa węzeł? (`example_node.py`)

```
┌─────────────────────────────────────────────────────┐
│                   ExampleNode                       │
│                                                     │
│  Timer (1 Hz)  ──►  timer_callback()               │
│                         │                           │
│                         ▼                           │
│                  publisher_.publish(msg)            │
│                         │                           │
│                         ▼                           │
│               Topic: /alf/status                   │
│               Type:  std_msgs/String               │
└─────────────────────────────────────────────────────┘
```

**Krok po kroku:**

1. **`__init__`** — konstruktor węzła:
   - Rejestruje węzeł w ROS2 pod nazwą `alf_example_node`
   - Tworzy **publisher** na topicu `/alf/status` (typ: `String`, głębokość kolejki: 10)
   - Tworzy **timer** wywołujący `timer_callback` co 1 sekundę

2. **`timer_callback`** — wywoływana cyklicznie co 1 sekundę:
   - Tworzy wiadomość `String` z tekstem `"ALF Example Node działa."`
   - Publikuje wiadomość na topicu `/alf/status`
   - Loguje komunikat na poziomie `DEBUG`

3. **`main`** — punkt wejścia programu:
   - Inicjalizuje `rclpy` (bibliotekę kliencką ROS2 dla Pythona)
   - Tworzy instancję węzła i uruchamia pętlę zdarzeń (`spin`)
   - Obsługuje graceful shutdown po `Ctrl+C`

---

## Uruchomienie

### 1. Zbuduj pakiet

```bash
cd ~/ros2_ws
colcon build --packages-select alf_example
source install/setup.bash
```

### 2. Uruchom węzeł

```bash
ros2 run alf_example example_node
```

Powinieneś zobaczyć w terminalu:
```
[INFO] [alf_example_node]: ALF Example Node uruchomiony.
```

### 3. Obserwuj publikowane wiadomości

W osobnym terminalu (po `source install/setup.bash`):

```bash
ros2 topic echo /alf/status
```

Oczekiwany wynik (co sekundę):
```
data: 'ALF Example Node działa.'
---
data: 'ALF Example Node działa.'
---
```

### 4. Sprawdź informacje o węźle

```bash
ros2 node info /alf_example_node
```

```bash
ros2 topic info /alf/status
```

---

## Testy

Pakiet zawiera trzy testy linterskie uruchamiane przez `colcon test`:

| Test | Co sprawdza |
|------|-------------|
| `test_copyright` | Nagłówki licencji Apache 2.0 w każdym pliku Python |
| `test_flake8` | Styl kodu (brak nieużywanych importów, błędów składniowych itp.) |
| `test_pep8` | Zgodność ze standardem PEP8 (wcięcia, długość linii itp.) |

```bash
cd ~/ros2_ws
colcon test --packages-select alf_example
colcon test-result --verbose
```

---

## Jak użyć tego pakietu jako szablonu?

### Krok 1 — Skopiuj pakiet

```bash
cp -r packages/alf_example packages/alf_moja_funkcjonalnosc
cd packages/alf_moja_funkcjonalnosc
```

### Krok 2 — Zmień nazwy (znajdź i zamień `alf_example` → `alf_moja_funkcjonalnosc`)

Pliki do edycji:
- `package.xml` — `<name>`, `<description>`, `<maintainer>`
- `setup.py` — `package_name`, `description`, `entry_points`
- `setup.cfg` — nazwa modułu
- Katalog `alf_example/` → `alf_moja_funkcjonalnosc/`
- Plik `resource/alf_example` → `resource/alf_moja_funkcjonalnosc`

### Krok 3 — Zaimplementuj logikę

Edytuj `alf_moja_funkcjonalnosc/example_node.py`:
- Zmień nazwę klasy i węzła
- Zmień typ i temat (topic) wiadomości
- Dodaj subskrybentów, serwisy lub parametry według potrzeb

### Krok 4 — Zbuduj i przetestuj

```bash
cd ~/ros2_ws
colcon build --packages-select alf_moja_funkcjonalnosc
colcon test --packages-select alf_moja_funkcjonalnosc
```

---

## Zasady kodowania

- Każdy plik Python musi zaczynać się od **nagłówka licencji Apache 2.0**
- Styl kodu: **PEP8** (weryfikowany przez `ament_pep8` i `ament_flake8`)
- Nazwy zmiennych, funkcji i klas: **angielski**
- Komentarze i docstringi: angielski lub polski

---

## Zależności

| Pakiet | Rola |
|--------|------|
| `rclpy` | Biblioteka kliencka ROS2 dla Pythona |
| `std_msgs` | Standardowe typy wiadomości ROS2 (tu: `String`) |
