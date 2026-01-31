from matplotlib.figure import Figure

def create_summary_chart(summary):
    fig = Figure(figsize=(5, 4))
    ax = fig.add_subplot(111)

    numeric_items = {
        k: v for k, v in summary.items()
        if isinstance(v, (int, float))
    }

    ax.bar(numeric_items.keys(), numeric_items.values())
    ax.set_title("Summary Metrics")
    ax.tick_params(axis="x", rotation=45)

    return fig
