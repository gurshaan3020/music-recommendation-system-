🎵 Emotion-Based Music Recommender

An intelligent desktop application that recommends songs based on the user's emotions and preferred music genre. The application analyzes mood-related inputs and provides personalized song recommendations from a Spotify dataset.

Features

- 🎭 Emotion detection based on:
  - Current mood
  - Favorite color
  - Energy level
- 🎵 Genre-specific song recommendations
- 🎨 Modern dark-themed GUI using "ttkbootstrap"
- 🔄 Reset form functionality
- 📊 Uses Spotify song dataset
- 🎲 Randomized recommendations for variety

Tech Stack

- Python
- Tkinter
- ttkbootstrap
- Pandas
- CSV Dataset

Project Structure

.
├── main.py
├── spotify_data.csv
├── requirements.txt
└── README.md

Installation

1. Clone the repository

git clone https://github.com/your-username/emotion-based-music-recommender.git
cd emotion-based-music-recommender

2. Create and activate a virtual environment

Windows

python -m venv .venv
.venv\Scripts\activate

Linux / macOS

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the application

python main.py

How It Works

1. The user answers a few questions:
   
   - How are you feeling today?
   - What's your favorite color right now?
   - What is your energy level?
   - Which music genre do you prefer?

2. The application maps these responses to an emotion:
   
   - Happy
   - Sad
   - Angry
   - Relaxed
   - Neutral

3. Songs with matching emotions and genres are selected from the Spotify dataset and displayed as recommendations.

Example Recommendation

🎵 Happy Songs in Pop Genre

🎶 'Track Name' by Artist Name
Album: Album Name
Popularity: 85

Dependencies

- pandas
- ttkbootstrap

Install them with:

pip install pandas ttkbootstrap

Future Improvements

- Integrate Spotify API
- Add album cover images
- Implement machine learning-based emotion prediction
- Save favorite songs
- Export playlists
- Improve recommendation accuracy

License

This project is created for educational purposes and personal learning.

---

⭐ If you found this project useful, consider giving it a star on GitHub!