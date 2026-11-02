# Artefact (ArchaeTron)

**Status: archived 2023 MSc prototype. Not maintained.** Kept public as the first working sketch of
ideas I later developed properly (see *Where this went* below).

## What it was

Exploratory code from my MSc in Artificial Intelligence & Big Data (Atlantic Technological University,
2023). The question was how archaeological records could be reorganised so they are usable as machine
learning training data.

The central idea, which still runs through my research, is in
`src/ArchaeTron/Archae_Objects/ArchaeObj_Base_Class.py`: an archaeological object has two separate
layers.

- **Sensed**: what was observed or measured (position, data, when it came into being and when it was destroyed)
- **Inferred**: interpretations derived from a sensed object, which are kept apart from it

The rest of the package was used to try out data sources and representations:

| Module | What it tried |
|---|---|
| `Factories/`, `Builders/` | Building Sensed/Inferred objects via factory and builder patterns |
| `DataFetcher/` | Loading OSi boundary shapefiles; querying the logainm.ie placenames API |
| `GeoDataHandler/` | GeoPandas handling and plotting |
| `TimeHandler/` | Early experiments treating dates as positions (state vectors over time) |
| `EPCIS_Interface/` | Expressing finds as GS1 EPCIS capture events (supply-chain provenance standard) |
| `WebInterface.py` | A Gradio front end |

## Honest caveats

- Written under deadline as a research sketch: no tests, hard-coded local file paths, several modules are stubs.
- `main.py` needs a logainm.ie API key in the `LOGAINM_API_KEY` environment variable.

## Where this went

The Sensed/Inferred separation became the SENSED vs INFERRED layers of the Universal Archaeological
Signal Object (UASO). It is described in:

D. Foley and E. Furey, "From Geospatial Patterns to Ancient Signals: A Signal-Based Framework for
Archaeological Machine Learning," *2025 35th Irish Signals and Systems Conference (ISSC)*, IEEE.
[doi:10.1109/ISSC67739.2025.11291309](https://doi.org/10.1109/ISSC67739.2025.11291309)
