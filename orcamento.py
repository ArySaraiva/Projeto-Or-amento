from tkinter import *
from tkinter import messagebox
from fpdf import FPDF


# Função para capturar e mostrar os valores inseridos
def mostrar_valores():
    try:
        # Captura os valores inseridos
        data = texto_data.get()
        cliente = texto_cliente.get()

        # Manutenção
        quantidade_manutencao = int(manutencao_quantidade.get())
        preco_unitario_manutencao = float(manutencao_preco_unitario.get())
        total_manutencao = quantidade_manutencao * preco_unitario_manutencao

        # Recarga
        quantidade_recarga = int(recarga_quantidade.get())
        preco_unitario_recarga = float(recarga_preco_unitario.get())
        total_recarga = quantidade_recarga * preco_unitario_recarga

        # Peças
        quantidade_pecas = int(pecas_quantidade.get())
        preco_unidade_pecas = float(pecas_preco_unidade.get())
        total_pecas = quantidade_pecas * preco_unidade_pecas

        # Outros Serviços
        quantidade_outros_servicos = int(outros_servicos_quantidade.get())
        preco_unidade_outros_servicos = float(outros_servicos_preco_unidade.get())
        total_outros_servicos = quantidade_outros_servicos * preco_unidade_outros_servicos

        # Soma de todos os totais       
        valor_total = float(total_manutencao + total_recarga + total_pecas + total_outros_servicos)
        texto_total_geral.config(state='normal')
        texto_total_geral.delete(0, END)
        texto_total_geral.insert(0, f"{valor_total:.1f}")
        texto_total_geral.config(state='readonly')


        # Geração do PDF
        gerar_pdf(data, cliente, manutencao_descricao.get(), manutencao_quantidade.get(),
                  manutencao_preco_unitario.get(), total_manutencao,
                  recarga_descricao.get(), recarga_quantidade.get(), recarga_preco_unitario.get(), total_recarga,
                  pecas_descricao.get(), pecas_quantidade.get(), pecas_preco_unidade.get(), total_pecas,
                  outros_servicos_descricao.get(), outros_servicos_quantidade.get(),
                  outros_servicos_preco_unidade.get(), total_outros_servicos, valor_total)
    except ValueError:
        # Mensagem de erro se algum valor não for válido
        messagebox.showerror("Entrada inválida", "Por favor, insira valores numéricos válidos para quantidade e preço.")


def gerar_pdf(data, cliente, manutencao_descricao, manutencao_quantidade, manutencao_preco_unitario, manutencao_total,
              recarga_descricao, recarga_quantidade, recarga_preco_unitario, recarga_total,
              pecas_descricao, pecas_quantidade, pecas_preco_unidade, pecas_total,
              outros_servicos_descricao, outros_servicos_quantidade, outros_servicos_preco_unidade,
              outros_servicos_total, valor_total):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=13)
    pdf.image("logo.png", x=0, y=0)

    pdf.text(30.5, 67.5, data)
    pdf.text(35.5, 74, cliente)
    pdf.text(49, 130, manutencao_descricao)
    pdf.text(145, 130, manutencao_preco_unitario)
    pdf.text(165, 130, manutencao_quantidade)
    pdf.text(180, 130, f"{manutencao_total:.1f}")

    pdf.text(49, 145, recarga_descricao)
    pdf.text(145, 145, recarga_preco_unitario)
    pdf.text(165, 145, recarga_quantidade)
    pdf.text(180, 145, f"{recarga_total:.1f}")

    pdf.text(49, 160, pecas_descricao)
    pdf.text(145, 160, pecas_preco_unidade)
    pdf.text(165, 160, pecas_quantidade)
    pdf.text(180, 160, f"{pecas_total:.1f}")

    pdf.text(49, 175, outros_servicos_descricao)
    pdf.text(145, 175, outros_servicos_preco_unidade)
    pdf.text(165, 175, outros_servicos_quantidade)
    pdf.text(180, 175, f"{outros_servicos_total:.1f}")

    pdf.text(165, 195, f"{valor_total:.1f}")

    pdf.output("OrcamentoASL.pdf")


# Criação da janela principal
janela_orcamento = Tk()
janela_orcamento.title("Orçamento ASL Climatização")
janela_orcamento.geometry("600x700")
janela_orcamento.configure(bg='#f0f0f0')

# Frames
frame_geral = Frame(janela_orcamento, bg='#e0e0e0', padx=10, pady=10)
frame_geral.pack(padx=20, pady=20, fill=BOTH, expand=True)

