from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileRequired,FileAllowed
from flask_ckeditor import CKEditorField
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, DateField, FloatField, SubmitField, \
    IntegerField, RadioField, SelectField, FileField
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


class CompetitionForm(RenderForm):
    competition_url = StringField(label='',
                              render_kw={"placeholder": "0-20个字符", "id": "tx_input_2", "class": "invisible", "type": "text",
                                         "readonly": "readonly"})
    competition_title = StringField(label='标题', validators=[Length(min=3, max=15, message="必须介于3-15个字符")],
                                render_kw={"placeholder": "3-15个字符"})
    competition_summary = TextAreaField(label='正文', validators=[Length(min=15, max=3000, message="必须介于15-3000个字符")],
                                    render_kw={"placeholder": "15-3000个字符", "id": "editor"})
    dateset = FileField(validators=[FileRequired(),
                                    FileAllowed(['zip', 'tar'], '.zip/.tar only')
                                    ])
    checker = FileField(validators=[FileRequired(),
                                    FileAllowed(['py'], '.py only')
                                    ])
    GroundTruth = FileField(validators=[FileRequired(),
                                    FileAllowed(['csv','xlsx'], '.csv/.xlsx only')
                                    ])
    example = FileField(validators=[FileRequired(),
                                        FileAllowed(['csv','xlsx'], '.csv/.xlsx only')
                                        ])
    submit = SubmitField('发布', render_kw={"class": "btn btn-success"})


class CommentForm(RenderForm):
    comment_text = StringField(label='标题', validators=[Length(min=3, max=15, message="必须介于3-15个字符")],
                               render_kw={"placeholder": "3-15个字符"})
    submit = SubmitField(label='发布', render_kw={"class": "btn btn-success"})
