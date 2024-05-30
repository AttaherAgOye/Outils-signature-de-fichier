import customtkinter as ctk
from PIL import Image, ImageTk

from Fonct_signer_fichier import signer_un_fichier
from Fonct_signer_une_application import signer_une_application
from tkinter import filedialog, messagebox

from Fonct_verifié_signature import verifier_signature

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Examen Securite informatique--Groupe 4")
        self.geometry("900x600")
        window_width = 900
        window_height = 600
        self.geometry(f"{window_width}x{window_height}")

        # Calculer la position pour centrer la fenêtre
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        self.configure(bg="#1c1c1c")  # Fond de la fenêtre
        self.resizable(False, False)

        self.canvas = ctk.CTkCanvas(self, width=800, height=600, bg="#1c1c1c", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        # Charger l'image de fond
        self.image = Image.open("bg.jpg")
        self.image_resized = ImageTk.PhotoImage(self.image.resize((900, 600), Image.LANCZOS))
        self.image_on_canvas = self.canvas.create_image(0, 0, anchor="nw", image=self.image_resized)

        # Ajouter le texte
        self.canvas.create_text(450, 200, text="Bienvenue !", font=("Arial", 25, "bold"), fill="white")
        self.canvas.create_text(450, 280, text="choissez une option. pour plus de détails sur l'utilisation rendez vous sur la page Aide",
                                font=("Arial", 16), fill="white", justify="center")

        # Ajouter les boutons
        self.sign_button = ctk.CTkButton(self, text="Signer un fichier ou une application", command=self.open_sign_options, fg_color="white", bg_color="blue", text_color="black", corner_radius=20, height=30, font=("Arial", 15, "bold"))
        self.verify_button = ctk.CTkButton(self, text="Vérifier une signature", command=self.open_verif_options, fg_color="white", bg_color="blue", text_color="black", corner_radius=20, height=30, font=("Arial", 15, "bold"))
        self.accueil_button = ctk.CTkButton(self, text="Aide", command=self.open_help, fg_color="#cf03fc", bg_color="#16097a", text_color="white", corner_radius=20, height=30, font=("Arial", 15, "bold"))
        # Placer les boutons
        self.canvas.create_window(300, 350, anchor="center", window=self.sign_button)
        self.canvas.create_window(600, 350, anchor="center", window=self.verify_button)
        self.canvas.create_window(800, 40, anchor="center", window=self.accueil_button)
        # Bind resize event
        self.bind("<Configure>", self.resize)

        # Appeler la fonction resize une première fois pour assurer le bon affichage initial
        self.update_idletasks()  # Assure que les dimensions de la fenêtre sont à jour
        self.resize(None)

    def resize(self, event):
        new_width = self.winfo_width()
        new_height = self.winfo_height()

        # Redimensionner l'image
        self.image_resized = ImageTk.PhotoImage(self.image.resize((new_width, new_height), Image.LANCZOS))
        self.canvas.itemconfig(self.image_on_canvas, image=self.image_resized)

        # Redimensionner le canvas
        self.canvas.config(width=new_width, height=new_height)

    sign_window = None
    def open_sign_options(self):
        # Création d'une nouvelle fenêtre pour les options de signature
        self.sign_window = ctk.CTkToplevel(self)
        self.sign_window.title("Options de Signature")
        window_width = 300
        window_height = 200
        self.sign_window.geometry(f"{window_width}x{window_height}")

        # Calculer la position pour centrer la fenêtre
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.sign_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        # Ajouter les boutons dans la nouvelle fenêtre
        sign_file_button = ctk.CTkButton(self.sign_window, text="Signer un fichier", command=self.signF)
        sign_app_button = ctk.CTkButton(self.sign_window, text="Signer une application", command=self.signA)

        # Placer les boutons
        sign_file_button.pack(pady=20)
        sign_app_button.pack(pady=20)
        self.sign_window.focus_force()
        self.sign_window.grab_set()

    def close(obj):   
        obj.destroy()
        
    verif_window = None
    def open_verif_options(self):
        # Création d'une nouvelle fenêtre pour les options de signature
        self.verif_window = ctk.CTkToplevel(self)
        self.verif_window.title("Options de Signature")
        self.verif_window.geometry("300x100")
        window_width = 300
        window_height = 100
        self.verif_window.geometry(f"{window_width}x{window_height}")

        # Calculer la position pour centrer la fenêtre
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.verif_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        # Ajouter les boutons dans la nouvelle fenêtre
        txt = ctk.CTkLabel(self.verif_window, text=" Chargez le fichier à vérifier")
        sign_file_button = ctk.CTkButton(self.verif_window, text="Charger", command=self.verif_sign)

        # Placer les boutons
        txt.pack()
        sign_file_button.pack(pady=20)
        txt
        self.verif_window.focus_force()
        self.verif_window.grab_set()

    chemin_de_apply=""

    def open_validate(self):
        # Création d'une nouvelle fenêtre pour les options de signature
        self.sign_window = ctk.CTkToplevel(self)
        self.sign_window.title("Options de Signature")

        window_width = 400
        window_height = 150
        self.sign_window.geometry(f"{window_width}x{window_height}")

        # Calculer la position pour centrer la fenêtre
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.sign_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        # Ajouter les boutons dans la nouvelle fenêtre
        txt = ctk.CTkLabel(self.sign_window, text=" Vous avez charger le fichier:\n"+ self.chemin_de_apply)
        sign_file_button = ctk.CTkButton(self.sign_window, text="Commencer", command=self.verif_sign_back)

        # Placer les boutons
        txt.pack()
        sign_file_button.pack(pady=20)
        close_button = ctk.CTkButton(
            self.sign_window, 
            text="Fermer", 
            command=self.sign_window.destroy
        )
        close_button.pack()

        self.sign_window.focus_force()
        self.sign_window.grab_set()
    def open_validate_sign_file(self):
        # Création d'une nouvelle fenêtre pour les options de signature
        self.signe_window = ctk.CTkToplevel(self)
        self.signe_window.title("Options de Signature")
        self.signe_window.geometry("400x150")

        window_width = 400
        window_height = 150
        self.signe_window.geometry(f"{window_width}x{window_height}")

        # Calculer la position pour centrer la fenêtre
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.signe_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        # Ajouter les boutons dans la nouvelle fenêtre
        txt = ctk.CTkLabel(self.signe_window, text=" Vous avez charger le fichier:\n"+ self.chemin_de_apply)
        sign_file_button = ctk.CTkButton(self.signe_window, text="Commencer", command=self.sign_file)

        # Placer les boutons
        txt.pack()
        sign_file_button.pack(pady=20)
        close_button = ctk.CTkButton(
            self.signe_window, 
            text="Fermer", 
            command=self.signe_window.destroy
        )
        close_button.pack()

        self.signe_window.focus_force()
        self.signe_window.grab_set()

    def open_validate_sign_app(self):
        # Création d'une nouvelle fenêtre pour les options de signature
        self.signe_window = ctk.CTkToplevel(self)
        self.signe_window.title("Options de Signature")
        self.signe_window.geometry("400x150")

        window_width = 400
        window_height = 150
        self.signe_window.geometry(f"{window_width}x{window_height}")

        # Calculer la position pour centrer la fenêtre
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.signe_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        # Ajouter les boutons dans la nouvelle fenêtre
        txt = ctk.CTkLabel(self.signe_window, text=" Vous avez charger l'application:\n"+ self.chemin_de_apply)
        sign_file_button = ctk.CTkButton(self.signe_window, text="Commencer", command=self.sign_app)

        # Placer les boutons
        txt.pack()
        sign_file_button.pack(pady=20)
        close_button = ctk.CTkButton(
            self.signe_window, 
            text="Fermer", 
            command=self.signe_window.destroy
        )
        close_button.pack()

        self.sign_window.focus_force()
        self.sign_window.grab_set()

    def open_help(self):
        # Création d'une nouvelle fenêtre pour l'aide
        self.help_window = ctk.CTkToplevel(self)
        self.help_window.title("Aide")
        window_width = 600
        window_height = 500
        self.help_window.geometry(f"{window_width}x{window_height}")

        # Calculer la position pour centrer la fenêtre
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)
        self.help_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
        # Style et contenu pour la fenêtre d'aide
        help_title = ctk.CTkLabel(
            self.help_window, 
            text="Guide d'utilisation de l'application", 
            font=("Arial", 24, "bold"),
            pady=10
        )
        help_title.pack()

        help_text = (
            "Bienvenue dans la section d'aide !\n\n"
            "Cette application vous permet de signer des fichiers et des applications, "
            "ainsi que de vérifier des signatures.\n\n"
            "Fonctionnalités disponibles :\n"
            "1. **Signer un fichier ou une application**\n"
            "   - Cliquez sur le bouton 'Signer un fichier ou une application'.\n"
            "   - Dans la nouvelle fenêtre, choisissez l'option 'Signer un fichier' ou 'Signer une application'.\n"
            "   - Suivez les instructions pour sélectionner le fichier ou l'application à signer.\n\n"
            "2. **Vérifier une signature**\n"
            "   - Cliquez sur le bouton 'Vérifier une signature'.\n"
            "   - Suivez les instructions pour sélectionner le fichier dont vous souhaitez vérifier la signature.\n\n"
            "Conseils et astuces :\n"
            "- Assurez-vous que les fichiers que vous souhaitez signer ou vérifier sont accessibles depuis votre ordinateur.\n"
            "- Si vous rencontrez des problèmes, essayez de redémarrer l'application.\n\n"
            "Nous espérons que cette application répondra à vos attentes. Merci de l'utiliser !"
        )

        help_label = ctk.CTkLabel(
            self.help_window, 
            text=help_text, 
            justify="left",
            wraplength=550,
            pady=10,
            padx=20
        )
        help_label.pack()

        # Ajouter un bouton de fermeture
        close_button = ctk.CTkButton(
            self.help_window, 
            text="Fermer", 
            command=self.help_window.destroy
        )
        close_button.pack(pady=20)

        # Mettre la nouvelle fenêtre au premier plan
        self.help_window.focus_force()
        self.help_window.grab_set()

    def sign_file(self):
        print("Option Signer un fichier sélectionnée")
        signer_un_fichier(self.chemin_de_apply)

    def sign_app(self):
        print("Option Signer une application sélectionnée")
        signer_une_application(self.chemin_de_apply)
    def verif_sign_back(self):
        print("Option Signer une application sélectionnée")
        verifier_signature(self.chemin_de_apply)
    def verif_sign(self):
        self.chemin_de_apply = filedialog.askopenfilename()
        self.open_validate()
        self.verif_window.destroy()
    def signF(self):
        self.chemin_de_apply = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
        self.open_validate_sign_file()
        self.sign_window.destroy()
    def signA(self):
        self.chemin_de_apply = filedialog.askopenfilename(filetypes=[("All Files", "*.*"), ("Executable Files", "*.exe *.msi *.sh *.apk *.deb *.rpm *.jar *.dmg")])
        self.open_validate_sign_app()
        self.sign_window.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
