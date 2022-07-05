from flask import Flask, render_template
app = Flask(__name__)
app.debug = True


headings = ("Nom du fichier", "Tags")
data = (
    ("image", "rguierh"),
    ("image", "kejfhviefndvkjn"),
    ("image", "jreifnvndvn")
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/search.html')
def search():
    return render_template('search.html', headings=headings, data=data)


if __name__ == '__main__':
    app.run()