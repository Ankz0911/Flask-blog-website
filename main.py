from flask import Flask, render_template, request, redirect
import requests
import smtplib
import os

app = Flask(__name__)
n_point_api = "https://api.npoint.io/ab312a499fe456df41c6"
my_email = os.environ.get('MY_EMAIL')
my_password = os.environ.get('MY_PASSWORD')


def send_email(username, usermail, userphone, usermessage):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ankur.khurana.cool@gmail.com",
                            msg=f'Subject: Contact Information received \n\n '
                                f'Name : {username}\n Email : {usermail}\n Phone:{userphone}\n Message: {usermessage}')


@app.route('/')
def hello():
    return redirect('index.html')


@app.route('/index.html')
def home():
    responses = requests.get(n_point_api).json()
    return render_template("index.html", input_data=responses)


@app.route('/about.html')
def about_page():
    return render_template("about.html")


@app.route('/contact.html')
def contact_me():
    return render_template("contact.html", message_sent=True)


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


@app.route('/form-entry', methods=["POST"])
def receive_data():
    user_name = request.form["name"]
    user_email = request.form["email"]
    user_phone = request.form["phone"]
    user_message = request.form["message"]
    send_email(user_name, user_email, user_phone, user_message)
    return render_template("contact.html", message_sent=False)


if __name__ == "__main__":
    app.run(debug=True)
