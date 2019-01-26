# "Restful User-Service"

## Aufgabenstellung
Die detaillierte [Aufgabenstellung](TASK.md) beschreibt die notwendigen Schritte zur Realisierung.

## Implementierung
### REST-APi
Mit Hilfe von FLASKRESTful wurde ein einfache REST-API erstellt. Dieser kann mit folgendem Befehl ausgeführt werden:
```
cd src\main\python\server
python rest.py
```
### Vue
Es wurde mit VUE ein einfacher Client erstellt. Der mit folgenden Befehlen ausgeführt werden kann:
```
cd src\main\python\client\frontend
npm start
```

### Cypress
Mit Cypress kann die grafische Oberfläche (VUE) getestet werden. Die Tests können mit folgenden Befehl ausgeführt werden.
```
$(npm bin)/cypress run --spec 'cypress/integration/test.spec.js' 
```
### PyTest
Mit Pytest können die definierten Python Tests für die RESt-API ausgeführt werden.
```
cd src\main\python\server
pytest
```
### Tox
Mit Tox werden die Pytests ausgeführt und ein REPORT erstellt. Die benötigten Requiremnts sind in der requirements Datei beschrieben. 
Alles was tox tun soll steht in der tox.ini
Tox kann mit folgendem Befehl im Hauptverzeichnis ausgeführt werden:
```
tox
```
### Travis
Bei einem PUSH sollen alle Tests (grafisch und pytest) ausgeführt werden. Dafür wurde die travis.yml geschrieben und das Repo in die Travis.cy eingebunden. 
## Quellen
https://impythonist.wordpress.com/2015/07/12/build-an-api-under-30-lines-of-code-with-python-and-flask/
