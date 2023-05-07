from clinica import *
# PACIENTES(id, nome, endereço, telefone)
# MÉDICOS(id, nome, especialidade_id)
# ESPECIALIDADES(id, descrição)
# CONSULTAS(id, paciente_id, medico_id, data)
# lista_especialidades = [
#     {'descricao':'Otorrino'},
#     {'descricao': 'Ortopedista'},
#     {'descricao': 'Oftamologista'}
#
# ]
# Especialidade.insert_many(lista_especialidades).execute()

#
#
descricao = Especialidade.select().where(Especialidade.id == 2)


for row in descricao:
    print(f'{row.id}-{row.descricao}')

