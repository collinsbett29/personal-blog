from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,ValidationError,BooleanField,TextAreaField,SelectField,RadioField
from wtforms.validators import Required

# post form
class PostForm(FlaskForm):
    content = TextAreaField('post')
    submit = SubmitField('Submit POst')

#Comment Form
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField()
    # vote=RadioField('default field arguments', choices=[('1', 'UpVote'), ('1', 'DownVote')])

# blogForm
class BlogForm(FlaskForm):
    name = TextAreaField('Blog')
    submit = SubmitField()

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')