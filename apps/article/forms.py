from flask_wtf import FlaskForm, RecaptchaField
from flask_ckeditor import CKEditorField
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, DateField, FloatField, SubmitField, \
    IntegerField, RadioField, SelectField
from wtforms.validators import DataRequired, Length, email, NumberRange


class RenderForm(FlaskForm):
    class Meta(FlaskForm.Meta):
        def render_field(self, field, render_kw):
            other_kw = getattr(field, 'render_kw', None)
            if other_kw is not None:
                class1 = other_kw.get('class', None)
                class2 = render_kw.get('class', None)
                if class1 and class2:
                    render_kw['class'] = class2 + ' ' + class1
                render_kw = dict(other_kw, **render_kw)
            return field.widget(field, **render_kw)


class ArticleForm(RenderForm):
    article_url = StringField(label='',
                              render_kw={"placeholder": "0-20个字符", "id": "tx_input_2", "class": "invisible", "type": "text",
                                         "readonly": "readonly"})
    article_title = StringField(label='标题', validators=[Length(min=3, max=15, message="必须介于3-15个字符")],
                                render_kw={"placeholder": "3-15个字符"})
    article_summary = TextAreaField(label='正文', validators=[Length(min=15, max=3000, message="必须介于15-3000个字符")],
                                    render_kw={"placeholder": "15-3000个字符", "id": "editor"})
    article_type = SelectField('板块', choices=[('讨论', '讨论'), ('竞赛', 'competition')],
                               validators=[DataRequired("板块必选！")])
    submit = SubmitField('发布', render_kw={"class": "btn btn-success"})


class CommentForm(RenderForm):
    comment_text = StringField(label='标题', validators=[Length(min=3, max=15, message="必须介于3-15个字符")],
                               render_kw={"placeholder": "3-15个字符"})
    submit = SubmitField(label='发布', render_kw={"class": "btn btn-success"})
