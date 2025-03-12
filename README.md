# Integração de Aplicativo de Corrida

Este projeto simula a integração de um aplicativo de corrida, cobrindo desde a solicitação até o pagamento e notificação do usuário.

### Estrutura do Projeto
```plaintext
ride_app_integration/

│-- src/
│   │-- main.py  # Código principal
│   │-- utils.py  # Funções auxiliares
│-- tests/
│   │-- test_main.py  # Testes de integração
│-- README.md  # Documentação do projeto
```

### Componentes do Sistema
- **Usuário (Passageiro e Motorista)**: Interface do usuário (App móvel).
- **Serviço de Corrida**: Backend que gerencia solicitações e confirmações.
- **Sistema de Pagamento**: Processamento financeiro.
- **Sistema de Notificações**: Envio de mensagens para usuários.
- **Serviço de Geolocalização**: Rota e cálculo de tempo estimado.

### Tecnologias Utilizadas
- Python
- Simulação de API e Notificações

### Como Executar
1. Clone o repositório
2. Acesse o diretório `src/`
3. Execute `python main.py`

O terminal deve retornar:

```
Carlos solicitou uma corrida de Rua A para Aeroporto.
Nenhum motorista disponível no momento.
Notificação enviada: Não foi possível completar a corrida.
```

### Testes

Os testes foram implementados para validar o fluxo de solicitação de corrida no sistema. Durante a execução, o comportamento pode variar dependendo das condições no teste, isso simula um ambiente real, onde cada solicitação pode ter diferentes desfechos. Os cenários possíveis são:

1. Nenhum motorista disponível
- O sistema retorna uma mensagem informando que não há motoristas no momento.
- O teste verifica se a resposta do sistema está correta.

2. Motorista disponível e pagamento aprovado
- O sistema encontra um motorista, inicia a corrida e finaliza com sucesso.
- O pagamento é processado corretamente.

3. Motorista disponível, mas pagamento falha
- O sistema encontra um motorista e conclui a corrida, mas o pagamento falha.
- O teste deve garantir que o sistema trata a falha corretamente.

Para rodar os testes, execute no diretório raiz do projeto (dentro do PowerShell):

```bash
cmd /c "set PYTHONPATH=src && python -m unittest discover tests"
```

O terminal deve retornar algo como:

````
Carlos solicitou uma corrida de Rua A para Aeroporto.
Motorista Carlos encontrado!
Carlos aceitou a corrida de Carlos.
Corrida de Rua A para Aeroporto em andamento...
Corrida concluída! Carlos chegou ao destino com Carlos.
Processando pagamento para Carlos...
Pagamento aprovado!

````

### Fluxo Implementado
1. **Usuário solicita uma corrida**
2. **Sistema busca motorista**
3. **Motorista aceita corrida**
4. **Usuário faz pagamento**
5. **Notificação é enviada**

### Tratamento de Erros
- Corrida não inicia sem motorista disponível
- Pagamento pode falhar e exigir nova tentativa

### Desenvolvedores

Clara Mohammad, Gabrielly Vitor, Luigi Macedo, Kaleb Isaias
