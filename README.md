## Simple flask API app

- create `.env` file(using `.env.example` as model) 
- To run use `docker-compose up`
- runs in http://localhost:8000

## Dependencies
- Docker
- mysql
- sqlalchemy
- flask

## Apps info
 * React app runs in port 3000 (using this default config)

## Local Development
## Docker install

1. Install dependencies
```
https://www.docker.com/products/docker-desktop
```

2. Clone repository
3. cd into repository folder

4. Create env files for docker and react 
- .env -> Replace variables with credentials and server variables
- ./poker-client/.env -> you need to set REACT_APP_HOST with your network ip
```
cp .env.example .env
cp ./poker-client/.env.example ./poker-client/.env
```

5. You can run the script me-ip.sh to set REACT_APP_HOST
```
./me-ip.sh
```

6. Run
```
docker-compose up
```