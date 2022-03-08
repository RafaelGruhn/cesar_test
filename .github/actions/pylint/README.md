# GitHub Actions - Executar Pylint.

Executa um lint em códigos Python.

Exemplo:

```yaml
    # Using one of the actions from Convair
  - name: PyLint
    uses: ./.convair-actions/pylint
    with:
      basePath: /caminho/para/projeto-Python  
```
# Entradas

* `configurationFile` - Caminho do arquivo .pylintrc, o padrão é a raiz do projeto.
* `basePath`          - Caminho para o pylint realizar a análise, o padrão também será a raiz do projeto.
