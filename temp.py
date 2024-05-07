import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go

def generate_plot():
    # Generate some sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Create a Matplotlib plot
    plt.plot(x, y)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Sample Plot')

    # Save the plot as a PNG image
    plt.savefig('sample_plot.png')

    # Convert the Matplotlib plot to Plotly format
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='sin(x)'))

    # Export the plot to HTML file
    fig.write_html('sample_plot.html')

if __name__ == "__main__":
    generate_plot()

