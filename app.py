from flask import Flask, render_template
import psutil
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)
def plot_resources():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    data = [cpu, memory]

    fig, ax = plt.subplots()
    ax.bar(["CPU", "RAM"], data)
    ax.set_ylim(0, 100)
    ax.set_yticks(range(0, 101, 10))

    for i in range(0, 101, 10):
        ax.axhline(i, color='gray', alpha=0.2)

    pngImage = io.BytesIO()
    plt.savefig(pngImage, format='png')
    pngImage.seek(0)
    plt.close()

    imageData = base64.b64encode(pngImage.getvalue()).decode('utf-8')

    return imageData
@app.route("/")
def index():
    imageData = plot_resources()
    return render_template("index.html", imageData=imageData)
@app.route("/refresh_data")
def refresh_data():
    imageData = plot_resources()
    return imageData

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(port=28777)
