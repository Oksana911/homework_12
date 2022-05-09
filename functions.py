import json
import logging
from json import JSONDecodeError


def load_json_data(path):
    try:
        with open(path, "r", encoding="UTF-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.info("Файл не найден")
        print("Файл не найден")
    except JSONDecodeError:
        logging.info("Файл не удается преобразовать")
        print("Файл не удается преобразовать")


def search_post_by_substring(posts, substring):
    posts = load_json_data("posts.json")

    found_posts = []
    for post in posts:
        if substring.lower() in post["content"].lower():
            found_posts.append(post)

    return found_posts



def is_filename_allowed(filename):
    ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False
