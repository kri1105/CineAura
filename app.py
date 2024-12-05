from flask import Flask, render_template, request, url_for,flash, redirect

app = Flask(__name__)

#basic route
@app.route('/')
def home() :
    return render_template('index.html')


@app.route("/", methods=["GET", "POST"])
def book_tickets():
    if request.method == "POST":
        theater = request.form.get("theater")
        movie = request.form.get("movie")
        screen = request.form.get("screen")
        food_items = request.form.getlist("food")
        flash("Tickets confirmed! Add details for payment or other preferences.")
        return redirect(url_for("book_tickets"))

    return render_template("bookTickets.html")



if __name__ == "__main__" :
    app.run(debug=True)