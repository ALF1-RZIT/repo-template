# Ruleset — ochrona gałęzi `main`

Repozytorium zawiera plik `.github/rulesets/main-protection.json` opisujący **ruleset GitHub** do ochrony gałęzi `main`. Ruleset ten należy ręcznie zaimportować lub skonfigurować w ustawieniach każdego repozytorium utworzonego z tego szablonu.

---

## Co to jest ruleset?

**Ruleset** (zestaw reguł) to mechanizm GitHub pozwalający wymusić określone zasady pracy z repozytorium — niezależnie od uprawnień użytkownika. W odróżnieniu od klasycznych branch protection rules, rulesets można eksportować, importować i stosować masowo w organizacji.

---

## Opisane reguły (`main-protection.json`)

| Reguła | Opis |
|--------|------|
| **Ochrona przed usunięciem** (`deletion`) | Zakazuje usunięcia gałęzi `main`. Nikt — włącznie z administratorami — nie może jej skasować przez pomyłkę. |
| **Zakaz force-push** (`non_fast_forward`) | Zakazuje wymuszonego nadpisania historii (`git push --force`) na gałęzi `main`. Chroni historię commitów przed utratą. |
| **Wymagany Pull Request** (`pull_request`) | Każda zmiana na `main` musi przejść przez PR. Bezpośredni push na `main` jest zablokowany. |
| ↳ Wymagane jedno zatwierdzenie | PR musi otrzymać co najmniej **1 zatwierdzenie** (approve) od recenzenta. |
| ↳ Odrzucenie nieaktualnych review | Po każdym nowym pushu do gałęzi PR dotychczasowe approvals są automatycznie **unieważniane** — recenzent musi zatwierdzić ponownie. |
| ↳ Wymagany review od CODEOWNERS | Zatwierdzenie musi pochodzić od osoby wskazanej w pliku `CODEOWNERS` jako właściciel zmienianych plików. |
| ↳ Wymagane zamknięcie dyskusji | Wszystkie wątki recenzji (`review threads`) muszą być **rozwiązane** przed mergem. |
| **Wymagane testy CI** (`required_status_checks`) | Merge jest zablokowany, dopóki skonfigurowane statusy CI nie przejdą pomyślnie. Lista wymaganych sprawdzeń jest pusta domyślnie — uzupełnij po dodaniu workflow CI. |
| ↳ Aktualny branch | Branch musi być **aktualny względem `main`** zanim przejdą testy — wymagany rebase lub merge przed finalnym sprawdzeniem. |

---

## Jak zaimportować ruleset do repozytorium

### Metoda 1 — interfejs GitHub (zalecana)

1. Przejdź do **Settings → Rules → Rulesets** w repozytorium.
2. Kliknij **„New ruleset" → „Import a ruleset"**.
3. Wgraj plik `.github/rulesets/main-protection.json`.
4. Przejrzyj ustawienia i kliknij **„Create"**.

### Metoda 2 — GitHub CLI

```bash
gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  /repos/ALF1-RZIT/<nazwa-repozytorium>/rulesets \
  --input .github/rulesets/main-protection.json
```

### Metoda 3 — organizacyjny ruleset (dla maintainerów)

Administratorzy organizacji mogą zastosować ruleset do **wszystkich repozytoriów** w organizacji jednocześnie:

1. Przejdź do **Organization Settings → Rules → Rulesets**.
2. Kliknij **„New ruleset"** i skonfiguruj docelowe repozytoria.
3. Wgraj lub ręcznie odwzoruj reguły z `main-protection.json`.

---

## Po zaimportowaniu — uzupełnij wymagane statusy CI

Jeśli repozytorium posiada workflow CI (np. w `.github/workflows/`), dodaj wymagane sprawdzenia:

1. Przejdź do **Settings → Rules → Rulesets → Ochrona gałęzi main**.
2. W sekcji **„Require status checks to pass"** dodaj nazwy swoich jobów CI (np. `build`, `test`).
3. Zapisz zmiany.

---

## Kto może ominąć reguły?

Domyślnie ruleset obowiązuje wszystkich, w tym administratorów. Jeśli konieczne jest tymczasowe ominięcie (np. hotfix), administrator może zmodyfikować ruleset lub dodać siebie do listy bypass actors. **Nie rób tego rutynowo** — każde ominięcie powinno być wyjątkiem i udokumentowane.

---

> 📌 W razie pytań dotyczących konfiguracji ruleset skontaktuj się z maintainerami: `@ALF1-RZIT/maintainers`
