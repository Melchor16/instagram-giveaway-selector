import instaloader
import random

L=instaloader.Instaloader()

L.login('USENAME', 'PASSWORD')

def lista_comentarios(shortc, tags): #insertar shortcode de post

  post= instaloader.Post.from_shortcode(L.context, shortc)

  comentarios = post.get_comments()
  Lista=[]

  for com in comentarios:
    comstr=com.text
    count=0

    for i in comstr:
      if i == '@':
        count+=1

    if count>=tags:
      Lista.append(com.owner.username)

  return Lista

def contador_comentarios(lista, nombre):
  
  count=0
  for j in lista:
    

    if j == nombre:
      count+=1

  return count


url=input('Paste the shortcode of the post: ')
tags2=int(input('Number of tags needed: '))
Lista = lista_comentarios(url, tags2)
ganador=random.choice(Lista)
cantidad = contador_comentarios(Lista, ganador)

print('\n\nNumber of participants: ', len(Lista))
print('\nParticipant list: ')
for i in Lista:
  print(i)
print('\n\nAnd the winner is!!!!:\n\n', ganador)
print('\n\nWith ', cantidad, ' valid comments.\n\n')
