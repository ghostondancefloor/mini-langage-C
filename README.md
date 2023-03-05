### Analyseur syntaxique pour un mini langage C

Dans le premier fichier nommé "class_grammaire.py", on y retrouve une class Grammaire qui va définir notre mini langage c.
</br>
Dans cette class on trouve :
<ul>
 <li>Les attributs de Grammaire:</li>
 <ul>
   <li> Une liste pour stocker les symboles terminaux</li>
   <li>Une liste pour stocker les symboles non terminaux</li>
   <li> Des listes pour stocker les règles de production</li>
 </ul>
 <li>Un dictionnaire imbriqué qui va représenter notre table d'analyse
 <li>La méthode <strong>analyse(chaine)</strong> qui va déterminer si la  chaine passer en paramètre est acceptée ou non.</ul>
 On commence l'analyse par l'initialisation de la pile principale et de la création d'une autre pile pour stocker les mots de la chaine passer en paramètre sans oublier l'ajout du $ à la fin de la pile.</li>
 </br>
 

J'ai aussi choisi de mettre en place une fenêtre pour recevoir la chaine à analyser grâce au module tkinter de python.

Pour tester le programme :
  La chaine acceptée : main() { float id int id if id = nombre id = nombre else id = nombre if id < nombre id = nombre else id = nombre }
  La chaine non acceptée : main() { int id float nombre if id = nombre else id < nombre }
