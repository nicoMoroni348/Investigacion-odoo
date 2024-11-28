# primeros-addons

Repositorio de trabajo para crear y probar nuestros primeros addons en la versión 15 de odoo

## Odoo levantado como servicio

En este orden:
./odoo-bin -c ../proyecto-odoo/odoo.conf -s --stop-after-init
./odoo-bin -c ../proyecto-odoo/odoo.conf -i nico

Y de ahí en más usas esta:
./odoo-bin -c ../proyecto-odoo/odoo.conf

## Odoo levantado como contenedor

docker compose down --rmi all --remove-orphans && docker compose up --build -d