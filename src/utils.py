import time
import random

def processar_pagamento(usuario):
    print(f"Processando pagamento para {usuario}...")
    time.sleep(2)
    sucesso = random.choice([True, False])
    
    if sucesso:
        print("Pagamento aprovado!")
        return True
    else:
        print("Pagamento falhou! Tente novamente.")
        return False

def enviar_notificacao(mensagem):
    print(f"Notificação enviada: {mensagem}")