import plotly.graph_objects as go
import pandas as pd

# Data (using the same DataFrame `df` from your previous data)
df = pd.read_csv('data/processed_data/summary_df.csv')
# Create the Plotly figure
fig = go.Figure()

# Add traces for each variant type
for variant_type in ['singletons', 'total_variants', 'clusters']:
    fig.add_trace(go.Bar(
        x=df['chr'],
        y=df[variant_type],
        name=variant_type,
        marker_color = {
            'singletons': '#999999',
            'total_variants': '#666666',
            'clusters': '#333333'
        }[variant_type]  # Neutral color palette
    ))

fig.update_layout(
    barmode='group',  # Ensure bars are grouped side-by-side
    xaxis_title='Chromosome',
    yaxis_title='Count of Singletons/Loci/Clusters',
    title='Variant Counts by Chromosome',
    xaxis={'categoryorder':'array', 'categoryarray':df['chr']} # Keep the order of the chromosomes
)
# font size
fig.update_layout(
    font=dict(
        size=25,
    )
)
#rename total_variants to loci
fig.for_each_trace(lambda trace: trace.update(name='Total Loci' if trace.name == 'total_variants' else trace.name))
fig.show()

if __name__ == '__main__':
    fig.show()