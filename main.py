# Install required packages in the notebook environment
import sys

import pandas as pd
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from tkinter import messagebox

# Load CSV
df = pd.read_csv("spotify_data.csv")

# Add emotion classification
def classify_emotion(row):
    valence = row['valence']
    energy = row['energy']
    if valence > 0.6 and energy > 0.6:
        return 'Happy'
    elif valence < 0.4 and energy < 0.5:
        return 'Sad'
    elif valence < 0.4 and energy > 0.6:
        return 'Angry'
    elif valence > 0.6 and energy < 0.5:
        return 'Relaxed'
    else:
        return 'Neutral'

df['emotion'] = df.apply(classify_emotion, axis=1)

# Map answers to emotion
def map_answers_to_emotion(mood, color, energy):
    mood = mood.lower()
    color = color.lower()
    energy = energy.lower()
    # Simple mapping logic
    if mood in ['happy', 'excited'] or color in ['yellow', 'orange'] or energy == 'high':
        return 'Happy'
    elif mood in ['sad', 'down'] or color in ['blue', 'grey'] or energy == 'low':
        return 'Sad'
    elif mood in ['angry', 'frustrated'] or color in ['red', 'black'] or (energy == 'high' and mood == 'angry'):
        return 'Angry'
    elif mood in ['relaxed', 'calm'] or color in ['green', 'purple'] or (energy == 'low' and mood == 'relaxed'):
        return 'Relaxed'
    else:
        return 'Neutral'

# Function to recommend songs
def get_recommendations():
    mood = mood_var.get()
    color = color_var.get()
    energy = energy_var.get()
    genre = genre_var.get()
    emotion = map_answers_to_emotion(mood, color, energy)
    num = 5
    # Ensure genre matching is case-insensitive and trimmed
    filtered = df[(df['emotion'].str.lower() == emotion.lower()) & (df['playlist_genre'].str.lower().str.strip() == genre.lower().strip())]
    if filtered.empty:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, f"No recommendations found for '{emotion}' emotion and '{genre}' genre.\n\n")
        result_text.insert(tk.END, f"Debug: Filtered DataFrame shape: {filtered.shape}\n")
        result_text.insert(tk.END, f"Available genres: {sorted(df['playlist_genre'].dropna().unique())}\n")
        return
    recommendations = filtered.sample(n=min(num, len(filtered)), random_state=42)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"🎵 {emotion.capitalize()} Songs in {genre.capitalize()} Genre:\n\n")
    for _, row in recommendations.iterrows():
        result_text.insert(tk.END, f"🎶 '{row['track_name']}' by {row['track_artist']} (Album: {row['track_album_name']}, Popularity: {row['track_popularity']})\n\n")

# Create GUI
app = tb.Window(themename="cyborg")
app.title("Emotion-Based Music Recommender")
app.geometry("700x650")

ttk.Label(app, text="Mood-Based Music Recommender", font=("Helvetica", 18, "bold")).pack(pady=20)

# Questionnaire
frame = ttk.Frame(app)
frame.pack(pady=10)

ttk.Label(frame, text="How are you feeling today?", font=("Helvetica", 12)).grid(row=0, column=0, sticky='w')
mood_var = tk.StringVar(value="Happy")
ttk.Combobox(frame, textvariable=mood_var, values=["Happy", "Sad", "Angry", "Excited", "Relaxed", "Calm", "Down", "Frustrated"], font=("Helvetica", 12), state="readonly").grid(row=0, column=1, padx=10)

ttk.Label(frame, text="What's your favorite color right now?", font=("Helvetica", 12)).grid(row=1, column=0, sticky='w')
color_var = tk.StringVar(value="Yellow")
ttk.Combobox(frame, textvariable=color_var, values=["Yellow", "Blue", "Red", "Green", "Orange", "Purple", "Grey", "Black"], font=("Helvetica", 12), state="readonly").grid(row=1, column=1, padx=10)

ttk.Label(frame, text="How is your energy level?", font=("Helvetica", 12)).grid(row=2, column=0, sticky='w')
energy_var = tk.StringVar(value="High")
ttk.Combobox(frame, textvariable=energy_var, values=["High", "Low"], font=("Helvetica", 12), state="readonly").grid(row=2, column=1, padx=10)

ttk.Label(frame, text="Select Playlist Genre:", font=("Helvetica", 12)).grid(row=3, column=0, sticky='w')
genre_var = tk.StringVar(value="pop")
genre_options = sorted([str(g).strip() for g in df['playlist_genre'].dropna().unique()])
ttk.Combobox(frame, textvariable=genre_var, values=genre_options, font=("Helvetica", 12), state="readonly").grid(row=3, column=1, padx=10)

ttk.Button(app, text="Get Recommendations", command=get_recommendations, bootstyle="success").pack(pady=10)

def reset_form():
    mood_var.set("Happy")
    color_var.set("Yellow")
    energy_var.set("High")
    genre_var.set("pop")
    result_text.delete("1.0", tk.END)

result_text = tk.Text(app, height=15, wrap=tk.WORD, font=("Consolas", 11))
result_text.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

ttk.Button(app, text="Reset", command=reset_form, bootstyle="warning").pack(pady=5)

app.mainloop()