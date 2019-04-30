from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Review,User
from .forms import ReviewForm,UpdateProfile,BlogForm
from flask_login import login_required,current_user
from .. import db,photos
import markdown2  


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')


@main.route('/blog/review/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_review(id):
    form = ReviewForm()
    blog = get_blog(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data

        #Updated review instance
        new_review = Review(blog_id=blog_id,blog_title=blog_title,blog_review=review,user=current_user)

        #save review method
        new_review.save_review()
        return redirect(url_for('.blog',id = blog.id ))

    title = f'{blog.title} review'
    return render_template('new_review.html',title = title, review_form=form, blog=blog)    

@main.route('/blog/<int:id>')
def blog(id):

    '''
    View blog page function that returns the blog details page and its data
    '''
    blog = get_blog(id)
    title = f'{blog.title}'
    reviews = Review.get_reviews(blog.id)

    return render_template('blog.html',title = title,blog = blog,reviews = reviews) 

@main.route("/profile/<uname>")
def profile(uname):
    user=User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html",user=user)    

@main.route('/profile/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data
       
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/review/<int:id>')
def single_review(id):
    review=Review.query.get(id)
    if review is None:
        abort(404)
    format_review = markdown2.markdown(review.movie_review,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('review.html',review = review,format_review=format_review)    

@main.route('/blog/new', methods =['GET','POST'])
@login_required
def new_blog():

    form = BlogForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        author = form
        user = current_user
        blog = Blog(title = form.title.data, author = form.author.data, description = form.description.data)

        db.session.add(new_blog)
        db.session.commit()
        return redirect(url_for('main.blog'),blogs=blogs)
    return render_template('new_blog.html', form=form)