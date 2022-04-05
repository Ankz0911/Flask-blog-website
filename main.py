from flask import Flask, render_template
import requests

app = Flask(__name__)
n_point_api = "https://api.npoint.io/ab312a499fe456df41c6"


@app.route('/index.html')
def home():
    responses = requests.get(n_point_api).json()
    return render_template("index.html", input_data = responses)


@app.route('/about.html')
def about_page():
    return render_template("about.html")


@app.route('/contact.html')
def contact_me():
    return render_template("contact.html")


@app.route("/blog/<int:blog_id>")
def blog_post(blog_id):
    responses = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
    for response in responses:
        if response["id"] == blog_id:
            post_title = response["title"]
            post_subtitle = response["subtitle"]
            post_body = response["body"]
        else:
            pass
    return render_template("post.html", post1_t=post_title, post1_st=post_subtitle, post1_b=post_body)


if __name__ == "__main__":
    app.run(debug=True)
