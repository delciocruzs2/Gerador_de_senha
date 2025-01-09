__version__ = "1.0.0"

import customtkinter as ctk
import win32com.client as win32
from PIL import Image
import pyperclip
import random

class App():
    """
    O aplicativo retorna senhas seguras, com a personalização escolhida pelo usuário. 
    """

    def __init__(self) -> object:
        self.raiz = ctk.CTk()
        self._configInterface()
        self.color_system()
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
        self.raiz.resizable(False,False)
        self.raiz.iconbitmap("imagens/main.ico")
        self.raiz._set_appearance_mode('light')
    
    def color_system(self) -> None:
        """ Cores usadas no sistema"""
        self.medium_gray = "#888888"
        self.dark_gray = "#A9A9A9"

    def frame_widgets(self) :
        """ Serviços de interface - Frame e checkboxs de escolhas do usuário """
        # Frame inicial de widgets
        self.frame_inicial = ctk.CTkFrame(master=self.raiz,
                                          corner_radius=0,
                                          border_color=self.dark_gray,
                                          fg_color="#D3D3D3",
                                          border_width=1)
        self.frame_inicial.place(relx=0.54, rely=0.1, relwidth=0.41, relheight=0.8)

        # Checkbox numeros
        self.VarCKB_numeros = ctk.CTkCheckBox(master=self.frame_inicial,
                                              border_color= self.medium_gray,
                                              text_color=self.medium_gray,
                                              border_width=2,  
                                              text="Numeros",                                 
                                              onvalue="on",
                                              offvalue="off")
        self.VarCKB_numeros.place(relx=0.17, rely=0.1, relwidth=0.5, relheight=0.2)

        # Checkbox simbolos
        self.VarCKB_simbolos = ctk.CTkCheckBox(master=self.frame_inicial,
                                               text_color=self.medium_gray,
                                               text="Simbolos",
                                               border_width=2,
                                               border_color=self.medium_gray, 
                                               onvalue="on",
                                               offvalue="off")
        self.VarCKB_simbolos.place(relx=0.17, rely=0.25, relwidth=0.5, relheight=0.2)

        # Checkbox Maiusculas
        self.VarCKB_maiusculas = ctk.CTkCheckBox(master=self.frame_inicial,
                                                 text_color=self.medium_gray,
                                                 text="Maiusculas",
                                                 border_width=2,
                                                 border_color=self.medium_gray, 
                                                 onvalue="on",
                                                 offvalue="off")
        self.VarCKB_maiusculas.place(relx=0.17, rely=0.4, relwidth=0.5, relheight=0.2)

        # Checkbox minusculas
        self.VarCKB_minusculas = ctk.CTkCheckBox(master=self.frame_inicial,
                                                 text_color=self.medium_gray,
                                                 text="Minusculas",
                                                 border_width=2,
                                                 border_color=self.medium_gray, 
                                                 onvalue="on",
                                                 offvalue="off")
        self.VarCKB_minusculas.place(relx=0.17, rely=0.55, relwidth=0.5, relheight=0.2)

        # Menu de opçoes para tamanho da senha
        self.menu_opcao = ctk.CTkOptionMenu(master=self.frame_inicial,
                                            fg_color= self.medium_gray,
                                            values=["4","5","6","7","8","9","10","11","12"])
        self.menu_opcao.place(relx=0.12, rely=0.75, relwidth=0.25, relheight=0.13)
        
        self.Label_menu_opcao = ctk.CTkLabel(master=self.frame_inicial,
                                             text_color=self.medium_gray,
                                             text="Tamanho da senha")
        self.Label_menu_opcao.place(relx=0.4, rely=0.75, relwidth=0.47, relheight=0.13)
    
    def frame_resultado(self) -> str:
        "Frame de saída do resultado"
        self.frame_local = ctk.CTkFrame(master=self.raiz,
                                        corner_radius=0,
                                        border_color=self.dark_gray,
                                        fg_color="#D3D3D3",
                                        border_width=1)
        self.frame_local.place(relx=0.07, rely=0.1, relwidth=0.4, relheight=0.28)

    def gerar_senha(self) -> (None | str):
        """ Labels, condicionais e estruturas para gerar a senha.
            Mapeamento do codigo:
                Limpa tela |
                Coleta e especificação requisitados na interface |
                Especificação de tuplas para fornecer dados ás condicionais |
                Condicional sem requisitos |
                Condicional - Numeros |
                Condicional - Simbolos |
                Condicional - Maiusculas |
                Condicional - Minusculas |
                Condicional - Numeros + simbolos |
                Condicional - Numeros + maiusculas |
                Condicional - Numeros + minusculas |
                Condicional - Numeros + simbolos + maiusculas |
                Condicional - Numeros + maiusculas + minusculas |
                Condicional - Simbolos + maiusculas + minusculas |
                Condicional - Simbolos + maiusculas |
                Condicional - Simbolos +  minusculas |
                Condicional - Maiusculas + minusculas |
                Condicional - Numeros + simbolos + maiusculas + minusculas |
                Resposta apresentada na interface
        """
        
        # Limpa tela
        self.label_resposta = ctk.CTkLabel(self.frame_local,
                                           text=" \t\t\t  ")
        self.label_resposta.place(relx=0.17 ,rely=0.35)

        # Coleta e especificação requisitados na interface
        self.valor_numeros = self.VarCKB_numeros.get()
        self.valor_simbolos = self.VarCKB_simbolos.get()
        self.valor_maiusculas = self.VarCKB_maiusculas.get()
        self.valor_minusculas = self.VarCKB_minusculas.get()
        self.valor_tamanho = self.menu_opcao.get()
        self.valor_convertido_tamanho = int(self.valor_tamanho)
        limitador = 0

    # Especificação de tuplas para fornecer dados ás condicionais
        tupla_numeros = (1,2,3,4,5,6,7,8,9)
        tupla_simbolos = ("@","#","$","%","!")
        tupla_maiusculas = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
        tupla_minusculas = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")
        tupla_numeros_simbolos = (tupla_numeros + tupla_simbolos) 
        tupla_numeros_maiusculas = (tupla_numeros + tupla_maiusculas)
        tupla_numeros_minusculas = (tupla_numeros + tupla_minusculas)
        tupla_numeros_simbolos_maiusculas = (tupla_numeros + tupla_simbolos + tupla_maiusculas)
        tupla_numeros_maiusculas_minusculas = (tupla_numeros + tupla_maiusculas + tupla_minusculas)
        tupla_simbolos_maiusculas_minusculas = (tupla_simbolos + tupla_maiusculas + tupla_minusculas)
        tupla_simbolos_maiusculas = (tupla_simbolos + tupla_maiusculas)
        tupla_simbolos_minusculas = (tupla_simbolos + tupla_minusculas)
        tupla_maiusculas_minusculas = (tupla_maiusculas + tupla_minusculas)
        tupla_total = (tupla_numeros + tupla_simbolos + tupla_maiusculas + tupla_minusculas)
        
        self.lista_resposta = []

        # Condicionais de senhas
        # Condicional sem requisitos
        if self.valor_numeros == "off" and self.valor_simbolos == "off" and self.valor_maiusculas == "off" and self.valor_minusculas == "off":
            self.resultado_final = "Sem requisitos"

        # Condicional - Numeros 
        elif self.valor_numeros == "on" and self.valor_simbolos == "off" and self.valor_maiusculas == "off" and self.valor_minusculas == "off":
            while limitador < self.valor_convertido_tamanho:
                numero = random.choice(tupla_numeros)
                self.lista_resposta.append(numero)
                limitador +=1
            
            self.resultado_final = "" .join(str(num) for num in self.lista_resposta)
        
        # Condicional - Simbolos 
        elif self.valor_numeros == "off" and self.valor_simbolos == "on" and self.valor_maiusculas == "off" and self.valor_minusculas == "off":
            while limitador < self.valor_convertido_tamanho:
                simbolo = random.choice(tupla_simbolos)
                self.lista_resposta.append(simbolo)
                limitador +=1
            
            self.resultado_final = "" .join(self.lista_resposta)

        # Condicional - maiusculas 
        elif self.valor_numeros == "off" and self.valor_simbolos == "off" and self.valor_maiusculas == "on" and self.valor_minusculas == "off":
            while limitador < self.valor_convertido_tamanho:
                maiuscula = random.choice(tupla_maiusculas)
                self.lista_resposta.append(maiuscula)
                limitador +=1
            
            self.resultado_final = "" .join(self.lista_resposta)
        
        # Condicional - minuscula 
        elif self.valor_numeros == "off" and self.valor_simbolos == "off" and self.valor_maiusculas == "off" and self.valor_minusculas == "on":
            while limitador < self.valor_convertido_tamanho:
                minuscula = random.choice(tupla_minusculas)
                self.lista_resposta.append(minuscula)
                limitador +=1
            
            self.resultado_final = "" .join(self.lista_resposta)
        
        # Condicional - Numeros + simbolos
        elif self.valor_numeros == "on" and self.valor_simbolos == "on" and self.valor_maiusculas == "off" and self.valor_minusculas == "off":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_numeros_simbolos)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(str(variavel) for variavel in self.lista_resposta)

        # Condicional - Numeros + maiusculas
        elif self.valor_numeros == "on" and self.valor_simbolos == "off" and self.valor_maiusculas == "on" and self.valor_minusculas == "off":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_numeros_maiusculas)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(str(variavel) for variavel in self.lista_resposta)

        # Condicional - Numeros + minusculas
        elif self.valor_numeros == "on" and self.valor_simbolos == "off" and self.valor_maiusculas == "off" and self.valor_minusculas == "on":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_numeros_minusculas)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(str(variavel) for variavel in self.lista_resposta)

        # Condicional - Numeros + simbolos + maiusculas
        elif self.valor_numeros == "on" and self.valor_simbolos == "on" and self.valor_maiusculas == "on" and self.valor_minusculas == "off":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_numeros_simbolos_maiusculas)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(str(variavel) for variavel in self.lista_resposta)

        # Condicional - Numeros + maiusculas + minusculas
        elif self.valor_numeros == "on" and self.valor_simbolos == "off" and self.valor_maiusculas == "on" and self.valor_minusculas == "on":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_numeros_maiusculas_minusculas)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(str(variavel) for variavel in self.lista_resposta)

        # Condicional - Simbolos + maiusculas + minusculas
        elif self.valor_numeros == "off" and self.valor_simbolos == "on" and self.valor_maiusculas == "on" and self.valor_minusculas == "on":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_simbolos_maiusculas_minusculas)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(self.lista_resposta)

        # Condicional - Simbolos + maiusculas
        elif self.valor_numeros == "off" and self.valor_simbolos == "on" and self.valor_maiusculas == "on" and self.valor_minusculas == "off":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_simbolos_maiusculas)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(self.lista_resposta)

        # Condicional - Simbolos +  minusculas
        elif self.valor_numeros == "off" and self.valor_simbolos == "on" and self.valor_maiusculas == "off" and self.valor_minusculas == "on":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_simbolos_minusculas)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(self.lista_resposta)

        # Condicional - Maiusculas + minusculas
        elif self.valor_numeros == "off" and self.valor_simbolos == "off" and self.valor_maiusculas == "on" and self.valor_minusculas == "on":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_maiusculas_minusculas)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(self.lista_resposta)

        # Condicional - Numeros + simbolos + maiusculas + minusculas
        elif self.valor_numeros == "on" and self.valor_simbolos == "on" and self.valor_maiusculas == "on" and self.valor_minusculas == "on":
            while limitador < self.valor_convertido_tamanho:
                variavel = random.choice(tupla_total)
                self.lista_resposta.append(variavel)
                limitador +=1
            
            self.resultado_final = "" .join(str(variavel) for variavel in self.lista_resposta)
    
        # Resposta apresentada na interface  
        self.label_resposta = ctk.CTkLabel(self.frame_local,
                                           text_color='black',
                                           text=f"{self.resultado_final}")
        self.label_resposta.place(relx=0.3 ,rely=0.35)
    
    def botao_requisitar_senha(self) -> None:
        """ Botão chama o metodo gerar senha """
        self.imagem_requisitar = ctk.CTkImage(light_image=Image.open("./imagens/cadeado.png"), 
                                              dark_image=Image.open("./imagens/cadeado.png"),
                                              size=(30,25))
        self.btt_requistar = ctk.CTkButton(master=self.raiz,
                                           corner_radius=0,
                                           fg_color="#4169E1",
                                           border_width=1,
                                           border_color=self.dark_gray,
                                           text="Gerar senha segura",
                                           image=self.imagem_requisitar,
                                           command=self.gerar_senha)
        self.btt_requistar.place(relx=0.07, rely=0.55, relwidth=0.4, relheight=0.15)
        
    def _enviar_email(self) -> (str | None):
        """A classe tem a funcionalidade de integrar as contas (Gmail, Hotmail, Outlook) logadas no outlook, para enviar o feedback do usuário 
        ao desenvolvedor. Método | Enviar( ) Configuraçoes nescessarias para enviar email ao desenvolvedor do sistema |
        """
        try:
            _outlook = win32.Dispatch("outlook.application") # Integração python outlook
            _email = _outlook.CreateItem(0) # Instancia no outlook
            self.caixa_dialogo = ctk.CTkInputDialog(title="Feedback",
                                                    text="\nEste sistema é seguro!\nDesde já agradecemos sua colaboração!\nEscreva seu feedback abaixo!")
            feedback = self.caixa_dialogo.get_input()

            if feedback is None or feedback.strip() == "":
                return

            _email.To = "delciocruzoficial@gmail.com"
            _email.Subject = "Feedback - Gerador de senhas"
            _email.Body = f"{feedback}"
            _email.Send()

        except ConnectionError as ce:
            raise Exception(f'Error de conexão com o outlook: {str(ce)}')
        except Exception as e:
            raise Exception(f'Algo inesperado aconteceu: {str(e)}')
    


    def botao_feedback(self):
        """ Botão responsavel pela chamada do feedback"""
        self.imagem_outlook = ctk.CTkImage(light_image=Image.open("./imagens/outlook.png"),
                                           dark_image=Image.open("./imagens/outlook.png"),
                                           size=(35,25))
                                           
        self.btt_feedback = ctk.CTkButton(master=self.raiz,
                                         corner_radius=0,
                                         fg_color="#4169E1",
                                         border_width=1,
                                         border_color="#C0C0C0",
                                         text="Feedback via outlook",
                                         image=self.imagem_outlook,
                                         command= self._enviar_email)
        self.btt_feedback.place(relx=0.07, rely=0.74, relwidth=0.4, relheight=0.15)

    def area_trasnferencia(self) -> str:
        """Copia as senhas geradas para a area de transferencia"""
        if self.resultado_final == None or self.resultado_final == "Sem requisitos":
            return
        else:
            pyperclip.copy(self.resultado_final)

    def botao_areaTrasferencia(self):
        """Botão de copiar para area de transferencia"""
        self.btt_areaTrasferencia = ctk.CTkButton(master=self.raiz,
                                                  fg_color="#D3D3D3",
                                                  border_width=1,
                                                  corner_radius=0,
                                                  border_color=self.dark_gray,
                                                  text_color=self.dark_gray,
                                                  text="Copiar para area de transferencia",
                                                  command= self.area_trasnferencia)
        self.btt_areaTrasferencia.place(relx=0.07, rely=0.4, relwidth=0.4, relheight=0.1)


if __name__ == "__main__":
    App()