#Definindo listas

lista_dados = [ "Nome", "nickname", "login", "senha", "email"]

print(lista_dados)
print(type(lista_dados))

#Incrementando a lista com variáveis

idade = 32
saldo_em_conta = 598,98
usuário_logged = True

lista_dados =  [ "Nome", idade, "nickname", "login", "senha", "email", saldo_em_conta, usuário_logged]
print(lista_dados)

print(type(lista_dados))

#Concatenação

redes_geração_z = ["tiktok","snapchat"]

redes_geração_y = ["facebook","instagram"]

redes_socias = redes_geração_y + redes_geração_z

print(redes_geração_z)
print(redes_geração_y)
print(redes_socias)

#Fatiamento Fixo

#Primeiro elemento do índice
print(f"0: {redes_geração_y[0]}")

#Último elemento do índice
print(f"-1: {redes_geração_z[-1]}")

#Fatiamento por intervalo

#indicamos o primeiro item da lista até o segundo item, pois o 2 é excluído
redes_geração_y = redes_socias[0:2] 

#indicamos a partir do segundo item da lista usando LEN para considerar até o final da lista
redes_geração_z = redes_socias[2:len(redes_socias)] 

#Reunindo as informações, conversando a lista em str para evitar o erro no código

print("Gen Z:" + str(redes_geração_z))

print("Gen Y:" + str(redes_geração_y))

#Alterando posições da lista

redes_socias[3] = "twitter"
print(redes_socias)

#Aplicando métodos em Listas - Inserção e remoção

números_primos = [11, 13, 17, 19]

#Método de inserção por índice através de list.insert(index,val)

números_primos.insert(0, 2)
print(números_primos) # Saída: [2, 11, 13, 17, 19]

#Método de inserção por índice através do slicing (fatiamento)

números_primos[1:1] = [3, 5, 7]
print(números_primos) # Saída: [2, 3, 5, 7, 11, 13, 17, 19]

#Método de inserção ao final da lista através do list.append(val)

números_primos.append(23)
print(números_primos) # Saída: [2, 3, 5, 7, 11, 13, 17, 19, 23]

#Método de inserção de mais de um elemento através do list.extend([list])

números_primos.extend([29, 31, 37])
print(números_primos) # Saída: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

#Método de remoção da primeira ocorrência de um elemento através do list.remove(val)

números_primos.remove(2)
print(números_primos) # Saída: [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

#Método de remoção de um elemento com base no índice através do list.pop(val)

quinto_número_primo = números_primos.pop(4)
print(quinto_número_primo) # Saída: 13
print(números_primos) # Saída: [3, 5, 7, 11, 17, 19, 23, 29, 31, 37]






