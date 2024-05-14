# Yami-Api-Client

Create your private key

    openssl ecparam -name prime256v1 -genkey -noout -out ecdsa.priv.key

Create your public key

    openssl ec -in ecdsa.priv.key -pubout -out ecdsa.public.key

   Send us your public ket to create your account 

Generate your token    

    python3 -m virtualenv .venv
    source .venv/bin/activate
    python3 gen_token.py ecdsa.priv.key

Use curl or openapi docs

    curl -X 'GET' '{API_HOST}:{API_PORT}/v1/leaks/query?domain={DOMAIN}&skip=0&limit=0' -H 'accept: application/json' -H 'x-yami-domain: {ACCOUNT}' -H 'x-yami-token: {JWT_TOKEN}'
    
    




