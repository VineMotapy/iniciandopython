# parte 3  Enviando o e-mail
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:  # Conecta no servidor SMTP do Gmail usando SSL
    server.login(remetente, senha_app)                  # Faz login com o e-mail e senha de app
    server.send_message(msg)                             # Envia a mensagem
    print("E-mail enviado com sucesso!")                # Mensagem de confirmação no console