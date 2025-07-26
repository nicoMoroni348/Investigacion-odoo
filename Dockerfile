# Usa la imagen oficial de Odoo como base
FROM odoo:17.0-20250131

# Cambia al usuario root para instalar paquetes
USER root

# Limpiar repos de PostgreSQL y luego actualizar e instalar en la misma capa
RUN rm -f /etc/apt/sources.list.d/postgresql.list \
  && sed -i '/^deb .*postgresql/d' /etc/apt/sources.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends \
       python3-pip \
       iputils-ping \
       build-essential \
       libssl-dev \
       libffi-dev \
       python3-dev \
       swig \
       libxml2-dev \
       libxslt1-dev \
       zlib1g-dev \
       libjpeg-dev \
  && rm -rf /var/lib/apt/lists/*

# Copia el archivo de dependencias (requirements.txt) al contenedor
COPY addons/requirements.txt /tmp/requirements.txt

# Instala las dependencias de Python
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Elimina archivos temporales para mantener la imagen ligera
RUN rm -rf /tmp/requirements.txt

# Cambia de nuevo al usuario odoo
USER odoo

# Comando por defecto
CMD ["odoo"]