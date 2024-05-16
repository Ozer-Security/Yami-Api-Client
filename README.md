# Yami-Api-Client

## Create your private key

    openssl ecparam -name prime256v1 -genkey -noout -out ecdsa.priv.key

## Create your public key

    openssl ec -in ecdsa.priv.key -pubout -out ecdsa.public.key

Send us your public key to create your account 

## Generate your token    

    python3 -m virtualenv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    python3 gen_token.py ecdsa.priv.key
    
## Use curl or openapi docs

    curl -X 'GET' '{API_HOST}:{API_PORT}/v1/leaks/query?domain={DOMAIN}&skip=0&limit=0' -H 'accept: application/json' -H 'x-yami-domain: {ACCOUNT}' -H 'x-yami-token: {JWT_TOKEN}'
    
    
## Extract unique values with jq (example given = email)

    Pipe your curl command or its output :
    | jq -r '.result[] | .email'
    This will output only the emails

