from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def love_tree():
    return render_template("love.html")  # Ensure your file in templates is named love.html

if __name__ == "__main__":
    app.run(debug=True)
