from flask import Flask, request, jsonify #import main Flask class and request object
import json
import requests
from helpers import Helpers
import pprint
import argparse

app = Flask(__name__) # create the Flask app
helpers = Helpers() # initialize helpers class
pp = pprint.PrettyPrinter(indent=4) # set up pretty print indentation

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--num", default=False, type=int)
parser.add_argument("--w1", default=False, type=float)
parser.add_argument("-host")
parser.add_argument("-port", type=str)
args = parser.parse_args()

@app.route('/add/pulse/<mood>', methods=['POST'])
def pulse(mood):
    if not mood:
        raise ValueError("Invalid Mood")

    if mood != 'happy' and mood != 'sad' and mood != 'angry':
        raise ValueError("Mood must be happy/sad/angry")

    # construct default response
    resp = {
        "Result": 'OK',
        "status": 200,
        "completed": False
    }

    print("Pulse Emotion Value: " +  str(mood))
    moods[1] = str(mood)

    resp["moods"] = moods

    if moods[0]:
        print("Both Values have been submit")
        # make playlist
        playlist = helpers.makePlaylist(moods, numSongs)
        print('playlist with ' + str(numSongs[0]) + ' ' + moods[0] + ' songs and ' + str(numSongs[1]) + ' ' + moods[1] + ' songs')
        pp.pprint(playlist)
        url = 'http://' + args.host + ':' + args.port + '/playlist/add'
        print("sending request to " + url)
        
        # send playlist to app
        #r = requests.post('http://localhost:5000/playlist/add', json = {'playlist': playlist})
        r = requests.post(url, json = {'playlist': playlist})
        print('request sent')
        resp["completed"] = True
        
        # delete moods
        moods[0] = ''
        moods[1] = ''

    resp = jsonify(resp)
    resp.status_code = 200
    return resp

@app.route('/add/face/<mood>', methods=['POST'])
def face(mood):
    if not mood:
        raise ValueError("Invalid Mood")

    if mood != 'happy' and mood != 'sad' and mood != 'angry':
        raise ValueError("Mood must be happy/sad/angry")

    # construct default response
    resp = {
        "Result": 'OK',
        "status": 200,
        "completed": False
    }

    print("Facial Emotion Value: " +  str(mood))
    moods[0] = str(mood)

    resp["moods"] = moods

    if moods[1]:
        print("Both Values have been submit")
        print(moods)
        
        # make playlist
        playlist = helpers.makePlaylist(moods, numSongs)
        print('playlist')
        pp.pprint(playlist)
        url = 'http://' + args.host + ':' + args.port + '/playlist/add'
        print("sending request to " + url)
        
        # send playlist to app
        #r = requests.post('http://localhost:5000/playlist/add', json = {'playlist': playlist})
        r = requests.post(url, json = {'playlist': playlist})
        print('request sent')
        resp["completed"] = True
        print('playlist with ' + str(numSongs[0]) + ' ' + moods[0] + ' songs and ' + str(numSongs[1]) + ' ' + moods[1] + ' songs')
        

        # send playlist to app
        r = requests.post('http://' + args.host + ':' + args.port + '/playlist/add', json = {'playlist': playlist})
        resp["completed"] = True
        
        # delete moods
        moods[0] = ''
        moods[1] = ''

    resp = jsonify(resp)
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    # default global variables
    moods = ['', '']
    totalSongs = 10
    weight_one = .7

    # parse command line arguments
    if args.num:
        totalSongs = args.num

    if args.w1:
        weight_one = args.w1 

    # calculate other values
    weight_two = 1 - weight_one
    numSongs = [int(weight_one * totalSongs), int(weight_two * totalSongs)]

    # make sure that it has the right number of songs
    if numSongs[0] + numSongs[1] == totalSongs - 1:
        numSongs[1] = numSongs[1] + 1
    elif numSongs[0] + numSongs[1] == totalSongs + 1:
        numSongs[1] = numSongs[1] - 1

    print('weight_one:')
    print(weight_one)
    print('weight_two:')
    print(weight_two)
    print('totalSongs:')
    print(totalSongs)
    print('numSongs:')
    print(numSongs)
    # run application
    app.run(debug=True, host='0.0.0.0' ,port=6000) #run app in debug mode on port 5000