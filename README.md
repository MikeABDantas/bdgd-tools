# bdgd-tools
Conjunto de ferramentas em Python para trabalhar com BDGD (GDB -> SHP, extração de coordenadas, etc.)

BDGD Coordinate Extractor

Script em Python para extrair coordenadas geográficas (latitude e longitude) de elementos da BDGD (Base de Dados Geográfica da Distribuidora) a partir de arquivos no formato shapefile. O código utiliza a biblioteca GeoPandas para ler a camada e recuperar as coordenadas correspondentes ao atributo COD_ID.

Este utilitário é útil para operações de análise espacial, estudos de perdas técnicas, inspeção de transformadores, validação de bases e integração com ferramentas como OpenDSS, ArcGIS, QGIS e painéis de geoprocessamento.

Instale as dependências:

pip install geopandas
pip install shapely

BDGD GDB to Shapefile Converter

Script em Python para converter todas as camadas de uma BDGD (Base de Dados Geográfica da Distribuidora) do formato File Geodatabase (.gdb) para Shapefiles (.shp). O código utiliza as bibliotecas GeoPandas e Fiona para leitura e exportação automática de todas as feature classes da geodatabase. É recomendado ter QGIS ou ArcGIS Pro instalado no computador. Também é recomendado rodar direto do QGis.

Este código é útil para análises em ferramentas como OpenDSS, QGIS, ArcGIS, estudos de perdas técnicas, validação espacial e manipulação de dados geográficos.

Você precisa ter instalados:

pip install geopandas

É recomendado instalar a biblioteca fiona através da instalação do software QGIS.
