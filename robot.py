#!/usr/bin/python3
# Curitiba 16/09/2024
# Editor Jeverson Dias da Silva

# Instruções

# Rodando co python3...(RODAR O COMANDOS A BAIXO CASO NÃO TENHA AS BIBLIOTECAS INSTALADAS)

# 1- Crie o ambiente virtual
# python3 -m venv myenv

# 2- Ative o ambiente virtual
# No Windows:
# myenv\Scripts\activate
# No macOS e Linux:
# source myenv/bin/activate

# 3- Instale as dependências
# pip install -r requirements.txt

import discord
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente a partir do arquivo .env
load_dotenv()

# Configurar intenções do bot
intents = discord.Intents.default()
intents.members = True

# Instanciar o cliente do bot
client = discord.Client(intents=intents)

# Função para enviar mensagem privada com opções de escolha
async def enviar_opcoes_escolha(member):
    options_message = (
        f"Olá {member.name},\n"
        "Por favor, escolha uma das opções abaixo:\n"
        "1️⃣ **Geral**\n"
        "2️⃣ **Valor**\n"
        "3️⃣ **Prazo**\n"
        "4️⃣ **Duração**\n"
        "5️⃣ **Conteto WhatsApp (Dúvidas e envio de comprovante para liberação de acesso)\\n**"
    )
    await member.send(options_message)

# Função para enviar mensagens personalizadas de acordo com a escolha
async def enviar_mensagem_personalizada(member, escolha):
    mensagens = {
        "1": f"🌟 Olá {member.mention} ! 🌟\nSeja bem-vindo(a) ao nosso servidor!\nEsperamos que você se sinta em casa aqui.\n Por favor, sinta-se à vontade para explorar os canais e participar das conversas. \n**Se precisar de ajuda, estamos à disposição!\n**Caso queira baixar alguma das imagens exclusivas **@JCGAMESCLASSICOS** preciso comentar que ...\nEste é um serviço liberado para apoiadores;\n**Saber o valor  (Tecle 2)**\n**Saber duração  (Tecle 3)**\n**Saber o que posso baixar  (Tecle 4)**\n**Para se tornar um apoiador (WhatsApp) ?  (Tecle 5)**\n\n",
        "2": "Pedimos a colaboração de R$30,00 **Para ajudar a manter o servidor**\n Como colaborar ? PIX **R$30,00**para **(41) 998205080**...\n🔗**Sala de dowwnloads será liberada imadiatamente...**\n\n",
        "3": "**O acesso será liberado por 30 dias .\nTODA E QUALQUER IMAGEM QUE FOR POSTADA NESTE INTERVALO VAI PODER DESFRUTAR.**",
        "4": "**Poderá baixar toda e qualquer imagem que estiver na sala de Downloads...(PELO PRAZO DE 30 DIAS)**",
        "5": "https://wa.me/5541998205080",
    }
    mensagem = mensagens.get(escolha, "Opção inválida")
    await member.send(mensagem)

@client.event
async def on_ready():
    print(f'Bot está online como {client.user}')

@client.event
async def on_member_join(member):
    try:
        # Mensagem de boas-vindas para o canal de boas-vindas
        welcome_message_channel = (
            f"🌟 Olá {member.mention}! 🌟\n"
            "Seja bem-vindo(a) ao nosso servidor!\n "
            "Esperamos que você se sinta em casa aqui.\n"
            " Por favor, sinta-se à vontade para explorar os canais e participar das conversas.\n"
            " **Se precisar de ajuda, estamos à disposição!**"
        )
        # Substitua 'ID_DO_CANAL_DE_BOAS_VINDAS' pelo ID do canal de boas-vindas no seu servidor Discord
        channel = client.get_channel(1158017965682335797)
        await channel.send(welcome_message_channel)
        print(f"Mensagem de boas-vindas enviada para {member.name}")



        welcome_message_private = (
            f"**🌟Vamos começar  {member.name}! Seja bem-vindo(a) à nossa comunidade! 🌟**\n\n"
            "**Para mais informações digite  * **"

        )

        await member.send(welcome_message_private)
        print(f"Mensagem de boas-vindas enviada para {member.name} em mensagem privada")
    except discord.errors.Forbidden:
        print(f"Não foi possível enviar mensagem de boas-vindas para {member.name}. O usuário pode ter bloqueado mensagens diretas ou o bot não tem permissão.")

@client.event
async def on_message(message):
    if message.content == "*":
        await enviar_opcoes_escolha(message.author)
    elif message.content in ["1", "2", "3", "4", "5"]:
        await enviar_mensagem_personalizada(message.author, message.content)

# Iniciar o bot usando o token do ambiente
client.run(os.getenv('TOKEN'))

