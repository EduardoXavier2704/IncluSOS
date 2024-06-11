def insert(mydb, tipo_ocorrencia, Nome, Cpf, Data_nasc, Email_ou_telefone, Endereco, Lugar_referencia, Descricao):
    mycursor = mydb.cursor()

    sql = "INSERT INTO ocorrencia (tipo_ocorrencia, Nome, Cpf, Data_nasc, Email_ou_telefone, Endereco, Lugar_referencia, Descricao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (tipo_ocorrencia, Nome, Cpf, Data_nasc, Email_ou_telefone, Endereco, Lugar_referencia, Descricao)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()

def insert_proximo(mydb, Tipo_ocorrencia_proximo, Nome_completo_proximo, Cpf_proximo, Data_nasc_proximo, Email_ou_telefone_proximo, Endereco_proximo, Local_referencia, Descricao):
    mycursor = mydb.cursor()

    sql = "INSERT INTO ocorrencia_proximo (Tipo_ocorrencia_proximo, Nome_completo_proximo, Cpf_proximo, Data_nasc_proximo, Email_ou_telefone_proximo, Endereco_proximo, Local_referencia, Descricao) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (Tipo_ocorrencia_proximo, Nome_completo_proximo, Cpf_proximo, Data_nasc_proximo, Email_ou_telefone_proximo, Endereco_proximo, Local_referencia, Descricao)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "Inserido com Sucesso.")

    mycursor.close()

def update(mydb, titulo_antigo, titulo_novo, autor, ano, status_):
    mycursor = mydb.cursor()

    sql = "UPDATE livros SET titulo = %s, autor = %s, ano = %s, status_ = %s WHERE titulo = %s"
    val = (titulo_novo, autor, ano, status_, titulo_antigo)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "registro(s) atualizado(s).")

    mycursor.close()


def delete(mydb, titulo):
    mycursor = mydb.cursor()

    sql = "DELETE FROM livros WHERE titulo = %s"
    val = (titulo,)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "registro(s) excluído(s).")

    mycursor.close()

def query(mydb):
    mycursor = mydb.cursor()

    sql = "SELECT tipo_ocorrencia, Nome, Cpf, Data_nasc, Email_ou_telefone, Endereco, Lugar_referencia, Descricao FROM ocorrencia"
    mycursor.execute(sql)

    rows = mycursor.fetchall()

    # Cria uma lista vazia para armazenar os dados formatados
    dados_formatados = []

    # Itera sobre cada linha retornada pela consulta e adiciona os dados formatados à lista
    for row in rows:
        # Formata os dados adequadamente
        tipo_ocorrencia = row[0] if row[0] else ""
        nome = row[1] if row[1] else ""
        cpf = row[2] if row[2] else ""
        data_nasc = row[3] if row[3] else ""
        email_ou_telefone = row[4] if row[4] else ""
        endereco = row[5] if row[5] else ""
        lugar_referencia = row[6] if row[6] else ""
        descricao = row[7] if row[7] else ""

        # Adiciona os dados formatados à lista
        dados_formatados.append("Tipo de Ocorrência: {}\nNome: {}\nCPF: {}\nData de Nascimento: {}\nEmail ou Telefone: {}\nEndereço: {}\nLugar de Referência: {}\nDescrição: {}".format(
            tipo_ocorrencia, nome, cpf, data_nasc, email_ou_telefone, endereco, lugar_referencia, descricao))

    # Retorna a lista de dados formatados
    return dados_formatados

def lista(mydb):
    mycursor = mydb.cursor()

    sql = "SELECT Tipo_ocorrencia_proximo, Nome_completo_proximo, Cpf_proximo, Data_nasc_proximo, Email_ou_telefone_proximo, Endereco_proximo, Local_referencia, Descricao FROM ocorrencia_proximo"
    mycursor.execute(sql)

    rows = mycursor.fetchall()

    # Cria uma lista vazia para armazenar os dados formatados
    dados_formatados = []

    # Itera sobre cada linha retornada pela consulta e adiciona os dados formatados à lista
    for row in rows:
        # Formata os dados adequadamente
        Tipo_ocorrencia_proximo = row[0] if row[0] else ""
        Nome_completo_proximo = row[1] if row[1] else ""
        Cpf_proximo = row[2] if row[2] else ""
        Data_nasc_proximo = row[3] if row[3] else ""
        Email_ou_telefone_proximo = row[4] if row[4] else ""
        Endereco_proximo = row[5] if row[5] else ""
        Local_referencia = row[6] if row[6] else ""
        Descricao = row[7] if row[7] else ""

        # Adiciona os dados formatados à lista
        dados_formatados.append("Nome: {}\nCPF: {}\nData de Nascimento: {}\nEmail ou Telefone: {}\nEndereço: {}\nLugar de Referência: {}\nDescrição: {}".format(
            Nome_completo_proximo, Cpf_proximo, Data_nasc_proximo, Email_ou_telefone_proximo, Endereco_proximo, Local_referencia, Descricao))

    # Retorna a lista de dados formatados
    return dados_formatados


def register(mydb, nome, email, celular, senha):
    mycursor = mydb.cursor()

    sql = "INSERT INTO registro_usuario (nome, email, celular, senha) VALUES (%s, %s, %s, %s)"
    val = (nome, email, celular, senha)

    mycursor.execute(sql, val)

    mydb.commit()

    print("Usuário registrado com sucesso.")

    mycursor.close()


def login(mydb, nome, senha):
    mycursor = mydb.cursor()

    sql = "SELECT * FROM registro_usuario WHERE nome = %s AND senha = %s"
    val = (nome, senha)

    mycursor.execute(sql, val)

    user = mycursor.fetchone()

    if user:
        print("Login bem-sucedido.")
        return user
    else:
        print("Credenciais inválidas.")
        return None


