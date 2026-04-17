import pandas as pd
import streamlit as st
import os
import json

def load_data():
    with open(f'dados_{ano_base}.json', 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)


def exibir_conteudo_mensal():
    add_slider = st.sidebar.slider("Selecione o mês", 1, 12)
    if add_slider == 1:
        st.title("Mês selecionado - JANEIRO")
        st.write(f" Total Vendas de R$ {tot_vendas_jan:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_jan:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_jan:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_jan:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_jan:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_jan:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_jan:.2f}")
        st.write(f"Total de Imposto: {tot_imp_jan:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_jan:.2f}")
    elif add_slider == 2:
        st.title("Mês selecionado - FEVEREIRO")
        st.write(f" Total Vendas de R$ {tot_vendas_fev:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_fev:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_fev:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_fev:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_fev:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_fev:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_fev:.2f}")
        st.write(f"Total de Imposto: {tot_imp_fev:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_fev:.2f}")
    elif add_slider == 3:
        st.title("Mês selecionado - MARÇO")
        st.write(f" Total Vendas de R$ {tot_vendas_mar:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_mar:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_mar:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_mar:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_mar:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_mar:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_mar:.2f}")
        st.write(f"Total de Imposto: {tot_imp_mar:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_mar:.2f}")
    elif add_slider == 4:
        st.title("Mês selecionado - ABRIL")
        st.write(f" Total Vendas de R$ {tot_vendas_abr:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_abr:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_abr:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_abr:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_abr:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_abr:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_abr:.2f}")
        st.write(f"Total de Imposto: {tot_imp_abr:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_abr:.2f}")
    elif add_slider == 5:
        st.title("Mês selecionado - MAIO")
        st.write(f" Total Vendas de R$ {tot_vendas_mai:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_mai:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_mai:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_mai:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_mai:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_mai:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_mai:.2f}")
        st.write(f"Total de Imposto: {tot_imp_mai:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_mai:.2f}")
    elif add_slider == 6:
        st.title("Mês selecionado - JUNHO")
        st.write(f" Total Vendas de R$ {tot_vendas_jun:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_jun:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_jun:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_jun:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_jun:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_jun:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_jun:.2f}")
        st.write(f"Total de Imposto: {tot_imp_jun:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_jun:.2f}")
    elif add_slider == 7:
        st.title("Mês selecionado - JULHO")
        st.write(f" Total Vendas de R$ {tot_vendas_jul:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_jul:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_jul:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_jul:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_jul:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_jul:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_jul:.2f}")
        st.write(f"Total de Imposto: {tot_imp_jul:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_jul:.2f}")
    elif add_slider == 8:
        st.title("Mês selecionado - AGOSTO")
        st.write(f" Total Vendas de R$ {tot_vendas_ago:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_ago:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_ago:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_ago:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_ago:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_ago:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_ago:.2f}")
        st.write(f"Total de Imposto: {tot_imp_ago:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_ago:.2f}")
    elif add_slider == 9:
        st.title("Mês selecionado - SETEMBRO")
        st.write(f" Total Vendas de R$ {tot_vendas_set:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_set:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_set:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_set:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_set:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_set:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_set:.2f}")
        st.write(f"Total de Imposto: {tot_imp_set:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_set:.2f}")
    elif add_slider == 10:
        st.title("Mês selecionado - OUTUBRO")
        st.write(f" Total Vendas de R$ {tot_vendas_out:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_out:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_out:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_out:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_out:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_out:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_out:.2f}")
        st.write(f"Total de Imposto: {tot_imp_out:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_out:.2f}")
    elif add_slider == 11:
        st.title("Mês selecionado - NOVEMBRO")
        st.write(f" Total Vendas de R$ {tot_vendas_nov:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_nov:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_nov:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_nov:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_nov:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_nov:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_nov:.2f}")
        st.write(f"Total de Imposto: {tot_imp_nov:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_nov:.2f}")
    elif add_slider == 12:
        st.title("Mês selecionado - DEZEMBRO")
        st.write(f" Total Vendas de R$ {tot_vendas_dez:.2f}")
        st.write(f"Total de Receitas s/Op.Comum: R$ {rec_comum_dez:.2f}")
        st.write(f"Total de Receitas s/Op. Trade: R$ {rec_trade_dez:.2f}")
        st.write(f"Total de Despesas s/Op.Comum: {desp_comum_dez:.2f}")
        st.write(f"Total de Despesas s/Op.Trade: {desp_trade_dez:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Comum: {res_comum_dez:.2f}")
        st.write(f"Total de Resultado líquido s/Op.Trade: {res_trade_dez:.2f}")
        st.write(f"Total de Imposto: {tot_imp_dez:.2f}")
        st.write(f"Total de Imposto a pagar: {imp_pagar_dez:.2f}")



