from flask import Flask
import os
import threading
import uuid

volume = os.environ.get("VOLUME", "/data")
size = os.environ.get("SIZE", 10)
app = Flask(__name__)


@app.route("/")
def root():
    return "sprayfoam is filling " + volume + " with " + size + "MB files"


@app.route("/healthz")
def healthz():
    return "OK"


def generate_big_files(volume, size):
    while True:
        with open(f"{volume}/{uuid.uuid4()}.txt", "w") as f:
            f.write("0" * 1024 * 1024 * int(size))


if __name__ == "__main__":
    thread = threading.Thread(
        target=generate_big_files,
        args=(
            volume,
            size,
        ),
    )
    thread.start()
    app.run(host="0.0.0.0", port=5000)
