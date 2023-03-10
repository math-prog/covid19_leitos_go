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
 - Observar se em algum momento houve declínio da capacidade hospitalar instalada;
 - Comparar a quantidade de leitos SUS e não SUS durante o período;
 - Previsão de leitos para o ano de 2023.
<br><br>
    
### 1.2. Base de dados
    
Os dados foram obtidos através da biblioteca microdatasus[1], observando o período de Janeiro de 2019 a Novembro de 2022, para entender como estava a capacidade hospitalar do Estado de Goias antes da descoberta do nCoV-2019 em Dezembro de 2019 até Novembro de 2022, ano em que os casos começaram a diminuir.  
    
1. SALDANHA, Raphael de Freitas; BASTOS, Ronaldo Rocha; BARCELLOS, Christovam. Microdatasus: pacote para download e pré-processamento de microdados do Departamento de Informática do SUS (DATASUS). Cad. Saúde Pública, Rio de Janeiro , v. 35, n. 9, e00032419, 2019 . Available from http://ref.scielo.org/dhcq3y.
<br><br>    

<details><summary>Variáveis originais do dataset:</summary><br>   
    Abaixo o dicionário de dados, de acordo com a documentação presente no site ftp://ftp.datasus.gov.br/dissemin/publicos/CNES/200508_/doc/IT_CNES_1706.pdf.
    <br>

| SEQ | CAMPO | TIPO E TAM | DESCRIÇÃO |
|-----|-------|------------|-----------|
| 1 | CNES | CHAR (7) | Número nacional do estabelecimento de saúde |
| 2 | CODUFMUN | CHAR (6) | Código do município do estabelecimento UF+ MUNIC (sem dígito)
| 4 | REGSAUDE | CHAR (6) | Código da região de saúde
| 5 | MICR_REG | CHAR (4) | Código da micro-região de saúde
| 6 | DISTRSAN | CHAR (4) | Código do distrito sanitário
| 7 | DISTRADM | CHAR (1) | Código do distrito administrativo
| 8 | PF_PJ | CHAR (1) | Indicador de pessoa: 1-Física 3-Jurídica
| 9 |CPF_CNPJ | CHAR (14) | CPF do Estabelecimento, caso pessoa física OU CNPJ, caso pessoa jurídica
| 10 | NIV_DEP | CHAR (1) | Grau de dependência: 1-Individual 3-Mantida
| 11 | CNPJ_MAN | CHAR (14) | CNPJ da mantenedora do Estabelecimento
| 12 | ESFERA_A | CHAR (2) | Código da esfera administrativa
| 13 | ATIVIDAD | CHAR (2) | Código da atividade de ensino
| 14 | RETENCAO | CHAR (2) | Código de retenção de tributos
| 15 | NATUREZA | CHAR (2) | Código da natureza da organização
| 16 | CLIENTEL | CHAR (2) | Código de fluxo da clientela
| 17 | TP_UNID | CHAR (2) | Tipo de unidade (Estabelecimento)
| 18 | TURNO_AT | CHAR (2) | Código de turno de atendimento
| 19 | NIV_HIER | CHAR (2) | Código do nível de hierarquia
| 20 | TERCEIRO | CHAR (1) | O estabelecimento é terceiro: 1-Sim 0-Não
| 21 | TP_LEITO | CHAR (2) | Tipo do LEITO
| 22 | CODLEITO | CHAR (2) | Especialidade do LEITO
| 23 | QT_EXIST | NUMERIC (4) | Quantidade de leitos existentes
| 24 | QT_CONTR | NUMERIC (4) | Quantidade de leitos contratados
| 25 | QT_SUS | NUMERIC (4) | Quantidade de leitos para o SUS
| 26 | QT_NSUS| CHAR(1) | Indicador de EQUIPAMENTO NÃO DISPONÍVEL para o SUS, onde: 1 = SIM 0 = NÃO
| 27 | COMPETEN | CHAR (6) | Ano e Mês de competência da informação (AAAAMM)
| 28 | NAT_JUR | CHAR (4) | Natureza Jurídica
</details>
<br>
<details><summary>Variáveis criadas durante a etapa de Feature Engineering:</summary><br>
    
