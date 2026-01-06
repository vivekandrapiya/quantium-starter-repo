import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px


df = pd.read_csv("data/output.csv")


df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")


fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "Date": "Date",
        "Sales": "Sales ($)"
    }
)


app = Dash(__name__)


app.layout = html.Div(
    children=[
        html.H1(
            "Soul Foods – Pink Morsel Sales Visualiser",
            style={"textAlign": "center"}
        ),
        dcc.Graph(
            id="sales-line-chart",
            figure=fig
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
