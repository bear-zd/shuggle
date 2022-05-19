import sqlalchemy
from flask import g, redirect, render_template, url_for, flash, current_app, request
from flask_login import login_required, current_user, login_user, logout_user

import os, uuid

from ..main import main, news

import markdown
from flask import g, redirect, render_template, request, url_for, Response, jsonify, make_response
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from . import competition
from ..models import db, Competition, Comment, User, Rank
from ..tools.other_tool import getnowtime, re_filename, HtmlToText, Base64_PNG, get_new, getTopNews
from ..message.views import new_message, sum_message
from .forms import CompetitionForm
from config import DATABASE, UPLOAD_FOLDER


@competition.route('/competition/', methods=['GET', 'POST'])
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
    competitions = Competition.query.order_by(Competition.competition_id.desc()).limit(
        current_app.art_n)  # 从数据库取出相应数量的帖子
    users = User.query.order_by(User.uid.desc()).all()  # 从数据库取出用户表（加载头像）
    if current_user.is_authenticated:
        sum_message(current_user.uid)

    return render_template('all_competitions.html', tip='主页', competitions=competitions, users=users, news=news,
                           flag=0)  # 向前台传递数据

@competition.route('/add_competition/', methods=['GET', 'POST'])
@login_required
def add_article():
    sum_message(current_user.uid)
    competitionForm = CompetitionForm()  # 构建帖子类型的表单样式
    if competitionForm.validate_on_submit():  # 获取前台提交的表单内容
        competition_url = competitionForm.competition_url.data
        competition_title = competitionForm.competition_title.data
        competition_summary = competitionForm.competition_summary.data
        competition_id = max(db.session.query(Competition.competition_id).all())[0] + 1
        dataset = competitionForm.dateset
        checker = competitionForm.checker
        gt = competitionForm.GroundTruth
        example = competitionForm.example
        save_path = os.path.abspath(os.path.join(os.getcwd(),"competition"))
        if not os.path.exists(os.path.join(save_path,'dataset', str(competition_id))):
            os.mkdir(os.path.join(save_path,'dataset', str(competition_id)))
        dataset.data.save(os.path.join(
            save_path, 'dataset', str(competition_id),dataset.data.filename
        ))
        if not os.path.exists(os.path.join(save_path,'checker', str(competition_id))):
            os.mkdir(os.path.join(save_path,'checker', str(competition_id)))
        checker.data.save(os.path.join(
            save_path, 'checker', str(competition_id),checker.data.filename
        ))
        if not os.path.exists(os.path.join(save_path,'ground_truth', str(competition_id))):
            os.mkdir(os.path.join(save_path,'ground_truth', str(competition_id)))
        gt.data.save(os.path.join(
            save_path, 'ground_truth', str(competition_id),gt.data.filename
        ))
        if not os.path.exists(os.path.join(save_path,'example', str(competition_id))):
            os.mkdir(os.path.join(save_path,'example', str(competition_id)))
        example.data.save(os.path.join(
            save_path, 'example', str(competition_id),example.data.filename
        ))
        competition = Competition(competition_id=competition_id,competition_title=competition_title,competition_summary=competition_summary,
                                  competition_date=getnowtime('-'),user_id=current_user.uid,dataset_url='competition/dataset/'+str(competition_id)+'/'+dataset.data.filename,
                                  checker_url='competition/checker/'+str(competition_id)+'/'+checker.data.filename,
                                  gt_url='competition/ground_truth/'+str(competition_id)+'/'+gt.data.filename,
                                  example_url='competition/example/'+str(competition_id)+'/'+example.data.filename,
                                  competition_read_cnt=0,competition_pl=0,competition_sc=0
                                  )
        db.session.add(competition)  # 将构造的对象存入数据库
        db.session.commit()
        thisarticles = Competition.query.filter_by(competition_id=competition.competition_id).first()
        competition_url = Base64_PNG(competition_url, competition.competition_id, type='article')
        thisarticles.competition_url = competition_url
        db.session.commit()
        return redirect(url_for('main.index'))  # 返回首页
    else:
        return render_template('baseform.html', form=competitionForm, flag='competition')  # 向前台传递构造的表单样式

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
    print(request.form, request.files)
    submission_file = request.files['file']
    suffix = secure_filename(submission_file.filename)[-4:]
    uuid_value = uuid.uuid1()
    save_name = os.path.join(UPLOAD_FOLDER[1:], uuid_value.hex)
    submission_file.save(save_name + suffix)
    checker = db.session.query(Competition.checker_url).filter_by(competition_id=output['competition_id']).first()
    with open(save_name + '.py', 'w+') as file:
        file.write(checker[0])  # 保存checker脚本
    gt_path = db.session.query(Competition.gt_url).filter_by(competition_id=output['competition_id']).first()[0]
    try:
        new_score = os.popen('python {} -sub {} -gt {}'.format(save_name + '.py', save_name + suffix, gt_path))
        new_score = new_score.read()  # 抓取修改数据库里的checker_url代码的输出（错误检测可以加到这里）
        os.remove(save_name + suffix)
        os.remove(save_name + '.py')
        old_score = db.session.query(Rank.score).filter_by(competition_id=output['competition_id'],
                                                           user_id=output['user_id']).first()
        if old_score is None:
            rank = Rank(user_id=output['user_id'], competition_id=output['competition_id'], score=new_score)
            db.session.add(rank)
        elif float(new_score) > old_score[0]:
            print(float(new_score), old_score[0])
            score_updated = Rank.query.filter_by(competition_id=output['competition_id'], user_id=output['user_id']).update(
                dict(score=new_score))
        db.session.commit()
        print('??')
        return make_response('successful', 302)
    except Exception:
         resp = make_response('failed', 404)
         return resp



# 目前没有写response，根据错误处理来搞


def get_index(score):
    ls = [1] * len(score)
    for i in range(1, len(score)):
        ls[i] = ls[i - 1] + 1 if score[i] != score[i - 1] else ls[i - 1]
    return ls


@competition.route('/get_competition/scoreboard/<competition_id>')
def score_board(competition_id):
    print("now:", competition_id)
    tot = Rank.query.filter_by(competition_id=competition_id).all()
    tot = list(sorted(tot, key=lambda x: x.score, reverse=True))
    competiton_name = Competition.query.filter_by(competition_id=competition_id).first().competition_title
    name_list = [User.query.filter_by(uid=i.user_id).first().account for i in tot]
    index_list = get_index(tot)
    print(name_list)
    print(index_list)
    return render_template('score_board.html', score=tot, competition_name=competiton_name, name=name_list,
                           num=len(tot), index_list=index_list)
