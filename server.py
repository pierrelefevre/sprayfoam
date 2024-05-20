from flask import Flask
import os
import threading
import uuid
import datetime
import subprocess

volume = os.environ.get("VOLUME", "/data")
size = os.environ.get("SIZE", 10)
app = Flask(__name__)
start_time = datetime.datetime.now().isoformat()


@app.route("/")
def root():
    return (
        "sprayfoam is filling "
        + volume
        + " with "
        + size
        + "MB files.<br/>Running since "
        + start_time
        + ".<br/><a href='/size'>Check size</a>"
    )


@app.route("/size")
def get_size():
    current_size = (
        subprocess.check_output(["du", "-sh", volume]).split()[0].decode("utf-8")
    )
    return "Volume size: " + current_size


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
