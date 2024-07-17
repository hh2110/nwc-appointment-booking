from datetime import datetime as dt

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State
from whitenoise import WhiteNoise

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Reference the underlying flask app (Used by gunicorn webserver in Heroku production deployment)
server = app.server

# Enable Whitenoise for serving static files from Heroku (the /static folder is seen as root by Heroku)
server.wsgi_app = WhiteNoise(server.wsgi_app, root="static/")


# Define Dash layout
def create_dash_layout(app):
    # Set browser tab title
    app.title = "Appointment Booking"

    url = dcc.Location(id="url", refresh=False)

    # Header
    header = html.H5("Appointment Booking", className="display-3")
    paragraph = html.P(
        "Book your appointment easily for", className="lead", id="paragraph"
    )

    # Calendar
    calendar = dbc.Form(
        [
            dbc.Label("Choose Date", html_for="date-picker"),
            dcc.DatePickerSingle(
                id="date-picker",
                min_date_allowed=dt(1995, 8, 5),
                max_date_allowed=dt(2017, 9, 19),
                initial_visible_month=dt(2017, 8, 5),
                date=str(dt(2017, 8, 25, 23, 59, 59)),
            ),
        ]
    )

    # Time slots
    time_slots = dbc.Form(
        [
            dbc.Label("Choose Time Slot", html_for="time-slot"),
            dcc.Dropdown(
                id="time-slot",
                options=[
                    {"label": "9:00 - 10:00", "value": "9:00 - 10:00"},
                    {"label": "10:00 - 11:00", "value": "10:00 - 11:00"},
                    # Add more time slots as needed
                ],
                value="9:00 - 10:00",
            ),
        ]
    )

    # Submit button
    submit_button = html.Button("Book Appointment", id="submit-button", n_clicks=0)

    # Notification
    notification = html.Div(id="notification")

    # Assemble dash layout
    app.layout = dbc.Container(
        [header, url, paragraph, calendar, time_slots, submit_button, notification],
        fluid=True,
    )

    return app


# Construct the dash layout
app = create_dash_layout(app)


# Define callback to handle button click
@app.callback(
    Output("notification", "children"),
    [Input("submit-button", "n_clicks")],
    [State("date-picker", "date"), State("time-slot", "value")],
)
def update_output(n_clicks, date, time_slot):
    if n_clicks > 0:
        return f"Appointment booked for {date} at {time_slot}!"
    else:
        return ""


@app.callback(
    Output("paragraph", "children"),
    [Input("url", "pathname")],
    suppress_callback_exceptions=True,
)
def update_paragraph(pathname):
    # Extract the doctor parameter from the URL
    try:
        doctor, token = pathname[1:].split("&")
    except ValueError:
        doctor = None
        token = None

    if doctor:
        return f"Book your appointment easily with {doctor=} for {token=}"
    else:
        return "No doctor selected"


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8050)
