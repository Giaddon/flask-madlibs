from flask import Flask, render_template, request
from stories import story, story_two, story_three
app = Flask(__name__)

# 1) HTML form, where user can see the word types and write them in (verb, adjective, etc)
# 2) Submit form -> see HTML story.

@app.route("/")
def story_dropdown():

    return render_template("dropdown.html")

    
@app.route("/form")
def story_form():
    
    story_choice = request.args.get("dropdown-story")

    if story_choice == "one":
        the_story = story
    elif story_choice == "two":
        the_story = story_two
    elif story_choice == "three":
        the_story = story_three
    
    return render_template("form.html", words= the_story.prompts)

@app.route("/story")
def show_story():


    return render_template(
        "story.html", 
        storytext= the_story.generate(request.args)
    )

