from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
    title = StringField('Заголовок', validators=[DataRequired()])
    media = StringField('Изображение', validators=[DataRequired()])
    content = TextAreaField('Контент', validators=[DataRequired()])
    submit = SubmitField('Обновить')
