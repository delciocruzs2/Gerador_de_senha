__version__ = "1.0.0"

import customtkinter as ctk
from PIL import Image
from envio_email import EnviarEmail
import pyperclip



class App():

    def __init__(self):
        self.raiz = ctk.CTk()
        self.SistemaEnviar = EnviarEmail() #instancia de EnviarEmail
        self._configInterface()
        self.frame_widgets()
        self.frame_resultado()
        self.resultado_final = None
        self.botao_requisitar_senha()
        self.botao_feedback()
        self.botao_areaTrasferencia()
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

        # checkbox numeros
        self.VarCKB_numeros = ctk.CTkCheckBox(master=self.frame_inicial,
                                            text="Numeros",
                                            border_width=2,
                                            border_color="#888888",                                   
                                            onvalue="on",
                                            offvalue="off")
        self.VarCKB_numeros.place(relx=0.17, rely=0.1, relwidth=0.5, relheight=0.2)

        #checkbox simbolos
        self.VarCKB_simbolos = ctk.CTkCheckBox(master=self.frame_inicial,
                                            text="Simbolos",
                                            border_width=2,
                                            border_color="#888888", 
                                            onvalue="on",
                                            offvalue="off")
        self.VarCKB_simbolos.place(relx=0.17, rely=0.25, relwidth=0.5, relheight=0.2)

        #checkbox Maiusculas
        self.VarCKB_maiusculas = ctk.CTkCheckBox(master=self.frame_inicial,
                                            text="Maiusculas",
                                            border_width=2,
                                            border_color="#888888", 
                                            onvalue="on",
                                            offvalue="off")
        self.VarCKB_maiusculas.place(relx=0.17, rely=0.4, relwidth=0.5, relheight=0.2)

        #checkbox minusculas
        self.VarCKB_minusculas = ctk.CTkCheckBox(master=self.frame_inicial,
                                            text="Minusculas",
                                            border_width=2,
                                            border_color="#888888", 
                                            onvalue="on",
                                            offvalue="off")
        self.VarCKB_minusculas.place(relx=0.17, rely=0.55, relwidth=0.5, relheight=0.2)

        #menu de opçoes para tamanho da senha
        self.menu_opcao = ctk.CTkOptionMenu(master=self.frame_inicial,
                                            values=["4","5","6","7","8","9","10","11","12"])
        self.menu_opcao.place(relx=0.12, rely=0.75, relwidth=0.25, relheight=0.13)
        
        self.Label_menu_opcao = ctk.CTkLabel(master=self.frame_inicial,
                                            text="Tamanho da senha")
        self.Label_menu_opcao.place(relx=0.4, rely=0.75, relwidth=0.47, relheight=0.13)
    
    def frame_resultado(self) -> str:
        "Frame de saída do resultado"
        self.frame_local = ctk.CTkFrame(master=self.raiz, border_width=1)
        self.frame_local.place(relx=0.07, rely=0.1, relwidth=0.4, relheight=0.28)

    def gerar_senha(self) -> str:
        self.valor_numeros = self.VarCKB_numeros.get()
        self.valor_simbolos = self.VarCKB_simbolos.get()
        self.valor_maiusculas = self.VarCKB_maiusculas.get()
        self.valor_minusculas = self.VarCKB_minusculas.get()
        self.valor_tamanho = self.menu_opcao.get()
        if self.valor_numeros == "off" and self.valor_simbolos == "off" and self.valor_maiusculas == "off" and self.valor_minusculas == "off":
            self.resultado_final = "Escolha os parametros"
            
        self.label_resposta = ctk.CTkLabel(self.frame_local,
                                               text=f"{self.resultado_final}")
        self.label_resposta.place(relx=0.17 ,rely=0.35)
    
    def botao_requisitar_senha(self):

        self.imagem_requisitar = ctk.CTkImage(light_image=Image.open("./imagens/cadeado.png"), 
                                            dark_image=Image.open("./imagens/cadeado.png"),
                                            size=(30,25))
        self.btt_requistar = ctk.CTkButton(master=self.raiz,
                                        fg_color="#4169E1",
                                        border_width=1,
                                        border_color="#A9A9A9",
                                        text="Gerar senha segura",
                                        image=self.imagem_requisitar,
                                        command=self.gerar_senha)
        self.btt_requistar.place(relx=0.07, rely=0.55, relwidth=0.4, relheight=0.15)
        
    def botao_feedback(self):
        self.imagem_outlook = ctk.CTkImage(light_image=Image.open("./imagens/outlook.png"),
                                        dark_image=Image.open("./imagens/outlook.png"),
                                        size=(35,25))
        self.btt_feedback = ctk.CTkButton(master=self.raiz,
                                        fg_color="#4169E1",
                                        border_width=1,
                                        border_color="#C0C0C0",
                                        text="Feedback via outlook",
                                        image=self.imagem_outlook,
                                        command= self.SistemaEnviar.Enviar)
        self.btt_feedback.place(relx=0.07, rely=0.74, relwidth=0.4, relheight=0.15)

    def area_trasnferencia(self) -> str:
        """Copia as senhas geradas para a area de transferencia"""
        if self.resultado_final == None or self.resultado_final == "Escolha os parametros":
            return
        else:
            pyperclip.copy(self.resultado_final)

    def botao_areaTrasferencia(self):
        """Botão deccopiar para area de transferencia"""
        self.btt_areaTrasferencia = ctk.CTkButton(master=self.raiz,
                                        fg_color="#D3D3D3",
                                        border_width=1,
                                        border_color="#A9A9A9",
                                        text_color="#A9A9A9",
                                        text="Copiar para area de transferencia",
                                        command=self.area_trasnferencia)
        self.btt_areaTrasferencia.place(relx=0.07, rely=0.4, relwidth=0.4, relheight=0.1)


if __name__ == "__main__":
    App()