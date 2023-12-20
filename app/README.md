# Api 
Projet monté à partir du modèle pip freeze > requirements

## Installation
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
Configurer un secret jwt
```bash
echo "secret: 'xxxx'" > confid/jwt.yml
```

Configurer un user d'api
```bash
cat << EOF > config/api_users.yml
users:
    unusername: unpassword
EOF
```
### Lancement local
```bash
./server.py
```
### Routes
Récupérer un tokent d'auth : 
```bash
curl -X POST -H 'Content-Type: application/json' -d '{"user":"unusername","password":"unpassword"}' "http://127.0.0.1:8000/auth"
```

Uploader un fichier: 
```bash
curl -X POST  -H 'Content-Type: application/json' -H "Bearer: <le token récupéré plus haut>" -F "file=@path/to/your/file.txt" http://localhost:8000/upload
```


## Contribuer à ce repository
Mettre à jour les requirements avant de pusher : 
```bash
pip freeze > requirements.txt
```