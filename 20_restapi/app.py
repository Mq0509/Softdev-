'''
Mussell Soup: Russell Goychayev, May Qiu
SoftDev
K20 -- A RESTful Journey Skyward/Calling API
2022-11-22
time spent: 1
'''
from flask import Flask, render_template
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def picture():
    #read key from file
    key = open("key_nasa.txt").read()
    #append to url string
    urlString = "https://api.nasa.gov/planetary/apod?api_key=" + key
    #make HTTP request to API using key
    jsonurl = urllib.request.urlopen(urlString)
    text = json.loads(jsonurl.read()) # <-- read from it 
    picture = text['url']
    desc = text['explanation']
    return render_template("main.html",picture_link=picture,explanation = desc)

if __name__ == '__main__':
    app.debug = True
    app.run()
