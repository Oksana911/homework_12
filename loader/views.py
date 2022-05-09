import json
from flask import Blueprint, render_template, request
import logging
from functions import load_json_data, is_filename_allowed

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")
logging.basicConfig(filename="logger.log", level=logging.INFO)


@loader_blueprint.route("/post", methods=["GET", "POST"])
def add_post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/upload", methods=["POST"])
def add_post_by_user():
    picture = request.files.get("picture")
    content = request.form.get("content")
    filename = picture.filename
    picture_path = f'uploads/images/{filename}'

    if not picture or not content:
        logging.INFO("Пользователь не загрузил картинку или текст")
        return "Ошибка загрузки, требуется картинка и текст"

    if is_filename_allowed(filename):
        picture.save(picture_path)
        logging.info(f"Файл {filename} сохранен")
    else:
        extension = filename.split(".")[-1]
        logging.info(f"Тип файлов {extension} не поддерживается")

    posts = load_json_data("posts.json")
    new_post = {"pic": picture_path, "content": content}
    posts.append(new_post)

    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)

    return render_template("post_uploaded.html", new_post=new_post)
