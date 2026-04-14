# 🎧 MySpotify CLI

Simple Spotify terminal UI.

## 🚀 Setup

### 1. Install dependencies

```
pip3 install -r requirements.txt
```

### 2. Create Spotify App

Go to:
https://developer.spotify.com/dashboard

* Create App
* Add Redirect URI:

```
http://127.0.0.1:8888/callback
```

### 3. Set environment variables

```
export SPOTIFY_CLIENT_ID=your_client_id
export SPOTIFY_CLIENT_SECRET=your_client_secret
```

### 4. Run

```
python3 myspotify.py
```

---

## ⚠️ Notes

* Must add your account in "Users and Access" (Developer Dashboard)
* Premium required for playback
