from flask import Flask, render_template, request, jsonify
from mcrcon import MCRcon
import json
import os

app = Flask(__name__)

# Konfiguration
SERVER_HOST = "127.0.0.1"  # Deine Minecraft Server IP ändern
SERVER_PORT = 25575  # RCON Port (in server.properties: rcon.port=25575)
SERVER_PASSWORD = "dein_rcon_passwort"  # RCON Passwort (in server.properties)
APP_PASSWORD = "meinpasswort123"  # Das Passwort für deine App

# Globale Variable für RCON Verbindung
rcon = None
logs = []

def connect_to_server():
    """Verbindung zum Minecraft Server herstellen"""
    global rcon
    try:
        rcon = MCRcon(SERVER_HOST, SERVER_PASSWORD, SERVER_PORT)
        rcon.connect()
        add_log("✓ Mit Server verbunden")
        return True
    except Exception as e:
        add_log(f"✗ Verbindungsfehler: {str(e)}")
        return False

def add_log(message):
    """Log-Nachricht hinzufügen"""
    logs.append(message)
    if len(logs) > 500:  # Nur letzte 500 Zeilen speichern
        logs.pop(0)

@app.route('/')
def login():
    """Login-Seite"""
    return render_template('login.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    """Login validieren"""
    data = request.json
    password = data.get('password', '')
    
    if password == APP_PASSWORD:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Falsches Passwort'})

@app.route('/dashboard')
def dashboard():
    """Dashboard (nach Login)"""
    return render_template('dashboard.html')

@app.route('/api/logs', methods=['GET'])
def get_logs():
    """Aktuelle Logs zurückgeben"""
    return jsonify({'logs': logs})

@app.route('/api/connect', methods=['POST'])
def api_connect():
    """Mit Minecraft Server verbinden"""
    if connect_to_server():
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': 'Verbindung fehlgeschlagen'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)