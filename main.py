from flask import Flask, render_template
import requests
app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name


def time_api():
    url = "http://worldtimeapi.org/api/PST8PDT"

    response = requests.get(url)

    for key, val in response.json().items():
        if key == 'datetime':
            date = val.split('T')[0]
            time_long = val.split('T')[1]
            time = time_long.split('.')[0]
            print(date)
            print(time)
            return [date, time]


@app.route("/")                          # this tells you the URL the method below is related to
def home_page():
    date = time_api()
    return render_template("home.html", var=date[0])        # this prints HTML to the webpage


@app.route("/page_2")
def page_2():
    return render_template("page_2.html")


if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, port=5000, host='0.0.0.0')
    