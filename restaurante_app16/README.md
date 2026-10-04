# Restaurante App

Aplicación de escritorio desarrollada en Python utilizando Tkinter para la gestión básica de un restaurante.

## Semana 16 - Manejo de eventos en Tkinter

En esta semana se continúa el desarrollo del proyecto realizado en las semanas anteriores, conservando la arquitectura modular, las funcionalidades de productos y ventas, el inicio de sesión y la persistencia de información mediante archivos JSON.

La principal evolución corresponde a la gestión de usuarios, incorporando operaciones de registro, consulta, actualización y eliminación, además del manejo de diferentes roles y eventos de interacción en Tkinter.

## Objetivos de la Semana 16

- Continuar el proyecto desarrollado en semanas anteriores.
- Implementar la gestión CRUD de usuarios.
- Incorporar roles para los usuarios.
- Aplicar eventos mediante `bind()`.
- Utilizar `Treeview` para mostrar los usuarios.
- Utilizar `Combobox` para seleccionar roles.
- Mantener la separación entre interfaz, servicios y persistencia.
- Conservar la información de los usuarios mediante `usuarios.json`.

## Gestión de usuarios

La aplicación permite administrar usuarios mediante las siguientes operaciones:

- Registrar usuarios.
- Consultar usuarios.
- Actualizar usuarios.
- Eliminar usuarios.
- Seleccionar usuarios desde un `Treeview`.
- Cambiar el rol de un usuario.
- Limpiar el formulario.

Los roles disponibles son:

| Rol | Descripción |
|---|---|
| Administrador | Puede acceder a la gestión administrativa de usuarios. |
| Empleado | Usuario del sistema con funciones de empleado. |
| Cliente | Usuario registrado como cliente del restaurante. |

La contraseña no se muestra en la tabla de usuarios.

## Manejo de eventos

Durante la Semana 16 se implementaron diferentes mecanismos de eventos de Tkinter.

### TreeviewSelect

El evento `<<TreeviewSelect>>` permite detectar la selección de una fila en la tabla de usuarios.

Cuando se selecciona un usuario, sus datos se cargan automáticamente en el formulario para poder consultarlos o modificarlos.

### Return

El evento `<Return>` permite utilizar la tecla Enter como atajo para registrar un usuario desde el formulario.

### Escape

El evento `<Escape>` permite limpiar el formulario y cancelar la selección actual.

### ComboboxSelected

El evento `<<ComboboxSelected>>` permite detectar el cambio de rol realizado mediante el `Combobox`.

## Uso de bind()

La función `bind()` permite asociar eventos de Tkinter con funciones callback.

En este proyecto se utiliza para responder a:

- `<<TreeviewSelect>>`
- `<Return>`
- `<Escape>`
- `<<ComboboxSelected>>`

Los callbacks reutilizan los métodos existentes de la aplicación para evitar duplicar la lógica de las operaciones.

## Uso de command=

Los botones principales utilizan `command=` para ejecutar sus respectivas acciones:

- Registrar
- Actualizar
- Eliminar
- Limpiar
- Registrar venta
- Ingresar

De esta manera se diferencia el uso de `command=` para botones y `bind()` para eventos de interacción y teclado.

## Arquitectura del proyecto

El proyecto mantiene una arquitectura modular:

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
│   └── logo.png
├── main.py
└── README.md