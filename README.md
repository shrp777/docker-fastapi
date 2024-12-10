# Kanban API - Preuve de concept : Docker + FastAPI (Python) + PostgreSQL

API REST basée sur le langage Python et le framework FastAPI (<https://fastapi.tiangolo.com/>).

- Attention le projet Kanban API est réalisé à titre pédagogique. Il s'agit d'une base qui mérite d'être améliorée pour envisager un passage en production.

- Améliorations possibles :
  - Architecture davantage découplée (cf. <https://fastapi.tiangolo.com/tutorial/bigger-applications/>)
  - Emploi de handlers pour chaque route pour éviter de mélanger routage, contrôleurs et logique métier
  - Emploi d'une couche de services

- Tutoriel officiel :
<https://fastapi.tiangolo.com/deployment/docker/>

- PostgreSQL + Docker
<https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/>

## Stack technologique

- Base de données : PostgreSQL
- Langage de programmation : Python 3.10
- Framework : FastAPI
- ORM : SQLAlchemy
- Validateur : Pydantic
- Architecture d'API : REST

## Installation

- Créer les fichiers ./api/.env et ./db/.env basés sur les fichiers modèles ./api/.env.example et ./db/.env.example (à adapter).

## Commandes Docker utiles

- Création d'une image Docker à partir du fichier Dockerfile et des sources :
`docker build -t fastapiimage .`

- Création d'un container à partir de l'image "fastapiimage" précédemment créée :
`docker run -d --name fastapi -p 8080:80 fastapiimage`

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

- Démarrage des services Docker :
`docker compose start`

- Consultation des services Docker actifs :
`docker compose ps`

- Clôture des services Docker :
`docker compose stop`

## Routes l'API

### Racine

```sh
curl http://localhost:8080
```

### Collection tasks

#### Création d'une task

```sh
curl --request POST \
  --url http://localhost:8080/tasks \
  --header 'content-type: application/json' \
  --data '{
  "content":"Faire du sport",
  "urgence":1,
  "importance":5
}'
```

```http
"POST /tasks HTTP/1.1" 201
```

```JSON
{
  "id": 1,
  "content": "Faire du sport",
  "urgence": 1,
  "importance": 5,
  "created_at": "2024-12-10T11:37:45.148692",
  "updated_at": null,
  "completed_at": null,
  "is_completed": false
}
```

#### Lecture de toutes les tasks

Par défaut la collection est vide.

```sh
curl --request GET \
  --url http://localhost:8080/tasks
```

```http
"GET /tasks HTTP/1.1" 200
```

```JSON
[
  {
    "id": 1,
    "content": "Faire du sport",
    "urgence": 1,
    "importance": 5,
    "created_at": "2024-12-10T11:37:45.148692",
    "updated_at": null,
    "completed_at": null,
    "is_completed": false
  },
  {
    "id": 2,
    "content": "Tondre la pelouse",
    "urgence": 1,
    "importance": 2,
    "created_at": "2024-12-10T11:39:06.424590",
    "updated_at": null,
    "completed_at": null,
    "is_completed": false
  }
]
```

#### Lecture de 1 task par son id

```sh
curl --request GET \
  --url http://localhost:8080/tasks/1
```

```http
"GET /tasks/1 HTTP/1.1" 200
```

```JSON
{
  "id": 1,
  "content": "Faire du sport",
  "urgence": 1,
  "importance": 5,
  "created_at": "2024-12-10T11:37:45.148692",
  "updated_at": null,
  "completed_at": null,
  "is_completed": false
}
```

### Mise à jour d'1 task par son id

```sh
curl --request PUT \
  --url http://localhost:8080/tasks/1 \
  --header 'content-type: application/json' \
  --data '{
  "id":1,
  "created_at":"2024-07-07 07:07:07",
  "content": "Faire du sport",
  "urgence": 1,
  "importance": 4,
  "is_completed":false
}'
```

```http
"PUT /tasks/1 HTTP/1.1" 200
```

```json
{
  "id": 1,
  "content": "Faire du sport",
  "urgence": 1,
  "importance": 4,
  "created_at": "2024-07-07T07:07:07",
  "updated_at": "2024-12-10T11:39:54.659197",
  "completed_at": null,
  "is_completed": false
}
```

#### Complètion d'une task selon son id

```sh
curl --request PATCH \
  --url http://localhost:8080/tasks/1
```

```http
"PATCH /tasks/1 HTTP/1.1" 200
```

```json
{
  "id": 1,
  "content": "Faire du sport",
  "urgence": 1,
  "importance": 4,
  "created_at": "2024-07-07T07:07:07",
  "updated_at": "2024-12-10T11:40:53.372111",
  "completed_at": "2024-12-10T11:40:53.372103",
  "is_completed": true
}
```

#### Suppression d'une task selon son id

```sh
curl --request DELETE \
  --url http://localhost:8080/tasks/1
```

```http
"DELETE /tasks/1 HTTP/1.1" 204
```

- Documentation Swagger générée automatiquement par FastAPI
<http://localhost:8080/docs>

## Adminer (interface d'administration de base de données)

<http://localhost:8181>

## Base de donénes PotsgreSQL

### Schéma

```sql
DROP TABLE IF EXISTS "tasks";
DROP SEQUENCE IF EXISTS pizzas_id_seq;
CREATE SEQUENCE pizzas_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."tasks" (
    "id" integer DEFAULT nextval('pizzas_id_seq') NOT NULL,
    "name" character varying NOT NULL,
    "ingredients" character varying NOT NULL,
    "price" double precision NOT NULL,
    CONSTRAINT "ix_pizzas_name" UNIQUE ("name"),
    CONSTRAINT "pizzas_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_pizzas_id" ON "public"."tasks" USING btree ("id");
```

### Data

```sql
INSERT INTO "tasks" ("id", "name", "ingredients", "price") VALUES
(1, 'Margherita', 'Basilic, Mozzarella', 6);
```

--

!["Logotype Shrp"](https://sherpa.one/images/sherpa-logotype.png)

__Alexandre Leroux__  
_Enseignant / Formateur_  
_Développeur logiciel web & mobile_

Nancy (Grand Est, France)

<https://shrp.dev>
