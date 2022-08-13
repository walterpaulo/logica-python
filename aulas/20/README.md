## Dia 20 - 13/08/2022[  🔙](../../README.md)

- Enviar dados do formulário para o servidor
- necessário criar rota para logar
- tratar dados do formulários
- passagem dados entre páginas html para arquivos comuns, [arquivo comun](../17/desafio21diaspython/web/templates/shared/_header.html) e [nomea o valor do título](../17/desafio21diaspython/web/templates/cliente/index.html);
- cookie de páginas, 
   - valor = request.COOKIES.get('usuario_logado')

Validação de campos:

```python
@require_http_mehotd(["POST"])
def logar(request):

   # pegar dados do formula
   email = request.POST["email"]
   senha = request.POST["senha"]
   
   # Validação dos dados recebidos
   if email is None or email == "":
      return return render(request, 'login/index.html', {"login": "true", "mensagem":"Email é obrigatório"})

   if senha is None or senha == "":
      return return render(request, 'login/index.html', {"login": "true", "mensagem":"Senha é obrigatório"})

   return render(request, 'login/index.html', {"login": "true", "mensagem":""})



```
Troca de informações entre páginas html para páginas comuns para toda aplicação, header, menu, footer...

```python
   # Adiciando o nome do título da página
  {% include '../shared/_header.html' with titulo="Home" %}
  <body>
    <div class="container">
      <div class="box">
      ...

```