import hashlib
from models.user_model import criar_usuario, buscar_usuario


def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def registrar(username, senha):
    if buscar_usuario(username):
        return False  # usuário já existe

    senha_hash = hash_senha(senha)
    criar_usuario(username, senha_hash)
    return True


def autenticar(username, senha):
    user = buscar_usuario(username)

    if not user:
        return False

    senha_hash = hash_senha(senha)
    return user[2] == senha_hash
