
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from partition import get_newest_partition

get_newest_partition()

exit()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Sound Sharing HLS Server"


@app.route("/upload")
def upload_file_template():
    return render_template("upload.html")


@app.route("/uploader", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["file"]

        if (f.filename.rsplit('.', 1)[1].lower() == 'wav' or
            f.filename.rsplit('.', 1)[1].lower() == 'mp3' or
            f.filename.rsplit('.', 1)[1].lower() == 'mp4'):

            f.save(secure_filename(f.filename))

            return "file uploaded successfully"
        else:
            f.close()
            return "file extension not supported"


if __name__ == "__main__":
    app.run(port=5001, debug=True)