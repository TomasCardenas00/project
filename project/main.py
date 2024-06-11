"""
This module contains the Main Class.

Author: Tomás Cardenas Benitez <20221020021> and Juan Jesus Poveda <20202020128>
"""


from SocialMediaFacade import SocialMediaFacade

class Menu:
    """
    This class provides a menu interface for interacting with the social media system.

    Attributes:
        socialmediafacade (SocialMediaFacade): An instance of the SocialMediaFacade class to interact with the social media functionality.

    Methods:
        display_menu: This method displays the initial menu options for login or user creation.
        login: This method prompts the user to log in with their username and password.
        create_user: This method prompts the user to create a new account with the required details.
        show_post_options: This method displays options for viewing or creating posts.
        add_post: This method prompts the user to create a new post of a selected type.
        see_posts: This method allows the user to interact with posts, including liking, commenting, reposting, muting, blocking, reporting posts and users.
    """

    def __init__(self):
        self.socialmediafacade = SocialMediaFacade(username=None,password=None)

    def display_menu(self):
        """
        This method displays the initial menu options for the user to either log in or create a new account.
        """
        print("Bienvenido al sistema de redes sociales!")
        print("1. Iniciar sesión")
        print("2. Crear usuario")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            self.login()
        elif choice == "2":
            self.create_user()
        else:
            print("Opción no válida. Por favor, seleccione 1 o 2.")

    def login(self):
        """
        This method prompts the user to enter their username and password to log in. If successful, shows post options.
        """
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")

        self.socialmediafacade = SocialMediaFacade(username, password)

        if self.socialmediafacade.login():
            print("¡Inicio de sesión exitoso!")
            self.show_post_options(username)
        else:
            print("Inicio de sesión fallido. Verifique su nombre de usuario y contraseña.")
        

    def create_user(self):
        """
        This method prompts the user to enter details to create a new account.
        """
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        bio = input("Ingrese su biografia:  ")
        pfp = input("Ingresa la direccion de tu imagen de usuario: ")
        birthday = input("Ingrese su cumpleaños: ")
        self.socialmediafacade.add_user(username,password,bio,pfp,birthday)
        print("Usuario creado exitosamente.")

    def show_post_options(self,username):
        """
        This method displays options for the logged-in user to either view posts or create a new post.

        Args:
            username (str): The username of the logged-in user.
        """
        print("¿Qué desea hacer?")
        print("1. Ver posts")
        print("2. Crear un nuevo post")
        choice = input("Seleccione una opción: ")

        if choice == "1":
            self.see_posts(username)
        elif choice == "2":
            self.add_post(username)

    def add_post(self,username):
        """
        This method prompts the user to create a new post by selecting the type and entering the relevant details.

        Args:
            username (str): The username of the logged-in user.
        """
        if self.socialmediafacade is None:
            print("Por favor inicie sesión primero.")
            return

        print("Seleccione el tipo de publicación que desea crear:")
        print("1. Publicación de texto")
        print("2. Publicación de imagen")
        print("3. Publicación de video")
        choice = input("Ingrese el número correspondiente al tipo de publicación: ")

        if choice not in ["1", "2", "3"]:
            print("Opción no válida.")
            return

        if choice == "1":
            text = input("Ingrese el texto de la publicación: ")
            post = self.socialmediafacade.create_post(choice, text)
        elif choice == "2":
            image_url = input("Ingrese la URL de la imagen: ")
            caption = input("Ingrese el pie de foto: ")
            text = f"Imagen: {image_url} || Pie de foto:{caption}"
            post = self.socialmediafacade.create_post(choice, text)
        elif choice == "3":
            video_url = input("Ingrese la URL del video: ")
            title = input("Ingrese el título del video: ")
            text = f"Imagen: {video_url} || Titulo:{title}"
            post = self.socialmediafacade.create_post(choice, text)

        self.socialmediafacade.add_post(username, post)
        print("Publicación agregada exitosamente.")


    def see_posts(self,username):
        """
        This method allows the user to view and interact with posts, including liking, commenting, reposting, muting, blocking, and reporting posts and users.

        Args:
            username (str): The username of the logged-in user.
        """
        while True:
            self.socialmediafacade.show_posts()
            new_post = self.socialmediafacade.get_current_post()
            new_username = self.socialmediafacade.get_current_user()
            print("1. Me gusta el post")
            print("2. Comentar en el post")
            print("3. Repostear el post")
            print("4. Silenciar Usuario")
            print("5. Bloquear Usuario")
            print("6. Reportar Post")
            print("7. Reportar usuario")
            print("8. Siguiente post")
            print("9. Salir")
            choice = input("Seleccione una opción: ")
            if choice not in ['1','2','3','4','5','6','7','8','9']:
                print("Opcion no valida")
            elif choice == "1":
                self.socialmediafacade.like_post(new_post)  
            elif choice == "2":
                comment = input("Ingrese el comentario que desea agregar")
                self.socialmediafacade.add_comment(comment)  
            elif choice == "3":
                self.socialmediafacade.repost_post(username,new_username,new_post)
            elif choice == "4":
                self.socialmediafacade.mute_user(username, new_username)
            elif choice == "5":
                self.socialmediafacade.block_user(username, new_username)
            elif choice == "6":
                self.socialmediafacade.report_post(new_post)
            elif choice == "7":
                reason = input("Razon del reporte: ")
                self.socialmediafacade.report_user(new_username, reason)
            elif choice == "9":
                print("Saliendo de la vista de posts...")
                break


menu = Menu()
menu.display_menu()