| SEQ | CAMPO | TIPO E TAM | DESCRIÇÃO |
|-----|-------|------------|-----------|
| 29 | ANO | DATETIME | Ano da Competência
| 30 | MES | DATETIME | Mês da Competência    
| 31 | DIA | DATETIME | Dia da Competência
| 32 | MUNICIPIO | STR | Cidade referente ao código do município de estabelecimento   
</details>    
<br>

## 2. Estratégia de Solução
O projeto foi desenvolvido através do método CRISP-DM, para atender os seguintes ciclos:

**Ciclo 01:** Análise do número de leitos durante o período de 2019 a 2022, observando quantidade total de leitos existentes e leitos SUS e verificação do declínio ou não da capacidade hospitalar instalada.

**Ciclo 02:** Criar um dashboard do mapa do Estado de Goiás, mostrando a quantidade total de leitos (SUS e não SUS) por município do período de 2019 a 2022.

**Ciclo 03:** Criar uma previsão do número total de leitos que será necessário para os próximos meses do ano de 2023. Para isso, coletar a evolução de casos de COVID-19 do período em que foi descorberto o vírus (Dezembro 2019) a Dezembro de 2022.

## 3. EDA

### Evolução de Leitos durante os anos de 2019 a 2022 e verificação de declínio hospitalar
<p align='center'>
    <img src = 'images/evolucao-leitos-2019_2022.png'>
</p>
<br> 
Durante o ano de 2019 a distribuição total de leitos permanece praticamente a mesma, variando de 19.050 a 19.200. Esse valor começa a subir depois de declarada a pandemia (Mar/2020) pela OMS. Desse período o número de leitos cresce até Dez/21, mês com a maior quantidade de unidades chegando ao valor próximo de 23.000. De Jan/22 até Nov/22 os números começam a cair, chegando próximo a 21.000 unidades existentes. 

### Comparação da quantidade total de leitos e apenas SUS durante os períodos abaixo:
<br>

**Período de Jan/19 a Fev/20:**

<p align='center'>
    <img src = 'images/leitos-2019_2020.png'>
</p><br>

**Período de Mar/20 a Fev/21:**

<p align='center'>
    <img src = 'images/leitos-2020_2021.png'>
</p><br>

**Período de Mar/21 a Fev/22:**

<p align='center'>
    <img src = 'images/leitos-2021_2022.png'>
</p><br>

**Período de Mar/22 a Nov/22:**

<p align='center'>
    <img src = 'images/leitos-mar2022-nov2022.png'>
</p><br>

Durante esse período, pode-se observar que a quantidade de Leitos SUS gira em torno de 59% a 61% da quantidade total de Leitos existentes, tendo o período de 2021 a 2022 uma proporção menor, 57,8%.

| **Tipo de leito** | **Jan/19 a Fev/20** | **Mar/20 a Fev/21** | **Mar/21 a Fev/22** | **Mar/22 a Nov/22** |
|---------------|-----------------|-----------------|-----------------|-----------------|
| Leitos totais | 19.311 | 21.500 | 22.730 | 21.225 |
| Leitos SUS    | 11.521 | 12.800 | 13.137 | 13.099 |
| Porcentagem   | 59,6%  | 59,5%  | 57,8%  | 61,7%  |

## 4. Próximos ciclos:
<br>

**4.1. Dashboard do Estado de Goiás referente a distribuição de leitos por municípios**
<br>

Essa Etapa trará um dashboard construído na ferramenta plotly, acompanhando o período de Janeiro de 2019 a Novembro de 2022, mostrando os valores totais de Leitos Existentes, Leitos SUS e não SUS por Município, juntamente com um ranking das TOP 5 cidades com maior quantidade de leitos existentes no período selecionado e as TOP 5 cidades com menor quantidade.
<br>

**4.2. Previsão de Leitos hospitalares para o ano de 2023**
<br>

Visto que está vindo uma nova onda de COVID-19 para o ano de 2023, montar um modelo de séries temporais em que mostra a quantidade de leitos (Totais e SUS) que haverão para cada mês do ano observado. Para isso, deve-se obter os dados dos casos de COVID-19 no Estado de Goiás durante todo o período analisado para os leitos hospitalares, levando-se em conta casos assintomáticos, sintomas leves, de internação e óbitos, para entender o comportamento da quantidade total de leitos e o que influencia essa variação para a criação de um modelo de previsão para o ano de 2023.

