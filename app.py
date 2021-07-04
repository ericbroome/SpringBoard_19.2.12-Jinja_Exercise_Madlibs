from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories
from random import randint

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)
story_index = 0
story = None

@app.route("/")
def show_homepage():
    """Create and show the form for a random story"""
    global story, story_index
    story_index = randint(0, len(stories) - 1)
    story = stories[story_index]
    return render_template("questions.html", template=story.template, prompts=story.prompts)

@app.route("/story")
def show_story():
    """Show the story"""
    return render_template("story.html", text=stories[story_index].generate(request.args))
