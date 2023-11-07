from flask import Flask, render_template, request, redirect

from extractor import extract_video_data_from_url

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/terms-conditions')
def terms():
    return render_template('terms-conditions.html')

@app.route('/download', methods=["POST", "GET"])
def download():
    url = request.form["url"]
    print("Someone just tried to download", url)
    video_data = extract_video_data_from_url(url)
    title = video_data["title"]
    thumbnail = video_data["thumbnail"]
    formats = video_data["formats"]
    return render_template("download2.html",title=title,thumbnail=thumbnail,formats=formats)
                           

if __name__ == '__main__':
    app.run(port=5000, debug=True)
#title=title,thumbnail=thumbnail,formats=formats
