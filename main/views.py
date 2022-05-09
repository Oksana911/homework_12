import logging

from flask import Blueprint, render_template, request

from functions import load_json_data, search_post_by_substring


main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@main_blueprint.route("/")
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    s = request.args.get("s", "")
    logging.info("Открытие страницы поиска")
    posts = load_json_data("posts.json")
    result = search_post_by_substring(posts, s)

    return render_template("post_list.html", posts=result, s=s)
