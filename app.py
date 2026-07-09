from flask import Flask, render_template, request, redirect, url_for

from db import create_car, create_user, get_car, get_cars, get_user, get_users, init_db

app = Flask(__name__)


@app.before_request
def setup_database():
    if not app.config.get("DATABASE_READY"):
        init_db()
        app.config["DATABASE_READY"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cars")
def list_cars():
    cars = get_cars()
    return render_template("cars.html", cars=cars)


@app.route("/cars/new", methods=["GET", "POST"])
def new_car():
    if request.method == "POST":
        create_car(
            request.form["make"],
            request.form["model"],
            int(request.form["year"]),
            request.form["color"],
            request.form["price"],
        )
        return redirect(url_for("list_cars"))
    return render_template("car_form.html")


@app.route("/cars/<int:car_id>")
def car_detail(car_id):
    car = get_car(car_id)
    return render_template("car.html", car=car, car_id=car_id)


@app.route("/users")
def list_users():
    users = get_users()
    return render_template("users.html", users=users)


@app.route("/users/new", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        create_user(
            request.form["name"],
            request.form["email"],
            request.form["phone"],
        )
        return redirect(url_for("list_users"))
    return render_template("user_form.html")


@app.route("/users/<int:user_id>")
def user_detail(user_id):
    user = get_user(user_id)
    return render_template("user.html", user=user)


if __name__ == "__main__":
    app.run(debug=True)
