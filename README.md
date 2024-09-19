# Yami CLI Client

## Overview
This project is a CLI client for Yami API. it is devised in two sub commands groups (`eva001` to query leaks and `eva002` to query stealers).

  - `eva001`:
    - `search-domain` => search for leaks on a specific domain
  - `eva002`:
    - `hwid` => get a complete stealer record if you know the HWID of the target
    - `search-username` => run a collection of curated YQL queries to search by username in collections FTPCredentials, RDPCredentials and Passwords
    - `search-domain` => run a collection of curated YQL queries to search by domain in collections FTPCredentials, RDPCredentials and Passwords
    - `query` => run a custom YQL query

## Installation
```sh
python3 -m virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

You then need to set the environement variable `YAMI_URL` to the url of yami api, put url given by us in the `.env` file.

```sh
YAMI_URL=http://127.0.0.1:8080
```

### Create your private key
As a client of Yami API you must generate your own ECDSA private and public key pair. Once done please communicate your public key tou the YAMI admin.

```sh
openssl ecparam -name prime256v1 -genkey -noout -out ecdsa.priv.key
```
### Create your public key
```sh
openssl ec -in ecdsa.priv.key -pubout -out ecdsa.public.key
```

## Authentication
Tha Yami authentication require a domain and a JWT token signed by ecdsa private key.

:warning: **THE PRIVATE KEY IS USED ONLY LOCALY AND NOT SENT TO THE SERVER**

These value can be passed in the command line. If they are missing from the command line, they will be prompted.

Command line example:
```sh 
python ./yami-client.py -d USER -k ./dev.priv eva001 search-domain -s yami-no-kagami.moe
```

Prompt example:
```sh 
python ./yami-client.py eva001 search-domain -s yami-no-kagami.moe
```
In this case you will be prompted twice, once for the Auth Domain and once for the path to your private key : 
```
Auth domain: example.com
Priv key path: ./dev.priv
```

## Output style

Each command can produce either a json, a csv output or an xlsx. 

The json output is the default one. 

To generate a csv file pass the `-c` flag to the command line.

To generate a excel file pass the `-x` flag to the command line.

```sh
python ./yami-client.py eva002 search-username -s yami-no-kagami.moe # Generate a json file

python ./yami-client.py -c eva002 search-username -s yami-no-kagami.moe # Generate a CSV file

