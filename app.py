from flask import Flask, render_template, request
from stories import story
app = Flask(__name__)

# 1) HTML form, where user can see the word types and write them in (verb, adjective, etc)
# 2) Submit form -> see HTML story.

@app.route("/")
def story_form():

    return render_template("form.html", words=story.prompts)

@app.route("/story")
def show_story():

    return render_template(
        "story.html", 
        storytext=story.generate(request.args)
    )

