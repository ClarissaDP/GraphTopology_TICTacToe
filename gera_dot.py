#!/usr/bin/python
import sys
import numpy as np
import os



def full (string):
    count = 0
    len_s = len(string)
    for i in range( 0, len_s ):
        if ( string[i] == '.' ):
            count += 1
    
    if ( count ): 
        return 1
    else:
        return 0


def terminou ( string ):
    # Checar se deu veia

    len_s = len(string)
    if ( full(string) ):
        
        # Linhas
        if ( string[0] != '.' and string[0] == string[1] and string[1] == string[2] ): 
            return 0
        if ( string[3] != '.' and string[3] == string[4] and string[4] == string[5] ): 
            return 0
        if ( string[6] != '.' and string[6] == string[7] and string[7] == string[8] ): 
            return 0
        
        # Colunas
        if ( string[0] != '.' and string[0] == string[3] and string[3] == string[6] ): 
            return 0
        if ( string[1] != '.' and string[1] == string[4] and string[4] == string[7] ): 
            return 0
        if ( string[2] != '.' and string[2] == string[5] and string[5] == string[8] ): 
            return 0

        # Diagonais
        if ( string[0] != '.' and string[0] == string[4] and string[4] == string[8] ): 
            return 0
        if ( string[2] != '.' and string[2] == string[4] and string[4] == string[6] ): 
            return 0

        return 1            

    else:
        return 0



def def_prox ( string, prox ):
    x_value = string.count('X')
    o_value = string.count('O')
    if ( x_value <= o_value ):
        return 'X'
    return 'O'



def gera_mais( seq, string, prox, quanto, out, lista ):
    
    prox = def_prox(string, prox)
    len_s = len(string)
    for i in range( 0, len_s ):
        
        if string[i] == '.':
            novo = string[:] 
            novo[i] = prox
            seq.append(novo)
            
            if ( terminou(novo) ):
                print "gera", novo, prox
                quanto = gera_mais(seq, novo, prox, quanto, out, lista)
                seq.pop()
                
            else:
                print "term", novo, "-->", seq , len(seq)  
                quanto += 1
                
                for j in range( 0, len(seq)-1 ):
                    item = [ ''.join(seq[j]), ''.join(seq[j+1]) ]
                    if item not in lista:
                        print "not in", item
                        lista.append( item )
                        print >> out, "\t\"" + ''.join(seq[j]) + "\" -> \"" + ''.join(seq[j+1]) + "\";"
                    else:
                        print "ja foi", item
                seq.pop()

    return quanto



# *********************** Main program ************************ #
if ( len(sys.argv) < 3 ):
    print("python gera_dot.py entrada saida.dot")
    sys.exit()


in_name = sys.argv[1]
out_name = sys.argv[2]


with open(in_name) as f:
    start = f.readline()
    start = start.rstrip('\n')
    p = f.readline()

start = list(start)
len_s = len(start)
print "inicial = ", start
print "tamanho = ", len(start)

if ( p ):
    prox = p.rstrip('\n')
else:
    prox = 'X'
print "comeca = ", prox


out = open(out_name, 'w')
print >> out, "digraph hue {"
#print >> out, "\t\"" + ''.join(start) + "\" [shape=box];"

seq = []
seq.append(start)
lista = []

quanto = gera_mais(seq, start, prox, 0, out, lista)    

print "quanto ", quanto
print start, prox


print >> out, "}"
out.close()

