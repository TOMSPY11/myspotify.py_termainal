#!/usr/bin/env python3

import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel

console = Console()

# 🎧 connect
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="user-read-playback-state,user-modify-playback-state,user-read-currently-playing"
))


def show_now_playing():
    try:
        current = sp.current_playback()
        if current and current["item"]:
            track = current["item"]
            name = track["name"]
            artist = track["artists"][0]["name"]

            console.print(Panel(f"🎧 {name}\n👤 {artist}", title="Now Playing"))
    except:
        pass


def search_and_play():
    query = Prompt.ask("🔍 Search song")
    results = sp.search(q=query, limit=5, type='track')

    tracks = results['tracks']['items']

    table = Table(title="Search Results")
    table.add_column("#", style="cyan")
    table.add_column("Song", style="magenta")
    table.add_column("Artist", style="green")

    for i, t in enumerate(tracks):
        table.add_row(str(i), t["name"], t["artists"][0]["name"])

    console.print(table)

    choice = int(Prompt.ask("Choose track"))
    uri = tracks[choice]['uri']

    try:
        sp.start_playback(uris=[uri])
        console.print("[green]▶️ Playing![/green]")
    except:
        console.print("[red]❌ Cannot play (need Premium)[/red]")


def main():
    console.print(Panel("🎧 MySpotify CLI", subtitle="myspotify_terminal"))

    while True:
        show_now_playing()

        cmd = Prompt.ask(
            "[bold cyan]Command[/bold cyan] (s=search, p=play, pa=pause, n=next, q=exit)"
        )

        if cmd in ["s", "search"]:
            search_and_play()
        elif cmd in ["pa", "pause"]:
            sp.pause_playback()
        elif cmd in ["p", "play"]:
            sp.start_playback()
        elif cmd in ["n", "next"]:
            sp.next_track()
        elif cmd in ["q", "exit"]:
            break


if __name__ == "__main__":
    main()
