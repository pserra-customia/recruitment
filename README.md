# Recruitment
Este proyecto es una prueba de nivel de Python de la empresa Customia-Fideltour. Se prentende testear la habilidad con las peticiones básicas a una API y con el tratamiento de datos.

# Explicación tarea
Dada una lista de contactos, ubicada en el fichero database.json, se pide: comprobar a través del email(email__iexact)
si el contacto existe en el HotelDataHub, si existe, actualizarlo, si no existe, crearlo. Para ello, se debe utilizar la
API del HotelDataHub.

# Resultado final
Como resultado final se espera una lista de contactos_procesados donde se indique el ID del contacto en el HotelDataHub y un
estado que indique si el contacto ha sido creado o actualizado.

```
contactos_procesados = [{"id": 8846342, "status": "created"}, {"id": 3232234, "status": "updated"}]
```

### Documentación de la API del HDH: [Pulsa aquí](https://learn.fideltour.com/external/manual/hoteldatahub-api-v1/article/primeros-pasos?p=a0f1f9539beee4f1ce92b65b4bf3ab0c242ac92ad5aba02ae25213d6ec34f971)
### Swagger de la API del HDH: [Pulsa aquí](https://app.hoteldatahub.io/swagger/)
### Credenciales de acceso a la API del HDH:

```
USERNAME = "recruitment"
PASSWORD = "cNs>?|~77D32"
BASE_URL = "https://app.hoteldatahub.io/api/v1/"
```
