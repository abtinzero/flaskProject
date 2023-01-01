from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


def get_meme():
    url = "https://meme-api.com/gimme/newiran/10"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["memes"][0]["preview"][-2]
    subreddit = response["memes"][0]["subreddit"]
    title = response["memes"][0]["title"]
    post_link = response["memes"][0]["postLink"]
    return meme_large, subreddit, post_link, title


@app.route("/")
def index():
    meme_pic, subreddit, post_link, title = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit, post_link=post_link, title=title)


if __name__ == '__main__':
    app.run()
