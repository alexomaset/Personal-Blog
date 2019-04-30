from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, SelectField

class BlogForm(FlaskForm):

    title = StringField('Blog title')
    category_id = SelectField
    content = TextAreaField('Post Of The Blog')
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):

    title = StringField('Comment Title')
    comment = TextAreaField('Post Of The Comment')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.')
    submit = SubmitField('Submit')