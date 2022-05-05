# instalação
docker build -t ams-ac2-ingrid -f ./Dockerfile .


## Docker com Postgres
#### Para ajustar o IP do banco de dados
> docker-compose up
>
> docker network inspect bridge
> 
> ver o ip do container do banco de dados
> 
> parar o container, ajustar o ip em config.py e subir de novo

#### Para criar a tabela desse execício
> docker-compose run web /usr/local/bin/python create_db.py

#### Para acessar a url e inserir os dados
> docker-compose up
> 
> acessar a porta que foi gerada (docker labs) ou a porta definida na aplicação

#### Para verificar a tabela criada e os dados salvos
> docker-compose run web /usr/local/bin/python create_db.py
> 
> docker ps
> 
> **pegar o ID do container postgres**
> 
> docker exec -it ___ed68d52e4ad3___ /bin/bash - alterar o id pelo id coletado na fase acima
> 
> su postgres
> 
> psql -U sis_web
> 
> select * from alunos;
