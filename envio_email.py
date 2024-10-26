import win32com.client as win32
import customtkinter as ctk

class EnviarEmail():
    """A classe tem a funcionalidade de integrar as contas (Gmail, Hotmail, Outlook) logadas no outlook, para enviar o feedback do usuário 
    ao desenvolvedor. Método | Enviar( ) contem as configuraçoes nescessarias para enviar email ao desenvolvedor do sistema |
    """

    def Enviar(self) -> (str | None):
        self._outlook = win32.Dispatch("outlook.application") # Integração python outlook
        self._email = self._outlook.CreateItem(0) # Instancia no outlook
        self.caixa_dialogo = ctk.CTkInputDialog(title="Feedback",
                                                text="\nEste sistema é seguro!\nDesde já agradecemos sua colaboração!\nEscreva seu feedback abaixo!")
        self.feedback = self.caixa_dialogo.get_input()
        self._email.To = "delciocruzoficial@gmail.com"
        self._email.Subject = "Feedback - Gerador de senhas"
        self._email.Body = f"{self.feedback}"
        self._email.Send()