terms = [0, 1] #criar uma lista e atribuila os primeiros termos

num_of_seq = 50 # numero de termos que queremos obter

for seq in range(0, num_of_seq - 1): # fazer uma sequencia que inicia do zero ate so num_of_seq
    first_term = terms[seq] #obtemos o penultimo termo da lista
    second_term = terms[seq+1] #obtemos o ultimo termo da lista
    next_term_of_list = (first_term + second_term) #obtermos o proximo termo da lista, cosoante a soma do penultimo com o ultimo
    terms.append(next_term_of_list) # salvamos o proximo termo na lista

print("Sequencia de fibonacce : ", terms)   