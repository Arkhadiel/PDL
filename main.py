import os

def limpar_tela():
    """Limpa o terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_resultado(preço, gramagem, quantia_restante, custo, comissao_ifood_pct, imposto_pct):
    """Exibe só o resultado final"""
    
    # Cálculos
    lucro_bruto = float(preço - custo)
    margem_lucro_pct = float(lucro_bruto / preço) * 100
    lucro_por_grama = lucro_bruto / gramagem
    comissao_ifood = preço * (comissao_ifood_pct / 100)
    imposto = preço * (imposto_pct / 100)
    lucro_liquido = lucro_bruto - comissao_ifood - imposto
    
    # Limpa tudo que foi digitado
    limpar_tela()
    
    # Exibe só o resultado
    print("\n" + "="*50)
    print("📊 ANÁLISE DE PRECIFICAÇÃO")
    print("="*50)
    print(f"\n💰 VALORES PRINCIPAIS:")
    print(f"  Preço de venda: R$ {preço:.2f}")
    print(f"  Gramagem: {gramagem}g")
    print(f"  Custo: R$ {custo:.2f}")
    print(f"  Estoque: {quantia_restante}kg")
    print(f"\n📈 LUCROS:")
    print(f"  Lucro bruto: R$ {lucro_bruto:.2f}")
    print(f"  Margem bruta: {margem_lucro_pct:.1f}%")
    print(f"  Lucro por grama: R$ {lucro_por_grama:.4f}")
    print(f"\n📉 DEDUÇÕES:")
    print(f"  Comissão iFood ({comissao_ifood_pct}%): R$ {comissao_ifood:.2f}")
    print(f"  Imposto ({imposto_pct}%): R$ {imposto:.2f}")
    print(f"  Total deduções: R$ {comissao_ifood + imposto:.2f}")
    print(f"\n✅ RESULTADO FINAL:")
    print(f"  Lucro líquido (real): R$ {lucro_liquido:.2f}")
    if preço > 0:
        margem_liquida = (lucro_liquido / preço) * 100
        print(f"  Margem líquida: {margem_liquida:.1f}%")
    print("="*50 + "\n")

# ===== MAIN =====
if __name__ == "__main__":
    preço = float(input("Digite o preço do produto: R$ "))
    gramagem = int(input("Digite a gramagem do produto (g): "))
    quantia_restante = float(input("Quantia restante em estoque (kg): "))
    custo = float(input("Digite o custo do produto: R$ "))
    
    print("\nQual é seu regime fiscal?")
    print("1 - MEI (5%)")
    print("2 - Simples Nacional (10%)")
    print("3 - Outro")
    regime = input("Escolha (1-3): ")
    
    if regime == "1":
        imposto_pct = 5
    elif regime == "2":
        imposto_pct = 10
    else:
        imposto_pct = float(input("Qual é seu imposto (%): "))
    
    print("\nQual plano do iFood?")
    print("1 - Básico (12%)")
    print("2 - Entrega (25%)")
    plano = input("Escolha (1-2): ")
    
    if plano == "1":
        comissao_ifood_pct = 12
    else:
        comissao_ifood_pct = 25
    
    # Chama a função para exibir resultado
    exibir_resultado(preço, gramagem, quantia_restante, custo, comissao_ifood_pct, imposto_pct)
