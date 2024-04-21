from flask import Blueprint, request, redirect, render_template
from models.db import db, BlogPost
from forms.form import NewPost
import datetime


main = Blueprint("main", __name__)

@main.route('/')
def home():
    posts = db.session.execute(db.select(BlogPost)).scalars().all()
    return render_template("index.html", all_posts=posts)

# TODO: Add a route so that you can click on individual posts.
@main.route('/post/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@main.route('/new-post', methods=['GET', 'POST'])
def make_post():
    blog_form = NewPost()
    
    now = datetime.datetime.now()
    x = datetime.datetime(now.year, now.month, now.day)
    month = x.strftime("%B")
    if request.method == "POST":
        new_data = BlogPost(
            title = request.form.get('title'),
            subtitle = request.form.get("subtitle"),
            date = f"{month} {now.day}, {now.year}",
            body = request.form.get('body'), 
            author = request.form.get('name'),
            img_url = request.form.get('img_url')
        )
        db.session.add(new_data)
        db.session.commit()
        return redirect('/')
    return render_template("make-post.html", forms=blog_form)
# TODO: edit_post() to change an existing blog post
@main.route('/edit-post/<int:id>', methods=["POST", "GET"])
def edit_post(id):
    data = db.get_or_404(BlogPost, id)
    blog_form = NewPost(
        title  = data.title,
        subtitle = data.subtitle,
        name = data.author,
        img_url =  data.img_url,
        body = data.body
    )
    if request.method == "POST":
        data.title = request.form.get('title')
        data.subtitle = request.form.get('subtitle')
        data.author = request.form.get('name')
        data.img_url = request.form.get('img_url')
        data.body = request.form.get('body')
        db.session.commit()
        return redirect(f'/post/{id}')
    
    
    return render_template("make-post.html", forms=blog_form, is_edit=True)

# TODO: delete_post() to remove a blog post from the database
@main.route("/delete-post/<int:id>")
def delete_post(id):
    data = db.get_or_404(BlogPost, id)
    db.session.delete(data)
    db.session.commit()
    return redirect('/')
# Below is the code from previous lessons. No changes needed.
@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/contact")
def contact():
    return render_template("contact.html")
