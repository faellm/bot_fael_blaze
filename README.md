# Análise de Resultados em Tempo Real

Este código em Python realiza uma análise de resultados em tempo real de um jogo de roleta. Ele utiliza a biblioteca `requests` para fazer uma requisição à API do jogo e obter os resultados mais recentes. Em seguida, os resultados são convertidos em uma lista contendo as cores dos números.

![GIF](https://media.giphy.com/media/87lqdEhl5YoViB4spO/giphy.gif)


## Funcionamento

1. O código faz uma requisição GET para a URL `'https://blaze.com/api/roulette_games/recent'` para obter os resultados do jogo de roleta.
2. Os resultados são convertidos em formato JSON.
3. Os resultados são processados para extrair apenas a cor de cada número e armazenados em uma lista chamada `ray`.
4. Os valores das cores são mapeados para "Vermelho", "Preto" e "Branco" de acordo com as convenções do jogo de roleta.
5. A lista `ray` é exibida no console.
6. O código espera por 15 segundos antes de repetir o processo.

## Envio de Notificações

O código também inclui uma função chamada `resultado(num)` que permite enviar notificações utilizando a plataforma de mensagens do Telegram. Para utilizar essa função, é necessário fornecer um token válido do BotFather e o ID do chat onde as mensagens devem ser enviadas. Você precisa preencher as variáveis `token` e `chat_id` com os valores adequados.

A função `resultado(num)` verifica os valores da lista `ray` e envia mensagens para o chat no Telegram de acordo com as condições estabelecidas. No exemplo fornecido, estão implementadas quatro condições diferentes, mas você pode adicionar mais análises de acordo com suas necessidades.

## Configuração

Certifique-se de ter instalado a biblioteca `requests` e `telebot` antes de executar o código. Você pode instalar as bibliotecas utilizando o pip:


## Observações

- Lembre-se de manter as informações do token e chat_id em segredo, pois são sensíveis e permitem acesso à sua conta no Telegram.
- É importante considerar as políticas e regras do jogo de roleta e da API utilizada para garantir a conformidade e legalidade do uso deste código.
- O código atualmente está configurado para executar indefinidamente, fazendo requisições a cada 15 segundos. Certifique-se de ajustar esse tempo de acordo com as necessidades do jogo e da API utilizada.

Espero que esse código seja útil para analisar os resultados do jogo de roleta em tempo real e enviar notificações no Telegram. Sinta-se à vontade para personalizar e adaptar o código de acordo com suas necessidades específicas.
