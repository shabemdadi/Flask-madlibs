from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    response = request.args.get("game")
    if response == 'no':
        return render_template("goodbye.html")
    if response == 'yes':
        return render_template("game.html")    

@app.route("/madlib")
def show_madlib():
    person = request.args.get("name")
    color  = request.args.get("color")
    adjective = request.args.get("adjective")
    noun = request.args.get("noun")
    verbs = request.args.getlist('verb[]')

    list_of_verbs=[]
    for verb in verbs:
        list_of_verbs.append(verb)

    print list_of_verbs

    verb = choice(list_of_verbs)

    list_of_templates = ["madlibs.html","madlibs_2.html","madlibs_3.html"]

    template = choice(list_of_templates)


    return render_template(template,person=person,color=color,
        noun=noun,adjective=adjective, verb=verb)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
