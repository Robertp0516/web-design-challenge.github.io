import pandas as pd

cities = pd.read_csv("WebVisualizations\Resources\cities.csv")
cities_df = pd.DataFrame(cities)
cities_table = cities_df.to_html()
print(cities_table)