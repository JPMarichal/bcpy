
## Requerimiento Técnico para el Desarrollo de una Aplicación Web con Django y Django REST Framework (DRF)

### **Objetivo del Proyecto**

Desarrollar una aplicación web moderna y escalable utilizando **Django** como framework principal, **Django REST Framework (DRF)** para la implementación de APIs REST, y **React** para el frontend. La aplicación debe ser responsiva, utilizar patrones de diseño adecuados como MTV y BEM, y permitir despliegues automáticos mediante GitHub Actions. La aplicación estará enfocada en potenciar el aprendizaje de los Santos de los Últimos Días, con recursos útiles que incluyan varias secciones temáticas.

---

### **Requerimientos Funcionales**

1. **Backend:**

   - Uso de **Django** como framework principal para manejar la lógica de negocio y la administración de datos.
   - Implementación de una API RESTful mediante **Django REST Framework (DRF)**.
   - Migración de datos utilizando **PostgreSQL** como base de datos en desarrollo y producción.
   - Gestión de usuarios y permisos, incluyendo roles y grupos.
   - Servicios de publicación a redes sociales, Telegram y una lista de correos (probablemente con **MailRelay**).

2. **Frontend:**

   - Uso de **React** para el desarrollo de una interfaz de usuario moderna e interactiva.
   - Manejo de estados globales con **Redux**, incluyendo sesión y preferencias de usuario.
   - Diseño responsivo mediante **Bootstrap** (usando CDN).
   - Utilización de **Sass** como preprocesador CSS, estructurado según el patrón BEM (Block Element Modifier).
   - Integración de íconos mediante **Font Awesome** (usando CDN).

3. **Secciones del Sitio:**

   - **Artículos:** Sección similar a un CMS como WordPress, con soporte para **RSS**, **sitemaps** y buenas prácticas de **SEO**.
   - **Noticias:** Una sección para la publicación de novedades relevantes.
   - **Glosario:** Con subcategorías como lugares, periodos, términos, objetos, biografías, personajes, entre otros.

4. **Diseño:**

   - Moderno, elegante y apropiado para un sitio de naturaleza religiosa e inspiradora.
   - Los controles deben seguir las mejores prácticas de usabilidad y diseño de interfaces.
   - Totalmente reactivo y responsivo para adaptarse a cualquier dispositivo.

5. **CI/CD:**

   - Automatización del proceso de compilación y despliegue mediante **GitHub Actions**.
   - Despliegue automático de archivos estáticos y código backend al servidor de producción mediante **FTP**.

6. **Producción:**

   - Despliegue en un servidor compartido que no tiene acceso a sudo ni Docker.
   - Compilación local de Sass y React antes del despliegue.
   - Configuración de Django para servir archivos estáticos en producción.

---

### **Requerimientos No Funcionales**

1. **Escalabilidad:**

   - Diseño modular y organizado del proyecto utilizando patrones como MTV para el backend y BEM para los estilos CSS.
   - División del frontend en componentes reutilizables de React.

2. **Compatibilidad:**

   - La aplicación debe ser compatible con navegadores modernos y dispositivos móviles.

3. **Mantenibilidad:**

   - El código debe seguir las mejores prácticas de programación en Django, DRF y React.
   - Uso de un archivo `.gitignore` para ignorar archivos innecesarios en el repositorio.

4. **Rendimiento:**

   - Uso de consultas optimizadas para evitar sobrecarga en la base de datos.
   - Implementación de un sistema de caché con el Django Cache Framework.
   - Diseño centrado en la eficiencia y el performance en todo momento.

5. **SEO:**

   - Configuración de metadatos y buenas prácticas para mejorar el SEO.
   - Uso de mapas del sitio y soporte para rich snippets.

6. **Documentación:**

   - Generación de documentación automática de la API mediante **Swagger** o **Redoc**.

---

### **Estructura del Proyecto**

```plaintext
project_root/
├── apps/
│   ├── core/             # Lógica central, como autenticación y usuarios
│   ├── api/              # Vistas y serializadores de la API (DRF)
│   ├── frontend/         # App que maneja React o vistas renderizadas
│   ├── articles/         # Sección de artículos
│   ├── news/             # Sección de noticias
│   ├── glossary/         # Sección de glosario
├── static/               # Archivos estáticos compilados
│   ├── css/              # CSS generado desde Sass
│   ├── js/               # Archivos JavaScript de React compilados
│   ├── images/           # Archivos de imagen
├── templates/            # Plantillas HTML (si se usan)
├── .github/              # Configuración de GitHub Actions
├── .gitignore            # Ignorar archivos innecesarios
├── requirements.txt      # Dependencias del proyecto
├── manage.py             # Script de administración de Django
```

---

### **Flujo de CI/CD con GitHub Actions**

1. **Triggers:**

   - El pipeline se ejecuta automáticamente al hacer un push a la rama `main`.

2. **Pasos Automatizados:**

   - Clonación del repositorio.
   - Configuración del entorno Python.
   - Instalación de dependencias de Python desde `requirements.txt`.
   - Compilación de Sass a CSS.
   - Compilación de React a JavaScript estático.
   - Ejecución de pruebas unitarias.
   - Generación de documentación automática de la API con Swagger.
   - Despliegue de archivos al servidor mediante FTP.

---

### **Lineamientos de Desarrollo**

1. **Django:**

   - Todas las apps deben estar encapsuladas dentro del directorio `apps/` para una mejor organización.
   - Uso de Django ORM para consultas a la base de datos.
   - Configuración del middleware para manejar autenticación y seguridad (CSRF, XSS, etc.).
   - Implementación de caché para optimizar tiempos de respuesta.

2. **DRF:**

   - Serializadores para transformar modelos en datos JSON.
   - Paginación de APIs REST para optimizar el consumo de datos.
   - Uso de Swagger para documentación de las APIs REST.

3. **Frontend (React + Sass):**

   - Estructura modular de componentes en React.
   - Uso de Sass y BEM para mantener un estilo organizado y escalable.
   - Manejo de estados globales con Redux para sesión y preferencias de usuario.

4. **Git y GitHub:**

   - Uso de un `.gitignore` que excluya archivos compilados y temporales.
   - Implementación de ramas de desarrollo y pull requests para colaboración.

---

### **Entregables**

1. Aplicación Django completamente funcional con APIs REST y un frontend responsivo.
2. Archivo `.gitignore` adecuado para evitar archivos innecesarios en producción.
3. Configuración de GitHub Actions para CI/CD.
4. Documentación automática de la API generada con Swagger o Redoc.
5. Manual de configuración y uso del sistema.

---

### **Próximos Pasos**

1. Configurar el entorno de desarrollo en Replit.
2. Implementar la estructura inicial del proyecto.
3. Configurar GitHub Actions para automatizar el despliegue.
4. Definir endpoints iniciales de la API REST.
5. Diseñar los primeros componentes de React con Sass y BEM.
6. Implementar Swagger para la documentación de las APIs REST.

---
