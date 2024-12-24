# primeros-addons

Repositorio de trabajo para crear mis primeros addons y desarrollos en odoo.

## Comandos útiles de docker

docker compose down --rmi all --volumes --remove-orphans

docker compose up --build -d --force-recreate

## Consideraciones

Para poder levantar odoo con esta configuración te hace falta crear en local las carpetas "*odoo-db-data*", "*odoo-web-data*", el archivo "*.env*" y el archivo "*odoo.conf*" (este último dentro de la carpeta config/, el resto debe ir en la raiz del repositorio).
Importante: la carpeta "*odoo-web-data*" debe tener permisos de escritura.
