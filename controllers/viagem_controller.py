import pandas as pd
from models.viagem_model import inserir_viagem
from models.database import get_connection

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

def obter_dashboard():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM viagens", conn)
    conn.close()
    return df
