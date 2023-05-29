from flask import Flask, render_template, request

import opencage

import phonenumbers

from phonenumbers import geocoder, carrier

from opencage.geocoder import OpenCageGeocode

app = Flask(__name__)

@app.route('/')

def index():

    return render_template('index.html')

@app.route('/track', methods=['GET', 'POST'])

def track():

    geoCodeKey = "USE_YOUR_OWN_API_KEY"

    number = request.form["phoneNumber"]

    numTrack = phonenumbers.parse(number)

    location = geocoder.description_for_number(numTrack, "en")

    someThingIDK = carrier.name_for_number(numTrack, "en")

    geo = OpenCageGeocode(geoCodeKey)

    query = str(location)

    results = geo.geocode(query)

    latitude = results[0]['geometry']['lat']

    longitude = results[0]['geometry']['lng']

    return render_template('index.html', location = location, something = someThingIDK, latitude = latitude, longitude = longitude, phnumber = number)

if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port='5000')
