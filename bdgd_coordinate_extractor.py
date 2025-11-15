import geopandas as gpd
from shapely.geometry import Point

# Caminho do shapefile da camada de transformadores
shp_path = r"C:\Users\MikeABDantas\Documents\BDGDs convertidas de gdb para shp 2\UNTRMT.shp"

# Ler o shapefile
gdf = gpd.read_file(shp_path)

# Função para buscar coordenadas pelo COD_ID
def buscar_coordenadas(cod_id):
    # Filtra o GeoDataFrame pelo COD_ID
    result = gdf[gdf['COD_ID'] == cod_id]
    
    if result.empty:
        return None  # COD_ID não encontrado
    
    # Extrair coordenadas do primeiro registro encontrado
    geom = result.geometry.iloc[0]
    
    # Retornar latitude e longitude
    return geom.y, geom.x  # y = latitude, x = longitude
    
#def distancia_metros(cod_id_1,cod_id_2)

# Exemplo de uso
coords = buscar_coordenadas("FT4322")
if coords:
    print(f"Transformador FT4322: Latitude = {coords[0]}, Longitude = {coords[1]}")
else:
    print("COD_ID não encontrado")
