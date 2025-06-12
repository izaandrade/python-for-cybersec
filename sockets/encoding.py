# encoding

# we send bytes = 10011010 -> 8 bits

string_var = "something"

print(type(string_var))

string_var = str.encode(string_var) # encode transforma a variável string em bytes, utilizada para enviar comunicações para a rede

print(type(string_var))

string_var = string_var.decode() # decode faz o processo inverso, pega a mensagem recebida em bytes e tranforma em string

print(type(string_var))
