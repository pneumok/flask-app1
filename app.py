from flask impor Flask, render_template, requests

app=Flask(__name__)
@app.route(/)
def index():
    return render_template("index.html")

@app.tables(/tables/)
def tables():
    return render_template("tables.html")

@app.movie(/movies/)
def movie():
    return render_template("movies.html")

