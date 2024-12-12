import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox

def gerar_qrcode():
    link = entrada_link.get()
    if not link:
        messagebox.showwarning("Atenção", "Por favor, insira um link.")
        return
    qr = qrcode.make(link)

    pasta = filedialog.askdirectory()
    if pasta:
        caminho_arquivo = f"{pasta}/qrcode.png"
        qr.save(caminho_arquivo)
        messagebox.showinfo("Sucesso", f"QR Code gerado e salvo em '{caminho_arquivo}'")

janela = tk.Tk()
janela.title("Gerador de QR Code")

label = tk.Label(janela, text="Digite o link:")
label.pack(pady=5)
entrada_link = tk.Entry(janela, width=50)
entrada_link.pack(pady=5)

botao = tk.Button(janela, text="Gerar QR Code", command=gerar_qrcode)
botao.pack(pady=10)

janela.mainloop()
