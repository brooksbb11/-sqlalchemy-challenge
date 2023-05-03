# Import the dependencies.
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine=create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base=automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session=Session(engine)

#################################################
# Flask Setup
#################################################
app=Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")

def welcome():
    """List all available api routes"""

    return (
        f"Avaiable Routes for HI Weather:<br/>"
        f"-- Daily Precipitation for 2016-2017 Season: <a 
        href=\"api/v1.0/precipitation\">/api/v1.0/precipitation<a><br/>"
        f"-- Weather Stations: <a
        href=\"api/v1.0/stations\">/api/v1.0/stations<a><br/>"
        f"-- Daily Temperature Observations for Station USC00519281 for 
         2016-2017 Season:<a href=\"api/v1.0/tobs\">/api/v1.0/tobs<a><br/> "
        f"-- Enter a start date to get the minimum, maximum, and average
        temperatures for all dates after the specified date:
        /api/v1.0/yyyy-mm-dd<br>"
        f"-- Enter both a start and end date to get the minimum, maximum,
        and average temperatures for that date range:
        /api/v1.0/yyyy-mm-dd<br>"
    )

   