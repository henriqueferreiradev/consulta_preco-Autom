import time
import pyautogui
import keyboard
import threading
import customtkinter as ctk
import os
 

IMAGEM_REFERENCIA = os.path.join(os.path.dirname(__file__), "barra.jpg")

executando = False
atalho_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'TVA.lnk')
EXE_REFERENCIA = atalho_path

if os.path.exists(EXE_REFERENCIA):
    print(f"O arquivo {EXE_REFERENCIA} foi encontrado!")
     
else:
    print(f"Erro: O arquivo {EXE_REFERENCIA} não foi encontrado.")
    
    
sys_login = 'ORCAMENTO'
sys_senha = "123"
sys_code = "07"

def abrir_sistema(): 
    os.startfile(atalho_path)
    time.sleep(10)
    
    pyautogui.write(sys_login)
    pyautogui.press('tab')
    pyautogui.write(sys_senha)
    pyautogui.press('enter')
    time.sleep(0.8)
    pyautogui.press('enter')
    print('logou')
    time.sleep(6)
    
    pyautogui.press('f5')
    pyautogui.write(sys_code)
    pyautogui.press('enter')
    
    
def detectar_tela():
    try:
        localizacao = pyautogui.locateOnScreen(IMAGEM_REFERENCIA, confidence=0.6)
        if localizacao:
            print("Imagem encontrada!", localizacao)
            return True
        else:
            print("Imagem não encontrada!")
            return False
    except pyautogui.ImageNotFoundException:
        print("Erro: Imagem não encontrada.")
        return False

def aguardar_digitacao():
    print("Aguardando digitação...")
    evento = keyboard.read_event()
    if evento.event_type == keyboard.KEY_DOWN:
        print(f"Tecla pressionada: {evento.name}")
        time.sleep(1)
        pyautogui.press('enter')

def fechar_tela():
    pyautogui.press('esc')
    print("Tela fechada!")

def executar_codigo():
    global executando
    executando = True
    abrir_sistema()
    print("Aguardando 5 segundos para trocar de sistema...")
    time.sleep(5) 
    
    while executando:
        if detectar_tela():
            aguardar_digitacao()
            time.sleep(7)
            fechar_tela()
        time.sleep(0.5)

def iniciar():
    thread = threading.Thread(target=executar_codigo)
    thread.daemon = True
    thread.start()

# Criar a interface gráfica
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Automação")
root.geometry("300x150")
root.resizable(False, False)

msg_inicio = ctk.CTkLabel(root, text="Iniciar o script?")
msg_inicio.pack(pady=5)
btn_iniciar = ctk.CTkButton(root, text="Sim", command=iniciar)
btn_iniciar.pack(pady=40)

root.mainloop()
