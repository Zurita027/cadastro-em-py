import tkinter as tk
from tkinter import messagebox
import csv

ARQUIVO = 'dados.csv'
caminhoes = {}

def carregar_dados():
    try:
        with open(ARQUIVO, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                caminhoes[row['placa']] = {
                    "chassi": row['chassi'],
                    "ano_fabricacao": row['ano_fabricacao'],
                    "modelo": row['modelo'],
                    "marca": row['marca'],
                    "pbt": row['pbt'],
                    "capacidade_carga": row['capacidade_carga'],
                    "eixos": row['eixos'],
                    "cor": row['cor'],
                    "proprietario": row['proprietario']
                }
    except FileNotFoundError:
        pass

def salvar_dados():
    with open(ARQUIVO, mode='w', newline='') as file:
        fieldnames = ['placa', 'chassi', 'ano_fabricacao', 'modelo', 'marca', 'pbt', 'capacidade_carga', 'eixos', 'cor', 'proprietario']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for placa, dados in caminhoes.items():
            writer.writerow({
                "placa": placa,
                "chassi": dados['chassi'],
                "ano_fabricacao": dados['ano_fabricacao'],
                "modelo": dados['modelo'],
                "marca": dados['marca'],
                "pbt": dados['pbt'],
                "capacidade_carga": dados['capacidade_carga'],
                "eixos": dados['eixos'],
                "cor": dados['cor'],
                "proprietario": dados['proprietario']
            })

def cadastrar_caminhao():
    def salvar_novo_caminhao():
        placa = placa_entry.get().upper()
        chassi = chassi_entry.get().upper()
        ano_fabricacao = ano_fabricacao_entry.get()
        modelo = modelo_entry.get()
        marca = marca_entry.get()
        pbt = pbt_entry.get()
        capacidade_carga = capacidade_carga_entry.get()
        eixos = eixos_entry.get()
        cor = cor_entry.get()
        proprietario = proprietario_entry.get()

        if not placa or not chassi:
            messagebox.showerror("Erro", "Placa e Chassi são obrigatórios!")
            return

        caminhoes[placa] = {
            "chassi": chassi,
            "ano_fabricacao": ano_fabricacao,
            "modelo": modelo,
            "marca": marca,
            "pbt": pbt,
            "capacidade_carga": capacidade_carga,
            "eixos": eixos,
            "cor": cor,
            "proprietario": proprietario
        }

        salvar_dados()
        messagebox.showinfo("Sucesso", f"Caminhão {placa} cadastrado com sucesso!")
        nova_janela.destroy()

    nova_janela = tk.Toplevel(root)
    nova_janela.title("Cadastrar Caminhão")

    tk.Label(nova_janela, text="Placa:").grid(row=0, column=0, padx=10, pady=5)
    placa_entry = tk.Entry(nova_janela)
    placa_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(nova_janela, text="Chassi:").grid(row=1, column=0, padx=10, pady=5)
    chassi_entry = tk.Entry(nova_janela)
    chassi_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(nova_janela, text="Ano Fabricação:").grid(row=2, column=0, padx=10, pady=5)
    ano_fabricacao_entry = tk.Entry(nova_janela)
    ano_fabricacao_entry.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(nova_janela, text="Modelo:").grid(row=3, column=0, padx=10, pady=5)
    modelo_entry = tk.Entry(nova_janela)
    modelo_entry.grid(row=3, column=1, padx=10, pady=5)

    tk.Label(nova_janela, text="Marca:").grid(row=4, column=0, padx=10, pady=5)
    marca_entry = tk.Entry(nova_janela)
    marca_entry.grid(row=4, column=1, padx=10, pady=5)

    tk.Label(nova_janela, text="PBT (toneladas):").grid(row=5, column=0, padx=10, pady=5)
    pbt_entry = tk.Entry(nova_janela)
    pbt_entry.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(nova_janela, text="Capacidade de Carga (toneladas):").grid(row=6, column=0, padx=10, pady=5)
    capacidade_carga_entry = tk.Entry(nova_janela)
    capacidade_carga_entry.grid(row=6, column=1, padx=10, pady=5)

    tk.Label(nova_janela, text="Número de Eixos:").grid(row=7, column=0, padx=10, pady=5)
    eixos_entry = tk.Entry(nova_janela)
    eixos_entry.grid(row=7, column=1, padx=10, pady=5)

    tk.Label(nova_janela, text="Cor:").grid(row=8, column=0, padx=10, pady=5)
    cor_entry = tk.Entry(nova_janela)
    cor_entry.grid(row=8, column=1, padx=10, pady=5)

    tk.Label(nova_janela, text="Proprietário:").grid(row=9, column=0, padx=10, pady=5)
    proprietario_entry = tk.Entry(nova_janela)
    proprietario_entry.grid(row=9, column=1, padx=10, pady=5)

    tk.Button(nova_janela, text="Salvar", command=salvar_novo_caminhao).grid(row=10, column=0, columnspan=2, pady=20)

def listar_caminhoes():
    listar_janela = tk.Toplevel(root)
    listar_janela.title("Listar Caminhões")

    if not caminhoes:
        tk.Label(listar_janela, text="Nenhum caminhão cadastrado.").pack(pady=10)
        return

    for placa, dados in caminhoes.items():
        info = f"Placa: {placa}, Modelo: {dados['modelo']}, Ano: {dados['ano_fabricacao']}"
        tk.Label(listar_janela, text=info).pack(anchor='w')

def consultar_caminhao():
    def consultar():
        placa = placa_entry.get().upper()
        if placa in caminhoes:
            dados = caminhoes[placa]
            resultado = f"Placa: {placa}\nChassi: {dados['chassi']}\nAno de Fabricação: {dados['ano_fabricacao']}\nModelo: {dados['modelo']}\nMarca: {dados['marca']}\nPBT: {dados['pbt']} toneladas\nCapacidade de Carga: {dados['capacidade_carga']} toneladas\nNúmero de Eixos: {dados['eixos']}\nCor: {dados['cor']}\nProprietário: {dados['proprietario']}"
            messagebox.showinfo("Consulta", resultado)
        else:
            messagebox.showerror("Erro", "Caminhão não encontrado.")
    
    consultar_janela = tk.Toplevel(root)
    consultar_janela.title("Consultar Caminhão")

    tk.Label(consultar_janela, text="Placa do caminhão:").grid(row=0, column=0, padx=10, pady=5)
    placa_entry = tk.Entry(consultar_janela)
    placa_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(consultar_janela, text="Consultar", command=consultar).grid(row=1, column=0, columnspan=2, pady=10)

def excluir_caminhao():
    def excluir():
        placa = placa_entry.get().upper()
        if placa in caminhoes:
            del caminhoes[placa]
            salvar_dados()
            messagebox.showinfo("Exclusão", f"Caminhão {placa} excluído com sucesso!")
            excluir_janela.destroy()
        else:
            messagebox.showerror("Erro", "Caminhão não encontrado.")
    
    excluir_janela = tk.Toplevel(root)
    excluir_janela.title("Excluir Caminhão")

    tk.Label(excluir_janela, text="Placa do caminhão:").grid(row=0, column=0, padx=10, pady=5)
    placa_entry = tk.Entry(excluir_janela)
    placa_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Button(excluir_janela, text="Excluir", command=excluir).grid(row=1, column=0, columnspan=2, pady=10)

root = tk.Tk()
root.title("Sistema de Cadastro de Caminhões")

tk.Button(root, text="Cadastrar Caminhão", width=25, command=cadastrar_caminhao).pack(pady=10)
tk.Button(root, text="Listar Caminhões", width=25, command=listar_caminhoes).pack(pady=10)
tk.Button(root, text="Consultar Caminhão", width=25, command=consultar_caminhao).pack(pady=10)
tk.Button(root, text="Excluir Caminhão", width=25, command=excluir_caminhao).pack(pady=10)

carregar_dados()

root.mainloop()
