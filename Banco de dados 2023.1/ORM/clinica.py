from peewee import *

db = PostgresqlDatabase('teste', port=5432, user='postgres', password='postgres')
# PACIENTES(id, nome, endereço, telefone)
# MÉDICOS(id, nome, especialidade_id)
# ESPECIALIDADES(id, descrição)
# CONSULTAS(id, paciente_id, medico_id, data)
class BaseModel(Model):
    class Meta():
        database = db
class Paciente(BaseModel):
    id = AutoField()
    nome = TextField()
    endereco = TextField()
    telefone = TextField()

class Especialidade(BaseModel):
    id = AutoField()
    descricao = TextField()

class Medico(BaseModel):
    id = AutoField()
    nome = TextField()
    especialidade = ForeignKeyField(Especialidade, backref='medicos')

class Consulta(BaseModel):
    id = AutoField()
    paciente = ForeignKeyField(Paciente, backref='consultas')
    medico = ForeignKeyField(Medico, backref='consultas')
    data = DateTimeField()




lista_tabelas = [Paciente,Especialidade,Medico,Consulta]

db.connect()
db.create_tables(lista_tabelas)
db.close()