# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

# class TaskForm(FlaskForm):
#     description = StringField("Task Description", validators=[DataRequired()])
#     submit = SubmitField("Add Task")
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class CreatePlayerForm(FlaskForm):
    name = StringField('Player Name', validators=[DataRequired()])
    description = SelectField('description', validators=[DataRequired()],
        choices=[
            ('GoalKeeper', 'GoalKeeper'),
            ('Defense', 'Defence'),
            ('Midfielder', 'Midfielder'),
            ('forward', 'forward')
        ]
    )
    submit = SubmitField('Add Player')