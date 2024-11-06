class Contatos:
    def __init__(self, id, nome, apelido, telefone, email):
        self.id = id
        self.nome = nome
        self.apelido = apelido
        self.telefone = telefone
        self.email = email

    def id(self):
        return self.id
    
    def nome(self):
        return self.nome
        
    def apelido(self):
        return self.apelido

    def telefone(self):
        return self.telefone

    def email(self):
        return self.email

    def id(self, id):
        self.id = id
    
    def nome(self, nome):
        self.nome = nome
        
    def apelido(self, apelido):
        self.apelido = apelido

    def telefone(self, telefone):
        self.telefone = telefone

    def email(self, email):
        self.email = email

    def __str__(self):
        return (f"Contatos(id= {self.id}, nome= {self.nome}, apelido= {self.apelido}, telefone= {self.telefone}, email= {self.email})\n")