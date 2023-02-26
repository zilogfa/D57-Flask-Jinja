# Dev: ali Jafarbeglou | Projects: Blog
# Languages: Python, HTML5, CSS3 | Technologies: Flask, Jinja, Requests, Datetime, OOP


from flask import Flask, render_template
from post import Post
import requests
import datetime

posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)
year = datetime.datetime.now().year

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects, year=year)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post, year=year)


if __name__ == "__main__":
    app.run(debug=True)


