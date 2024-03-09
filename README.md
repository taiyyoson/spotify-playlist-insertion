# Making a Playlist Automator

## Intro/Explanation 
This is a personal project I made for my student government position @ ASUSF Senate. We have a QR code set up around campus for students to scan and enter songs they want to add to some collective playlist. We have this setup with the endgoal of events that utilize this collective playlist. So that we don't have to manually insert every entry into our playlist, I wanted to make a program using the Spotify Web API to **automate** the process. 

It's a pretty simple process using two different APIs/frameworks. A Google form stores all its entries into a Google Sheets file, so I use the built-in Python library `gspread` to pull data from Google Sheets and feed it into my program. That data then gets parsed into some string array, which we will use as an argument when calling the function that requests data from the Spotify web API. I make a request access token at the beginning and store it in `token`. For reference, the token is a long string of letters and numbers you get when you use your Client_ID and Client_Secret to make an API call. 

I use the token for every API call, and I use it to locate the songs given in the Google Sheets, and then insert that song in the playlist I created. It also prints the songs everytime a new song is added. 

### Notes/Improvements

This program is still very much in the development phase, since I have to figure out how to **append** songs to a playlist instead of creating a new playlist everytime the function is called.

## Files

I have three files: `.env`, `senatePlaylist.py`, and `test.py`. 


`.env` is where I store my CLIENT_ID and CLIENT_SECRET to keep it secure, since I don't want people messing with my Spotify App (although it doesn't matter too much haha). 

`senatePlaylist.py` is still a mess, since I used chatGPT to partially generate code and tweaked it as a start. It uses libraries/frameworks I'm not familiar with yet (`spotipy` & `oauth2`), but I leave it as a reference and for the potential this project has. 

`test.py` is where I play with methods and features the Spotify API has to offer. I created a bunch of basic methods with basic functions, like `get_songs_by_artist`, which returns the top tracks of some given `artist_id`. Of course, I have another method that takes care of finding the `artist_id` of some given artist.

Code block: 
```
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result 
```

<img width="793" alt="Screenshot 2024-03-09 at 1 05 47 PM" src="https://github.com/taiyyoson/playlistAutomator/assets/123409233/68ce15d8-a50d-4635-8934-7c347f15933e">
This is what the sample output looks like for the sample method. I used ACDC as my example artist.

## Future Commits

In the near future--when I have time to work on this project again--I plan on implementing Shazam API to make this a little more interesting. I want to be able to use my Shazam, and when I do, the song Shazam returns automatically gets input into a playlist I have set aside called "COOL SONGS I DON'T KNOW THE NAME TO." Of course, it will be a while before I allot myself the time to work on this. I like to consider myself a busy person, I didn't achieve much in high school since I always felt out-of-place, so I am compensating now.


## For Viewers

You are welcome to use this code! I am not trying to copyright this in anyway (which is why I made my `.env` easily visible lmao), this is just a fun little side project I have been working on. Thanks for taking the time to read all this.
