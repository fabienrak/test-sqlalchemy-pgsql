from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

##### configuration database #####
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admindev007@127.0.0.1:5432/datatest"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#### Model ####
class Etudiant(db.Model):
    __tablename__='etudiant'
    
    id = db.Column(db.Integer, primary_key=True)
    nom_complet = db.Column(db.String())
    classe = db.Column(db.String())
    
    def __init__(self, nom_complet, classe):
        self.nom_complet = nom_complet
        self.classe = classe
    
    def __repr__(self):
        return f"<Etudiant {self.nom_complet}>"
    
    @property
    def serialize(self):
        ## serialisation donnee
        return {"nom_complet":self.nom_complet, "classe": self.classe}        
    

### Endpoint ###
@app.route('/etudiant', methods=['GET','POST'])
def handle_etudiant():
    ### POST request ###
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_etudiant = Etudiant(nom_complet=data['nom_complet'], classe=data['classe'])
            db.session.add(new_etudiant)
            db.session.commit()
            return {"message": f"Etudiant  {new_etudiant.nom_complet} creer avec success !!"}
        else:
            return {"error":"Requete json malformer "}
        
    ### GET request ###
    elif request.method == 'GET':
        etudiant = Etudiant.query.all()
        return jsonify([et.serialize for et in etudiant])    
    
          
@app.route('/')
def initialisation():
    return {'sample':'Flask Project for test'}

if __name__ == '__main__':
    app.run(debug=True)  