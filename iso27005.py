#!/usr/bin/python
# -*- coding: cp1252 -*-
#
from bottle import route,run,install
from bottle_pgsql import PgSQLPlugin

install(PgSQLPlugin('host=localhost port=5432 dbname=iso27005 user=postgres password=secret'))

@route('/iso27005')
def help():
    sDoc = ""
    sDoc = sDoc + "Exemple de requete pour connaitre l echelle de valorisation des actifs:" + "<br>"
    sDoc = sDoc + "-    /iso27005/eva/1" + "<br><br>"
    sDoc = sDoc + "Exemple de requete pour connaitre les criteres d impact:" + "<br>"
    sDoc = sDoc + "-    /iso27005/ci/2" + "<br><br>"
    sDoc = sDoc + "Exemple de requete pour connaitre les echelles de consequence:" + "<br>"
    sDoc = sDoc + "-    /iso27005/ec/3" + "<br><br>"
    sDoc = sDoc + "Exemple de requete pour connaitre les criteres d acceptation des risques:" + "<br>"
    sDoc = sDoc + "-    /iso27005/car/1" + "<br><br>"
    sDoc = sDoc + "Exemple de requete pour connaitre les echelles de vraisemblance:" + "<br>"
    sDoc = sDoc + "-    /iso27005/ev/4" + "<br><br>"
    sDoc = sDoc + "Exemple de requete pour connaitre les criteres d evaluation des risques:" + "<br>"
    sDoc = sDoc + "-    /iso27005/cer/4,3" + "<br><br>"
    return sDoc

@route('/iso27005/eva/<v1>')
def eva(db,v1):
    #
    #   Affiche l echelle de valorisation des actifs
    #
    db.execute('select * from echellevaloraisationactif where idvaleur=' + str(v1))     
    row = db.fetchone()
    if row:
        return row

@route('/iso27005/ci/<v1>')
def ci(db,v1):
    #
    #   Affiche les criteres d impact
    #
    db.execute('select * from critereimpact where idimpact=' + str(v1))     
    row = db.fetchone()
    if row:
        return row

@route('/iso27005/ec/<v1>')
def ec(db,v1):
    #
    #   Affiche les echelles de consequence
    #
    db.execute('select * from echelleconsequence where idconsequence=' + str(v1))     
    row = db.fetchone()
    if row:
        return row

@route('/iso27005/car/<v1>')
def car(db,v1):
    #
    #   Affiche les criteres d acceptation des risques
    #
    db.execute('select * from critereacceptionrisque where idrisque=' + str(v1))     
    row = db.fetchone()
    if row:
        return row
    
@route('/iso27005/ev/<v1>')
def ev(db,v1):
    #
    #   Affiche les echelles de vraisemblance
    #
    db.execute('select * from echellevraisemblance where idvraisemblance=' + str(v1))     
    row = db.fetchone()
    if row:
        return row

@route('/iso27005/cer/<v1>,<v2>')
def cer(db,v1,v2):
    #
    #   Affiche les criteres d evaluation des risques
    #
    db.execute('select * from critereevaluationrisque where idimpact=' + str(v1) + ' and idvraisemblance=' + str(v2))     
    row = db.fetchone()
    if row:
        return row
    
run(host='0.0.0.0', port=8080, debug=True)
