from flask import Flask
from Config import app_config, app_active
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
import Forms
import LDB,gGraficos


config = app_config[app_active]


def create_app(config_name):
    app = Flask(__name__, template_folder='templates')

    app.secret_key = config.SECRET
    app.config.from_object(app_config[app_active])
    app.config.from_pyfile('Config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost:3306/csv'
    db = SQLAlchemy(app)
    db.__init__(app)

    @app.route('/')
    def index():
        return render_template('index.html')
    @app.route('/grafico', methods = ["POST","GET"])
    def grafico():
        info = Forms.info()
        if info.idade.data == None and  info.sexo.data == None:
            arq = 'Figura'
            return render_template('grafico.html',
                               info=info,
                               arq=arq)
        else:
            dados = LDB.leitura(info.idade.data, info.sexo.data)
            arq = gGraficos.criarimg(dados[0][0], dados[0][1], dados[1][0], dados[1][1], dados[2][0], dados[2][1],tipo=info.tipo.data)
            return render_template('grafico.html',
                                   info=info,
                                   arq=arq)

    return app