import customtkinter as ctk
from PIL import Image

class App():

    def __init__(self):
        self.raiz = ctk.CTk()
        self._configInterface()
        self.frame_widgets()
        self.frame_resultado()
        self.botao_requisitar_senha()
        self.botao_feedback()
        self.raiz.mainloop()

    def _configInterface(self):
        "Configuraçoes de personalização da tela principal"
        self.raiz.title("Gerador de senha segura")
        self.raiz.geometry("556x280")
        self.raiz.resizable(False, False)
        self.raiz.iconbitmap("imagens/main.ico")
        self.raiz._set_appearance_mode("light")

    def frame_widgets(self):
        "Frame com checkbox contendo as escolhas do usuário"
        self.frame_inicial = ctk.CTkFrame(master=self.raiz, border_width=1)
        self.frame_inicial.place(relx=0.54, rely=0.1, relwidth=0.41, relheight=0.8)
    
    def frame_resultado(self) -> str:
        "Frame de saída do resultado"
        self.frame_local = ctk.CTkFrame(master=self.raiz, border_width=1)
        self.frame_local.place(relx=0.07, rely=0.1, relwidth=0.4, relheight=0.28)
    
    def botao_requisitar_senha(self):
        self.imagem_requisitar = ctk.CTkImage(light_image=Image.open("./imagens/cadeado.png"), 
                                            dark_image=Image.open("./imagens/cadeado.png"),
                                            size=(30,25))
        self.btt_requistar = ctk.CTkButton(master=self.raiz,
                                        fg_color="#4169E1",
                                        border_width=1,
                                        border_color="#A9A9A9",
                                        text="Gerar senha",
                                        image=self.imagem_requisitar)
        self.btt_requistar.place(relx=0.07, rely=0.53, relwidth=0.4, relheight=0.15)

    def botao_feedback(self):
        self.imagem_outlook = ctk.CTkImage(light_image=Image.open("./imagens/outlook.png"),
                                        dark_image=Image.open("./imagens/outlook.png"),
                                        size=(35,25))
        self.btt_feedback = ctk.CTkButton(master=self.raiz,
                                        fg_color="#4169E1",
                                        border_width=1,
                                        border_color="#C0C0C0",
                                        text="Feedback",
                                        image=self.imagem_outlook)
        self.btt_feedback.place(relx=0.07, rely=0.74, relwidth=0.4, relheight=0.15)

if __name__ == "__main__":
    App()