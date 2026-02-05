import os, time, json

end_program = False
SAVE = "save.json"
shop_cart = "cart.json"
cart = []

def save_data():
    try:
        stock.sort(key=lambda x: int(x['id']))
    except ValueError:
        stock.sort(key=lambda x: x['id'])

    with open(SAVE, 'w', encoding='utf-8') as arquivo:
        json.dump(stock, arquivo, indent=4, ensure_ascii=False)

    with open(shop_cart, 'w', encoding='utf-8') as arquivo:
        json.dump(cart, arquivo, indent=4, ensure_ascii=False)

def load_data():
    try:
        with open(SAVE, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    
def load_cart_data():
    try:
        with open(shop_cart, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

cart = load_cart_data()    

stock = load_data()

def erase_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def error(text):
    erase_screen()
    print(text)
    time.sleep(0.5)

def menu():  
    erase_screen()

    print("O que deseja fazer? \n")
    print("1. Adicionar produto")
    print("2. Remover produto")
    print("3. Editar produto")
    print("4. Registrar venda")
    print("5. Carrinho")
    print("6. Listar produtos")
    print("7. Informações do estoque")
    print("8. Sair \n")
    
    num = input("")

    erase_screen()
    if num == "1":
        add()
    elif num == "2":
        remove()
    elif num == "3":
        edit_product()
    elif num == "4":
        sell_product()
    elif num == "5":
        shopping_cart()
    elif num == "6":
        list_products()
    elif num == "7":
        data_stock()
    elif num == "8":
        print("Salvando dados...")
        save_data()
        time.sleep(1)
        print("Dados salvos")
        print("Finalizando programa...")
        time.sleep(1)
        return True        
    else:
        print("\nDigite um numero válido!")
        time.sleep(0.5)


def add():
    erase_screen()
    print("Qual o nome do produto? ")
    product_add_name = input()
    print("Qual o ID do produto? ")
    product_add_ID = input()
    for item in stock:
        if item['id'] == product_add_ID:
            erase_screen()
            print("ERRO! Já existe um produto com esse ID")
            time.sleep(1)
            return
        
    print("Qual o custo do produto?")
    product_add_COST = input()
    try:
        float(product_add_COST)
    except ValueError:
        error("ERRO! Digite um número!")
        return
    
    print("Qual o valor do produto? ")
    product_add_VALUE = input()
    try:
        float(product_add_VALUE)
    except ValueError:
        error("ERRO! Digite um número!")
        return

    print("Qual a quantidade do produto?")
    product_add_quantity = input()
    try:
        float(product_add_quantity)
    except ValueError:
        error("ERRO! Digite um número!")
        return

    

    new_product = {
        "id": product_add_ID,
        "name": product_add_name.lower(),
        "cost": float(product_add_COST),
        "profit": float(product_add_VALUE) - float(product_add_COST),
        "value": float(product_add_VALUE),
        "quantity": float(product_add_quantity)
    }

    stock.append(new_product)
    save_data()

    erase_screen()
    print("Produto adicionado com sucesso!")
    time.sleep(1)


def remove():
    founded_product = None
    print("Qual o ID ou NOME do produto?")
    product_remove_ID = input()

    for item in stock:
        if item['id'] == product_remove_ID or item['name'] == product_remove_ID:
            founded_product = item
            break

    if founded_product:
        stock.remove(founded_product)
        save_data()
        erase_screen()
        print("Produto removido!")
        time.sleep(1)  
    else:
        erase_screen()
        print("ERRO! Produto não encontrado!")
        time.sleep(1)


def edit_product():
    while True:
        while True:
            while True:
                erase_screen()
                edited_product_ID = input("Qual o ID ou NOME do produto? \n")
                is_product_founded = False
                erase_screen()
                print("Produto selecionado: ")
                for item in stock:
                    if item['id'] == edited_product_ID or item['name'] == edited_product_ID.lower():
                        is_product_founded = True
                        product_founded = item
                        print(f"ID: {item['id']} \nNome: {item['name']} \nCusto: R$ {item['cost']:.2f} \nR${item['value']:.2f} \nEstoque: {item['quantity']}")
                if not is_product_founded:
                    erase_screen()
                    print("ERRO! Selecione um ID ou NOME válido!")
                    time.sleep(1)
                    return
                else:
                    break

            
            edited_product_TYPE = input("\n1. ID\n2. Nome\n3. Custo\n4. Preço\n5. Estoque\n")
            try:
                float(edited_product_TYPE)
                break
            except ValueError:
                error("ERRO! Digite um número")

        if edited_product_TYPE in ['1', '3', '4', '5']:
            erase_screen()
            print("VALOR ATUAL: ")
            if edited_product_TYPE == '1':
                print(f"ID: {product_founded['id']}")
            elif edited_product_TYPE == '3':
                print(f"Custo: R${product_founded['cost']}")
            elif edited_product_TYPE == '4':
                print(f"Preço: R${product_founded['value']}")
            elif edited_product_TYPE == '5':
                print(f"Estoque: {product_founded['quantity']}")
            print("Digite o novo valor:")
            new_value = input()
            try:
                float(new_value)
                break
            except ValueError:
                error("ERRO! Digite um número")
        elif edited_product_TYPE == '2':
            erase_screen()
            print("Digite o novo nome:")
            new_value = input()
            break
        else:
            erase_screen()
            print("ERRO! Selecione uma opção válida!")
            time.sleep(1)

    if edited_product_TYPE == '1':
        product_founded['id'] = new_value
    elif edited_product_TYPE == '2':
        product_founded['name'] = new_value
    elif edited_product_TYPE == '3':
        product_founded['cost'] = float(new_value)
    elif edited_product_TYPE == '4':
        product_founded['value'] = float(new_value)
    elif edited_product_TYPE == '5':
        product_founded['quantity'] = float(new_value)

    product_founded['profit'] = product_founded['value'] - product_founded['cost']

    erase_screen()
    save_data()
    print("INFORMAÇÃO EDITADA!")
    print(f"ID: {product_founded['id']} \nNome: {product_founded['name']} \nCusto: R$ {product_founded['cost']:.2f} \nR${product_founded['value']:.2f} \nEstoque: {product_founded['quantity']}")
    input("\nPressione enter para voltar\n")

def sell_product():
    while True:
        erase_screen()
        print("MONTANDO CARRINHO...\n ")
        print("Qual o ID ou NOME do produto?")
        item_CART = input()
        selected_ITEM = None

        for item in stock:
            if item['id'] == item_CART or item['name'] == item_CART.lower():
                selected_ITEM = item


        if selected_ITEM == None:
            error("ERRO! Produto não encontrado")
            break

        erase_screen()
        print("MONTANDO CARRINHO...\n ")
        print(f"Item selecionado: \nID: {selected_ITEM['id']} \nNome: {selected_ITEM['name']} \nR$ {selected_ITEM['value']:.2f} \nEstoque: {selected_ITEM['quantity']}")
        print("\nQuantos produtos? ")
        quantity = input("")
        try:
            float(quantity)
        except ValueError:
            error("ERRO! Digite um número!")
            break

        if selected_ITEM['quantity'] < float(quantity):
            error("ERRO! Quantidade indisponível!")
            time.sleep(1)
            break

        cart_data = {
            "id": selected_ITEM['id'],
            "name": selected_ITEM['name'],
            "quantity": float(quantity),
            "value": selected_ITEM['value'],
            "profit": selected_ITEM['profit']
        }


        print("Item adicionado ao carrinho!")
        cart.append(cart_data)
        time.sleep(1)
        save_data()
        erase_screen()
        print("Quer adicionar mais itens?")
        choose = input()
        if choose.lower() in ['nao', 'n', 'nn']:
            save_data()
            break
        elif choose.lower() in ['sim', 's', 'ss']:
            print("voltando...")
            time.sleep(1)
        else:
            save_data()
            break
            
def shopping_cart():
    while True:
        total_value = 0
        total_items = 0
        erase_screen()
        print("CARRINHO")
        for item in cart:
            print(f"ID: {item['id']} | Nome: {item['name']} | R${item['value']:.2f} | Quantidade: {item['quantity']}")
            total_value += float(item['value']) * float(item['quantity'])
            total_items += float(item['quantity'])

        if cart == []:
            print("NÃO HÁ NADA NO CARRINHO!")
            time.sleep(2)
            break

        print(f"\nR$ {total_value}")
        print(f"{total_items} produtos")

        print("\n(S) Finalizar carrinho | (X) Apagar carrinho")
        choose = input()

        if choose.lower() == 's':
            erase_screen()
            print("CARRINHO FINALIZADO")
            for item in stock:
                for product in cart:
                    if item['id'] == product['id']:
                        item['quantity'] = float(item['quantity']) - float(product['quantity'])

            time.sleep(1)
            save_data()
            erase_screen()
            erase_screen()
            print("----------Recibo----------")
            print(f"Valor total: R${total_value}")
            print(f"{total_items:.0f} produtos")
            print("\n-----Produtos-----")
            for item in cart:
                print(f"Produto: {item['name']} | Preço: R${item['value']} | Quantidade: {item['quantity']}")
            input("\nPressione enter para sair\n")
            cart.clear()
            save_data()
        elif choose.lower() == 'x':
            erase_screen()
            print("CARRINHO APAGADO!")
            cart.clear()
            save_data()
            time.sleep(1)
            break
        else:
            break

def list_products():
    print("----------LISTA----------")
    for item in stock:
        print(f"ID: {item['id']} | Nome: {item['name']} | Custo: {item['cost']} | R$ {item['value']:.2f} | Estoque: {item['quantity']:.0f}")

    input("\nPressione enter para voltar")


def data_stock():
    erase_screen()
    total_COST = 0
    gross_PROFIT = 0
    total_VALUE = 0
    total_ITEMS = 0

    for item in stock:
        total_COST += item['cost'] * item['quantity']
        gross_PROFIT += item['profit'] * item['quantity']
        total_VALUE += item['value'] * item['quantity']
        total_ITEMS += item['quantity']
    
    print(f"Custo total: {total_COST} \nLucro bruto: {gross_PROFIT} \nValor total: {total_VALUE} \nTotal de itens: {total_ITEMS}")

    input("\nPressione enter para voltar")


while not end_program:
    end = menu()
    if end == True:
        end_program = True