def exibir_conteudo_anual():
    st.title(f"Ano Base - {ano_base}")
    st.write(f"Receita s/operações comuns: R$ {rec_op_comum:.2f}")
    st.write(f"Despesa s/operações comuns: R$ {desp_op_comum:.2f}")
    st.write(f"Resultado Líquido s/operações comuns: R$ {res_liq_op_comum:.2f}")
    st.write('************************************')
    st.write(f"Receita s/operações Day-trade: R$ {rec_op_trade:.2f} ")
    st.write(f"Despesa s/operações Day-trade: R$ {desp_op_trade:.2f}")
    st.write(f"Resultado Líquido s/operações Day-Trade: R$ {res_liq_op_trade:.2f}")
    st.write('************************************')
    st.write(f"Imposto s/operações: R$ {total_imp:.2f}")
    st.write(f"Total de Imposto pago(a pagar): R$ {total_imp_pagar:.2f}")
    st.write('************************************')


tabela_anos = ['2024', '2025', '2026']
ano_base = st.sidebar.selectbox(
    'Escolha o ano-base da declaração.',
    tabela_anos, index=None, placeholder="Defina o ano"
)

st.title("DADOS FICTICIOS PARA SIMULAÇÃO")


if ano_base:
    try:
        data = load_data()
        df = pd.read_json(f'dados_{ano_base}.json', orient='split', compression='infer')
        # st.write(df)
        opcao = st.sidebar.radio(
        "Escolha uma opção:",
        ('Resumo do Mês', 'Resumo Anual'), index=None)
        dados_ideal = df.transpose()
        tot_vendas = dados_ideal.loc['Total Vendas']
        rec_comum = dados_ideal.loc['Receita_Comum']
        rec_trade = dados_ideal.loc['Receita_Trade']
        desp_comum = dados_ideal.loc['Despesa_Comum']
        desp_trade = dados_ideal.loc['Despesa_Trade']
        res_comum = dados_ideal.loc['Resultado Comum']
        res_trade = dados_ideal.loc['Resultado Trade']
        tot_imp = dados_ideal.loc['Total Imp Devido']
        imp_pagar = dados_ideal.loc['Imposto a Pagar']
        tot_vendas_jan = tot_vendas.loc['Jan']
        rec_comum_jan = rec_comum.loc['Jan']
        rec_trade_jan = rec_trade.loc['Jan']
        desp_comum_jan = desp_comum.loc['Jan']
        desp_trade_jan = desp_trade.loc['Jan']
        res_comum_jan = res_comum.loc['Jan']
        res_trade_jan = res_trade.loc['Jan']
        tot_imp_jan = tot_imp.loc['Jan']
        imp_pagar_jan = imp_pagar.loc['Jan']
        tot_vendas_fev = tot_vendas.loc['Fev']
        rec_comum_fev = rec_comum.loc['Fev']
        rec_trade_fev = rec_trade.loc['Fev']
        desp_comum_fev = desp_comum.loc['Fev']
        desp_trade_fev = desp_trade.loc['Fev']
        res_comum_fev = res_comum.loc['Fev']
        res_trade_fev = res_trade.loc['Fev']
        tot_imp_fev = tot_imp.loc['Fev']
        imp_pagar_fev = imp_pagar.loc['Fev']
        tot_vendas_mar = tot_vendas.loc['Mar']
        rec_comum_mar = rec_comum.loc['Mar']
        rec_trade_mar = rec_trade.loc['Mar']
        desp_comum_mar = desp_comum.loc['Mar']
        desp_trade_mar = desp_trade.loc['Mar']
        res_comum_mar = res_comum.loc['Mar']
        res_trade_mar = res_trade.loc['Mar']
        tot_imp_mar = tot_imp.loc['Mar']
        imp_pagar_mar = imp_pagar.loc['Mar']
        tot_vendas_abr = tot_vendas.loc['Abr']
        rec_comum_abr = rec_comum.loc['Abr']
        rec_trade_abr = rec_trade.loc['Abr']
        desp_comum_abr = desp_comum.loc['Abr']
        desp_trade_abr = desp_trade.loc['Abr']
        res_comum_abr = res_comum.loc['Abr']
        res_trade_abr = res_trade.loc['Abr']
        tot_imp_abr = tot_imp.loc['Abr']
        imp_pagar_abr = imp_pagar.loc['Abr']
        tot_vendas_mai = tot_vendas.loc['Mai']
        rec_comum_mai = rec_comum.loc['Mai']
        rec_trade_mai = rec_trade.loc['Mai']
        desp_comum_mai = desp_comum.loc['Mai']
        desp_trade_mai = desp_trade.loc['Mai']
        res_comum_mai = res_comum.loc['Mai']
        res_trade_mai = res_trade.loc['Mai']
        tot_imp_mai = tot_imp.loc['Mai']
        imp_pagar_mai = imp_pagar.loc['Mai']
        tot_vendas_jun = tot_vendas.loc['Jun']
        rec_comum_jun = rec_comum.loc['Jun']
        rec_trade_jun = rec_trade.loc['Jun']
        desp_comum_jun = desp_comum.loc['Jun']
        desp_trade_jun = desp_trade.loc['Jun']
        res_comum_jun = res_comum.loc['Jun']
        res_trade_jun = res_trade.loc['Jun']
        tot_imp_jun = tot_imp.loc['Jun']
        imp_pagar_jun = imp_pagar.loc['Jun']
        tot_vendas_jul = tot_vendas.loc['Jul']
        rec_comum_jul = rec_comum.loc['Jul']
        rec_trade_jul = rec_trade.loc['Jul']
        desp_comum_jul = desp_comum.loc['Jul']
        desp_trade_jul = desp_trade.loc['Jul']
        res_comum_jul = res_comum.loc['Jul']
        res_trade_jul = res_trade.loc['Jul']
        tot_imp_jul = tot_imp.loc['Jul']
        imp_pagar_jul = imp_pagar.loc['Jul']
        tot_vendas_ago = tot_vendas.loc['Ago']
        rec_comum_ago = rec_comum.loc['Ago']
        rec_trade_ago = rec_trade.loc['Ago']
        desp_comum_ago = desp_comum.loc['Ago']
        desp_trade_ago = desp_trade.loc['Ago']
        res_comum_ago = res_comum.loc['Ago']
        res_trade_ago = res_trade.loc['Ago']
        tot_imp_ago = tot_imp.loc['Ago']
        imp_pagar_ago = imp_pagar.loc['Ago']
        tot_vendas_set = tot_vendas.loc['Set']
        rec_comum_set = rec_comum.loc['Set']
        rec_trade_set = rec_trade.loc['Set']
        desp_comum_set = desp_comum.loc['Set']
        desp_trade_set = desp_trade.loc['Set']
        res_comum_set = res_comum.loc['Set']
        res_trade_set = res_trade.loc['Set']
        tot_imp_set = tot_imp.loc['Set']
        imp_pagar_set = imp_pagar.loc['Set']
        tot_vendas_out = tot_vendas.loc['Out']
        rec_comum_out = rec_comum.loc['Out']
        rec_trade_out = rec_trade.loc['Out']
        desp_comum_out = desp_comum.loc['Out']
        desp_trade_out = desp_trade.loc['Out']
        res_comum_out = res_comum.loc['Out']
        res_trade_out = res_trade.loc['Out']
        tot_imp_out = tot_imp.loc['Out']
        imp_pagar_out = imp_pagar.loc['Out']
        tot_vendas_nov = tot_vendas.loc['Nov']
        rec_comum_nov = rec_comum.loc['Nov']
        rec_trade_nov = rec_trade.loc['Nov']
        desp_comum_nov = desp_comum.loc['Nov']
        desp_trade_nov = desp_trade.loc['Nov']
        res_comum_nov = res_comum.loc['Nov']
        res_trade_nov = res_trade.loc['Nov']
        tot_imp_nov = tot_imp.loc['Nov']
        imp_pagar_nov = imp_pagar.loc['Nov']
        tot_vendas_dez = tot_vendas.loc['Dez']
        rec_comum_dez = rec_comum.loc['Dez']
        rec_trade_dez = rec_trade.loc['Dez']
        desp_comum_dez = desp_comum.loc['Dez']
        desp_trade_dez = desp_trade.loc['Dez']
        res_comum_dez = res_comum.loc['Dez']
        res_trade_dez = res_trade.loc['Dez']
        tot_imp_dez = tot_imp.loc['Dez']
        imp_pagar_dez = imp_pagar.loc['Dez']
        rec_op_comum = df['Receita_Comum'].sum()
        desp_op_comum = df['Despesa_Comum'].sum()
        res_liq_op_comum = df['Resultado Comum'].sum()
        rec_op_trade = df['Receita_Trade'].sum()
        desp_op_trade = df['Despesa_Trade'].sum()
        res_liq_op_trade = df['Resultado Trade'].sum()
        total_imp = df['Total Imp Devido'].sum()
        total_imp_pagar = df['Imposto a Pagar'].sum()
        if opcao == 'Resumo do Mês':
            exibir_conteudo_mensal()
        elif opcao == 'Resumo Anual':
            exibir_conteudo_anual()

            
    except FileNotFoundError:
        st.error(f"Arquivo 'dados_{ano_base}.json' não encontrado.")
    
        




