# DATASUS

#  Análise Exploratória sobre a evolução dos leitos hospitalares no Estado de Goiás durante a pandemia de COVID-19.
O projeto a seguir trata-se de uma análise sobre os leitos hospitalares no estado de Goias, obtidos a partir do repositório DATASUS.

<p align='center'>
    <img src = 'images/Datasus-logo.jpg'>
</p>
<br>    


## 1. Sobre o DATASUS

O DATASUS (Departamento de Informática do Sistema Único de Saúde) é um órgão do governo brasileiro responsável por gerenciar e promover a informatização dos serviços de saúde no país. O orgão atua como uma central de dados para a saúde, coletando e armazenando informações sobre o sistema de saúde brasileiro, incluindo dados de registro de doenças, procedimentos médicos, medicamentos e outros, disponibilizando esses dados para pesquisadores, profissionais de saúde e outros interessados em utilizá-los para fins de análise e estudo. Além disso, o DATASUS também oferece serviços e ferramentas online para ajudar a promover a qualidade e a eficiência dos serviços de saúde no país.
<br><br>    
    
### 1.1 O problema de negócio
    
O projeto foi desenvolvido para avaliar a evolução da capacidade hospitalar (leitos) no Estado de Goiás durante a pandemia de COVID-19, entendendo a distribuição de leitos diante do período obtido. A partir dessas análises servirá de base para possíveis cenários do ano de 2023, visto que o número de casos tende a aumentar com a nova onda presente. Abaixo pontos que devem ser esclarecidos pela análise:
    - Distribuição geográfica dos leitos por municipio antes e depois da pandemia;
    - Evolução do número de leitos no período;
    - Observar a se em algum momento houve declínio da capacidade hospitalar instalada;
    - Comparar a quantidade de leitos SUS e não SUS durante o período;
    - Previsão de leitos para o ano de 2023.
<br><br>
    
### 1.2. Base de dados
    
Os dados foram obtidos através da biblioteca microdatasus[1], observando o período de Janeiro de 2019 a Novembro de 2022, para entender como estava a capacidade hospitalar do Estado de Goias antes da descoberta do nCoV-2019 em Dezembro de 2019, ocorridos registros na China, até Novembro de 2022 ano em que os casos começaram a diminuir.  
    
1. SALDANHA, Raphael de Freitas; BASTOS, Ronaldo Rocha; BARCELLOS, Christovam. Microdatasus: pacote para download e pré-processamento de microdados do Departamento de Informática do SUS (DATASUS). Cad. Saúde Pública, Rio de Janeiro , v. 35, n. 9, e00032419, 2019 . Available from http://ref.scielo.org/dhcq3y.
<br><br>    

## 2. Estratégia de Solução
O projeto foi desenvolvido através do método CRISP-DM, para atender os seguintes ciclos:

**Ciclo 01:** Análise do número de leitos durante o período de 2019 a 2022, quantidade total de leitos existentes e total de leitos SUS e declínio da capacidade hospitalar instalada.

**Ciclo 02:** Criar um dashboard do mapa do Estado de Goiás, mostrando a quantidade total de leitos (SUS e não SUS) por município do período de 2019 a 2022.

**Ciclo 03:** Criar uma previsão do número total de leitos que será necessário para os próximos meses do ano de 2023. Para isso, coletar a evolução de casos de COVID-19 do período em que foi descorberto o vírus (Dezembro 2019) a Dezembro de 2022.

