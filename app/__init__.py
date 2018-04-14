from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort,make_response
from sqlalchemy import create_engine
from functools import wraps
import jwt
import datetime
import os


#SECURITY
#app.config['SECRET_KEY'] = 'minhachavesecreta'

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.args.get("token")

        if not token:
            return jsonify({'message': 'Token is missing!'}),403

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid!'}),403

        return func(*args, **kwargs)
    return decorated

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

db_engine = create_engine(os.getenv('DATABASE_URL'))

def create_app(config_name):
    from app.models import Cliente
    from app.models import Venda
    from app.models import Produto

    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    
    @app.route('/clienteslista/', methods=['GET'])
    def clienteslista():
        # GET
        clientes = Cliente.get_all()
        results = []

        for cliente in clientes:
            obj = {
                'id': cliente.id,
                'nome': cliente.nome,
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/vendaslista/', methods=['GET'])
    def vendaslista():
        # GET
        vendas = Venda.get_all()
        results = []

        for venda in vendas:
            obj = {
                'id': venda.id,
                'clienteId': venda.clienteId,
                'data': venda.data,
                'vendedor': venda.vendedor
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/produtoslista/', methods=['GET'])
    def produtoslista():
        # GET
        produtos = Produto.get_all()
        results = []

        for produto in produtos:
            obj = {
                'id': produto.id,
                'descricao': produto.descricao,
                'preco': str(produto.preco),
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/clientes_mais_compraram_produto/', methods=['GET'])
    def clientes_mais_compraram_produto():
        # GET

        result = db_engine.execute('''
            SELECT c.nome,p.descricao,vd.quantidade
            FROM "Cliente" as  c INNER JOIN "Venda" as v ON c.id=v."clienteId"
            INNER JOIN "VendaDetalhe" as vd ON vd."vendaId"=v.id
            INNER JOIN "Produto" as p ON p.id=vd."produtoId"
            GROUP BY p.descricao,c.nome,vd.quantidade
            ORDER BY vd.quantidade DESC;
        ''')

        results = []

        for r in result:
            obj = {
                'nome': r.nome,
                'descricao': r.descricao,
                'quantidade': r.quantidade,
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/venda_vendedor_mes/', methods=['GET'])
    def venda_vendedor_mes():
        # GET

        result = db_engine.execute('''
            SELECT v.vendedor,to_char(v.data , 'MM') as "mes",(vd.quantidade * p.preco) as "total"
            FROM "Cliente" as  c
            INNER JOIN "Venda" as v ON c.id=v."clienteId"
            INNER JOIN "VendaDetalhe" as vd ON vd."vendaId"=v.id
            INNER JOIN "Produto" as p ON p.id=vd."produtoId"
            GROUP BY v.vendedor,"mes","total"
            ORDER BY "mes";
        ''')

        results = []

        for r in result:
            obj = {
                'vendedor': r.vendedor,
                'mes': r.mes,
                'total': str(r.total),
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response

    @app.route('/faturamento_mensal/', methods=['GET'])
    def faturamento_mensal():
        # GET

        result = db_engine.execute('''
            SELECT to_char(v.data , 'MM') as "mes",SUM(vd.quantidade * p.preco) as "total"
            FROM "Cliente" as  c
            INNER JOIN "Venda" as v ON c.id=v."clienteId"
            INNER JOIN "VendaDetalhe" as vd ON vd."vendaId"=v.id
            INNER JOIN "Produto" as p ON p.id=vd."produtoId"
            GROUP BY "mes"
            ORDER BY "mes";
        ''')

        results = []

        for r in result:
            obj = {
                'mes': r.mes,
                'total': str(r.total),
            }
            results.append(obj)
        response = jsonify(results)
        response.status_code = 200
        return response


    return app
