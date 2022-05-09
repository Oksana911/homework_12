from flask import Flask, request, render_template, send_from_directory
from main.views import main_blueprint
from loader.views import loader_blueprint

# POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"
# app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
# не смогла разобраться почему строка 7 всё роняет

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "main":
    app.run()
