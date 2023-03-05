from collections import deque

class Grammaire:
    nonTerminaux=['<Programme>','<liste_declarations>','<liste_instructions>','<une_declaration>','<une_instruction>','<affectation>','<test>','<type>','<condition>','<operateur>']
    terminaux=['main()','{','}','id','int','float','nombre','else','if','nombre','>','<','=','$']
    
    #Liste des règles de production
    regle1=['main()','{','<liste_declarations>','<liste_instructions>','}']
    regle2_1=['<une_declaration>','<liste_declarations>']
    regle2_2=['vide']
    regle3=['<type>','id']
    regle4_1=['<une_instruction>','<liste_instructions>']
    regle4_2=['vide']
    regle5_1=['<affectation>']
    regle5_2=['<test>']
    regle6_1=['int']
    regle6_2=['float']
    regle7=['id','=','nombre']
    regle8=['if','<condition>','<une_instruction>','else','<une_instruction>']
    regle9=['id','<operateur>','nombre']
    regle10_1=['<']
    regle10_2=['>']
    regle10_3=['=']

    #choix pour la table d'analyse : dictionnaire imbriqué
    tableAnalyse = {
            '<Programme>':{
                  'main()': regle1 
                },   
            '<liste_declarations>':{
                  'int':regle2_1 ,
                  'float':regle2_1 ,
                  '$':regle2_1 ,
                  'id':regle2_2,
                  'if':regle2_2  
                },
            '<une_declaration>':{
                  'int':regle3,
                  'float': regle3
                },
            '<liste_instructions>':{
                  'id': regle4_1,
                  'if': regle4_1,
                  '$': regle4_1,
                  '}':regle4_2 
                },
            '<une_instruction>':{
                  'id': regle5_1,
                  'if': regle5_2
                },
             '<type>':{
                  'int': regle6_1,
                  'float': regle6_2
                 },
             '<affectation>':{
                  'id': regle7
                 },
             '<test>':{
                  'if': regle8
                 },
             '<condition>':{
                  'id':regle9 
                 },
             '<operateur>':{
                  '<': regle10_1 ,
                  '>': regle10_2 ,
                  '=': regle10_3 
                 }
             
         }
    
    
    def analyseur(self,programme) :
        
        chaine = deque(programme.split(" "))
        chaine.append('$')

        pile=deque(['<Programme>','$'])
        print("Debut de l'analyse")

        while len(chaine)>0:
           
            if pile[0] in self.nonTerminaux:

                if chaine[0] in self.tableAnalyse[pile[0]]:

                    regle = self.tableAnalyse[pile[0]][chaine[0]]
                    print(pile[0],"::="," ".join(regle))
                    pile.popleft()
                    
                    for j in reversed(regle):
                        if j != 'vide':
                         pile.appendleft(j)
   
                else:
                    print("Fin de l'analyse")
                    print("La chaine n'est pas acceptee") 
                    return False
                            
            else:
                if pile[0] =='$' and chaine[0]=='$': 
                    chaine.pop()   
                    print("Fin de l'analyse")
                    print("La chaine est acceptee")
                    return True
                 
                else :
                 if pile[0] == chaine[0] :
                     pile.popleft()  
                     chaine.popleft()  
                 else :
                     print("Fin de l'analyse")
                     print("La chaine n'est pas acceptee") 
                     return False
                     

"""
main() { int id float nombre if id = nombre else id < nombre } chaine pas acceptée
main() { float id int id if id = nombre id = nombre else id = nombre if id < nombre id = nombre else id = nombre } chaine acceptée
"""