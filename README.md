# Yami-Api-Client

Create your private key

    openssl ecparam -name prime256v1 -genkey -noout -out ecdsa.priv.key

Create your public key

    openssl ec -in ecdsa.priv.key -pubout -out ecdsa.public.key

    





