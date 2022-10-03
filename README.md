## Instructions

Create a git project with a single python script that reads the PM data (https://datasets.simula.no/pmdata/) and generates a single a csv file containing the following columns:


1. Person
2. Calories
3. Distance
4. Heart rate
5. Type of activity
6. Time stamp


PM data and output csv should not be part of the git project.

## Getting the data

Raw data is available at (https://datasets.simula.no/pmdata/) as zip file. 
Unzip it and save it in a folder called `raw_data` in the root of the project.

## Creating and activating virtual environment

Execute instructions:

```
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```
