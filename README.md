# Integração de Aplicativo de Corrida

### Descrição
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


### Testes
Para rodar os testes, execute no diretório raiz do projeto:
```bash
python -m unittest discover tests
```

### Fluxo Implementado
1. **Usuário solicita uma corrida**
2. **Sistema busca motorista**
3. **Motorista aceita corrida**
4. **Usuário faz pagamento**
5. **Notificação é enviada**

### Tratamento de Erros
- Corrida não inicia sem motorista disponível
- Pagamento pode falhar e exigir nova tentativa
```
