
# -----------------------------------------------DETALLE TAREA----------------------------------------------------------
# Dada una lista de contactos, ubicada en el fichero database.json, se pide: comprobar a través del email(email__iexact)
# si el contacto existe en el HDH, si existe, actualizarlo, si no existe, crearlo. Para ello, se debe utilizar la
# API del HDH.

# Como resultado final se espera una lista de contactos_procesados donde se indique el ID del contacto en el HDH y un
# estado que indique si ha sido creado o actualizado.
# Ejemplo resultado: contactos_procesados = [{'id': 8846342, 'status': 'created'}, {'id': 3232234, 'status': 'updated'}]
# ---------------------------------------------FIN DETALLE TAREA--------------------------------------------------------

# Documentación de la API del HDH: https://learn.fideltour.com/external/manual/hoteldatahub-api-v1/article/primeros-pasos?p=a0f1f9539beee4f1ce92b65b4bf3ab0c242ac92ad5aba02ae25213d6ec34f971
# Swagger de la API del HDH: https://app.hoteldatahub.io/swagger/
# Credenciales de acceso a la API del HDH:
USERNAME = 'recruitment'
PASSWORD = 'cNs>?|~77D32'
BASE_URL = 'https://app.hoteldatahub.io/api/v1/'


if __name__ == '__main__':
    print('Hello World')



