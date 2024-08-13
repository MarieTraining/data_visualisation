import plotly.graph_objects as go
import numpy as np

# Generate sample data
np.random.seed(0)
n = 100
x = np.random.randn(n)
y = np.random.randn(n)
z = np.random.randn(n)
colors = np.random.rand(n)

# Create 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=8,
        color=colors,
        colorscale='Viridis',
        opacity=0.8
    )
)])

fig.update_layout(
    title='3D Scatter Plot',
    scene=dict(
        xaxis_title='X Axis',
        yaxis_title='Y Axis',
        zaxis_title='Z Axis'
    )
)

fig.show()
