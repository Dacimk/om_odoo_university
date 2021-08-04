version: '2'
services:
  db:
    image: postgres:10
    environment:
      - POSTGRES_USER=odoo
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_DB=postgres
      - PGDATA=/var/lib/postgresql/data/pgdata
    volumes:
      - /srv/Databases/oodo:/var/lib/postgresql/data

  odoo:
    image: odoo:latest
    links:
      - db:db
    depends_on:
      - "db"
    ports:
      - 8069:8069
    volumes:
      - /srv/Configs/oodo:/etc/oodo