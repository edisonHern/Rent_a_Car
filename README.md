# 🚗 Rent_a_Car_7

**Rent_a_Car_7** es una aplicación web desarrollada en **Django** que permite gestionar el arriendo de automóviles. Incluye un catálogo de autos, sistema de reservas, administración de clientes, gestión de pagos y un panel para administradores. Su objetivo es facilitar el proceso de arriendo tanto para clientes como para la empresa.

---

## 📌 Funcionalidades principales
- Registro e inicio de sesión de clientes y administradores.  
- Catálogo de vehículos con detalles e imágenes.  
- Sistema de reservas con fechas disponibles.  
- Administración de usuarios y autos.  
- Gestión de pagos y control de transacciones.  
- Panel de administración con reportes.  

---

## 🛠️ Tecnologías utilizadas
- **Backend:** Python 3.12 + Django  
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap  
- **Base de datos:** SQLite (desarrollo), PostgreSQL/MySQL (producción opcional)  
- **Control de versiones:** Git y GitHub  

---

## 📂 Estructura básica del proyecto

Rent_a_Car_7a/
├── administradorApp/ # Gestión de administradores
├── clientesApp/ # Gestión de clientes
├── core/ # Configuración y modelos principales
├── templatesApp/ # Plantillas HTML
├── static/ # Archivos estáticos (CSS, JS, imágenes)
├── media/ # Archivos subidos por usuarios
├── manage.py # Script principal de Django
└── requirements.txt # Dependencias del proyecto


---

## 🚀 Instalación y uso

### 1. Clonar el repositorio
```bash
git clone https://github.com/edisonHern/Rent_a_Car.git
cd Rent_a_Car

(Opcional) Crear entorno virtual
py -3.12 -m venv venv
venv\Scripts\activate

Instalar dependencias
pip install -r requirements.txt

Aplicar migraciones
python manage.py migrate

Crear superusuario
python manage.py createsuperuser

Ejecutar servidor
python manage.py runserver

Abrir en el navegador: 👉 http://localhost:8000
