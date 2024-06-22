import datetime
import sqlite3
import tkinter as tk
from tkinter import Image, PhotoImage, font
from tkinter import messagebox
from config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from PIL import ImageTk, Image

class Autor:  # Creacion de la clase autor
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido

    def get_nombre(self):  # metodo para obtener el nombre del autor
        return self._nombre

    def get_apellido(self):  # metodo para obtener el apellido del autor
        return self._apellido

    #setters

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def mostrar_info(self):
        print(f"El nombre del autor es: {self._nombre} {self._apellido}")

class Categoria:  # Creacion de la clase categoria
    def __init__(self, nombre):
        self._nombre = nombre

    def get_nombre(self):  # metodo para obtener el nombre de la categoria
        return self._nombre

    #setters

    def set_nombre(self, nombre):
        self._nombre = nombre

    def mostrar_info(self):
        print(f"El categoria es: {self._nombre}")

class Libro:  # Creacion de la clase libro
    def __init__(self, titulo, isbn, autor, categoria):
        self._titulo = titulo
        self._isbn = isbn
        self._autor = autor
        self._categoria = categoria

    def get_titulo(self):  # metodo para obtener el titulo del libro
        return self._titulo

    def get_isbn(self):  # metodo para obtener el isbn del libro
        return self._isbn

    def get_autor(self):  # metodo para obtener el autor
        return self._autor

    def get_categoria(self): #metodo para obtener la categoria
        return self._categoria

    #setters

    def set_titulo(self, titulo):
        self._titulo = titulo

    def set_isbn(self, isbn):
        self._isbn = isbn

    def set_autor(self, autor):
        self._autor = autor

    def set_categoria(self, categoria):
        self._categoria = categoria

    def mostrar_info(self):
        print(f"Título: {self._titulo}")
        print(f"ISBN: {self._isbn}")
        self._autor.mostrar_info()
        self._categoria.mostrar_info()

class Usuario:#clase usuario
    def __init__(self, nombre, apellido, id_user): 
        self._nombre = nombre
        self._apellido = apellido
        self._id_user = id_user

    def get_nombre(self):  # metodo para obtener el nombre del usuario
        return self._nombre

    def get_apellido(self):  # metodo para obtener el apellido del usuario
        return self._apellido

    def get_id_user(self):  # metodo para obtener el id del usuario
        return self._id_user

    #setters

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_apellido(self, apellido):
        self._apellido = apellido

    def set_id_user(self, id_user ):
        self._id_user  = id_user

class Prestamo: # creacion de la clase prestamo
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion):
        self._libro = libro
        self._usuario = usuario
        self._fecha_prestamo = fecha_prestamo
        self._fecha_devolucion = fecha_devolucion

    def get_libro(self): #metodo para obtener el libro que se va a prestar
        return self._libro

    def get_usuario(self): #metodo para obtener el usuario que realizara el prestamo
        return self._usuario

    def get_fecha_prestamo(self): #metodo para obtener la fecha del prestamo
        return self._fecha_prestamo

    def get_fecha_devolucion(self): #metodo para obtener la fecha en la que se devuelve el libro
        return self._fecha_devolucion

    #setters
    def set_libro(self, libro):
        self._libro = libro

    def set_usuario(self, usuario):
        self._usuario = usuario

    def set_fecha_prestamo(self, fecha_prestamo):
        self._fecha_prestamo = fecha_prestamo

    def set_fecha_devolucion(self, fecha_devolucion):
        self._fecha_devolucion = fecha_devolucion

    def mostrar_info(self):
        print(f"Préstamo: {self._fecha_prestamo} - {self._fecha_devolucion}")
        self._libro.mostrar_info()
        self._usuario.mostrar_info()

