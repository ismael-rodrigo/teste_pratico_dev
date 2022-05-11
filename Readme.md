# REST API  aplicação DEV-JR Polícia Civil

## Install
    git clone https://github.com/ismael-rodrigo/teste_pratico_dev

    cd teste_pratico_dev

    pip install -r requirements.txt

## Run the app

    python manage.py runserver

# REST API

REST API criada para teste de vaga Dev.Jr da Polícia Civil.

---
&nbsp;
# ENDPOINTS
| endpoint | method | Descript |
| :--- | :--- | :--- |
| `api/calibres/` | `GET , POST` | Calibres |
| `api/calibres/{id}` | `PUT , DEL` | Calibres |
| `api/objetos-tipo/` | `GET , POST` | Objeto Tipo |
| `api/objetos-tipo/{id}` | `PUT , DEL` | Objeto Tipo |
| `api/armas/` | `GET , POST` | Armas |
| `api/armas/{id}` | `PUT , DEL` | Armas |
| `api/municoes/` | `GET , POST` | Munições |
| `api/municoes/{id}` | `PUT , DEL` | Muniçoes |
&nbsp;
---

&nbsp;
&nbsp;
# Calibres
## listar Calibres

### Request

`GET api/calibres/`

### Response

```javascript
[
    {
        "id" : integer,
        "desc_calibre" : string,
    },
]   
```

## Criar novo Calibre

### Request

`POST api/calibres/`



| Paramentro | Tipo | Descrição |
| :--- | :--- | :--- |
| `desc_calibre` | `string` | **Required**. Descrição do Calibre |



### Response

```javascript
{
    "id" : integer,
    "desc_calibre" : string,
}
```

## Buscar Calibre específico

### Request

`GET api/calibres/id/`

### Response

```javascript
{
    "id" : integer,
    "desc_calibre" : string,
}
```

## Alterar atributo de Calibre específico

### Request

`PUT api/calibres/id/`

| Paramentro | Tipo | Descrição |
| :--- | :--- | :--- |
| `desc_calibre` | `string` | **Required**. Nova descrição do Calibre |

### Response

```javascript
{
    "id" : integer,
    "desc_calibre" : string,
}
```

## Deletar Calibre específico

### Request

`DEL api/calibres/id/`


## Response

`status 204`



# Objeto-Tipo
## listar Objeto-Tipo

### Request

`GET api/objetos-tipo/`

### Response

```javascript
[
    {
        "id" : integer,
        "tipo_de_objeto" : string,
    },
]   
```

## Criar novo Objeto-Tipo

### Request

`POST api/objetos-tipo/`



| Paramentro | Tipo | Descrição |
| :--- | :--- | :--- |
| `tipo_de_objeto` | `string` | **Required**. Tipo do objeto |



### Response

```javascript
{
    "id" : integer,
    "tipo_de_objeto" : string,
}
```

## Buscar Objeto-Tipo específico

### Request

`GET api/objetos-tipo/id/`

### Response

```javascript
{
    "id" : integer,
    "tipo_de_objeto" : string,
}
```

## Alterar atributo de Objeto-Tipo específico

### Request

`PUT api/objetos-tipo/id/`

| Paramentro | Tipo | Descrição |
| :--- | :--- | :--- |
| `tipo_de_objeto` | `string` | **Required**. Nova tipo de objeto |

### Response

```javascript
{
    "id" : integer,
    "tipo_de_objeto" : string,
}
```

## Deletar Objeto-Tipo específico

### Request

`DEL api/objetos-tipo/id/`


## Response

`status 204`

&nbsp;
&nbsp;

# Armas
## listar Armas

### Request

`GET api/armas/`

### Response

```javascript
[
    {
        "id" : integer,
        "objeto" : {
            "id" : integer,
            "objeto_tipo": integer
        },
        "marca" : string ,
        "modelo" : string ,
        "quantidade_de_tiros" : integer ,
        "valor_estimado" : double ,
        "imagem" : image ,
        "calibre" : integer

    },
]   
```

## Criar nova Arma

### Request

`POST api/armas/`



| Paramentro | Tipo | Descrição |
| :--- | :--- | :--- |
| `marca` | `string` | **Required**. Marca da arma |
| `modelo` | `string` | **Required**. Modelo da arma |
| `quantidade_de_tiros` | `int` | **Required**. Quantidade de tiros |
| `valor_estimado` | `float` | **Required**. Valor estimado |
| `imagem` | `image` | **Required**. Imagem |
| `calibre` | `int` | **Required**. Chave de Calibre |


