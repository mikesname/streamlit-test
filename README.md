# Streamlit utilities for EHRI geospatial data

Experimental tools on the [Streamlit](https://streamlit.io/) platform
for doing things with Geospatial data:

csv2gpkg
--------

Provides a simple UI for converting CSV/TSV files to the GeoPackage format.

gpkg2gs
-------

Allows ingesting a GeoPackage into a configured Geoserver instance via the
REST API. The workspace and connection parameters must be set up in the
Streamlit app secrets.
