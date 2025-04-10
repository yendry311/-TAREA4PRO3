# Proyecto: Tienda de Computadoras con Pruebas Automatizadas

Este proyecto consiste en una página web de una tienda de computadoras que incluye funcionalidades de inicio de sesión, visualización de productos y cierre de sesión. Además, se han implementado pruebas automatizadas utilizando Selenium y Pytest para garantizar el correcto funcionamiento de las funcionalidades principales.

---

## **Características del Proyecto**

### **Página Web**
- **Inicio de Sesión:**
  - Permite a los usuarios autenticarse con un nombre de usuario y contraseña.
  - Muestra un mensaje de "Inicio de sesión exitoso" al autenticarse correctamente.
- **Visualización de Productos:**
  - Los productos solo son visibles después de iniciar sesión.
  - Cada producto incluye una imagen, nombre, descripción y precio.
- **Cierre de Sesión:**
  - Permite al usuario cerrar sesión, ocultando los productos y mostrando nuevamente el formulario de inicio de sesión.
- **Diseño Responsivo:**
  - La página se adapta a diferentes tamaños de pantalla, siendo accesible desde computadoras, tablets y móviles.

### **Pruebas Automatizadas**
- **Tecnologías Utilizadas:**
  - Selenium para la automatización del navegador.
  - Pytest para la ejecución de pruebas.
  - Pytest-HTML para la generación de reportes en formato HTML.
- **Pruebas Implementadas:**
  - Verificar que el inicio de sesión funcione correctamente.
  - Verificar que los productos sean visibles después de iniciar sesión.
  - Verificar que el cierre de sesión oculte los productos y muestre el formulario de inicio de sesión.
  - Generar capturas de pantalla en momentos clave:
    - Antes de iniciar sesión.
    - Después de iniciar sesión.
    - Después de cerrar sesión.

---

## **Estructura del Proyecto**
