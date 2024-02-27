import gspread
from oauth2client.service_account import ServiceAccountCredentials
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
SPOTIPY_CLIENT_ID = 'b13974f2a4e649b08f2012388a5b22f7'
SPOTIPY_CLIENT_SECRET = '4f526024d02a4a2494ba63df6cbc9c37'
SPOTIPY_REDIRECT_URI = 'http://localhost:3000' #change this later

# Google Sheets credentials
GOOGLE_SHEET_JSON_PATH = 'path/to/your/credentials.json'
GOOGLE_SHEET_NAME = 'YourSheetName'

# Spotify playlist ID
PLAYLIST_ID = 'your_playlist_id'

# Set up Spotify authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope='playlist-modify-public'))

# Set up Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_SHEET_JSON_PATH, scope)
client = gspread.authorize(creds)

# Access the Google Sheet
sheet = client.open(GOOGLE_SHEET_NAME).sheet1

# Get all values from the Google Sheet
values = sheet.get_all_values()

# Iterate through each row in the Google Sheet
for row in values:
    # Search for the song on Spotify
    results = sp.search(q=f"{row[0]} {row[1]}", type='track', limit=1)
    
    # Check if a track is found
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        
        # Add the track to the playlist
        sp.playlist_add_items(playlist_id=PLAYLIST_ID, items=[track_id])
        print(f"Added {row[1]} by {row[0]} to the playlist.")
    else:
        print(f"Song {row[1]} by {row[0]} not found on Spotify.")
