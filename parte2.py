
from email.mime.text import MIMEText  # import usado apenas aqui #

mensagem = MIMEText("Teste de envio pelo Python")  # corpo do e-mail
mensagem["Subject"] = "Teste"                     # assunto
mensagem["From"] = remetente                      # quem envia 
mensagem["To"] = destinatario                     # quem recebe

# PARTE 2: Montando a mensagem 
# Usando a classe MIMEText para criar uma mensagem de texto simples.
# Aqui defino o conteúdo, o assunto e os cabeçalhos básicos.

from email.mime.text import MIMEText  # import usado apenas aqui #

mensagem = MIMEText("Teste de envio pelo Python")  # corpo do e-mail
mensagem["Subject"] = "Teste"                     # assunto
mensagem["From"] = remetente                      # quem envia 
mensagem["To"] = destinatario                     # quem recebe