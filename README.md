# 🎮 Minecraft Server Console

Eine einfache Web-App um die Server-Konsole deines Minecraft Servers zu überwachen - mit Passwort-Schutz und Read-Only Zugriff.

## ✨ Features

✅ Passwort-Login  
✅ Live Server-Konsole (Echtzeit-Updates)  
✅ Read-Only Modus (keine Befehle möglich)  
✅ Automatische Farbcodierung (Errors, Warnings, etc.)  
✅ Responsive Design (Web + Desktop)  

## 🚀 Installation

### 1. Requirements installieren
```bash
pip install -r requirements.txt
```

### 2. Minecraft Server vorbereiten

Öffne `server.properties` und stelle sicher, dass RCON aktiviert ist:

```properties
enable-rcon=true
rcon.port=25575
rcon.password=dein_rcon_passwort
```

### 3. App konfigurieren

Öffne `app.py` und passe folgende Einstellungen an:

```python
SERVER_HOST = "127.0.0.1"          # Deine Server IP (localhost für lokale Server)
SERVER_PORT = 25575                 # RCON Port (default 25575)
SERVER_PASSWORD = "dein_rcon_passwort"  # RCON Passwort aus server.properties
APP_PASSWORD = "meinpasswort123"    # App-Login Passwort
```

### 4. App starten

```bash
python app.py
```

Dann öffne deinen Browser und gehe zu: **http://localhost:5000**

## 📋 Anleitung

1. **Passwort eingeben** → Das ist dein `APP_PASSWORD`
2. **Dashboard öffnen** → Server-Konsole lädt automatisch
3. **Live-Logs ansehen** → Konsolen-Output wird in Echtzeit aktualisiert
4. **Logout** → Button oben rechts

## ⚙️ Troubleshooting

**Problem:** "Verbindung fehlgeschlagen"
- Überprüfe ob der Minecraft Server läuft
- Überprüfe ob RCON aktiviert ist (`enable-rcon=true`)
- Überprüfe die Passwörter und IP-Adressen

**Problem:** Logs werden nicht angezeigt
- Überprüfe die Server Console direkt auf Fehler
- Starte die App neu

## 📝 Nächste Schritte (Optional)

- [ ] Befehle mit Bestätigung erlauben
- [ ] Mehrere Benutzer mit Authentifizierung
- [ ] Spieler-Liste anzeigen
- [ ] Server-Stats (RAM, CPU, TPS)
- [ ] Dunkles Theme (bereits vorhanden!)

---

**Made with ❤️ für Minecraft Fans**