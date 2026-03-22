# ALF Template — Szablon projektu grupowego dla Unitree G1 EDU

> **Szablon repozytorium** dla uczelnianych projektów Unitree G1 EDU — ROS2 (Python), workflow zespołowy i checklisty bezpieczeństwa.

---

## Cel

- Szablon repozytorium służący jako baza do tworzenia nowych repozytoriów funkcjonalności robota **Unitree G1 EDU**.
- Zapewnia: konwencje workflow (issue → branch → PR → review → merge), przykładowy pakiet ROS2 (Python), checklisty bezpieczeństwa do testów na fizycznym robocie oraz zasady współpracy zespołowej.

## Kiedy używać tego szablonu

- Każda nowa funkcjonalność (np. algorytm percepcji, moduł planowania ruchu, moduł kognicji) powinna zaczynać się od repo utworzonego z tego szablonu.
- Repo może być rozwijane przez zespół kognicji, percepcji, akcji lub przez zespół interdyscyplinarny łączący wszystkie obszary.

## Szybki start

1. **Użyj tego repozytorium jako szablonu** → utwórz nowe repo (przycisk „Use this template" na GitHub).
2. Stwórz issue opisujące zadanie i kryteria akceptacji.
3. Branch: `feature/<issue>-<krótki-opis>`.
4. Otwórz PR z opisem, instrukcjami testowymi i checklistą bezpieczeństwa.
5. Po review i testach (symulator + fizyczny robot, jeśli konieczne) zmerguj.

> 📖 Szczegółowa instrukcja krok po kroku: [`docs/instrukcja.md`](docs/instrukcja.md)

---

## Struktura repozytorium

```
.
├── .github/
│   ├── CODEOWNERS                  # Właściciele kodu
│   ├── ISSUE_TEMPLATE/
│   │   ├── config.yml              # Konfiguracja wyboru szablonu issue
│   │   ├── feature.md              # Szablon zgłoszenia nowej funkcjonalności
│   │   ├── bug_report.md           # Szablon zgłoszenia błędu
│   │   └── task.md                 # Szablon ogólnego zadania
│   ├── rulesets/
│   │   └── main-protection.json    # Ruleset do importu w ustawieniach repo
│   └── PULL_REQUEST_TEMPLATE.md    # Szablon PR z checklistą bezpieczeństwa
├── docs/
│   ├── instrukcja.md               # Instrukcja krok po kroku — praca z szablonem
│   ├── ruleset.md                  # Opis ruleset i instrukcja konfiguracji
│   └── safety.md                   # Procedury bezpieczeństwa przy pracy z robotem
├── packages/
│   └── alf_example/                # Przykładowy pakiet ROS2 (Python)
│       ├── alf_example/
│       │   ├── __init__.py
│       │   └── example_node.py
│       ├── resource/
│       │   └── alf_example
│       ├── test/
│       │   ├── test_copyright.py
│       │   ├── test_flake8.py
│       │   └── test_pep8.py
│       ├── package.xml
│       ├── setup.cfg
│       └── setup.py
├── LICENSE
└── README.md
```

### Pliki obowiązkowe przy każdym feature

| Element | Opis |
|---------|------|
| **ISSUE** | Opis zadania, cel, kryteria akceptacji |
| **Branch** | `feature/<numer-issue>-<krótki-opis>` |
| **PR** | Opis zmian, instrukcje testowe, checklisty bezpieczeństwa (wypełnione) |
| **Review** | Min. 1 approver (patrz CODEOWNERS) |
| **Testy** | Symulator (obowiązkowo) + fizyczny robot (jeśli konieczne) |

---

## Szablony issues

Po utworzeniu repozytorium z tego szablonu dostępne są trzy typy issues:

| Szablon | Prefiks tytułu | Zastosowanie |
|---------|---------------|-------------|
| **Nowa funkcjonalność** | `[FEATURE]` | Nowy moduł, algorytm, węzeł ROS2 |
| **Zgłoszenie błędu** | `[BUG]` | Błąd w kodzie lub niespodziewane zachowanie robota |
| **Zadanie** | `[TASK]` | Refaktoryzacja, konfiguracja, research, dokumentacja |

Tworzenie pustych issues jest zablokowane — należy zawsze wybrać odpowiedni szablon.

---

## Ruleset — ochrona gałęzi `main`

Plik `.github/rulesets/main-protection.json` zawiera gotowy ruleset GitHub do ochrony gałęzi `main`. Po utworzeniu repozytorium z szablonu **należy go ręcznie zaimportować** w ustawieniach repozytorium.

Ruleset wymusza:
- **Zakaz bezpośredniego push** na `main` — każda zmiana musi przejść przez PR
- **Minimum 1 approval** od recenzenta (wymagany CODEOWNER)
- **Zakaz force-push** i usunięcia gałęzi `main`
- **Rozwiązanie wszystkich wątków** recenzji przed mergem
- **Aktualizację brancha** względem `main` przed mergem

> 📖 Szczegółowa instrukcja importu i opis reguł: [`docs/ruleset.md`](docs/ruleset.md)

---

## Rola zespołów

| Zespół | Odpowiedzialność |
|--------|-----------------|
| **Kognicja** | Logika wysokiego poziomu, planowanie, podejmowanie decyzji |
| **Percepcja** | Przetwarzanie sensorów, widzenie komputerowe, wykrywanie obiektów |
| **Akcja** | Kontrola ruchu, wykonanie komend ruchu, interfejs z hardware |

---

## Bezpieczeństwo

Przed każdym testem na **fizycznym robocie** obowiązkowo przeczytaj [`docs/safety.md`](docs/safety.md) i wypełnij checklistę bezpieczeństwa w PR.

**Podstawowe zasady:**
- Zawsze testuj najpierw w symulatorze.
- Podczas testu na robocie — co najmniej dwie osoby w pobliżu (jedna przy przycisku awaryjnym).
- Nigdy nie uruchamiaj kodu na robocie bez wcześniejszego review PR.
- W razie wątpliwości — ZATRZYMAJ robota i skonsultuj z maintainerami.

---

## Licencja

Copyright 2026 ALF1-RZIT

Licensed under the Apache License, Version 2.0. See [LICENSE](LICENSE) for details.