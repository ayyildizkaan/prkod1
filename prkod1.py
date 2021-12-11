# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

"""""""""""""""""
def flatten_func(liste):
    flat_liste = []
    for i in liste:
        if type(i) is list:
            flat_liste.extend(flatten_func(i))
        else:
            flat_liste.append(i)
    return flat_liste

"""""""""""""""""""""

# 2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün.

""""""""""""""""""""
def reverse_list(list):
    reverse_list = []
    boyut = len(list)
    for i in range(0,boyut):
        reverse_list.append(list[boyut-i-1][::-1])
    return reverse_list

"""""""""""""""""""""

