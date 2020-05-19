# ISO27005

 API REST /iso27005    Auteur: Rioche Patrick                  le 18/05/2020

   Cette API REST a ete concue dans un but pedagogique pour servir de support a
   une formation MBA Secure en SI pour la MySchoolDigital de l'ESPL à Angers.

   Les specifcations de l'API sont donnees par la norme iso27005 permettant de
   connaitre les critère d'impact, de conséquences et d'évaluation des risques.
       
       voir : https://www.slideshare.net/michaeldean/netclu09-27005/

   Exemple de requête pour connaitre l'echelle de valorisation des actifs

       /iso27005/eva/1
       => {"idvaleur": 1, "valeur": "Faible", "signifiremplace": , "Actif facilement remplaçable" , "signifiachat": "Coût d'achat faible", "signifimaint": "Coût de maintenance faible", "significonnais": "Ne nécessite pas de compétence particilière"}

   Exemple de requête pour connaitre les critères d'impact :
   
       /iso27005/ci/2
       => {"idimpact": 2, "impact": "Significatif", "Confidentialité": "Accès autorisé à l'ensemeble de l'entreprise", "integrite":, "Simple validation possible (peut être partielement intégré)", "disponibilité": "Arrêt 1 jour à 3 jours"}

   Exemple de requête pour connaitre les echelles de conséquences:
   
       /iso27005/ec/3
       => {"idconsequence", "consequence": "Fort", .... }
       
   Exemple de requête pour connaitre les critères d'acception des risques:
   
       /iso27005/car/1
       => {"idrisque": 1, "risque": "faible, "niveaurisquede": 1, "niveaurisquea": 8, "acceptationrisque": "Oui"}

   Exemple de requête pour connaitre les echelles de vraisemblance:
   
       /iso27005/cv/4
       => {"idvraisemblance": 4, "vraisemblance": "Très élevée (Fréquente)"}

   Exemple de requête pour connaitre les critères d'évaluation des risques avec impact et vraisemblance:
   
       /iso27005/cer/4,3
       => {"idevaluationrisque": 12}