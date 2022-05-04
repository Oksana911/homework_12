from flask import Blueprint, render_template
import logging

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)

@loader_blueprint.route("/post")
def get_post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/search")
def search_page():
    return render_template("post_list.html")