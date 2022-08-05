from utils import limpar_tela, obtem_opcao_menu, validar_email, gerador_id
from service import salvar_dados


def salva_cliente(db=[], nome='', email='', exibir_titulo=True):
    if exibir_titulo:
        limpar_tela()
        print(f"{'_'*10}| CADASTRO DE CLIENTE |{'_'*10}\n")
    try:
        if nome.strip() == "":
            nome = input("Digite o nome:")
            if nome.strip() == "":
                raise TypeError("Digite o nome correto.")

        email = input("Digite o e-mail:")
        if email.strip() == "":
            raise TypeError("Email inválido.")
        if validar_email(email) == False:
            raise TypeError("Email inválido.")
        novo_cliente = {
            "id": gerador_id(db),
            "nome": nome,
            "email": email
        }
        db.append(novo_cliente)
        salvar_dados("db_clientes.json", db)
        return novo_cliente
    except Exception as e:
        print(f"Alerta: {e}")
        return salva_cliente(db, nome, email, exibir_titulo=False)


def lista_cliente(db_clientes=[]):
    limpar_tela()
    print(f"{'_'*10}| Lista de Cliente|{'_'*10}\n")
    for cliente in db_clientes:
        print(
            f"Código: {cliente['id']} | Nome: {cliente['nome']} | Email: {cliente['email']}")
    print('\n')


def exec(db=[]):
    limpar_tela()
    while True:
        print(f"{'_'*10}| Cadastro de Produto |{'_'*10}")
        print("1 - Novo Cliente")
        print("2 - Lista de Cliente")
        print("0 - Voltar")
        opcao_selecionada = obtem_opcao_menu(1, 2)

        if opcao_selecionada == 0:
            limpar_tela()
            break
        elif opcao_selecionada == 1:
            limpar_tela()
            salva_cliente(db)
        elif opcao_selecionada == 2:
            limpar_tela()
            lista_cliente(db)


if __name__ == "__main__":
    exec()
