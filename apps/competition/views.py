from . import competition

@competition.route('/competition')
def get_competition():
    return "hello"