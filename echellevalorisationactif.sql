create table echellevalorisationactif ( idvaleur interger primary key , valeur varchar(50) , significationremplacement varchar(50) , significationachat varchar(50) , significationmaintenance varchar(50) , significationcompetence varchar(50) );
insert into echellevalorisationactif ( idvaleur , valeur , significationremplacement , significationachat , significationmaintenance , significationcompetence )   values (  '1' , 'Faible' , 'Actif facilement remplacable' , 'Co�t d achat faible' , 'Co�t de maintenance faible' , 'Ne necessite pas de competence particuliere' );
insert into echellevalorisationactif ( idvaleur , valeur , significationremplacement , significationachat , significationmaintenance , significationcompetence )   values (  '2' , 'Moyen' , 'Actif remplacable dans la journee' , 'Co�t d achat moyen' , 'Co�t de maintenance moyen' , 'Necessite des connaissances de base' );
insert into echellevalorisationactif ( idvaleur , valeur , significationremplacement , significationachat , significationmaintenance , significationcompetence )   values (  '3' , 'Eleve' , 'Actif remplacable dans la semaine' , 'Co�t d achat eleve' , 'Co�t de maintenance eleve' , 'Necessite des connaissances techniques particulieres' );
insert into echellevalorisationactif ( idvaleur , valeur , significationremplacement , significationachat , significationmaintenance , significationcompetence )   values (  '4' , 'Tres eleve' , 'Actif remplacable dans le mois' , 'Co�t d achat tres eleve' , 'Co�t de maintenance tres eleve' , 'Necessite des connaissances specifiques' );
