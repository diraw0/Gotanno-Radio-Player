import tkinter as tk
import vlc
from pypresence import Presence
import time
import threading

DISCORD_CLIENT_ID = "" // Pon aqui tu id de discord

RADIO_URL = "https://radio.gotanno.love/"

class RadioPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Gotanno Love")
        master.geometry("300x250")
        master.resizable(False, False)
        master.configure(bg="#282c34")

        self.label = tk.Label(master, text="Gotanno Love ❤️", font=("Arial", 12), fg="white", bg="#282c34")
        self.label.pack(pady=10)

        self.play_button = tk.Button(master, text="▶ Reproducir", command=self.play_radio, bg="#61afef", fg="white", width=20)
        self.play_button.pack(pady=5)

        self.stop_button = tk.Button(master, text="⏹ Detener", command=self.stop_radio, bg="#e06c75", fg="white", width=20)
        self.stop_button.pack(pady=5)

        
        self.volume_label = tk.Label(master, text="🔊 Volumen", bg="#282c34", fg="white", font=("Arial", 10))
        self.volume_label.pack(pady=(10, 0))

        self.volume_slider = tk.Scale(master, from_=0, to=100, orient=tk.HORIZONTAL,
                                      command=self.set_volume, bg="#282c34", fg="white",
                                      troughcolor="#61afef", highlightbackground="#282c34")
        self.volume_slider.set(50)  
        self.volume_slider.pack()

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media = self.instance.media_new(RADIO_URL)
        self.player.set_media(self.media)

        self.player.audio_set_volume(50)  

        
        self.rpc = Presence(DISCORD_CLIENT_ID)
        self.rpc_connected = False

    def play_radio(self):
        self.player.play()

        if not self.rpc_connected:
            threading.Thread(target=self.connect_discord_presence, daemon=True).start()

    def stop_radio(self):
        self.player.stop()
        if self.rpc_connected:
            try:
                self.rpc.clear()
            except:
                pass

    def set_volume(self, value):
        volume = int(value)
        self.player.audio_set_volume(volume)

    def connect_discord_presence(self):
        try:
            self.rpc.connect()
            self.rpc_connected = True
            self.rpc.update(
                state="Gotanno love!♡",
                details="🎧 Escuchando Gotanno Love",
                large_image="Avatar",  
                large_text="Gotanno Love",
                start=time.time()
            )
        except Exception as e:
            print("No se pudo conectar con Discord:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = RadioPlayer(root)
    root.mainloop()

