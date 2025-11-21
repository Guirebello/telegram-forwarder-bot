# Telegram Forwarder

Bot para encaminhar automaticamente mensagens de canais do Telegram para um grupo específico.

## Descrição

Este projeto monitora canais públicos do Telegram e encaminha automaticamente todas as novas mensagens para um grupo de destino. Ideal para centralizar promoções, notícias ou atualizações de múltiplos canais em um único lugar.

## Requisitos

- Python 3.7 ou superior
- Conta no Telegram
- Credenciais da API do Telegram

## Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd telegram-forwarder
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Configuração

### 1. Obter API_ID e API_HASH

1. Acesse https://my.telegram.org/
2. Faça login com seu número de telefone
3. Clique em **"API development tools"**
4. Preencha o formulário:
   - **App title**: escolha um nome (ex: "Forwarder Bot")
   - **Short name**: escolha um nome curto (ex: "forwarder")
   - **URL** e **Platform**: são opcionais, pode deixar em branco ou preencher como preferir
5. Clique em "Create application"
6. Copie os valores de **api_id** e **api_hash**

⚠️ **Importante**: Se a página não carregar corretamente ou aparecer em branco, desative seu adblock/bloqueador de anúncios.

### 2. Obter TARGET_GROUP_ID

1. Adicione o bot [@getidsbot](https://t.me/getidsbot) ao grupo onde você quer receber as mensagens
2. O bot enviará uma mensagem com o ID do grupo
3. Copie o ID (será um número negativo, ex: `-1001234567890`)

### 3. Configurar CHANNEL_USERNAMES

Para encontrar o username de um canal:

1. Abra o canal no Telegram
2. Veja o link do canal (ex: `https://t.me/LinksBrazil`)
3. O username é a parte depois de `t.me/` (neste caso: `LinksBrazil`)

Para monitorar múltiplos canais, separe os usernames por vírgula (ex: `LinksBrazil,OutroCanal,MaisUm`).

### 4. Gerar SESSION_STRING (para produção)

Para rodar o bot em produção (servidores, VPS, etc), você precisa gerar uma session string:

1. Crie um arquivo `.env` com `API_ID` e `API_HASH` (veja exemplo abaixo)
2. Execute o script de geração:
```bash
python generate_session.py
```
3. Digite seu número de telefone no formato internacional com o símbolo `+`:
   - Exemplo: `+5511972922345` (Brasil)
   - Formato: `+<código_país><DDD><número>`
4. Digite o código de confirmação que você receberá no Telegram
5. Copie a **SESSION_STRING** que será exibida no terminal
6. Adicione essa string no arquivo `.env`

### 5. Criar arquivo .env

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```env
# Credenciais da API do Telegram (obtenha em https://my.telegram.org/)
API_ID=12345678
API_HASH=abc123def456ghi789jkl012mno345pq

# ID do grupo de destino (obtenha com @getidsbot)
TARGET_GROUP_ID=-1001234567890

# Canais para monitorar (separados por vírgula, sem espaços extras)
CHANNEL_USERNAMES=LinksBrazil,OutroCanal,MaisUm

# Session string para produção (obtenha executando generate_session.py)
# Deixe em branco para desenvolvimento local
SESSION_STRING=sua_session_string_aqui_se_for_usar_em_producao
```

## Como Usar

### Desenvolvimento (Local)

Para rodar localmente, você pode deixar `SESSION_STRING` vazio no `.env`. Na primeira execução, será solicitado login via telefone e será criado um arquivo `.session`:

```bash
python forwarder.py
```

### Produção (Servidor/VPS)

Para rodar em produção, configure a `SESSION_STRING` no `.env` conforme explicado acima:

```bash
python forwarder.py
```

O bot ficará rodando e monitorando os canais. Para parar, pressione `Ctrl+C`.

## Observações

### Diferença entre Desenvolvimento e Produção

- **Desenvolvimento (sem SESSION_STRING)**: 
  - Usa arquivo `.session` local para armazenar a sessão
  - Na primeira vez, pede login via telefone
  - Ideal para testar localmente

- **Produção (com SESSION_STRING)**:
  - Usa a session string no formato texto
  - Não precisa de arquivos `.session`
  - Ideal para servidores, containers Docker, etc.
  - Pode ser facilmente movido entre ambientes

### Permissões Necessárias

- Você deve estar inscrito nos canais que deseja monitorar
- Você deve ser membro (com permissão de enviar mensagens) do grupo de destino
- O bot não funciona com canais/grupos privados que você não tem acesso

## Troubleshooting

- **Erro "API_ID ou API_HASH não configurados"**: Verifique se o arquivo `.env` existe e está preenchido corretamente
- **Erro ao conectar**: Verifique sua conexão com a internet e se as credenciais estão corretas
- **Mensagens não são encaminhadas**: Certifique-se de que você está inscrito nos canais e tem permissão no grupo de destino
- **Página my.telegram.org em branco**: Desative seu adblock ou bloqueador de anúncios

## Licença

MIT

