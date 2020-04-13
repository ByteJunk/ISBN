# ISBN
Uma pequena experiência em python para gerar e validar ISBN10 e ISBN13

O projeto é composto por 2 pequenos scripts, um para gerar e outro para validar ISBNs.  

## Gerar ISBN
Invocar o gerador via terminal. O resultado será um par de ISBNs (10 e 13) fictícios, mas válidos.
Por exemplo:

```console
$ py gerarISBN.py
***** Novo livro inventado *****
ISBN10: 604-412-018-X
ISBN13: 978-604-412-018-8
```

## Validar ISBN
Invocar o validador via terminal. Será pedido o ISBN, que pode ser introduzido com ou sem hífens. Pode ser um ISBN10 ou ISBN13.
```console
$ py validarISBN.py
Insira o ISBN10 ou ISBN13 que pretende validar.
ISBN: 978-972-37-0274-3
Temos um ISBN13 para validar.
ISBN13 válido.
```


