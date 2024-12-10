# Kanban API - Preuve de concept : Docker + FastAPI (Python) + PostgreSQL

API REST basée sur le langage Python et le framework FastAPI (<https://fastapi.tiangolo.com/>).

Ce projet est réalisé à des fins pédagogiques. Des améliorations doivent être envisagées pour un passage en production (sécurité, modularité...).

## Stack technologique

- Base de données : PostgreSQL
- Langage de programmation : Python 3.10
- Framework : FastAPI
- ORM : SQLAlchemy
- Validateur : Pydantic
- Architecture d'API : REST

## Installation

Créer les fichiers :

- ./api/.env
- ./db/.env

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

- Démarrage des services Docker :
`docker compose start`

- Consultation des services Docker actifs :
`docker compose ps`

- Clôture des services Docker :
`docker compose stop`

- Création d'une image Docker à partir du fichier Dockerfile et des sources :
`docker build -t fastapiimage .`

- Création d'un container à partir de l'image "fastapiimage" précédemment créée :
`docker run -d --name fastapi -p 8080:80 fastapiimage`

## Routes de l'API

### Documentation Swagger générée automatiquement par FastAPI

<http://localhost:8080/docs>

### API testable avec le logiciel Bruno

- Télécharger et installer Bruno (<https://docs.usebruno.com/introduction/what-is-bruno>)
- Importer la collection dans le dossier ./Kanban API Python

### Racine

```sh
curl http://localhost:8080
```

### Endpoint tasks

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

## Adminer (interface d'administration de base de données)

<http://localhost:8181>

## Base de donénes PotsgreSQL

### Adminer

- Interface d'administration web [Adminer](http://localhost:8181/?pgsql=db&username=kanban&db=kanban&ns=public)
- Sélectionner Système : __postgresql__
- Serveur : __db__
- Utilisateur : cf. ./db/.env
- Mot de passe : cf. ./db/.env
- Base de données : cf. ./db/.env

### Schéma

```sql
DROP TABLE IF EXISTS "tasks";
DROP SEQUENCE IF EXISTS tasks_id_seq;
CREATE SEQUENCE tasks_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1;

CREATE TABLE "public"."tasks" (
    "id" integer DEFAULT nextval('tasks_id_seq') NOT NULL,
    "content" character varying NOT NULL,
    "urgence" integer NOT NULL,
    "importance" integer NOT NULL,
    "created_at" timestamp NOT NULL,
    "updated_at" timestamp,
    "is_completed" boolean NOT NULL,
    "completed_at" timestamp,
    CONSTRAINT "tasks_pkey" PRIMARY KEY ("id")
) WITH (oids = false);

CREATE INDEX "ix_tasks_id" ON "public"."tasks" USING btree ("id");
```

### Data

```sql
INSERT INTO "tasks" ("id", "content", "urgence", "importance", "created_at", "updated_at", "is_completed", "completed_at") VALUES
(1, 'Tondre la pelouse', 1, 2, '2024-12-10 14:36:00.503193', NULL, 'f', NULL);
```

--

!["Logotype Shrp"](https://sherpa.one/images/sherpa-logotype.png)

__Alexandre Leroux__  
_Enseignant / Formateur_  
_Développeur logiciel web & mobile_

Nancy (Grand Est, France)

<https://shrp.dev>
