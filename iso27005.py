#!/usr/bin/python
# -*- coding: cp1252 -*-
#
from bottle import route,run,install
from bottle_pgsql import PgSQLPlugin

install(PgSQLPlugin('host=localhost port=5432 dbname=iso27005 user=postgres password=secret'))

@route('/iso27005')
def help():
    sDoc = ""
    sDoc = sDoc + "Exemple de requete pour connaitre le critere d'impact :" + "<br>"
    sDoc = sDoc + "-    /iso27005/ci/2" + "<br><br>"
    sDoc = sDoc + "Exemple de requete pour connaitre l'echelle de consequence :" + "<br>"
    sDoc = sDoc + "-    /iso27005/ec/3" + "<br><br>"
    return sDoc

@route('/iso27005/ci/<v1>')
def ci(db,v1):
    #
    #   Affiche le critere d'impact
    #
    db.execute('select * from critereimpact where idimpact=' + str(v1))     
    row = db.fetchone()
    if row:
        return row

@route('/iso27005/cc/<v1>')
def question(db,v1):
    #
    #   Affiche la question
    #
    db.execute('select * from echelleconsequence where idconsequence=' + str(v1))     
    row = db.fetchone()
    if row:
        return row
    
run(host='0.0.0.0', port=8080, debug=True)