### Response


```javascript

    {
        "id" : integer,
        "objeto" : {
            "id" : integer,
            "objeto_tipo": integer
        },
        "marca" : string ,
        "modelo" : string ,
        "quantidade_de_tiros" : integer ,
        "valor_estimado" : double ,
        "imagem" : image ,
        "calibre" : integer

    },
   
```

## Buscar Arma específica

### Request

`GET api/armas/id/`

### Response

```javascript

    {
        "id" : integer,
        "objeto" : {
            "id" : integer,
            "objeto_tipo": integer
        },
        "marca" : string ,
        "modelo" : string ,
        "quantidade_de_tiros" : integer ,
        "valor_estimado" : double ,
        "imagem" : image ,
        "calibre" : integer

    },
   
```

## Alterar atributos de Arma específica

### Request

`PUT api/armas/id/`

| Paramentro | Tipo | Descrição |
| :--- | :--- | :--- |
| `marca` | `string` | **Required**. Nova marca da arma |
| `modelo` | `string` | **Required**. Novo modelo da arma |
| `quantidade_de_tiros` | `int` | **Required**. Nova quantidade de tiros |
| `valor_estimado` | `float` | **Required**. Novo valor estimado |
| `imagem` | `image` | **Required**. Nova Imagem |
| `calibre` | `int` | **Required**. Nova chave de Calibre |


### Response

```javascript

    {
        "id" : integer,
        "objeto" : {
            "id" : integer,
            "objeto_tipo": integer
        },
        "marca" : string ,
        "modelo" : string ,
        "quantidade_de_tiros" : integer ,
        "valor_estimado" : double ,
        "imagem" : image ,
        "calibre" : integer

    },
   
```


## Deletar Arma específica

### Request

`DEL api/armas/id/`


## Response

`status 204`

&nbsp;
&nbsp;


# Munição
## listar Munições

### Request

`GET api/municoes/`

### Response

```javascript
[
    {
        "id" : integer,
        "objeto" : {
            "id" : integer,
            "objeto_tipo": integer
        },
        "marca" : string ,
        "modelo" : string ,
        "valor_estimado" : double ,
        "calibre" : integer

    },
]   
```

## Criar nova Munição

### Request

`POST api/municoes/`



| Paramentro | Tipo | Descrição |
| :--- | :--- | :--- |
| `marca` | `string` | **Required**. Marca da arma |
| `modelo` | `string` | **Required**. Modelo da arma |
| `valor_estimado` | `float` | **Required**. Valor estimado |
| `calibre` | `int` | **Required**. Chave de Calibre |


### Response


```javascript

    {
        "id" : integer,
        "objeto" : {
            "id" : integer,
            "objeto_tipo": integer
        },
        "marca" : string ,
        "modelo" : string ,
        "valor_estimado" : double ,
        "calibre" : integer

    },
   
```

## Buscar Munição específica

### Request

`GET api/municoes/id/`

### Response

```javascript

    {
        "id" : integer,
        "objeto" : {
            "id" : integer,
            "objeto_tipo": integer
        },
        "marca" : string ,
        "modelo" : string ,
        "valor_estimado" : double ,
        "calibre" : integer

    },
   
```

## Alterar atributos de Munição específica

### Request

`PUT api/municoes/id/`

| Paramentro | Tipo | Descrição |
| :--- | :--- | :--- |
| `marca` | `string` | **Required**. Nova marca da arma |
| `modelo` | `string` | **Required**. Novo modelo da arma |
| `valor_estimado` | `float` | **Required**. Novo valor estimado |
| `calibre` | `int` | **Required**. Nova chave de Calibre |


### Response

```javascript

    {
        "id" : integer,
        "objeto" : {
            "id" : integer,
            "objeto_tipo": integer
        },
        "marca" : string ,
        "modelo" : string ,
        "valor_estimado" : double ,
        "calibre" : integer

    },
   
```


## Deletar Munição específica

### Request

`DEL api/municoes/id/`


## Response

`status 204`

&nbsp;
&nbsp;

## Status Codes

Status retornados pela API:

| Status Code | Description |
| :--- | :--- |
| 200 | `OK` |
| 201 | `CREATED` |
| 204 | `NO CONTENT` |
| 400 | `BAD REQUEST` |
| 404 | `NOT FOUND` |
| 500 | `INTERNAL SERVER ERROR` |