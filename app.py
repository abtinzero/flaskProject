from flask import Flask, render_template

from meme_flask.meme_flask import get_meme

app = Flask(__name__)


@app.route('/')
def index():
    meme_pic, subreddit, post_link, title = get_meme()
    return render_template("meme_index.html", meme_pic=meme_pic, subreddit=subreddit, post_link=post_link, title=title)


if __name__ == '__main__':
    app.run()
