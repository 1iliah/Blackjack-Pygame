cartes = [
    
    #piques 
    ("As", "Pique",[1,11]),
    ("2", "Pique" ,2),
    ("3", "Pique",3),
    ("4","Pique",4),
    ("5","Pique",5),
    ("6","Pique",6),
    ("7","Pique",7),
    ("8","Pique",8),
    ("9","Pique",9),
    ("10","Pique",10),
    ("valet","Pique",10),
    ("dame","Pique",10),
    ("roi","Pique",10),
    #coeur ,
    ("As","coeur",[1,11]),
    ("2","coeur",2),
    ("3","coeur",3),
    ("4","coeur",4),
    ("5","coeur",5),
    ("6","coeur",6),
    ("7","coeur",7),
    ("8","coeur",8),
    ("9","coeur",9),
    ("10","coeur",10),
    ("valet","coeur",10),
    ("dame","coeur",10),
    ("roi","coeur",10),
    #carreau 
    ("As","carreau ",[1,11]),
    ("2","carreau ",2),
    ("3","carreau",3),
    ("4","carreau ",4),
    ("5","carreau ",5),
    ("6","carreau ",6),
    ("7","carreau ",7),
    ("8","carreau ",8),
    ("9","carreau ",9),
    ("10","carreau ",10),
    ("valet","carreau ",10),
    ("dame","carreau ",10),
    ("roi","carreau ",10),
    #Trèfle
    ("As","Trèfle",[1,11]),
    ("2","Trèfle",2),
    ("3","Trèfle",3),
    ("4","Trèfle",4),
    ("5","Trèfle",5),
    ("6","Trèfle",6),
    ("7","Trèfle",7),
    ("8","Trèfle",8),
    ("9","Trèfle",9),
    ("10","Trèfle",10),
    ("valet","Trèfle",10),
    ("dame","Trèfle",10),
    ("roi","Trèfle",10)
]
#on verifie au il y est 52 cartes
import random
random.shuffle(cartes)
carte1= cartes.pop()
carte2= cartes.pop()
valeur1 = carte1[2]
valeur2 = carte2[2]
#dans le cas ou on as un as
total=0
nombre_as =0 
for valeur in [valeur1,valeur2]:
    if isinstance(valeur ,list):
       choix = input("ton as vaut 1 ou 11").strip()
       while choix not in["1" ,"11"] :
         choix = input("choisis uniquement 1 ou 11").strip()
       if choix == "1":
        total+=1 
       else:
            total+=11
    else :
                total+= valeur
print("carte1:",carte1)
print("carte2 :",carte2)
print("total",total)
while True :
  choix = input("Appuie sur t pour tirer une autre carte ou n pour laisser :")
  if choix == "t":
      nouvelle_carte= cartes.pop()
      valeur3 =nouvelle_carte[2]
      print("nouvelle carte:",nouvelle_carte) 
      if isinstance(valeur3 ,list):
         choix_as= input("ton as vaut 1 ou 11").strip()
         while choix_as not in["1" ,"11"] :
          choix_as = input("choisis uniquement 1 ou 11").strip()
          if choix_as== "1":
             total+=1 
          else:
            total+=11
      else:
           total += valeur3
           print("ton nouveau total est :",total)
      if total>21:
       print ("tu as depasse 21 !! perdue tu est nul bahahahhaha")
       break
  elif choix == "n" :
    print("ton total reste :",total )
    break
  else :
      print("appuie sur t pour tirer une autre carte ou n pour laisser")
      
