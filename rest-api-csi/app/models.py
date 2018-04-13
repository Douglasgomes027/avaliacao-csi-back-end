from app import db

class Cliente(db.Model):

    __tablename__ = 'Cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255),nullable=False)

    def __init__(self, nome):
        self.nome = nome

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cliente.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Cliente: {}>".format(self.nome)

class Venda(db.Model):

    __tablename__ = 'Venda'

    id = db.Column(db.Integer, primary_key=True)
    clienteId = db.Column(db.Integer, db.ForeignKey('Cliente.id'),
        nullable=False)
    data = db.Column(db.DateTime,nullable=False, default=db.func.current_timestamp())
    vendedor = db.Column(db.String(255),nullable=False)

    def __init__(self, vendedor):
        self.vendedor = vendedor

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Venda.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Venda: {}>".format(self.vendedor)

venda_detalhe = db.Table('VendaDetalhe',
    db.Column('vendaId', db.Integer, db.ForeignKey('Venda.id'), primary_key=True),
    db.Column('produtoId', db.Integer, db.ForeignKey('Produto.id'), primary_key=True),
    db.Column('quantidade', db.Integer,nullable=False)
)

class Produto(db.Model):

    __tablename__ = 'Produto'

    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255),nullable=False)
    preco = db.Column(db.DECIMAL(precision=8, scale=2, asdecimal=True),nullable=False)

    def __init__(self, descricao,preco):
        self.descricao = descricao
        self.preco = preco

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Produto.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Produto: {}>".format(self.nome)
