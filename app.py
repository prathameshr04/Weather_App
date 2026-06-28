from flask import Flask, render_template, request
import requests

app = Flask(__name__)  #intialize object to class flask

API_Key = "api key"

@app.route("/", methods=["GET","POST"])
def home():
    weather = None

    if request.method == "POST":
        city = request.form["city"]
        print("City Entered:", city)
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}&units=metric"
        response = requests.get(url)
        print("Status Code:", response.status_code)
        print(response.text)

        if response.status_code == 200:
            data = response.json()

            weather = {
                "city": city,
                "temp": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind": data["wind"]["speed"],
                "description": data["weather"][0]["description"]
            }
    return render_template("index.html" , weather=weather)

if __name__ == "__main__":
    app.run(debug=True)