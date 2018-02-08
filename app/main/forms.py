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
    category =SelectField('lease pick from the following categories',choices=[('pick_up','Pick-up lines'),('interview','Interview Pitches'),
        ('bussines', 'bussiness pitches'),
        ('product', 'product pitch')],validators=[Required()])
    submit = SubmitField('Submit') 