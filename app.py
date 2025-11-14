"""
Simple Flask frontend for the Forensic Analysis Tool
- Upload a CSV or use the sample `incident_log.csv`
- Run analysis using `forensic_analyzer_advanced` functions
- Display summary and provide links to download results

Run:
    pip install -r requirements.txt
    python app.py

Access: http://127.0.0.1:5000/
"""

import os
from pathlib import Path
from datetime import datetime
from flask import Flask, request, render_template, send_from_directory, redirect, url_for, flash
from werkzeug.utils import secure_filename

# Import analysis functions
try:
    from forensic_analyzer_advanced import (
        ensure_output_directory,
        compute_hash,
        analyze_abuse,
        generate_summary,
        save_results_csv,
        save_forensic_report,
        visualize_sentiment,
    )
except Exception:
    # fallback to forensic_analyzer if advanced not available
    from forensic_analyzer import (
        ensure_output_directory,
        compute_hash,
        analyze_abuse,
        generate_summary,
        save_results_csv,
        save_forensic_report,
        visualize_sentiment,
    )

# Flask app configuration
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / "uploads"
RESULTS_FOLDER = BASE_DIR / "results"
ALLOWED_EXTENSIONS = {"csv"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = str(UPLOAD_FOLDER)
app.secret_key = "replace-with-a-secure-key"

# Ensure folders exist
UPLOAD_FOLDER.mkdir(exist_ok=True)
ensure_output_directory()


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle file upload
        file = request.files.get("file")
        use_sample = request.form.get("use_sample") == "on"
        keyword_preset = request.form.get("keyword_preset", "general")

        if use_sample:
            input_path = BASE_DIR / "incident_log.csv"
            if not input_path.exists():
                flash("Sample file not found.", "error")
                return redirect(url_for("index"))
        else:
            if not file or file.filename == "":
                flash("No file selected.", "error")
                return redirect(url_for("index"))
            if not allowed_file(file.filename):
                flash("Only CSV files are allowed.", "error")
                return redirect(url_for("index"))

            filename = secure_filename(file.filename)
            input_path = UPLOAD_FOLDER / f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{filename}"
            file.save(str(input_path))

        # Compute hash
        file_hash = compute_hash(str(input_path)) or "N/A"

        # Run analysis
        df = analyze_abuse(str(input_path), keyword_preset)
        if df is None:
            flash("Analysis failed. Check server logs.", "error")
            return redirect(url_for("index"))

        # Generate summary and outputs
        summary = generate_summary(df)

        # Save outputs with timestamped names to avoid clobber
        ts = datetime.now().strftime("%Y%m%d%H%M%S")
        csv_name = f"analysis_results_{ts}.csv"
        report_name = f"forensic_report_{ts}.txt"
        viz_name = f"sentiment_analysis_{ts}.png"

        save_results_csv(df, str(RESULTS_FOLDER / csv_name))
        save_forensic_report(df, summary, str(input_path), file_hash, str(RESULTS_FOLDER / report_name))
        visualize_sentiment(df, str(RESULTS_FOLDER / viz_name))

        # Render results page
        return render_template(
            "results.html",
            summary=summary,
            csv_file=csv_name,
            report_file=report_name,
            viz_file=viz_name,
            input_file=input_path.name,
            file_hash=file_hash,
        )

    # GET
    return render_template("index.html")


@app.route('/results/<path:filename>')
def download_file(filename):
    return send_from_directory(str(RESULTS_FOLDER), filename, as_attachment=True)


@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(str(UPLOAD_FOLDER), filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
