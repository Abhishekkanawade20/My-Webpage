from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")   # serves index.html

@app.route("/newpage")
def new_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>New Page</title>
    </head>
    <body>
        <h1>This is the new page!</h1>
        <p>You clicked the button and opened this page.</p>
        <a href="/">Go Back</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
