import html
from django.shortcuts import render
# imports a function called render, from shortcut module that renders a page
from . import util
#Means that you import the module from the same file directory
import markdown
# installed through pip, converts markdown files to html
import random
# this module will help us randomly choose between entries


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def convert_to_html(title):
    entry = util.get_entry(title)
    html = markdown.markdown(entry) if entry else None
    return html




