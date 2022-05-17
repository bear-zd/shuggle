import sqlalchemy
from flask import g, redirect, render_template, url_for, flash, current_app, request
from flask_login import login_required, current_user, login_user, logout_user

import os, uuid

from ..main import main, news

import markdown
from flask import g, redirect, render_template, request, url_for, Response, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from . import competition
from ..models import db, Competition, Comment, User, Rank
from ..tools.other_tool import getnowtime, re_filename, HtmlToText, Base64_PNG, get_new, getTopNews
from ..message.views import new_message, sum_message

from config import DATABASE, UPLOAD_FOLDER

@competition.route('/', methods=['GET', 'POST'])
def show_competitions():
    all_cnt = Competition.query.count()  # 获取所有帖子数量
    if request.method == 'POST':
        id = request.form["DATA"]  # 获取前台传递的更多请求
        if id == 'more':  # 若请求为more则加载更多，否则为正常刷新
            try:
                if current_app.art_n <= all_cnt - 8:
                    current_app.art_n = current_app.art_n + 8  # 加载数量上增加8条
                else:
                    current_app.art_n = all_cnt
            except:
                current_app.art_n = 8
    else:  # 初始化current_app.art_n变量
        try:
            if current_app.art_n == 0:
                current_app.art_n = 8
        except:
            current_app.art_n = 8
    competitions = Competition.query.order_by(Competition.competition_id.desc()).limit(current_app.art_n)  # 从数据库取出相应数量的帖子
    users = User.query.order_by(User.uid.desc()).all()  # 从数据库取出用户表（加载头像）
    if current_user.is_authenticated:
        sum_message(current_user.uid)

    return render_template('all_competitions.html', tip='主页', competitions=competitions, users=users, news=news, flag=0)  # 向前台传递数据



@competition.route('/get_competition/<competition_id>', methods=['GET'])
@login_required
def get_competition(competition_id):

    if current_user.is_authenticated:
        sum_message(current_user.uid)

    competition = Competition().query.filter_by(competition_id=competition_id).first()  # 根据帖子id从数据库获取帖子实例
    competition.competition_read_cnt = competition.competition_read_cnt + 1  # 帖子阅读量+1
    db.session.add(competition)  # 阅读量更改写入数据库
    db.session.commit()

    account = User().query.filter_by(uid=competition.user_id).first().account
    uid = current_user.uid

    return render_template('competition.html', competition=competition, account=account, uid=uid)  # 后续可能需要填排名


@competition.route('/competition_uploader/', methods=['POST'])
def upload_score():
    output = request.form
    submission_file = request.files['file']
    suffix = secure_filename(submission_file.filename)[-4:]
    uuid_value = uuid.uuid1()
    save_name = os.path.join(UPLOAD_FOLDER[1:],uuid_value.hex)
    submission_file.save(save_name+suffix)
    checker = db.session.query(Competition.checker_url).filter_by(competition_id=output['competition_id']).first()


def get_index(score):
    ls = [1]*len(score)
    for i in range(1,len(score)):
        ls[i] = ls[i-1]+1 if score[i]!=score[i-1] else ls[i-1]
    return ls


@competition.route('/get_competition/scoreboard/<competition_id>')
def score_board(competition_id):
    print("now:",competition_id)
    tot = Rank.query.filter_by(competition_id=competition_id).all()
    tot = list(sorted(tot,key=lambda x : x.score,reverse=True))
    competiton_name = Competition.query.filter_by(competition_id=competition_id).first().competition_title
    name_list = [User.query.filter_by(uid=i.user_id).first().account for i in tot]
    index_list = get_index(tot)
    print(name_list)
    print(index_list)
    return render_template('score_board.html',score=tot,competition_name=competiton_name,name=name_list,num=len(tot),index_list=index_list)