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
INSERT INTO "pizzas" ("id", "name", "created_at", "updated_at")
VALUES (
        1,
        'Margherita',
        '2024-12-12 13:25:25.162192',
        NULL
    );