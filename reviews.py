import zipfile
import pandas as pd

# Open the ZIP file and read the CSV data
with zipfile.ZipFile('data/winemag-data-130k-v2.csv.zip', 'r') as zip_file:
    with zip_file.open('winemag-data-130k-v2.csv') as csv_file:
        df = pd.read_csv(csv_file, index_col=0)

# calculate average number of points and number of reviews for each country
reviews_per_country = df['country'].value_counts()
average_points_per_country = df.groupby('country')['points'].mean().round(1)

# create summary DF
summary_df = pd.DataFrame({
    'count': reviews_per_country,
    'points': average_points_per_country
})
summary_df.index.name = 'country'

# write summary data to a new file in `data` folder
summary_df.to_csv('data/reviews-per-country.csv')

# output summary DF
print(summary_df)

