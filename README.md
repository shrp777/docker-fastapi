# Docker + FastAPI (Python) + PostgreSQL

Projet modèle pour la mise en place d'une API REST avec le langage Python et le framework FastAPI (<https://fastapi.tiangolo.com/>) et Docker.

Ce projet est fourni à des fins pédagogiques.

## Stack technologique

- Langage de programmation : Python 3.10
- Framework : FastAPI
- Validateur : Pydantic
- Base de données : PostgreSQL
- ORM : SQLAlchemy
- Architecture d'API : REST

## Installation

Créer les fichiers :

- ./api/.env
- ./db/.env

## Arborescence du projet

```text
api
├── Dockerfile
├── README.md
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   └── main.cpython-39.pyc
│   ├── db.py
│   ├── internal
│   │   ├── __init__.py
│   │   └── admin.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── pizza.py
│   ├── routers
│   │   ├── __init__.py
│   │   └── pizza_router.py
│   └── services
│       ├── __init__.py
│       ├── exceptions
│       │   └── __init__.py
│       └── pizza_service.py
└── requirements.txt
```

## Commandes Docker utiles

- Initialisation des services Docker :
`docker compose up`

- Rénitialisation des services Docker (suppression des données) :
`docker compose down`

- Initialisation des services Docker en mode détaché (reprise de la main dans le terminal) :
`docker compose up -d`

- Initialisation des services Docker avec reconstruction de l'image :
`docker compose up --build`

- Initialisation des services Docker avec activation du mode watch (= hot reloading) :
`docker compose up --watch`

- Consultation des services Docker actifs :
`docker compose ps`

- Clôture des services Docker :
`docker compose stop`

- Création d'une image Docker à partir du fichier Dockerfile et des sources :
`docker build -t <image-name> .`

- Création d'un container à partir de l'image `<image-name>` précédemment créée :
`docker run -d --name <image-name> -p 8080:80 <image-name>`

## Routes de l'API

### Documentation Swagger générée automatiquement par FastAPI

<http://localhost:8080/docs>

### Endpoint pizzas

#### Lecture de tous les items

```sh
curl --request GET \
  --url http://localhost:8080/pizzas
```

```http
GET /pizzas HTTP/1.1
Host: localhost:8080
```

```json
[
  {
    "id": 1,
    "name": "Margherita",
    "created_at": "2024-12-12T13:25:25.162192",
    "updated_at": null
  }
]
```

#### Lecture d'un item sélectionné par son id

```sh
curl --request GET \
  --url http://localhost:8080/pizzas/1
```

```http
GET /pizzas/1 HTTP/1.1
Host: localhost:8080
```

```json
{
  "id": 1,
  "name": "Margherita",
  "created_at": "2024-12-12T13:25:25.162192",
  "updated_at": null
}
```

## Adminer (interface web d'administration de base de données)

Pour des raisons de sécurité, __désactiver ce service en production__.

<http://localhost:8181>

- Interface d'administration web [Adminer](http://localhost:8181/?pgsql=db&username=pizzas&db=pizzas&ns=public)
- Sélectionner Système : __postgresql__
- Serveur : __db__
- Utilisateur : cf. ./db/.env
- Mot de passe : cf. ./db/.env
- Base de données : cf. ./db/.env

## Base de données PostgreSQL

```SQL

DROP TABLE IF EXISTS "pizzas";
DROP SEQUENCE IF EXISTS pizzas_id_seq;
CREATE SEQUENCE pizzas_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."pizzas" (
    "id" integer DEFAULT nextval('pizzas_id_seq') NOT NULL,
    "name" character varying NOT NULL,
    "created_at" timestamp NOT NULL,
    "updated_at" timestamp,
    CONSTRAINT "pizzas_name_key" UNIQUE ("name"),
    CONSTRAINT "pizzas_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_pizzas_id" ON "public"."pizzas" USING btree ("id");

INSERT INTO "pizzas" ("id", "name", "created_at", "updated_at") VALUES
(1, 'Margherita', '2024-12-12 13:25:25.162192', NULL);
```

--

!["Logotype Shrp"](https://sherpa.one/images/sherpa-logotype.png)

__Alexandre Leroux__  
_Enseignant / Formateur_  
_Développeur logiciel web & mobile_

Nancy (Grand Est, France)

<https://shrp.dev>
