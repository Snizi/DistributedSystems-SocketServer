# Project README

## WebSocket Chat Server

### Visão Geral

Este projeto é um servidor de chat baseado em WebSocket que permite aos clientes entrarem em salas de chat, enviarem mensagens e saírem das salas. O servidor é capaz de gerenciar vários clientes simultaneamente, possibilitando comunicação em tempo real dentro de diferentes salas de chat. O projeto é construído usando Python e utiliza threads para o gerenciamento concorrente de clientes. Ele também se integra a um banco de dados PostgreSQL para gerenciar usuários e mensagens.

### Recursos

- **Handshake WebSocket**: Gerencia o handshake WebSocket para estabelecer uma conexão com os clientes.
- **Gerenciamento de Salas**: Permite que os usuários entrem e saiam de salas de chat e mantém o controle sobre quais clientes estão em quais salas.
- **Broadcast de Mensagens**: Transmite mensagens para todos os clientes em uma sala.
- **Integração com Banco de Dados**: Armazena dados de usuários e mensagens em um banco de dados PostgreSQL.
- **Gerenciamento de Clientes em Threads**: Gerencia múltiplas conexões de clientes simultaneamente usando threads.

### Estrutura do Projeto

- **main.py**: O script principal do servidor. Gerencia conexões de clientes, handshakes WebSocket, roteamento de mensagens e gerenciamento de salas.
- **message_handlers.py**: Contém funções que interagem com o banco de dados PostgreSQL para gerenciar usuários, salas e mensagens.

### Configuração e Instalação

#### Pré-requisitos

- Python 3.x
- PostgreSQL

#### Passos de Instalação

1. **Clone o repositório:**:

   ```bash
   git clone https://github.com/Snizi/DistributedSystems-SocketServer
   cd https://github.com/Snizi/DistributedSystems-SocketServer
   ```

2. **Instale as dependências**:
   Certifique-se de ter todos os pacotes Python necessários instalados:

   ```bash
   pip install -r requirements.txt
   ```

3. **Preencha as variáveis de ambiente**:

Baseado no .env example

4. **Run the server**:
   ```bash
   python main.py
   ```
   The server will start running on `ws://0.0.0.0:8080`.
