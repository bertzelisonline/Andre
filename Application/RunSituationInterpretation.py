#Dateien:
#1. Datei (RoadNetwork): Hier ist das Interface definiert. Sobald die Daten von ADTF ankommen, erzeuge eine Klasse, die genauso aufgebaut ist wie die IDL und befülle sie. Denk an die Initialisierung aller Werte
#2. Datei (Ontology): HIer kommt alles rein, was die Ontology betrifft
#3. Application (RunSituationinterpreter): in Zeile 17-24 siehst du den Runner

#Vorschlag: Erzeuge dir eine Logger Klasse (nimm dazu mein Repository (Syncar))

#Reihenfolge:
#1. Wir erzeugen ein RoadNetwork: https://cryptpad.fr/code/#/2/code/edit/fhDT+3l8kgxTE-OqqSvoOC5V/
#2. Dann erzeugen wir ein Ontologie-Objekt: https://cryptpad.fr/code/#/2/code/edit/PauRw1EHojUnUCkLzBeda8Nk/
#3. Dann erstellen wir den Ontologie-Raum: https://cryptpad.fr/code/#/2/code/edit/PauRw1EHojUnUCkLzBeda8Nk/ - Zeile 170
#4. Dann speichern wir den Ontology-Raum: https://cryptpad.fr/code/#/2/code/edit/PauRw1EHojUnUCkLzBeda8Nk/ - Zeile 234



from ADTFInstance.RoadNetwork import RoadNetwork
from LogicLayer.Ontology import Ontology

road_network = RoadNetwork()
ontology = Ontology("New", "Path", road_network)
ontology.load_ontology
ontology.create_ontology_space()
ontology.save_ontology()