## DATA7901 Galaxy Classification Starter (UQ)

This repository is a ready-to-run starter kit for the semester project described in `galaxy_classification_guide.md`. It walks you through getting the data from SDSS, exploring key columns, and downloading/visualising galaxy images and spectra.

### What you’ll do
- Run the provided SQL on SDSS CasJobs to build your project table
- Export the table to CSV and place it in this repo
- Use the notebooks to validate data, plot histograms, and fetch/preview cutouts and spectra

### Repo layout
- `galaxy_classification_guide.md`: Project background and goals (read this first)
- `input/queries/DATA7901_DR19_casjobs.sql`: SQL to run on SDSS CasJobs
- `input/tables/`: Put your exported CSV here (expected filename: `DATA7901_DR19.csv`)
- `input/images/`: JPEG cutouts downloaded by the notebook
- `input/spectra/`: FITS spectra downloaded by the notebook
- `notebooks/explore_tables.ipynb`: Main walkthrough: load CSV, validate fields, histograms, download and visualise images and spectra
- `notebooks/get_cutouts.ipynb`: Additional cutout helper notebook (optional)
- `src/`: We will keep all the Python scripts associated with the project here. If we talk about a Python script (any `*.py` file), it is stored in `src/`.
- `models/`: This folder keeps all the trained models (saved checkpoints/weights, experiment outputs).

### Prerequisites
- Python 3.10+ (tested with 3.12)
- Jupyter (Lab or Notebook)
- Packages: `numpy`, `pandas`, `matplotlib`, `astropy`
- Command-line `wget` (recommended) for downloads
  - macOS: `brew install wget`
  - Ubuntu/Debian: `sudo apt-get install wget`
  - Windows: use WSL or install wget; the notebook also includes a Python fallback for images

Suggested environment setup:
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install jupyter numpy pandas matplotlib astropy
```

Alternative using conda:
```bash
conda create -n data7901 python=3.12 -y
conda activate data7901
pip install jupyter numpy pandas matplotlib astropy
```

### Step 1 — Build the table in SDSS CasJobs
1) Go to the SDSS CasJobs website and sign in (create an account if needed).
2) Open a new query window and paste the contents of `input/queries/DATA7901_DR19_casjobs.sql`.
   - The query creates `mydb.DATA7901_DR19` with the following (key) columns:
     - `objid`, `ra`, `dec`, Galactic `l`, `b`
     - Spectra identifiers: `specObjID`, `plate`, `mjd`, `fiberid`, `class`, `programname`, `sdssPrimary`
     - Galaxy Zoo votes: `p_el`, `nvote_tot`
   - The filters in the SQL (magnitude and redshift cuts, and `zWarning = 0`) keep the result manageable.
3) Run the query. When it completes, export the results from `mydb.DATA7901_DR19` as CSV.
4) Save the CSV locally as `DATA7901_DR19.csv` and place it at:
```
input/tables/DATA7901_DR19.csv
```

Notes:
- Some tools may rename duplicate column names (e.g., `ra`, `dec` appear in multiple joined tables). The provided notebooks expect the CSV format produced by CasJobs; the examples here already work with the CSV used during development.

### Step 2 — Explore and validate the table
Open `notebooks/explore_tables.ipynb` and run the cells in order:
- Load the CSV from `input/tables/DATA7901_DR19.csv`.
- Validate completeness and ranges for `p_el` (0–1) and `nvote_tot` (non-negative integer) for rows where `class == 'GALAXY'`.
- Plot histograms of `p_el` and `nvote_tot`.

### Step 3 — Download a few image cutouts (optional throttle)
In the same notebook:
- A cell prepares “valid galaxies” and builds the Legacy Survey cutout URLs.
- By default, it prints commands and limits downloads (e.g., first 10). You can increase or decrease `num_to_download`.
- Images are saved as `input/images/<objid>.jpeg`.

If you don’t have `wget`, either install it or use the Python fallback cell (already included) that uses `urllib` to fetch the same URLs.

### Step 4 — Visualise the cutouts
- The notebook includes a cell that shows the first 5 downloaded JPEGs side-by-side with titles from the filename (`objid`).

### Step 5 — Download and visualise spectra (optional)
- The notebook includes a cell to download the first N spectra using `plate`, `mjd`, and `fiberid` into `input/spectra/`.
- It then plots a few spectra using `astropy.io.fits` to read common SDSS formats (prefers table HDUs with `loglam`/`flux`, falls back to image HDUs with `COEFF0/COEFF1`).

Tips:
- Spectra URLs in the example target the SDSS DR14 “lite” paths. If a URL returns 404, skip or adjust the base URL to a matching DR for your rows.
- Be gentle with external services. Keep download limits small (e.g., 10–50) while testing.

### Troubleshooting
- “File not found”: confirm your CSV is named `DATA7901_DR19.csv` and placed under `input/tables/`.
- Missing `wget`: install it or use the Python fallback image downloader cell.
- Missing `astropy`: `pip install astropy`.
- Spectra 404s: not every `plate/mjd/fiberid` exists at the hard-coded path. Try a few, or adjust the base URL.
- Duplicate columns in CSV: CasJobs (and pandas) may rename duplicates; the provided notebook uses columns as exported during development.

### Next steps (project work)
After you’ve verified the data flows end-to-end:
- Feature engineering from tables (e.g., thresholds on `p_el`, vote counts)
- Image models (CNNs) and spectral models
- Model evaluation and reporting

### Acknowledgements
- SDSS CasJobs and data services
- Legacy Survey image cutouts


