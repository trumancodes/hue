import json
import pandas as pd

with open('color_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

combined_df = pd.DataFrame()
seen_hex_colors = []

for brand_data in data:
    for brand, colors in brand_data.items():
      brand_df = pd.DataFrame(colors)
      brand_df['brand'] = brand
      combined_df = pd.concat([combined_df, brand_df], ignore_index=True)

      for _, row in brand_df.iterrows():
        if (brand, row['hex']) not in seen_hex_colors:
          seen_hex_colors.append((brand, row['hex']))
        else:
          combined_df.drop_duplicates(subset=['hex', 'brand'], keep='first', inplace=True)

with open('processed_data.json', 'w') as f:
    json.dump(combined_df.to_dict('records'), f)
