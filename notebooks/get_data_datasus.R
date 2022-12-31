#Obter dados datasus atraves da biblioteca microdatasus
# Baixar biblioteca
#remotes::install_github("rfsaldanha/microdatasus", force = TRUE)

#Carrega biblioteca
library(microdatasus)

#Baixar dados referente aos leitos no estado de GO, no periodo de jan/19 a nov/22
dados <- fetch_datasus(year_start = 2019, year_end = 2022, month_start = 1, month_end = 11, uf = "GO", information_system = "CNES-LT")
#dados <- process_cnes(dados, information_system = "CNES-ST")

# Grava os dados em .csv
write.csv(dados, file = "../data/raw/cnes_lt-2019_2022.csv", row.names = TRUE)