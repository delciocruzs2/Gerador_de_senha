import customtkinter as ctk

class App():

    def __init__(self):
        self.raiz = ctk.CTk()
        self.configInterface()
        self.raiz.mainloop()

    def configInterface(self):
        self.raiz.title("Gerador de senha segura")
        self.raiz.geometry("556x280")
        self.raiz.resizable(False, False)
        self.raiz.iconbitmap("imagens/main.ico")
        self.raiz._set_appearance_mode("light")



if __name__ == "__main__":
    App()