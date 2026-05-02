import customtkinter as ctk
from tkinter import filedialog, END
import pygame
import os
from mutagen.mp3 import MP3
import random

# ---------------- Setup ----------------
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")  # required (we override colors)

pygame.mixer.init()

app = ctk.CTk()
app.geometry("750x550")
app.title("💗 Premium Music Player")

# ---------------- Pink Theme Colors ----------------
PRIMARY = "#ff4da6"
HOVER = "#ff3385"
LIGHT = "#ffe6f0"

app.configure(fg_color=LIGHT)

playlist = []
current_index = 0
paused = False

# ---------------- Functions ----------------

def load_music():
    files = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
    for file in files:
        playlist.append(file)
        listbox.insert(END, os.path.basename(file))


def play_music():
    global paused, current_index

    if paused:
        pygame.mixer.music.unpause()
        paused = False
        return

    try:
        current_index = listbox.curselection()[0]
    except:
        if not playlist:
            return

    song = playlist[current_index]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

    song_label.configure(text=os.path.basename(song))
    update_progress()
    animate_bars()


def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True


def next_music():
    global current_index
    if not playlist:
        return
    current_index = (current_index + 1) % len(playlist)
    listbox.select_clear(0, END)
    listbox.select_set(current_index)
    play_music()


def prev_music():
    global current_index
    if not playlist:
        return
    current_index = (current_index - 1) % len(playlist)
    listbox.select_clear(0, END)
    listbox.select_set(current_index)
    play_music()


def set_volume(val):
    pygame.mixer.music.set_volume(float(val))


def update_progress():
    if pygame.mixer.music.get_busy():
        current_time = pygame.mixer.music.get_pos() / 1000
        try:
            song_length = MP3(playlist[current_index]).info.length
            progress.set(current_time / song_length)
        except:
            pass
        app.after(1000, update_progress)


# ---------------- Equalizer Animation ----------------

bars = []

def create_bars():
    for i in range(20):
        bar = ctk.CTkFrame(anim_frame, width=8, height=15,
                           fg_color=PRIMARY, corner_radius=3)
        bar.grid(row=0, column=i, padx=2)
        bars.append(bar)

def animate_bars():
    if pygame.mixer.music.get_busy():
        for bar in bars:
            bar.configure(height=random.randint(10, 60))
        app.after(200, animate_bars)
    else:
        for bar in bars:
            bar.configure(height=10)

# ---------------- UI ----------------

title = ctk.CTkLabel(app, text="🎶 Music Player",
                     font=("Arial", 24, "bold"),
                     text_color=PRIMARY)
title.pack(pady=10)

song_label = ctk.CTkLabel(app, text="No song playing",
                         font=("Arial", 14),
                         text_color="#444")
song_label.pack()

# Playlist
listbox = ctk.CTkTextbox(app, height=120)
listbox.pack(padx=20, pady=10, fill="x")

# Progress bar
progress = ctk.CTkProgressBar(app,
                             width=500,
                             progress_color=PRIMARY)
progress.set(0)
progress.pack(pady=10)

# Animation
anim_frame = ctk.CTkFrame(app, fg_color="transparent")
anim_frame.pack(pady=10)

create_bars()

# Controls
controls = ctk.CTkFrame(app, fg_color="transparent")
controls.pack(pady=10)

ctk.CTkButton(controls, text="⏮", width=60,
              fg_color=PRIMARY, hover_color=HOVER,
              command=prev_music).grid(row=0, column=0, padx=5)

ctk.CTkButton(controls, text="▶", width=60,
              fg_color=PRIMARY, hover_color=HOVER,
              command=play_music).grid(row=0, column=1, padx=5)

ctk.CTkButton(controls, text="⏸", width=60,
              fg_color=PRIMARY, hover_color=HOVER,
              command=pause_music).grid(row=0, column=2, padx=5)

ctk.CTkButton(controls, text="⏭", width=60,
              fg_color=PRIMARY, hover_color=HOVER,
              command=next_music).grid(row=0, column=3, padx=5)

# Volume
volume = ctk.CTkSlider(app,
                       from_=0, to=1,
                       progress_color=PRIMARY,
                       button_color=PRIMARY,
                       button_hover_color=HOVER,
                       command=set_volume)
volume.set(0.5)
volume.pack(pady=10)

# Load button
ctk.CTkButton(app, text="📂 Load Songs",
              fg_color=PRIMARY,
              hover_color=HOVER,
              command=load_music).pack(pady=10)

app.mainloop()