import pandas as pd
from models.viagem_model import inserir_viagem
from models.database import get_connection
from models.viagem_model import inserir_viagem, listar_viagens, atualizar_viagem, excluir_viagem

def salvar_viagem(dados):
    inserir_viagem(
        dados['data'],
        dados['origem'],
        dados['destino'],
        dados['frete'],
        dados['diesel'],
        dados['pedagio'],
        dados['manutencao'],
        dados['outros']
    )

def cadastrar_viagem(
    data,
    origem,
    destino,
    frete,
    diesel,
    pedagio,
    manutencao,
    outros,
    lucro
):
    inserir_viagem(
        data=data,
        origem=origem,
        destino=destino,
        frete=frete,
        diesel=diesel,
        pedagio=pedagio,
        manutencao=manutencao,
        outros=outros,
        lucro=lucro
    )

def editar_viagem(
    id,
    data,
    origem,
    destino,
    frete,
    diesel,
    pedagio,
    manutencao,
    outros,
    lucro
):
    atualizar_viagem(
        id, data, origem, destino, frete,
        diesel, pedagio, manutencao, outros, lucro
    )

def deletar_viagem(id):
    excluir_viagem(id)

def obter_dashboard():
    return listar_viagens()

def obter_dashboard():
    dados = listar_viagens()

    colunas = [
        "id", "data", "origem", "destino", "frete",
        "diesel", "pedagio", "manutencao", "outros", "lucro"
    ]

    return pd.DataFrame(dados, columns=colunas)

def obter_dashboard():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM viagens", conn)
    conn.close()
    return df
