# Flask and Google Sheets prototype

A historical Flask application that reads page content from Google Sheets and accepts contact-form submissions.

## Structure

- `app.py` — Flask routes and Sheets integration.
- `templates/` — HTML templates.
- `requirements.txt` — original Python dependencies.
- `Dockerfile` and Compose files — original container configuration.

## Configuration

See [CONFIGURATION.md](CONFIGURATION.md) for external credential setup. The application also expects an existing spreadsheet with the worksheet layout referenced in `app.py`. Importing the app establishes the Sheets connection; it requires configured credentials.

The dependencies and deployment configuration are historical and need validation before deployment. Contact-form submissions write to the configured spreadsheet.

For the current company website, visit [QAVEAI](https://qaveai.com).
