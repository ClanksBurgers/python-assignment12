import plotly.express as px
import plotly.data as pldata
import pandas as pd

# Load the wind dataset
df = pldata.wind(return_type='pandas')

# Print the first and last 10 lines
print('First 10 rows:')
print(df.head(10))
print('\nLast 10 rows:')
print(df.tail(10))

# Clean the 'strength' column: remove non-numeric characters and convert to float
df['strength'] = df['strength'].astype(str).str.replace(r'[^\d.]+', '', regex=True).astype(float)

# Create interactive scatter plot
fig = px.scatter(df, x='strength', y='frequency', color='direction',
                 title='Wind Strength vs Frequency by Direction',
                 labels={'strength': 'Strength', 'frequency': 'Frequency', 'direction': 'Direction'})

# Save the plot as HTML
fig.write_html('wind.html')

# Optionally, open the HTML file in the default browser (uncomment if desired)
# import webbrowser
# webbrowser.open('wind.html')
