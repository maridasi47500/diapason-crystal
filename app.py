from flask import Flask, render_template, request, session
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_language", methods=["GET","POST"])
def add_one_language():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into language (name,short_name) values (:name,:short_name)",hey)
        user = query_db('select * from language')

        return render_template("languageform.html", languages=user, one_user=one_user, the_title="add new language")


    user = query_db('select * from language')
    one_user = query_db("select * from language limit 1", one=True)
    return render_template("languageform.html", languages=user, one_user=one_user, the_title="add new language")

@app.route("/add_one_musicalinstrument", methods=["GET","POST"])
def add_one_musicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicalinstrument (name) values (:name)",hey)
        user = query_db('select * from musicalinstrument')

        return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")


    user = query_db('select * from musicalinstrument')
    one_user = query_db("select * from musicalinstrument limit 1", one=True)
    return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")

@app.route("/add_one_musicalinstrumentpart", methods=["GET","POST"])
def add_one_musicalinstrumentpart():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusicalinstrument= query_db("select * from musicalinstrument")

        tousleslanguage= query_db("select * from language")

        one_user = query_db("insert into musicalinstrumentpart (musicalinstrument_id,name,language_id) values (:musicalinstrument_id,:name,:language_id)",hey)
        user = query_db('select * from musicalinstrumentpart')

        return render_template("musicalinstrumentpartform.html", musicalinstrumentparts=user, one_user=one_user, the_title="add new musicalinstrumentpart", touslesmusicalinstrument=touslesmusicalinstrument, tousleslanguage=tousleslanguage)


    touslesmusicalinstrument= query_db("select * from musicalinstrument")

    tousleslanguage= query_db("select * from language")

    user = query_db('select * from musicalinstrumentpart')
    one_user = query_db("select * from musicalinstrumentpart limit 1", one=True)
    return render_template("musicalinstrumentpartform.html", musicalinstrumentparts=user, one_user=one_user, the_title="add new musicalinstrumentpart", touslesmusicalinstrument=touslesmusicalinstrument, tousleslanguage=tousleslanguage)

@app.route("/add_one_scoreparts", methods=["GET","POST"])
def add_one_scoreparts():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        tousleslanguage= query_db("select * from language")

        one_user = query_db("insert into scoreparts (name,language_id,musical_part) values (:name,:language_id,:musical_part)",hey)
        user = query_db('select * from scoreparts')

        return render_template("scorepartsform.html", scorepartss=user, one_user=one_user, the_title="add new scoreparts", tousleslanguage=tousleslanguage)


    tousleslanguage= query_db("select * from language")

    user = query_db('select * from scoreparts')
    one_user = query_db("select * from scoreparts limit 1", one=True)
    return render_template("scorepartsform.html", scorepartss=user, one_user=one_user, the_title="add new scoreparts", tousleslanguage=tousleslanguage)

@app.route("/add_one_translation_score_parts", methods=["GET","POST"])
def add_one_translation_score_parts():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesscoreparts= query_db("select * from scoreparts")

        tousleslanguage= query_db("select * from language")

        one_user = query_db("insert into translation_score_parts (scoreparts_id,language_id,content) values (:scoreparts_id,:language_id,:content)",hey)
        user = query_db('select * from translation_score_parts')

        return render_template("translation_score_partsform.html", translation_score_partss=user, one_user=one_user, the_title="add new translation_score_parts", touslesscoreparts=touslesscoreparts, tousleslanguage=tousleslanguage)


    touslesscoreparts= query_db("select * from scoreparts")

    tousleslanguage= query_db("select * from language")

    user = query_db('select * from translation_score_parts')
    one_user = query_db("select * from translation_score_parts limit 1", one=True)
    return render_template("translation_score_partsform.html", translation_score_partss=user, one_user=one_user, the_title="add new translation_score_parts", touslesscoreparts=touslesscoreparts, tousleslanguage=tousleslanguage)

@app.route("/add_one_translation_musicalinstrumentpart", methods=["GET","POST"])
def add_one_translation_musicalinstrumentpart():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusicalinstrumentpart= query_db("select * from musicalinstrumentpart")

        tousleslanguage= query_db("select * from language")

        one_user = query_db("insert into translation_musicalinstrumentpart (musicalinstrumentpart_id,language_id,content) values (:musicalinstrumentpart_id,:language_id,:content)",hey)
        user = query_db('select * from translation_musicalinstrumentpart')

        return render_template("translation_musicalinstrumentpartform.html", translation_musicalinstrumentparts=user, one_user=one_user, the_title="add new translation_musicalinstrumentpart", touslesmusicalinstrumentpart=touslesmusicalinstrumentpart, tousleslanguage=tousleslanguage)


    touslesmusicalinstrumentpart= query_db("select * from musicalinstrumentpart")

    tousleslanguage= query_db("select * from language")

    user = query_db('select * from translation_musicalinstrumentpart')
    one_user = query_db("select * from translation_musicalinstrumentpart limit 1", one=True)
    return render_template("translation_musicalinstrumentpartform.html", translation_musicalinstrumentparts=user, one_user=one_user, the_title="add new translation_musicalinstrumentpart", touslesmusicalinstrumentpart=touslesmusicalinstrumentpart, tousleslanguage=tousleslanguage)

