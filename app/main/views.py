from flask import render_template,request,redirect,url_for,abort,jsonify, flash
from flask_login import current_user
from .. import db
from . import main
from .forms import BlogForm, CommentForm
from ..models import User, Blog, Comment
from flask_login import login_required


@main.route('/')
def index():

    return render_template("home.html")


@main.route('/contact')
def contact():

    return render_template("contact.html")


@main.route('/footer')
def footer():

    return render_template("footer.html")


@main.route('/blog/new', methods=['GET', 'POST'])
@login_required
def blogs():
    """
    View Blog function that returns the Blog page and data
    """
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        title_blog= blog_form.title_blog.data
        description = blog_form.description.data
        new_blog = Blog(title_blog=title_blog, description=description)
        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.theblog'))
    title = 'PrimeDale|Blog'
    return render_template('blogs.html', title=title, blog_form=blog_form)

@main.route('/blog/allblogs', methods=['GET', 'POST'])
@login_required
def theblog():
    blogs = Blog.query.all()
    return render_template('myblogs.html', blogs=blogs)



# @main.route('/Update/<int:id>', methods=['GET', 'POST'])
# @login_required
# def update_blog(id):
#     blog = Blog.query.get_or_404(id)
#     if blog.user != current_user:
#         abort(403)
#     form = BlogForm()
#     if form.validate_on_submit():
#         blog.title_blog = form.title_blog.data
#         blog.description = form.description.data
#         db.session.commit()

#         return redirect(url_for('main.theblog'))
#     elif request.method == 'GET':
#         form.title_blog.data = blog.title_blog
#         form.description.data = blog.description
#     return render_template('update_blog.html', form=form)


# @main.route('/view/<int:id>', methods=['GET', 'POST'])
# @login_required
# def view(id):
#     blog = Blog.query.get_or_404(id)
#     blog_comments = Comment.query.filter_by(blog_id=id).all()
#     comment_form = CommentForm()
#     if comment_form.validate_on_submit():
#         new_comment = Comment(blog_id=id, comment=comment_form.comment.data, user=current_user)
#         new_comment.save_comment()
#     return render_template('view.html', blog=blog, blog_comments=blog_comments, comment_form=comment_form)

# @main.route('/delete/<int:id>', methods=['GET', 'POST'])
# @login_required
# def delete(id):
#     blog = Blog.query.get_or_404(id)
#     if blog.user != current_user:
#         abort(403)
#     db.session.delete(blog)
#     db.session.commit()
 
#     return redirect(url_for('main.theblog'))



# @main.route('/delete_comment/<int:comment_id>', methods=['GET', 'POST'])
# @login_required
# def delete_comment(comment_id):
#     comment =Comment.query.get_or_404(comment_id)
#     if (comment.user.id) != current_user.id:
#         abort(403)
#     db.session.delete(comment)
#     db.session.commit()
#     flash('comment succesfully deleted')
#     return redirect (url_for('main.theblog'))
