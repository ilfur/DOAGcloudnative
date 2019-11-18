DOAGRepository.git

Enthält Python-Skripte zum Laden von Daten (LoopVAG) und Bereitstellung als REST Service (DeparturesVAG).
Die Daten werden alle 5 Minuten von den OpenData Seiten des Nürnberger Verkerhrsnetzes abgeholt.

Damit die Zugriffe funktionieren sind in den Python-Skripten die ADMIN-Kenwörter anzupassen und die TNS Connect Informationen:
Eine Autonome Datenbank bietet ein Wallet zum Download mit darin enthaltener TNSNAMES.ORA und Service-Namen - bitte eien daraus auswählen und eintragen :-)

Weiter enthalten sind Deployment Infos für Docker (Dockerfile) und Kubernetes (app.yaml). In app.yaml ist der Name des verwendeten Docker-Images zu ändern...

