from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField


class ReviewForm(FlaskForm):

    title = StringField('Write your comment here',validators=[Required()])
    review = TextAreaField('Blog review')
    submit = SubmitField('Submit')

class PostForm(FlaskForm):

    title = StringField('Blog title')
    category_id = SelectField
    content = TextAreaField('Post Of The Blog')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    title = StringField('Comment Title')
    comment = TextAreaField('Post Of The Comment')
    submit = SubmitField('Submit')

class DeleteBlog(FlaskForm):
    delete=SubmitField("Delete this Blog")    

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.')
    submit = SubmitField('Submit')