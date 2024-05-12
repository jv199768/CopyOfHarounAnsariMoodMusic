import requests
import pprint


# auth token expires
auth_token = 'BQBivr17XD2fkWVRybcfPt8PpFJlAlm67abFQY292LlvkjvjK4vqP6HSjZcFtPHE6CdFMG85Wz92oexh7CXWPJx07RMVeC1NvIx1rRMOJpHtPqATVHLEPJNt3QIGeCdqqvN7UCC4KSM7tvyyScPuwyVfv0u3vd6-lcYnG8yldg'
headers = {'Authorization': 'Bearer ' + auth_token}
playlist_id = '0KPEhXA3O9jHFtpd1Ix5OB'
url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
pp = pprint.PrettyPrinter(indent=4) # set up pretty print indentation
print(url)
print('url')
print('headers')
print(headers)

r = requests.get(url, headers=headers)
#pp.pprint(r.json()["items"][0]["track"]["uri"])
songs = []

for item in r.json()["items"]:
    songDict = {}
    songDict["name"] = item["track"]["name"]
    songDict["uri"] = item["track"]["uri"]

    songs.append(songDict)

pp.pprint(songs)
