from models.database import get_connection

def calcular_lucro(frete, diesel, pedagio, manutencao, outros):
    return frete - (diesel + pedagio + manutencao + outros)

def inserir_viagem(data, origem, destino, frete, diesel, pedagio, manutencao, outros, lucro):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO viagens
    (data, origem, destino, frete, diesel, pedagio, manutencao, outros, lucro)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (data, origem, destino, frete, diesel, pedagio, manutencao, outros, lucro))

    conn.commit()
    conn.close()

def listar_viagens():
    conn = get_connection()
    df = conn.execute("SELECT * FROM viagens").fetchall()
    conn.close()
    return df

def atualizar_viagem(
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
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE viagens SET
            data = ?,
            origem = ?,
            destino = ?,
            frete = ?,
            diesel = ?,
            pedagio = ?,
            manutencao = ?,
            outros = ?,
            lucro = ?
        WHERE id = ?
    """, (
        data, origem, destino, frete,
        diesel, pedagio, manutencao, outros,
        lucro, id
    ))

    conn.commit()
    conn.close()


def excluir_viagem(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM viagens WHERE id = ?", (id,))
    conn.commit()
    conn.close()