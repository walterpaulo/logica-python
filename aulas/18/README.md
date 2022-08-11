## Dia 18 - 11/08/2022[  🔙](../../README.md)

- = context_type = application/json
- templates -> página padrão do Django;
    - em rota informa;
    - na views -> return render(request, 'index.html')
- static, páginas estáticas.
    - precisar informar essa pasta para reconhecer o projeto
    - informar a pasta static no arquivo settings.py
        -na linha 131 STATIC_URL = 'static/'
        -na linha 132 digita, STATIC_ROOT = os.path.join(BASE_DIR, "/web/stactic")
        - depois vá no urls.py em web e adiciona no final do bloco
            - deve definir o nome diferente da diferente da aplicação principal, pode nomear 'public'.


```s
def index(request):
    resposta = {}
    resposta["conteudo"] = "Agora com API JSON"
    return JsonResponse(resposta)
```