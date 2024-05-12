# helpers.py
# helper function 
import json
import random
from pprint import pprint

class Helpers:
    def __init__(self):
        with open('songs.json') as f:
            self.songs = json.load(f)

    def makePlaylist(self, moods, counts):
        playlist = []

        # first emotion
        for i in range(0, counts[0]):
            # get random index of song
            index = random.randint(0, len(self.songs[moods[0]]) - 1 )
        
            # construct song object
            songDict = {
                "song": self.songs[moods[0]][index]["uri"],
                "emotion": moods[0],
                "name": self.songs[moods[0]][index]["name"]
            }

            # add song to playlist
            playlist.append(songDict)

            # remove from songs json
            del self.songs[moods[0]][index]

        # second emotion
        for i in range(0, counts[1]):
            # get random index of song
            index = random.randint(0, len(self.songs[moods[1]]) - 1 )
        
            # construct song object
            songDict = {
                "song": self.songs[moods[1]][index]["uri"],
                "emotion": moods[1],
                "name": self.songs[moods[1]][index]["name"]
            }

            # add song to playlist
            playlist.append(songDict)

            # remove from songs json
            del self.songs[moods[1]][index]

        # shuffle playlist
        random.shuffle(playlist)

        return playlist
