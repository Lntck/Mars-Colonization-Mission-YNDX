from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    job = TextAreaField("Job Title", validators=[DataRequired()])
    team_leader = IntegerField('Team Leader id', validators=[DataRequired()])
    work_size = IntegerField('Work Size', validators=[DataRequired()])
    collaborators = TextAreaField("Collaborators")
    is_finished = BooleanField('is job finished?')
    submit = SubmitField('Submit')
