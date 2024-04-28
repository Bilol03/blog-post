from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, URL
from wtforms import StringField, SubmitField, PasswordField, EmailField
from flask_ckeditor import CKEditorField


class NewPost(FlaskForm):
    title = StringField(label="Blog Post Title", validators=[DataRequired()])
    subtitle = StringField(label="Subtitle", validators=[DataRequired()])
    name = StringField(label="Your Name", validators=[DataRequired()])
    img_url = StringField(label="Blog Img Url", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    
    submit = SubmitField(label="Submit")
  
class NewUser(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    name = StringField(label='Name', validators=[DataRequired()])
    
    submit = SubmitField(label="Submit")
    

class ExistingUser(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    
    submit = SubmitField(label="Submit")
    
