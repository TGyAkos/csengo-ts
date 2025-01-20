#!/bin/python

# --- Imports --------------------------------

import time
from pygame import mixer
import sys
import uuid
import schedule
import requests
import json
from dotenv import load_dotenv
import os
import requests
import socketio
import threading
# --- Global ---------------------------------

csengo_times = [
    '08:00', '08:45',
    '08:55', '09:40',
    '09:50', '10:35',
    '10:45', '11:30',
    '11:40', '12:25',
    '12:35', '13:20',
    '13:25', '14:10',
    '14:15', '15:00',
]

config = load_dotenv()


# url = os.getenv("API_URL")+"/api/songs/get-winner-audio"
wsUrl = os.getenv("WS_URL")
wsHandshakePath = os.getenv("WS_HANDSHAKE_PATH")

myobj = {"ws_api_key": os.getenv("WS_API_KEY") }

song = "song.mp3"

sio = socketio.Client()

retry_connection = False

# --- Functions ------------------------------

def on_connect():
    global retry_connection
    print("Socket.IO connection established")
    retry_connection = False

def on_disconnect():
    global retry_connection
    print("Socket.IO connection closed. Retrying every 5 seconds...")
    retry_connection = True

def on_message(data):
    print(f"Received message: {data}")

def on_updateAudioOnServer(data):
    print(f"Received message: {data}")
    get_winning_song()


def on_startAudioOnServer(data):
    print(f"Received message: {data}")
    start_audio()

def on_stopAudioOnServer(data):
    print(f"Received message: {data}")
    stop_audio()

def connect_to_socketio():
    global retry_connection
    while True:
        try:
            if sio.connected:
                sio.disconnect()
                print("Disconnected from previous connection")

            sio.on('connect', on_connect)
            sio.on('disconnect', on_disconnect)
            sio.on('message', on_message)
            sio.on('updateAudioOnServer', on_updateAudioOnServer)
            sio.on('startAudioOnServer', on_startAudioOnServer)
            sio.on('stopAudioOnServer', on_stopAudioOnServer)

            sio.connect(url=wsUrl, headers=myobj, socketio_path=wsHandshakePath)
            sio.wait()
        except Exception as e:
            print(f"Connection failed: {e}. Retrying in 5 seconds...")
            time.sleep(5)
        if retry_connection:
            print(f"Connection failed after disconnect. Retrying in 5 seconds...")
            retry_connection = False
            continue

def start_socketio_listener():
    socketio_thread = threading.Thread(target=connect_to_socketio)
    socketio_thread.daemon = True
    socketio_thread.start()

def get_csengo_times():
    print("Getting csengo times")

def get_csengo_times():
    print("Getting csengo times")

def get_songs():
    song = None

    # Get  winner from server
    # r = requests.get(url)
    # if r.text == "":
    #     print("Can't get data from server")
    #     return

    # getting sound file from server    
    # files = json.loads(r.text)
    # soundurl = os.getenv("API_URL")+"/sounds/"+ files["sounds"][0]["id"]

    # writing response to mp3 file
    # response = requests.get( soundurl,headers = myobj  )
    # open("sound.mp3", "wb").write(response.content)


def get_winning_song():
    print("Getting winning song")
    winning_song_url = os.getenv("API_URL") + "/api/songs/get-winner-audio"

    try:
        response = requests.get(winning_song_url)
        if response.status_code != 200:
            print("Error getting winning song")
            error_message = response.json().get("message", "Error parsing json")
            sio.emit('updateAudioOnServer', {"status": "error", "message": f"Error getting winning song, {error_message}"})
            return
        if os.path.exists(song):
            try:
                os.remove(song)
                print("Deleted old song")
            except PermissionError:
                print("File is in use, retrying...")
                time.sleep(1)
                os.remove(song)
        with open("song.mp3", "wb") as file:
            file.write(response.content)
        sio.emit('updateAudioOnServer', {"status": "success", "message": "Successfully updated winning song"})
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        sio.emit('updateAudioOnServer', {"status": "error", "message": "Request failed"})
    except IOError as e:
        print(f"File operation failed: {e}")
        sio.emit('updateAudioOnServer', {"status": "error", "message": "File operation failed, the song might be in use, try again in a few seconds"})


def play_song(filename):
    if not os.path.isfile(filename):
        print(f"File {filename} not found in working directory")
        return
    mixer.music.load(filename)
    mixer.music.play()
    while mixer.music.get_busy():  # Wait for music to finish playing
        time.sleep(1)
    mixer.music.unload()

def start_audio():
    try:
        mixer.music.set_volume(.80)
        sio.emit('startAudioOnServer', {"status": "success", "message": "Successfully started audio"})
    except Exception as e:
        print(f"Failed to set volume: {e}")
        sio.emit('startAudioOnServer', {"status": "error", "message": f"Failed to start audio: {e}"})

def stop_audio():
    try:
        mixer.music.set_volume(0)
        sio.emit('stopAudioOnServer', {"status": "success", "message": "Successfully stopped audio"})
    except Exception as e:
        print(f"Failed to set volume: {e}")
        sio.emit('stopAudioOnServer', {"status": "error", "message": f"Failed to stop audio: {e}"})


def csengo():
    play_song(song)


# --- Init -----------------------------------

mixer.init()
mixer.music.set_volume(.80) # preventing earrape

# Start WebSocket listener
start_socketio_listener()


# --- Main ----------------------------------

# Get filenames from server
get_songs()

play_song(song)

# Schedule times
# schedule.every().day.at('00:01').do(get_songs) # Every night get the new music files (and delete the old ones)


# TISZTA KOD ELVE!!!1111!!!!
for t in csengo_times:
    schedule.every().monday.at(t).do(csengo)
    schedule.every().tuesday.at(t).do(csengo)
    schedule.every().wednesday.at(t).do(csengo)
    schedule.every().thursday.at(t).do(csengo)
    schedule.every().friday.at(t).do(csengo)


# Wait for schedules
while True:
    schedule.run_pending()
    time.sleep(1)


