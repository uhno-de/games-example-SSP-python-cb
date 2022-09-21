# Schere - Stein - Papier -> Python

Beispiel-Implementation des Spiels "Schere - Stein - Papier" in Python.

Spielbeschreibung: https://games.uhno.de/game/SSP

Dieser Bot zieht in jedem Zug zufällig Schere, Stein oder Papier.

Den Socket.IO-Client und die Doku dazu gibt es hier: https://github.com/miguelgrinberg/python-socketio

## Starten des Bots

### Per Docker

```sh
docker build -t uhno-ssp-example-python .
docker run -e BOT_SECRET="geheimer-bot-api-key" uhno-ssp-example-python
```

### Manuell

Optional, startet eine virtuelle Umgebung:

```sh
python -m venv venv
. .venv/bin/activate
# unter Windows:
# .venv\Scripts\activate.bat
```

Dann:

```sh
python -m pip install -r requirements.txt
BOT_SECRET="geheimer-bot-api-key" python bot.py

# unter Windows kann man vielleicht am einfachsten die Variable SECRET
# in der bot.py bearbeiten und dann starten mit:
# python bot.py
```
