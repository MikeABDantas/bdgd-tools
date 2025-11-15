import geopandas as gpd
import fiona
import os

# Caminho da sua File Geodatabase (.gdb)
gdb_path = r"C:\Users\MikeABDantas\Documents\Neoenergia_Brasilia_5160_2023-12-31_V11_20241211-0819.gdb\Neoenergia_Brasilia_5160_2023-12-31_V11_20241211-0819.gdb"

# Pasta de saída para os shapefiles
output_folder = r"C:\Users\MikeABDantas\Documents\BDGDs convertidas de gdb para shp 2"

# Listar todas as camadas da GDB
layers = fiona.listlayers(gdb_path)
print("Camadas encontradas na GDB:", layers)

# Converter cada camada em shapefile
for layer_name in layers:
    try:
        # Ler a camada
        gdf = gpd.read_file(gdb_path, layer=layer_name)

        if gdf.empty:
            print(f"Camada '{layer_name}' está vazia. Pulando...")
            continue

        # Gerar caminho do shapefile de saída
        shp_name = layer_name

        shp_path = os.path.join(output_folder, f"{shp_name}.shp")

        # Salvar como shapefile
        gdf.to_file(shp_path, driver="ESRI Shapefile", encoding="UTF-8")
        print(f"Camada '{layer_name}' salva em {shp_path}")

    except Exception as e:
        print(f"Erro ao converter a camada '{layer_name}': {e}")

print("Conversão concluída!")
