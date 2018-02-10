from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SubmitField,BooleanField,RadioField,SelectField,FileField,PasswordField,SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')



class PitchForm(FlaskForm):
    title = StringField('Pitch Title',validators=[Required()])
    body =TextAreaField('Pitch Content',validators=[Required()])
    submit = SubmitField('Submit') 

class CommentsForm(FlaskForm):
    comment = TextAreaField('Comment', validators=[Required()])
    submit = SubmitField('SUBMIT') 



class CategoryForm(FlaskForm):
    '''
    Class to create a wtf form for creating a pitch
    '''
    name =  StringField('Category Name', validators=[Required()])
    description = TextAreaField('Pitch Content',validators=[Required()])
    submit = SubmitField('Create')