from flask_wtf import FlaskForm, RecaptchaField
from flask_ckeditor import CKEditorField
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, DateField, FloatField, SubmitField, \
    IntegerField, RadioField, SelectField, FileField
from wtforms.validators import DataRequired, Length, email, NumberRange
from flask_wtf.file import FileRequired


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
    competition_id = StringField(label='',
                                 render_kw={"id": "competition_id", "class": "invisible", "type": "text",
                                            "readonly": "readonly"})
    user_id = StringField(label='',
                                 render_kw={"id": "user_id", "class": "invisible", "type": "text",
                                            "readonly": "readonly"})
    submit_file = FileField(validators=[FileRequired(u'文件未选择！')])


    submit = SubmitField('上传', render_kw={"class": "btn btn-success"})


class CommentForm(RenderForm):
    comment_text = StringField(label='标题', validators=[Length(min=3, max=15, message="必须介于3-15个字符")],
                               render_kw={"placeholder": "3-15个字符"})
    submit = SubmitField(label='发布', render_kw={"class": "btn btn-success"})
