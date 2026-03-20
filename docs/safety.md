# Procedury bezpieczeństwa — Unitree G1 EDU

## Zasady ogólne

1. **Najpierw symulator.** Każdy nowy kod musi być przetestowany w symulatorze zanim trafi na fizycznego robota.
2. **Minimum dwie osoby.** Podczas testów na fizycznym robocie w pobliżu muszą być co najmniej dwie osoby.
3. **Przycisk awaryjny (e-stop).** Jedna z obecnych osób musi mieć dostęp do przycisku awaryjnego przez cały czas trwania testu.
4. **Review przed testem.** Kod musi być zreviewowany (PR zaapproved) przed uruchomieniem na robocie.
5. **W razie wątpliwości — STOP.** Jeśli coś wygląda nieprawidłowo, zatrzymaj robota i skonsultuj z maintainerami.

## Przed testem na fizycznym robocie

- [ ] Kod przetestowany w symulatorze bez błędów
- [ ] PR zreviewowany i zaapproved przez co najmniej 1 osobę
- [ ] Przestrzeń wokół robota wolna (min. 2 m w każdą stronę)
- [ ] Robot w bezpiecznej pozycji startowej
- [ ] Bateria naładowana do wymaganego poziomu
- [ ] Połączenie sieciowe / WiFi stabilne
- [ ] Obecna osoba z dostępem do e-stop

## Podczas testu

- [ ] Prędkości ograniczone do wartości testowych
- [ ] Obserwuj zachowanie robota przez cały czas
- [ ] Loguj wszystkie błędy i niespodziewane zachowania
- [ ] Nie odchodź od stanowiska podczas ruchu robota

## Po teście

- [ ] Zatrzymaj robota w bezpiecznej pozycji
- [ ] Zapisz logi
- [ ] Udokumentuj wyniki w PR / issue
- [ ] Zgłoś wszelkie incydenty (nawet drobne) maintainerom

## Kontakty awaryjne

<!-- Uzupełnij po utworzeniu repo z tego szablonu -->

- Maintainer 1: @ALF1-RZIT/maintainers
- Kierownik laboratorium: _uzupełnij_
- Numer alarmowy uczelni: _uzupełnij_
