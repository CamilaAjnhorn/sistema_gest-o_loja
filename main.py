class Produto:
    def __init__(self, nome : str, preco : float,
                  estoque : int, peso_kg : float):
        if isinstance(nome, str):    
            self.nome = nome
        
        if isinstance(preco, float):
            self.preco = preco

        if isinstance(estoque, int):
            self.estoque = estoque

        if isinstance(peso_kg, float):
            self.peso_kg = peso_kg
    
    def atualizar_preco (self, novo):
        if novo > 0 and novo != self.preco:
            self.preco = novo
        else:
            return ValueError
        
    def aplicar_desconto(self, porcentagem):
        porcentagem = porcentagem * 0.01
        self.preco = self.preco * (1 - porcentagem) 

    def verificar_estoque_baixo (self):
        if self.estoque < 5:
            return True
        
    def __eq__(self, value):
        if isinstance(value, Produto):
            return self.nome == value.nome and self.preco == value.preco
        return False
    
    def __str__(self):
        return f"Produto: {self.nome} | Preço: {self.preco} | Estoque: {self.estoque} | Peso (kg): {self.peso_kg}" 
    

class Cliente:
    def __init__(self, nome : str, email : str):
        if isinstance(nome, str):
            self.nome = nome
        if isinstance(email, str):
            self.email = email
        
        self.pontos_fidelidade = 0

    def adicionar_pontos (self, pontos):
        if isinstance(pontos, int) and pontos > 0:
            self.pontos_fidelidade += pontos
    
    def resgatar_pontos (self, pontos):
        if isinstance(pontos, int) and pontos > 0:
            self.pontos_fidelidade -= pontos
    
    def verificar_vip (self):
        if self.pontos_fidelidade >= 1000:
            return True
        
    def __eq__(self, value):
        return self.email == value.email
    
    def __iadd__ (self, pontos):
        self.pontos_fidelidade += pontos
        return self
    
    def __str__(self):
        return f"Cliente: {self.nome} | Pontos: {self.pontos_fidelidade} | Email: {self.email}"
