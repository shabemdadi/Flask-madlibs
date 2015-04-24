from random import choice, sample

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

    compliments = sample(AWESOMENESS,3)

    return render_template("compliment.html", person=player, compliment=compliments)

@app.route('/game')
def show_game_form():
    response = request.args.get("game")
    if response == 'no':
        return render_template("goodbye.html")
    if response == 'yes':
        return render_template("game.html")    

@app.route("/madlib", methods=["POST","GET"])
def show_madlib():
    
    if request.method == "POST":

        person = request.form.get("name")
        color  = request.form.get("color")
        adjective = request.form.get("adjective")
        noun = request.form.get("noun")
        verb = request.form.get('verb')

    else:

        person = request.args.get("name")
        color  = request.args.get("color")
        adjective = request.args.get("adjective")
        noun = request.args.get("noun")
        verb = request.args.get('verb')
        # print verbs
        # list_of_verbs=[]
        # for verb in verbs:
        #     list_of_verbs.append(verb)
        # print list_of_verbs
        # verb = choice(verbs)

    list_of_templates = ["madlibs.html","madlibs_2.html","madlibs_3.html"]

    template = choice(list_of_templates)


    return render_template(template,person=person,color=color,
        noun=noun,adjective=adjective, verb=verb)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
