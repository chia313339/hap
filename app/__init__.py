from flask import Flask
from app.route import index, page_not_found, hadoop_hue, hadoop_jupyter, hadoop_hivetable


def create_app():
    app = Flask(__name__)
    app.add_url_rule('/', 'index', index, methods=['GET', 'POST'])
    app.add_url_rule('/index', 'index', index, methods=['GET', 'POST'])
    app.add_url_rule('/hadoop_hue', 'hadoop_hue', hadoop_hue, methods=['GET', 'POST'])
    app.add_url_rule('/hadoop_jupyter', 'hadoop_jupyter', hadoop_jupyter, methods=['GET', 'POST'])
    app.add_url_rule('/hadoop_hivetable', 'hadoop_hivetable', hadoop_hivetable, methods=['GET', 'POST'])
    app.register_error_handler(404, page_not_found)

    return app