class Biblioteca: #creacion de la clase biblioteca
    def __init__(self):
        self._libros = []
        self._usuarios = []
        self._prestamos = []

    def registrar_libro(self, libro): #metodo para registrar los respectivos libros
        self._libros.append(libro)

    def registrar_usuario(self, usuario): #metodo para realizar el registro de usuarios a la biblioteca
        self._usuarios.append(usuario)

    def realizar_prestamo(self, prestamo): #metodo para la realizacion de los prestamos
        self._prestamos.append(prestamo)

    def devolver_libro(self, prestamo): #metodo para la devolucion de los libros
        if prestamo in self._prestamos:
            self._prestamos.remove(prestamo)

    def mostrar_usuarios(self):
        for usuario in self._usuarios:
            usuario.mostrar_info()

    def mostrar_libros(self): #metodo para mostrar los libros de la biblioteca
        for libro in self._libros:
            libro.mostrar_info()

    def mostrar_prestamos(self):
        for prestamo in self._prestamos:
            prestamo.mostrar_info()

    def buscar_libro_por_titulo(self, titulo):
        for libro in self._libros:
            if libro.get_titulo().lower() == titulo.lower():
                return libro
        return None

    def libro_esta_prestado(self, libro):
        for prestamo in self._prestamos:
            if prestamo.get_libro().get_isbn() == libro.get_isbn():
                return True
        return False

