from flask import Flask, render_template, request
import requests

app = Flask(__name__)  #intialize object to class flask

API_Key = "c3ba553a1debd0f0b4fc926bbcac2cef"

@app.route("/", methods=["GET","POST"]) # to get and post user data from forms(Html) an it is a decoretor
def home():# default home function
    weather = None# we do not have any weather data

    if request.method == "POST": #if user search a city
        city = request.form["city"]# to get city data from the forms
        print("City Entered:", city)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric" #api url
        response = requests.get(url)# to store response
        print("Status Code:", response.status_code)
        print(response.text)

        if response.status_code == 200:# if status code is sucesseful then
            data = response.json()#get the data from the api in string fromat 
            # amking a different dictionary to  only get percise data
            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "description": data["weather"][0]["description"]
            }
    return render_template("index.html" , weather=weather)# to redirect data to html forms

if __name__ == "__main__":
    app.run(debug=True)