from flask import Flask, redirect, render_template, request, flash, session, request
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import UserSignForm, UserLogInForm
from newsapi import HEADLINES, TECH_CRUNCH_data, get_news, search_news, get_news_by_category
import requests
from sqlalchemy.exc import IntegrityError


app = Flask(__name__)

app.config["SECRET_KEY"] = "news-app"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///news-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
toolbar = DebugToolbarExtension(app)

# ROUTES TO REGISTER & AUTHENCTICATE USERS


# Sign Up route
@app.route("/register", methods=["GET", "POST"])
def register_page():

    form = UserSignForm()
    if form.validate_on_submit():
        username = form.username.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        dateofbirth = form.dateofbirth.data
        email = form.email.data
        password = form.password.data

        new_user = User.register(username=username, firstname=firstname, lastname=lastname,
                                 dateofbirth=dateofbirth, email=email, password=password)

        db.session.add(new_user)
        try:
            db.session.commit()
        except IntegrityError:
            flash("Username already taken, Please try another user", "danger")
            return render_template("users/register.html", form=form)

        session["username"] = new_user.username

        flash("Welcome to News Webpage, Your Account was created successfully", "success")
        return redirect("/")

    return render_template("users/register.html", form=form)


# ROUTE TO LOG IN
@app.route("/login", methods=["GET", "POST"])
def login_Page():

    form = UserLogInForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username=username, password=password)
        if user:
            session["username"] = user.username
            flash(f"Welcome to News Website {user.lastname}", "info")
            return redirect("/")
        else:
            flash("Invalid Username or Password", "danger")

    return render_template("users/login.html", form=form)


# ROUTE TO LOG OUT
@app.route("/logout")
def user_logout():

    flash("You are logged out Successfully", "danger")
    session.pop("username")
    return redirect("/")


# Routes to News Pages
    ######################################################


# Root Route
@app.route("/")
def root_page():
    headlines_data = HEADLINES
    tech_crunch_data = TECH_CRUNCH_data
    return render_template("region_news/index.html", headlines_data=headlines_data, tech_crunch_data=tech_crunch_data)


# Home Page Route
@app.route("/headlines")
def home_page():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")
    data = HEADLINES
    return render_template("region_news/top_headlines_news.html", data=data)


# Route to Search Articles
@app.route("/search")
def search_article():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")
    input = request.args['search']
    if not input:
        flash("Sorry, No result found")
    search = search_news(input)
    return render_template("region_news/search.html", search=search)


# TECH CRUNCH NEWS
@app.route("/techcrunch")
def tech_crunch():
    data = TECH_CRUNCH_data
    return render_template("region_news/tech_crunch.html", data=data)


# Route to USA News
@app.route("/region/us")
def get_news_usa():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("us")
    return render_template("region_news/usa_news.html", news=news)


# Route to UK News
@app.route("/region/uk")
def get_news_uk():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("gb")
    return render_template("region_news/uk_news.html", news=news)


# Route to Egypt News
@app.route("/region/eg")
def get_news_egypt():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("eg")
    return render_template("region_news/egypt_news.html", news=news)


# Route to Australia News
@app.route("/region/au")
def get_news_australia():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("au")
    return render_template("region_news/australia_news.html", news=news)


# Route to China News
@app.route("/region/cn")
def get_news_china():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("cn")
    return render_template("region_news/china_news.html", news=news)


# Route to India News
@app.route("/region/in")
def get_news_india():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("in")
    return render_template("region_news/india_news.html", news=news)


# Route to Israel News
@app.route("/region/il")
def get_news_israel():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("il")
    return render_template("region_news/israel_news.html", news=news)


# Route to Japan News
@app.route("/region/jp")
def get_news_japan():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("jp")
    return render_template("region_news/japan_news.html", news=news)


# Route to Korea News
@app.route("/region/kr")
def get_news_korea():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("kr")
    return render_template("region_news/korea_news.html", news=news)


# Route to Philippines News
@app.route("/region/ph")
def get_news_philippines():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("ph")
    return render_template("region_news/philippines_news.html", news=news)


# Route to Saudi Arabia News
@app.route("/region/sa")
def get_news_saudi_arabia():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("sa")
    return render_template("region_news/saudi_arabia_news.html", news=news)


# Route to Turkey News
@app.route("/region/tr")
def get_news_turkey():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("tr")
    return render_template("region_news/turkey_news.html", news=news)


# Route to United Arab Emirates News
@app.route("/region/ae")
def get_news_united_arab_emirates():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("ae")
    return render_template("region_news/united_arab_emirates_news.html", news=news)


# Route to France News
@app.route("/region/fr")
def get_news_france():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("fr")
    return render_template("region_news/france_news.html", news=news)


# Route to Germany News
@app.route("/region/de")
def get_news_germany():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("de")
    return render_template("region_news/germany_news.html", news=news)


# Route to Italy News
@app.route("/region/it")
def get_news_italy():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("it")
    return render_template("region_news/italy_news.html", news=news)


# Route to Sweden News
@app.route("/region/se")
def get_news_sweden():
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    news = get_news("se")
    return render_template("region_news/sweden_news.html", news=news)


@ app.route("/category/<country>/<cat>")
def get_news_category(country, cat):
    if "username" not in session:
        flash("Please Log In or Sign Up to register", "danger")
        return redirect("/login")

    cat_news = get_news_by_category(country, cat)
    return render_template("region_news/category.html", cat_news=cat_news)


# ERROR HANDLERS
############################
# 404 ROUTE
@app.errorhandler(404)
def error_404(error):

    return render_template("errors/404_error.html"), 404


@app.errorhandler(500)
def error_500(error):

    return render_template("errors/500_error.html"), 500
