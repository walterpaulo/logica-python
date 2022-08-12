## Dia 19 - 12/08/2022[  🔙](../../README.md)

- Repartido o template - Partitions
    - cria a pasta shared no diretório templates. Coloca as partes do front que são partes comuns, como header.html, menu.html, footer.html ...
    - depois aponta esse arquivos compartihlhas no main, adicona este código com o caminho dos arquivos:
        - exemplo, para o header:
            -   {% include '../shared/_header.html' %}[ exemplo](../17/desafio21diaspython/web/templates/home/)
- enviar dados do formulário para o servidor há dois modos disabilitar o token ou colocar o token no formulário
 - {% crsf_token %}
    -irá aparecer automaticamente o campo do tipo hidden e com os valores preenchidos em name e value;
 
 Adicionado o if caso recebe dados do servidor:
 ```python
 {% if mensagem != None %} 
    <p>{{mensagem}}</p>
 {% endif %}
 ```

Pegar um dado via post
  - request.POST["email"]