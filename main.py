from flask import Flask, render_template
app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name


@app.route("/")                          # this tells you the URL the method below is related to
def home_page():
    return render_template("home.html")        # this prints HTML to the webpage


@app.route("/page_2")
def page_2():
    return render_template("page_2.html")


if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, port=5000, host='0.0.0.0')
    