frame_dados = LabelFrame(frame_geral, text="Data e Cliente", bg='#e0e0e0', padx=10, pady=10)
frame_dados.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

frame_itens = LabelFrame(frame_geral, text="Dados do Orçamento", bg='#e0e0e0', padx=15, pady=15)
frame_itens.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Data
Label(frame_dados, text="Digite uma data", bg='#e0e0e0').grid(column=0, row=0, sticky=W)
texto_data = Entry(frame_dados)
texto_data.grid(column=1, row=0)

# Cliente
Label(frame_dados, text="Nome do cliente", bg='#e0e0e0').grid(column=0, row=1, sticky=W)
texto_cliente = Entry(frame_dados)
texto_cliente.grid(column=1, row=1)

# Manutenção
Label(frame_itens, text="Manutenção descrição:", bg='#e0e0e0').grid(column=0, row=0, sticky=W)
manutencao_descricao = Entry(frame_itens)
manutencao_descricao.grid(column=1, row=0, sticky=W)

Label(frame_itens, text="Manutenção quantidade:", bg='#e0e0e0').grid(column=0, row=1, sticky=W)
manutencao_quantidade = Entry(frame_itens)
manutencao_quantidade.grid(column=1, row=1, sticky=W)

Label(frame_itens, text="Manutenção preço da unidade:", bg='#e0e0e0').grid(column=0, row=2, sticky=W)
manutencao_preco_unitario = Entry(frame_itens)
manutencao_preco_unitario.grid(column=1, row=2, sticky=W)

# Recarga
Label(frame_itens, text="Recarga descrição:", bg='#e0e0e0').grid(column=0, row=4, sticky=W)
recarga_descricao = Entry(frame_itens)
recarga_descricao.grid(column=1, row=4, sticky=W)

Label(frame_itens, text="Recarga quantidade:", bg='#e0e0e0').grid(column=0, row=5, sticky=W)
recarga_quantidade = Entry(frame_itens)
recarga_quantidade.grid(column=1, row=5, sticky=W)

Label(frame_itens, text="Recarga preço da unidade:", bg='#e0e0e0').grid(column=0, row=6, sticky=W)
recarga_preco_unitario = Entry(frame_itens)
recarga_preco_unitario.grid(column=1, row=6, sticky=W)


# Peças
Label(frame_itens, text="Peças descrição:", bg='#e0e0e0').grid(column=0, row=8, sticky=W)
pecas_descricao = Entry(frame_itens)
pecas_descricao.grid(column=1, row=8, sticky=W)

Label(frame_itens, text="Peças quantidade:", bg='#e0e0e0').grid(column=0, row=9, sticky=W)
pecas_quantidade = Entry(frame_itens)
pecas_quantidade.grid(column=1, row=9, sticky=W)

Label(frame_itens, text="Peças preço da unidade:", bg='#e0e0e0').grid(column=0, row=10, sticky=W)
pecas_preco_unidade = Entry(frame_itens)
pecas_preco_unidade.grid(column=1, row=10, sticky=W)


# Outros Serviços
Label(frame_itens, text="Outros serviços descrição:", bg='#e0e0e0').grid(column=0, row=12, sticky=W)
outros_servicos_descricao = Entry(frame_itens)
outros_servicos_descricao.grid(column=1, row=12, sticky=W)

Label(frame_itens, text="Outros serviços quantidade:", bg='#e0e0e0').grid(column=0, row=13, sticky=W)
outros_servicos_quantidade = Entry(frame_itens)
outros_servicos_quantidade.grid(column=1, row=13, sticky=W)

Label(frame_itens, text="Outros serviços preço da unidade:", bg='#e0e0e0').grid(column=0, row=14, sticky=W)
outros_servicos_preco_unidade = Entry(frame_itens)
outros_servicos_preco_unidade.grid(column=1, row=14, sticky=W)

# Valor Total
Label(frame_itens, text="Valor Total:",font=('Arial', 13, 'bold'), bg='#e0e0e0').grid(column=0, row=15, sticky=W)
texto_total_geral = Entry(frame_itens, state='readonly')
texto_total_geral.grid(column=1, row=15, sticky=W)

# Botão
botao_mostrar = Button(frame_geral, text="Mostrar Valores e Gerar PDF", command=mostrar_valores, bg='#4CAF50',
                       fg='white', font=('Arial', 12, 'bold'))
botao_mostrar.grid(column=0, row=16, pady=10)

# Inicia o loop da interface gráfica
janela_orcamento.mainloop()
