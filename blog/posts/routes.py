from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from blog import db
from blog.models import Post
from blog.posts.forms import PostForm
from datetime import datetime

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, media=form.media.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Пост создан!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Новый пост', form=form, legend = 'Новый пост')

@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        post.media = form.media.data
        post.date_posted = datetime.today()
        db.session.commit()
        flash('Контент обновлен!','success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method =='GET':
        form.title.data = post.title
        form.content.data = post.content
        form.media.data = post.media
    return render_template('create_post.html', title='Update Post', form=form, legend='Обновить пост')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Контент удален!','success')
    return redirect(url_for('main.home'))