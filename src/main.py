import time
import random
from utils import enviar_notificacao, processar_pagamento
def solicitar_corrida(usuario, local_partida, destino):
    print(f"{usuario} solicitou uma corrida de {local_partida} para {destino}.")
    time.sleep(1)
    motorista = buscar_motorista()
    if motorista:
        return iniciar_corrida(usuario, motorista, local_partida, destino)
    else:
        print("Nenhum motorista disponível no momento.")
        return None
def buscar_motorista():
    motoristas_disponiveis = ["João", "Maria", "Carlos"]
    if random.choice([True, False]):
        motorista = random.choice(motoristas_disponiveis)
        print(f"Motorista {motorista} encontrado!")
        return motorista
    return None
def iniciar_corrida(usuario, motorista, local_partida, destino):
    print(f"{motorista} aceitou a corrida de {usuario}.")
    time.sleep(2)
    print(f"Corrida de {local_partida} para {destino} em andamento...")
    time.sleep(3)
    return finalizar_corrida(usuario, motorista)
def finalizar_corrida(usuario, motorista):
    print(f"Corrida concluída! {usuario} chegou ao destino com {motorista}.")
    return processar_pagamento(usuario)
if __name__ == "__main__":
    usuario = "Carlos"
    local_partida = "Rua A"
    destino = "Aeroporto"
    corrida = solicitar_corrida(usuario, local_partida, destino)
    if corrida:
        enviar_notificacao("Corrida finalizada com sucesso!")
    else:
        enviar_notificacao("Não foi possível completar a corrida.")