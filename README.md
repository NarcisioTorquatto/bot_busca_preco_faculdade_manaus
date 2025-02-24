
# Web Automation with BotCity

Este projeto utiliza a biblioteca BotCity para automação de navegação web com o Selenium, em conjunto com o BotMaestro SDK. O objetivo é criar um bot que navega automaticamente até o site da BotCity e executa algumas ações, com captura de erros e gerenciamento de navegador.

## Requisitos

Antes de executar o projeto, é necessário instalar algumas dependências:

1. **Python 3.x**: O projeto foi desenvolvido utilizando Python 3. Certifique-se de ter o Python instalado.
2. **Bibliotecas**: Você precisará instalar as bibliotecas listadas no arquivo `requirements.txt`.

Para instalar as dependências, execute o seguinte comando:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` contém as seguintes bibliotecas:

- `botcity-web`
- `botcity-maestro`
- `webdriver-manager`
- `selenium`
- `time`

## Estrutura do Projeto

O projeto contém os seguintes arquivos principais:

- **main.py**: Script principal que inicializa o bot e realiza as ações de navegação.
- **erro.png**: Arquivo gerado quando ocorre um erro durante a execução do bot.

## Como Usar

### Passo 1: Clone o Repositório

Clone o repositório para a sua máquina local:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

### Passo 2: Instale as Dependências

Instale as dependências necessárias com o comando:

```bash
pip install -r requirements.txt
```

### Passo 3: Execute o Script

Execute o script `main.py` para iniciar a navegação automatizada:

```bash
python main.py
```

O bot irá:

- Inicializar a navegação.
- Abrir o site da BotCity (`https://www.botcity.dev`).
- Capturar quaisquer erros e salvar uma captura de tela chamada `erro.png` caso algo dê errado.
- Fechar o navegador após a execução.

## Funcionalidade do Código

### Classe `MyBotWeb`
A classe `MyBotWeb` contém os métodos principais do bot, incluindo:

- **`__init__(self, headless=True)`**: Inicializa o bot com as configurações de navegador (headless ou não).
- **`alerts(self)`**: Exibe informações sobre a execução do bot.
- **`open_site(self)`**: Abre o site da BotCity.
- **`run(self)`**: Método principal que executa o fluxo de navegação e captura erros.

### Arquivo de Log de Erro

Caso ocorra algum erro durante a execução, o bot salvará uma captura de tela chamada `erro.png`.

## Contribuições

Sinta-se à vontade para abrir issues e enviar pull requests. Se você encontrar bugs ou tiver sugestões de melhorias, ficaremos felizes em receber sua contribuição.

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
