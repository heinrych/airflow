Criando ambiente local

Clone o repositório
Mude para o diretóri nifi/Auth/, exclua o termo '_local' do nome dos aquivos e configura suas credencais.
Abra o terminal e entre no diretório poli-nifi
Execute o comando docker-compose up --build -d  no terminal para criar a imagem do Nifi com o python e suas devidas bibliotecas.
Acesse o ambiente pela url: http://localhost:8080/airflow/

Faça o login: airflow, airflow

Para modificar o template do nifi execute docker cp nifi_python:/opt/nifi/nifi-current/conf/flow.xml.gz ./ na raiz do projeto.

obs:
url webhook : https://webhook-nifi.prod.cloud.polichat.com.br