python ./yami-client.py -x eva002 search-username -s yami-no-kagami.moe # Generate a XLSX file
```

The results of the commands are saved in the `./query-results` directory.

## Commands details
### eva001 search-domain for leak in forums/sites
Json output:
```sh 
python ./yami-client.py eva001 search-domain -s yahoo.fr
```

```json
[
    {
        "email": "example1@yahoo.fr",
        "database": "zarafa.com",
        "dataclasses": ["email_address", "password", "salt", "userid", "username"]
    },
    {
        "email": "example2@yahoo.fr",
        "database": "zarafa.com",
        "dataclasses": ["email_address", "password", "salt", "userid", "username"]
    }
]
```

Csv output:
```sh 
python ./yami-client.py eva001 -c search-domain -s yahoo.fr
```

```csv
email,database,dataclasses
example1@yahoo.fr,zarafa.com,"email_address, password, salt, userid, username"
example2@yahoo.fr,zarafa.com,"email_address, password, salt, userid, username"
```

Excel output:

![image](https://github.com/user-attachments/assets/4723fb79-4635-42b9-86c1-10fb87474a63)



### eva002 search for leak in info-stealer
#### hwid
Json output:
```sh
python .\yami-client.py eva002 hwid -w XXXXXXXXXXXXXXX
```

```json
[
    {
        "user": {
            "hwid": "XXXXXXXXXXXXXXX",
            "telegram": "https://t.me/SOURCE",
            "build_id": "@BradMax",
            "ip": "10.0.0.42",
            "date": "10/2/2022 5:45:06 AM",
            "id": "00000000-0000-0000-0000-000000000000"
        },
        "passwords": [
            {
                "url": "https://www.netflix.com",
                "user_name": "email@example.com",
                "password": "123456789",
                "user_log_id": "00000000-0000-0000-0000-000000000000",
                "id": "11111111-0000-0000-0000-000000000000"
            }
        ],
        "rdp_credentials": [],
        "ftp_credentials": [],
        "tokens": [],
        "credit_cards": [],
        "stolen_files": []
    }
]
```
Csv output:
```sh
python .\yami-client.py -c eva002 hwid -w XXXXXXXXXXXXXXX
```

```csv
hwid,telegram,build id,ip,date stolen,url,username,password
XXXXXXXXXXXXXXX,https://t.me/SOURCE,@BradMax,10.0.0.42,10/2/2022 5:45:06 AM,https://www.netflix.com,email@example.com,123456789
```

#### search-username
Json output:
```sh
python .\yami-client.py eva002 search-username -u admin     
```

```json
[
    {
        "hwid": "XXXXXXXXXXXXXXX111",
        "telegram": "https://t.me/SOURCE",
        "build_id": "@ggfate",
        "ip": "10.0.0.42",
        "leak_date": "6/11/2023 9:58:06 AM",
        "url": "http://10.40.0.1",
        "user_name": "admin",
        "password": "admin",
        "credential_type": "Password"
    },
    {
        "hwid": "XXXXXXXXXXXXXXX222",
        "telegram": "https://t.me/SOURCE",
        "build_id": "@ggfate",
        "ip": "10.0.73.42",
        "leak_date": "6/10/2023 9:41:25 PM",
        "url": "http://192.168.43.168",
        "user_name": "admin",
        "password": "admin",
        "credential_type": "Password"
    }
]
```
Csv output:
```sh
python .\yami-client.py -c eva002 search-username -u admin     
```

```csv
hwid,telegram,build_id,ip,leak_date,url,user_name,password,credential_type
XXXXXXXXXXXXXXX111,https://t.me/SOURCE,@ggfate,10.0.0.42,6/11/2023 9:58:06 AM,http://10.40.0.1,admin,admin,Password
XXXXXXXXXXXXXXX222,https://t.me/SOURCE,@ggfate,10.0.73.42,6/10/2023 9:41:25 PM,http://192.168.43.168,admin,admin,Password

```


#### search-domain
Json output:
```sh
python .\yami-client.py eva002 search-domain -d example.com     
```

```json
[
    {
        "hwid": "XXXXXXXXXXXXXXX111",
        "telegram": "https://t.me/SOURCE",
        "build_id": "@ggfate",
        "ip": "10.0.0.42",
        "leak_date": "6/11/2023 9:58:06 AM",
        "url": "http://10.40.0.1",
        "user_name": "admin",
        "password": "admin",
        "credential_type": "Password"
    },
    {
        "hwid": "XXXXXXXXXXXXXXX222",
        "telegram": "https://t.me/SOURCE",
        "build_id": "@ggfate",
        "ip": "10.0.73.42",
        "leak_date": "6/10/2023 9:41:25 PM",
        "url": "http://192.168.43.168",
        "user_name": "admin",
        "password": "admin",
        "credential_type": "Password"
    }
]
```
Csv output:
```sh
python .\yami-client.py -c eva002 search-username -u admin     
```

```csv
hwid,telegram,build_id,ip,leak_date,url,user_name,password,credential_type
XXXXXXXXXXXXXXX111,https://t.me/SOURCE,@ggfate,10.0.0.42,6/11/2023 9:58:06 AM,http://10.40.0.1,admin,admin,Password
XXXXXXXXXXXXXXX222,https://t.me/SOURCE,@ggfate,10.0.73.42,6/10/2023 9:41:25 PM,http://192.168.43.168,admin,admin,Password

```
