# demo-ca
demo-ca



Webserver Starten

python3 demo.py 

Mit zertifikat aufrufen - 
curl --cacert ca.crt https://localhost:8443

Ohne zertifikat aufrufen - 
curl https://localhost:8443
