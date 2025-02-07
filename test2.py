import requests
import csv
import json
import naver_real



# Extract article list


# Define CSV file name
csv_filename = "real_estate_listings.csv"

# Define the fields to extract
fields = [
    "articleNo", "articleName", "tradeTypeName", "dealOrWarrantPrc", "rentPrc",
    "floorInfo", "areaName", "area1", "area2", "direction", "articleConfirmYmd",
    "buildingName", "realtorName", "latitude", "longitude"
]

# Open CSV file and write data
with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    
    # Write header
    writer.writeheader()
    

    page = 1
    while True:
        print(f'fetching page={page}')
        response = naver_real.fetch_hellio(page)
        data = response.json()  # Convert response to JSON

        articles = data.get("articleList", [])

         # Stop if no more data
        if not articles:
            print("✅ No more data. Stopping.")
            break

        print(f'got {len(articles)} articles for page={page}')

        # Write each row
        for article in articles:
            writer.writerow({field: article.get(field, "") for field in fields})

        # Check if there are more pages
        if not data.get("isMoreData", False):
            print("✅ Reached last page. Stopping.")
            break

        page = page + 1

print(f"✅ Data saved successfully in {csv_filename}")