class LoginWindow(tk.Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Login")
        self.geometry("1500x1500")
        self.crear_widgets()

        # Conectar a la base de datos SQLite
        self.conexion = sqlite3.connect("usuario.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla_usuarios()
        

        self.biblioteca = Biblioteca() 
        # Lista de usuarios predefinidos

        usuarios = [
            Usuario("Juan", "Pérez", 1),
            Usuario("Ana", "Martínez", 2),
            Usuario("Luis", "Rodríguez", 3),
            Usuario("María", "López", 4),
            Usuario("Pedro", "González", 5),
            Usuario("Lucía", "Fernández", 6),
            Usuario("José", "García", 7),
            Usuario("Sofía", "Hernández", 8),
            Usuario("Miguel", "Ramírez", 9),
            Usuario("Marta", "Suárez", 10)
        ]
        
        for usuario in usuarios:
            self.registrar_usuario(usuario)

        autores = [
            Autor("Gabriel", "García Márquez"),
            Autor("Isabel", "Allende"),
            Autor("Julio", "Cortázar"),
            Autor("Antoine","de Saint-Exupéry")
        ]

        categorias = [
            Categoria("Novela"),
            Categoria("Ficción"),
            Categoria("Cuento")
        ]

        libros = [
            Libro("Cien años de soledad", "978-3-16-148410-0", autores[0], categorias[0]),
            Libro("La casa de los espíritus", "978-0-14-303996-9", autores[1], categorias[1]),
            Libro("Rayuela", "978-0-394-70691-5", autores[2], categorias[2]),
            Libro("El Principito", "978-7-13-131226-5", autores[3], categorias[0])
        ]

        for libro in libros:
            self.biblioteca.registrar_libro(libro)

        prestamos = [
            Prestamo(libros[0], usuarios[0], "2024-05-01", "2024-06-01"),
            Prestamo(libros[1], usuarios[1], "2024-05-02", "2024-06-02"),
            Prestamo(libros[2], usuarios[2], "2024-05-03", "2024-06-03"),
        ]

        for prestamo in prestamos:
            self.biblioteca.realizar_prestamo(prestamo)


    def crear_tabla_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL
            )
        """)
        self.conexion.commit()

    def registrar_usuario(self, usuario):
        self.cursor.execute("INSERT OR IGNORE INTO usuarios (id, nombre, apellido) VALUES (?, ?, ?)", 
                            (usuario.get_id_user(), usuario.get_nombre(), usuario.get_apellido()))
        self.conexion.commit()

    def crear_widgets(self):
        # Título
        self.label = tk.Label(self, text="Biblioteca José Rafael Faría", fg="black", font=("Helvetica", 22))
        self.label.pack(pady=20)

        # Imagen
        ruta_imagen = "./imagenes/icono.png"
        imagen = PhotoImage(file=ruta_imagen)
        imagen_redimensionada = imagen.subsample(3, 3)
        etiqueta_imagen = tk.Label(self, image=imagen_redimensionada)
        etiqueta_imagen.image = imagen_redimensionada
        etiqueta_imagen.pack()

        # Bienvenida
        self.label_bienvenida = tk.Label(self, text="Bienvenido, digite sus datos en los siguientes campos para acceder al sistema.", fg="black", font=("Helvetica", 16))
        self.label_bienvenida.pack(pady=20)

        # Campos de entrada
        self.label_nombre = tk.Label(self, text="Nombre:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_nombre.pack(pady=5)
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.pack(pady=5)

        self.label_apellido = tk.Label(self, text="Apellido:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_apellido.pack(pady=5)
        self.entry_apellido = tk.Entry(self)
        self.entry_apellido.pack(pady=5)

        self.label_id = tk.Label(self, text="ID:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_id.pack(pady=5)
        self.entry_id = tk.Entry(self)
        self.entry_id.pack(pady=5)

        # Botones
        self.btn_iniciar_sesion = tk.Button(self, text="Iniciar Sesión", command=self.iniciar_sesion)
        self.btn_iniciar_sesion.pack(pady=5)

        self.label_registro = tk.Label(self, text="¿Eres nuevo? Regístrate", bg="Light Yellow", fg="black", font=("Helvetica", 16))
        self.label_registro.pack(pady=15)

        self.btn_crear_usuario = tk.Button(self, text="Crear Usuario", command=self.abrir_ventana_crear_usuario)
        self.btn_crear_usuario.pack(pady=5)

        self.boton_salir = tk.Button(self, text="Salir", command=self.destroy, bg="#f44336", fg="#ffffff", relief=tk.FLAT)
        self.boton_salir.pack(pady=10)

    def iniciar_sesion(self):
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        id_usuario = self.entry_id.get()
        
        self.cursor.execute("SELECT * FROM usuarios WHERE nombre = ? AND apellido = ? AND id = ?", (nombre, apellido, id_usuario))
        resultado = self.cursor.fetchone()
        
        if resultado:
            messagebox.showinfo("Éxito", "Inicio de sesión exitoso")
        # Ocultar la ventana principal y mostrar la ventana de opciones
            self.parent.show_main_window()  # Llamar al método para mostrar la ventana principal
            self.destroy()
        else:
            messagebox.showerror("Error", "Nombre, apellido o ID incorrectos")

    def abrir_ventana_crear_usuario(self):
        ventana_crear_usuario = CrearUsuarioWindow(self)
        ventana_crear_usuario.grab_set()

class CrearUsuarioWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Crear Usuario")
        self.geometry("400x300")
        self.configure(bg="light blue")
        self.crear_widgets()
        self.usuarios = []
    
        self.conexion = sqlite3.connect("usuario.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla_usuarios()

        usuarios = [
            Usuario("Juan", "Pérez", 1),
            Usuario("Ana", "Martínez", 2),
            Usuario("Luis", "Rodríguez", 3),
            Usuario("María", "López", 4),
            Usuario("Pedro", "González", 5),
            Usuario("Lucía", "Fernández", 6),
            Usuario("José", "García", 7),
            Usuario("Sofía", "Hernández", 8),
            Usuario("Miguel", "Ramírez", 9),
            Usuario("Marta", "Suárez", 10)
        ]
        
        for usuario in usuarios:
            self.registrar_usuario(usuario)

    def crear_tabla_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL
            )
        """)
        self.conexion.commit()

    def crear_usuario(self):
        nombre = self.entry_nuevo_nombre.get()
        apellido = self.entry_nuevo_apellido.get()
        id_usuario = self.entry_nuevo_id.get()

        if id_usuario and nombre and apellido:
            try:
                self.cursor.execute("INSERT INTO usuarios (id, nombre, apellido) VALUES (?, ?, ?)", (id_usuario, nombre, apellido))
                self.conexion.commit()
                messagebox.showinfo("Éxito", "Usuario creado con éxito")
            except sqlite3.IntegrityError:
                messagebox.showerror("Error", "El ID de usuario ya existe")
            except Exception as e:
                messagebox.showerror("Error", f"Error al crear el usuario: {e}")
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios")



    def crear_widgets(self):

        self.label_nuevo_nombre = tk.Label(self, text="Nombre:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_nuevo_nombre.pack(pady=5)
        self.entry_nuevo_nombre = tk.Entry(self)
        self.entry_nuevo_nombre.pack(pady=5)

        self.label_nuevo_apellido = tk.Label(self, text="Apellido:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_nuevo_apellido.pack(pady=5)
        self.entry_nuevo_apellido = tk.Entry(self)
        self.entry_nuevo_apellido.pack(pady=5)

        self.label_nuevo_id = tk.Label(self, text="ID:", bg="light blue", fg="black", font=("Helvetica", 12, "bold"))
        self.label_nuevo_id.pack(pady=5)
        self.entry_nuevo_id = tk.Entry(self)
        self.entry_nuevo_id.pack(pady=5)

        self.btn_confirmar_crear_usuario = tk.Button(self, text="Crear Usuario", command=self.crear_usuario)
        self.btn_confirmar_crear_usuario.pack(pady=5)


class FormularioMaestroDesign(tk.Tk):
    def __init__(self):
        super().__init__()
        self.withdraw()  # Ocultar la ventana principal al inicio
        LoginWindow(self)
        self.logo = util_img.leer_imagen("./imagenes/icono.png", (460, 336))
        self.perfil = util_img.leer_imagen("./imagenes/user.png", (100, 100))
        self.img_sitio_construccion = util_img.leer_imagen("./imagenes/sitio_construccion.png", (200, 200))
        self.config_window()
        self.paneles()
        self.controles_barra_superior()        
        self.controles_menu_lateral()
        self.controles_cuerpo()

        self.prestamos = []
        self.usuarios = []
        self.libros = []

        self.conexion = sqlite3.connect("usuario.db")
        self.cursor = self.conexion.cursor()
        self.crear_tabla_usuarios()
        self.biblioteca = Biblioteca()
        usuarios = [
            Usuario("Juan", "Pérez", 1),
            Usuario("Ana", "Martínez", 2),
            Usuario("Luis", "Rodríguez", 3),
            Usuario("María", "López", 4),
            Usuario("Pedro", "González", 5),
            Usuario("Lucía", "Fernández", 6),
            Usuario("José", "García", 7),
            Usuario("Sofía", "Hernández", 8),
            Usuario("Miguel", "Ramírez", 9),
            Usuario("Marta", "Suárez", 10)
        ]
        
        for usuario in usuarios:
            self.registrar_usuario(usuario)

        autores = [
            Autor("Gabriel", "García Márquez"),
            Autor("Isabel", "Allende"),
            Autor("Julio", "Cortázar"),
            Autor("Antoine","de Saint-Exupéry")
        ]

        categorias = [
            Categoria("Novela"),
            Categoria("Ficción"),
            Categoria("Cuento")
        ]

        libros = [
            Libro("Cien años de soledad", "978-3-16-148410-0", autores[0], categorias[0]),
            Libro("La casa de los espíritus", "978-0-14-303996-9", autores[1], categorias[1]),
            Libro("Rayuela", "978-0-394-70691-5", autores[2], categorias[2]),
            Libro("El Principito", "978-7-13-131226-5", autores[3], categorias[0])
        ]

        for libro in libros:
            self.biblioteca.registrar_libro(libro)

        prestamos = [
            Prestamo(libros[0], usuarios[0], "2024-05-01", "2024-06-01"),
            Prestamo(libros[1], usuarios[1], "2024-05-02", "2024-06-02"),
            Prestamo(libros[2], usuarios[2], "2024-05-03", "2024-06-03"),
        ]

        for prestamo in prestamos:
            self.biblioteca.realizar_prestamo(prestamo)
            self.prestamos.append(prestamo)

    def crear_tabla_usuarios(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL
            )
        """)
        self.conexion.commit()

    def registrar_usuario(self, usuario):
        self.cursor.execute("INSERT OR IGNORE INTO usuarios (id, nombre, apellido) VALUES (?, ?, ?)", 
                            (usuario.get_id_user(), usuario.get_nombre(), usuario.get_apellido()))
        self.conexion.commit()

    def show_main_window(self):
        self.deiconify()  # Mostrar la ventana principal

    def config_window(self):
        # Configuración inicial de la ventana
        self.title('Biblioteca')
        self.iconbitmap("./imagenes/unip.ico")
        w, h = 1024, 600        
        util_ventana.centrar_ventana(self, w, h)        

    def paneles(self):        
         # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(
            self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Menú")
        self.labelTitulo.config(fg="#000000", font=(
            "Roboto", 15), bg=COLOR_BARRA_SUPERIOR, pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg=COLOR_BARRA_SUPERIOR, fg="black")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelTitulo = tk.Label(
            self.barra_superior, text="correo@unipamplona.edu.co")
        self.labelTitulo.config(fg="#000000", font=(
            "Roboto", 10), bg=COLOR_BARRA_SUPERIOR, padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
         # Etiqueta de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        
        self.buttonlibro= tk.Button(self.menu_lateral)        
        self.buttonprestamo = tk.Button(self.menu_lateral)        
        self.buttonrealizarprest = tk.Button(self.menu_lateral)
        self.buttondevolucion = tk.Button(self.menu_lateral)        
        self.buttonSettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Libros", "📚", self.buttonlibro,self.mostrar_libros),
            ("Préstamos", "📖", self.buttonprestamo,self.mostrar_prestamos),
            ("Realizar préstamo", "📝", self.buttonrealizarprest,self.realizar_prestamo),
            ("Devolución", "🔙", self.buttondevolucion,self.devolucion),
            ("Salir", "📤", self.buttonSettings,self.destroy)
        ]

        for text, icon, button,comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu,comando)                    
          

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        logo_image = Image.open("./imagenes/unip.png")
        logo_image = logo_image.resize((360, 336), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo_image)

        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg=COLOR_CUERPO_PRINCIPAL)
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg=COLOR_MENU_LATERAL, fg="black", width=ancho_menu, height=alto_menu,
                      command = comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg=COLOR_MENU_CURSOR_ENCIMA)

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg=COLOR_MENU_LATERAL)

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def mostrar_libros(self):
        self.limpiar_cuerpo()
        cuadro_texto = tk.Text(self.cuerpo_principal, wrap="word", width=250, height=200)
        cuadro_texto.pack(padx=30, pady=30)

        for libro in self.biblioteca._libros:
            info_libro = f"Título: {libro.get_titulo()}\nISBN: {libro.get_isbn()}\nAutor: {libro.get_autor().get_nombre()} {libro.get_autor().get_apellido()}\nCategoría: {libro.get_categoria().get_nombre()}\n\n"
            cuadro_texto.insert(tk.END, info_libro)
        
        cuadro_texto.config(state=tk.DISABLED)


    def mostrar_prestamos(self):
        self.limpiar_cuerpo()
        cuadro_texto = tk.Text(self.cuerpo_principal, wrap="word", width=150, height=150)
        cuadro_texto.pack(padx=30, pady=30)

        for prestamo in self.biblioteca._prestamos:
            info_prestamo = f"Libro: {prestamo.get_libro().get_titulo()}\nUsuario: {prestamo.get_usuario().get_nombre()} {prestamo.get_usuario().get_apellido()}\nFecha Préstamo: {prestamo.get_fecha_prestamo()}\nFecha de Devolución: {prestamo.get_fecha_devolucion()}\n\n" 
            cuadro_texto.insert(tk.END, info_prestamo)            
        
        cuadro_texto.config(state=tk.DISABLED)

    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def realizar_prestamo(self):
        self.limpiar_cuerpo()

        def confirmar_prestamo():
            titulo = self.entry_libro_titulo.get()
            usuario_id = self.entry_usuario_id.get()
            fecha_devolucion = self.entry_fecha_devolucion.get()

            libro = self.biblioteca.buscar_libro_por_titulo(titulo)
            if not libro:
                messagebox.showerror("Error", "Libro no encontrado")
                return

            if self.biblioteca.libro_esta_prestado(libro):
                messagebox.showerror("Error", "El libro ya está prestado")
                return

            self.cursor.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,))
            usuario = self.cursor.fetchone()
            if not usuario:
                messagebox.showerror("Error", "Usuario no encontrado")
                return

            fecha_prestamo = datetime.datetime.now().strftime("%Y-%m-%d")
            nuevo_prestamo = Prestamo(libro, usuario, fecha_prestamo, fecha_devolucion)
            self.biblioteca.realizar_prestamo(nuevo_prestamo)
            messagebox.showinfo("Éxito", "Préstamo realizado con éxito")
            self.prestamos.append(nuevo_prestamo)
            self.mostrar_prestamos()


        label_titulo = tk.Label(self.cuerpo_principal, text="Ingrese su ID y el nombre del libro que necesita", font=("Helvetica", 16), bg=COLOR_CUERPO_PRINCIPAL)
        label_titulo.pack(pady=10)

        # Campos de entrada

        self.label_usuario_id = tk.Label(self.cuerpo_principal, text="ID Usuario:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_usuario_id.pack(pady=5)
        self.entry_usuario_id = tk.Entry(self.cuerpo_principal)
        self.entry_usuario_id.pack(pady=5)

        self.label_libro_titulo = tk.Label(self.cuerpo_principal, text="Título del Libro:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_libro_titulo.pack(pady=5)
        self.entry_libro_titulo = tk.Entry(self.cuerpo_principal)
        self.entry_libro_titulo.pack(pady=5)

        self.label_fecha_devolucion = tk.Label(self.cuerpo_principal, text="Fecha de devolución (YYYY-MM-DD):", bg=COLOR_CUERPO_PRINCIPAL, fg="black", font=("Helvetica", 12,))
        self.label_fecha_devolucion.pack(pady=5)
        self.entry_fecha_devolucion = tk.Entry(self.cuerpo_principal)
        self.entry_fecha_devolucion.pack(pady=5)

        # Botón para confirmar el préstamo
        self.btn_confirmar_prestamo = tk.Button(self.cuerpo_principal, text="Confirmar Préstamo", command=confirmar_prestamo)
        self.btn_confirmar_prestamo.pack(pady=10)
        

    def devolucion(self):
        self.limpiar_cuerpo()
        def devolver():
            usuario_id = self.entry_usuario_id.get()
            titulo = self.entry_libro_titulo.get()

            libro = self.biblioteca.buscar_libro_por_titulo(titulo)
            if not libro:
                messagebox.showerror("Error", "Libro no encontrado")
                return
            if not self.biblioteca.libro_esta_prestado(libro):
                messagebox.showerror("Error", "El libro no está prestado")
                return

            self.cursor.execute('SELECT * FROM usuarios WHERE id = ?', (usuario_id,))
            usuario = self.cursor.fetchone()
            if not usuario:
                messagebox.showerror("Error", "Usuario no encontrado")
                return
            
            self.biblioteca.devolver_libro(libro, usuario)
            messagebox.showinfo("Éxito", "Devolución realizada con éxito")
        

            
        label_titulo = tk.Label(self.cuerpo_principal, text="Ingrese su ID y el nombre del libro que desea devolver", font=("Helvetica", 16), bg=COLOR_CUERPO_PRINCIPAL)
        label_titulo.pack(pady=10)

        # Campos de entrada

        self.label_usuario_id = tk.Label(self.cuerpo_principal, text="ID Usuario:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_usuario_id.pack(pady=5)
        self.entry_usuario_id = tk.Entry(self.cuerpo_principal)
        self.entry_usuario_id.pack(pady=5)

        self.label_libro_titulo = tk.Label(self.cuerpo_principal, text="Título del Libro:", font=("Helvetica", 12), bg=COLOR_CUERPO_PRINCIPAL)
        self.label_libro_titulo.pack(pady=5)
        self.entry_libro_titulo = tk.Entry(self.cuerpo_principal)
        self.entry_libro_titulo.pack(pady=5)


        # Botón para confirmar el préstamo
        self.btn_confirmar_prestamo = tk.Button(self.cuerpo_principal, text="Confirmar Devolución", command=devolver)
        self.btn_confirmar_prestamo.pack(pady=10)    
       