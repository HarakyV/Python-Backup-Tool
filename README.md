# 🗂️ Backup Tool

**Backup Tool** to proste narzędzie napisane w Pythonie z graficznym interfejsem użytkownika (GUI) przy użyciu biblioteki `Tkinter`. Program umożliwia szybkie tworzenie kopii zapasowych plików z jednego folderu do drugiego za pomocą automatycznie generowanego skryptu `.bat`.

---

## 📌 Funkcje

✅ Intuicyjny interfejs graficzny  
✅ Automatyczne generowanie i uruchamianie skryptu `.bat` do kopiowania plików  
✅ Zapisywanie i wczytywanie ścieżek źródłowych i docelowych  
✅ Tworzenie logów z informacjami o wykonanych kopiowaniach

---

## 🚀 Jak używać

1. **Uruchom program**
   - Upewnij się, że masz zainstalowanego Pythona i wymagane biblioteki (`tkinter`, `PIL`).
   - Uruchom skrypt Pythona:  
     ```bash
     python main.py
     ```

2. **Podaj ścieżki**
   - Wpisz ścieżkę do folderu, z którego mają być kopiowane pliki.
   - Wpisz ścieżkę do folderu, do którego pliki mają być skopiowane.

3. **Uruchom kopiowanie**
   - Kliknij przycisk `Submit`, aby rozpocząć kopiowanie.
   - Pliki zostaną skopiowane, a operacja zostanie zapisana w pliku `logs.txt`.

4. **Zapisz ścieżki**
   - Możesz zapisać ścieżki źródłową i docelową do pliku, aby użyć ich ponownie później.
   - Użyj przycisku `Zapisz ścieżki`.

5. **Wczytaj zapisane ścieżki**
   - Kliknij `Wczytaj Ścieżki`, aby automatycznie ustawić zapisane wcześniej foldery.

---

## 📂 Struktura projektu

