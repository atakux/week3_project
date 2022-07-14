from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_behind_proxy import FlaskBehindProxy

import requests
app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name
proxied = FlaskBehindProxy(app)

app.config['SECRET_KEY'] = 'b20e38d339bdd8c3cfe994fee5370ec7'


class InputTimezone(FlaskForm):
    timezone = StringField('Enter Timezone', validators=[DataRequired()])
    submit = SubmitField('Submit')


def time_api(timezone):
    url = "http://worldtimeapi.org/api/" + str(timezone)

    response = requests.get(url)

    for key, val in response.json().items():
        if key == 'datetime':
            date = val.split('T')[0]
            time_long = val.split('T')[1]
            time = time_long.split('.')[0]
            print(date)
            print(time)
            return [date, time]


def get_zones():
    url = "http://worldtimeapi.org/api/timezone"

    response = requests.get(url)

    return response.json()


@app.route("/", methods=["GET", "POST"])                          # this tells you the URL the method below is related to
def home_page():
    user_input = InputTimezone()
    if user_input.validate_on_submit():
        date = time_api(user_input.timezone.data)
        return render_template("home.html", day=date[0], time=date[1], form=user_input)        # this prints HTML to the webpage
    return render_template("home.html", options=get_zones(), form=user_input)


@app.route("/page_2")
def page_2():
    return render_template("page_2.html")


if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, port=5000, host='0.0.0.0')
    