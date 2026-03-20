## Opis zmian

<!-- Zwięzły opis co zostało zmienione i dlaczego. -->

Closes #<!-- numer issue -->

## Typ zmiany

- [ ] Nowa funkcjonalność (feature)
- [ ] Naprawa błędu (bug fix)
- [ ] Refaktoryzacja (bez zmiany funkcjonalności)
- [ ] Dokumentacja
- [ ] Inne: 

## Instrukcje testowe

<!-- Opisz jak przetestować wprowadzone zmiany. -->

### Symulator

```bash
# Kroki uruchomienia testu w symulatorze
```

### Fizyczny robot (jeśli dotyczy)

```bash
# Kroki uruchomienia testu na fizycznym robocie
```

---

## Checklista bezpieczeństwa — symulator

- [ ] Kod uruchomiony i przetestowany w symulatorze
- [ ] Brak niespodziewanych ruchów / kolizji w symulacji
- [ ] Logi nie zawierają błędów krytycznych

## Checklista bezpieczeństwa — fizyczny robot (wypełnij jeśli test na robocie)

- [ ] Test przeprowadzony najpierw w symulatorze ✅
- [ ] W pobliżu robota były co najmniej **dwie osoby**
- [ ] Jedna osoba miała dostęp do **przycisku awaryjnego (e-stop)**
- [ ] Robot był w bezpiecznej pozycji startowej przed uruchomieniem
- [ ] Przestrzeń wokół robota była wolna od przeszkód i ludzi
- [ ] Prędkości i siły ograniczone do wartości testowych (nie produkcyjnych)
- [ ] Kod zreviewowany przez co najmniej jedną inną osobę przed testem na robocie
- [ ] Wyniki testu udokumentowane (logi, nagranie wideo jeśli możliwe)

---

## Checklista PR

- [ ] Kod przeczytany i zrozumiany przez autora przed wystawieniem PR
- [ ] Branch aktualny względem `main`
- [ ] Testy jednostkowe / integracyjne przechodzą
- [ ] Dokumentacja zaktualizowana (jeśli konieczne)
- [ ] Checklisty bezpieczeństwa wypełnione
