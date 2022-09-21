#!/usr/bin/python

SECRET = ""
SERVER_URL = "https://games.uhno.de"

import asyncio
import socketio
import random
import os

sio = socketio.AsyncClient()

async def handle_auth(success):
    if success:
        print("Anmeldung erfolgreich")
    else:
        print("Anmeldung fehlgeschlagen")
        await sio.disconnect()

@sio.event
async def connect():
    print('Verbunden!')
    await sio.emit('authenticate', SECRET, callback=handle_auth)

def handle_init(data):
    print("Neue Runde!")
    return None

def handle_result(data):
    print("Runde vorbei!")
    return None

def handle_round(data):
    figures = ['SCHERE', 'STEIN', 'PAPIER']
    # figures = ['STEIN']
    choice = random.choice(figures)
    print(f"Wir sind dran und nehmen {choice}")
    return choice

handlers = {
    'INIT': handle_init,
    'ROUND': handle_round,
    'RESULT': handle_result }

@sio.event
async def data(data):
    t = data['type']
    if t in handlers:
        return handlers[t](data)
    else:
        print("Unbekannte Nachricht: ", data)

@sio.event
async def disconnect():
    print('Verbindung beendet!')
    asyncio.get_event_loop().stop()

async def main():
    await sio.connect(SERVER_URL, transports=['websocket'])
    await sio.wait()

if __name__ == '__main__':
    secret_env = os.environ.get('BOT_SECRET')
    if secret_env:
        SECRET = secret_env
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
        loop.close()
    except:
        print("Byebye")

