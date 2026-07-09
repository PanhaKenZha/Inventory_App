import os
from functools import wraps

from flask import Flask, flash, redirect, render_template, request, session, url_for

from db import (
    authenticate_user,
    create_car,
    create_auth_user,
    create_category,
    create_user,
    get_car,
    get_cars,
    get_categories,
    get_category,
    get_user,
    get_users,
    init_db,
)

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-secret-key-change-me")


@app.before_request
def setup_database():
    if not app.config.get("DATABASE_READY"):
        init_db()
        app.config["DATABASE_READY"] = True


def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)

    return wrapped_view


@app.context_processor
def inject_current_user():
    return {
        "current_user_name": session.get("user_name"),
    }


@app.route("/")
@login_required
def index():
    cars = get_cars()
    users = get_users()
    categories = get_categories()
    available_cars = sum(1 for car in cars if not car.get("sold"))

    stats = {
        "cars": len(cars),
        "available_cars": available_cars,
        "users": len(users),
        "categories": len(categories),
    }

    return render_template("index.html", stats=stats)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match.")
            return render_template("register.html")

        created = create_auth_user(
            request.form["name"],
            request.form["email"],
            request.form["phone"],
            password,
        )

        if not created:
            flash("That email is already registered.")
            return render_template("register.html")

        flash("Account created. Please log in.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = authenticate_user(
            request.form["email"],
            request.form["password"],
        )

        if not user:
            flash("Invalid email or password.")
            return render_template("login.html")

        session.clear()
        session["user_id"] = user["id"]
        session["user_name"] = user["name"]

        next_page = request.args.get("next") or url_for("index")
        return redirect(next_page)

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/cars")
@login_required
def list_cars():
    cars = get_cars()
    return render_template("cars.html", cars=cars)


@app.route("/cars/new", methods=["GET", "POST"])
@login_required
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
@login_required
def car_detail(car_id):
    car = get_car(car_id)
    return render_template("car.html", car=car, car_id=car_id)


@app.route("/users")
@login_required
def list_users():
    users = get_users()
    return render_template("users.html", users=users)


@app.route("/users/new", methods=["GET", "POST"])
@login_required
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
@login_required
def user_detail(user_id):
    user = get_user(user_id)
    return render_template("user.html", user=user)


@app.route("/categories")
@login_required
def list_categories():
    categories = get_categories()
    return render_template("categories.html", categories=categories)


@app.route("/categories/new", methods=["GET", "POST"])
@login_required
def new_category():
    if request.method == "POST":
        create_category(
            request.form["name"],
            request.form.get("description", ""),
        )
        return redirect(url_for("list_categories"))
    return render_template("category_form.html")


@app.route("/categories/<int:category_id>")
@login_required
def category_detail(category_id):
    category = get_category(category_id)
    return render_template("category.html", category=category)


if __name__ == "__main__":
    app.run(debug=True)
