#Obter dados datasus atraves da biblioteca microdatasus

install.packages("remotes")
remotes::install_github("rfsaldanha/microdatasus", force = TRUE)

library(microdatasus)
dados <- fetch_datasus(year_start = 2019, year_end = 2022, month_start = 1, month_end = 11, uf = "GO", information_system = "CNES-LT")
dados <- process_sim(dados)