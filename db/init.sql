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