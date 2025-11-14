# 🧩 Forensic Analysis Tool for Online Abuse Detection

A Python-based forensic analysis tool that detects abusive or harassing messages from datasets and performs digital evidence integrity checks using SHA256 hashing.

---

## 📋 Features

✅ **Abuse Detection**: Identifies messages containing abusive keywords from a configurable list  
✅ **Sentiment Analysis**: Analyzes sentiment polarity and subjectivity using TextBlob  
✅ **File Integrity**: Computes SHA256 hashes for digital evidence verification  
✅ **CSV Report**: Exports detailed analysis results to CSV format  
✅ **Forensic Report**: Generates a comprehensive text-based forensic report  
✅ **Visualization**: Creates professional charts showing sentiment distribution  
✅ **Modular Design**: Clean, well-commented functions for easy maintenance and extension  

---

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Navigate to project directory**:
   ```bash
   cd c:\Users\vaide\OneDrive\Desktop\forensic_analysis
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Download TextBlob corpora** (required for sentiment analysis):
   ```bash
   python -m textblob.download_corpora
   ```

---

## 📖 Usage

### Basic Usage

Run the tool with the default input file (`incident_log.csv`):
```bash
python forensic_analyzer.py
```

### With Custom Input File

Specify a custom CSV file as argument:
```bash
python forensic_analyzer.py path\to\your\data.csv
```

### Example
```bash
python forensic_analyzer.py evidence.csv
```

---

## 📊 Input CSV Format

Your input CSV must contain the following columns:

| Column | Type | Description |
|--------|------|-------------|
| `id` | int/str | Unique message identifier |
| `datetime_utc` | str | Timestamp in ISO format |
| `platform` | str | Social media platform (Twitter, Facebook, etc.) |
| `url` | str | URL/link to original message |
| `short_text` | str | **REQUIRED** - The message content to analyze |
| `victim_follows_abuser` | bool | Whether victim follows abuser |

**Example CSV**:
```csv
id,datetime_utc,platform,url,short_text,victim_follows_abuser
1,2025-11-10T08:15:23Z,Twitter,https://twitter.com/user1/status/123,You are worthless and stupid,False
2,2025-11-10T08:20:45Z,Facebook,https://facebook.com/post/456,I hope you have a great day,True
```

---

## 📁 Output Files

The tool generates the following files in the `results/` directory:

| File | Description |
|------|-------------|
| `analysis_results.csv` | Full dataset with analysis columns (abuse flag, sentiment) |
| `forensic_report.txt` | Detailed text-based forensic report with findings |
| `sentiment_analysis.png` | 4-panel visualization of sentiment analysis |
| `integrity_hashes.txt` | Log of file hashes for evidence integrity verification |

---

## 🔍 Analysis Details

### Abuse Detection

The tool searches for the following keywords (case-insensitive):

```
worthless, hate, kill, stupid, idiot, disgusting, pathetic, loser, 
trash, scum, waste, deserve, die, cancer, plague, evil, demonic, 
horrible, despicable
```

**Configuration**: Edit `ABUSIVE_KEYWORDS` in `forensic_analyzer.py` to customize the keyword list.

### Sentiment Analysis

- **Polarity**: Measures positivity/negativity (-1 to +1)
- **Subjectivity**: Measures objectivity/subjectivity (0 to 1)
- **Classification**:
  - Polarity < -0.1 → Negative
  - Polarity > 0.1 → Positive
  - Otherwise → Neutral

### File Integrity

- **Hash Algorithm**: SHA256
- **Purpose**: Verify evidence hasn't been tampered with
- **Log File**: `integrity_hashes.txt` stores hash and timestamp

---

## 📈 Output Examples

### Console Output
```
🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 
FORENSIC ANALYSIS TOOL - ONLINE ABUSE DETECTION
🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 🔍 

✓ Output directory ensured: results

🔐 Computing file integrity hash...
✓ SHA256: a3b45f9e8c12d7f4e6b2a9c1d5f8e3b7a2c9e4f6d1b8a5c3e7f2a9d6b1e4c8

📂 Loading data from: incident_log.csv
✓ Loaded 20 records

🔍 Analyzing messages...

======================================================================
📊 FORENSIC ANALYSIS SUMMARY
======================================================================
File: incident_log.csv
Hash (SHA256): a3b45f9e8c12d7f4e6b2a9c1d5f8e3b7a2c9e4f6d1b8a5c3e7f2a9d6b1e4c8
Analysis Date: 2025-11-12 10:30:45
----------------------------------------------------------------------
Total Messages: 20
Abusive Messages: 7 (35.00%)
Average Polarity: -0.0452
Average Subjectivity: 0.5894

Sentiment Distribution:
  - Neutral: 10 (50.00%)
  - Negative: 6 (30.00%)
  - Positive: 4 (20.00%)
======================================================================
```

### CSV Output
```csv
id,datetime_utc,platform,url,short_text,victim_follows_abuser,is_abusive,sentiment_polarity,sentiment_subjectivity,sentiment_class
1,2025-11-10T08:15:23Z,Twitter,https://twitter.com/user1/status/123,You are worthless and stupid,False,True,-0.85,0.9,Negative
2,2025-11-10T08:20:45Z,Facebook,https://facebook.com/post/456,I hope you have a great day,True,False,0.7,0.6,Positive
```

### Visualization Output
Four-panel chart showing:
1. **Sentiment Class Distribution** (pie chart)
2. **Abuse Detection Results** (bar chart)
3. **Polarity Distribution** (histogram)
4. **Subjectivity Distribution** (histogram)

---

## 🔧 Customization

### Change Abusive Keywords
Edit the `ABUSIVE_KEYWORDS` set in `forensic_analyzer.py`:
```python
ABUSIVE_KEYWORDS = {
    "your_keyword_1",
    "your_keyword_2",
    # Add more as needed
}
```

### Adjust Sentiment Thresholds
Modify sentiment classification thresholds:
```python
NEGATIVE_THRESHOLD = -0.1  # Lower = more sensitive
POSITIVE_THRESHOLD = 0.1   # Raise = less sensitive
```

### Change Output Directory
Edit the output configuration:
```python
OUTPUT_DIR = "your_custom_directory"
```

---

## 🧬 Function Reference

### Core Functions

#### `compute_hash(file_path, algorithm="sha256")`
Computes SHA256 hash of a file for integrity verification.

#### `contains_abuse(text)`
Detects if text contains abusive keywords.

#### `analyze_sentiment(text)`
Performs sentiment analysis using TextBlob.

#### `analyze_abuse(input_file)`
Main analysis orchestrator - loads CSV and runs all analyses.

#### `generate_summary(df)`
Generates statistics summary from analyzed data.

#### `visualize_sentiment(df, output_file)`
Creates multi-panel visualization of sentiment analysis.

#### `save_results_csv(df, output_file)`
Exports analysis results to CSV.

#### `save_forensic_report(df, summary, input_file, file_hash, output_file)`
Generates comprehensive forensic report.

---

## 📝 Example Workflow

```python
# 1. Load and analyze data
df = analyze_abuse("evidence.csv")

# 2. Generate summary
summary = generate_summary(df)

# 3. Save results
save_results_csv(df, "results.csv")

# 4. Create visualization
visualize_sentiment(df, "report.png")

# 5. Export forensic report
save_forensic_report(df, summary, "evidence.csv", file_hash, "report.txt")
```

---

## 🚀 Advanced Features

### Command Line Arguments
```bash
python forensic_analyzer.py incident_log.csv
```

### Running from Script
```python
from forensic_analyzer import main

# Run analysis with custom file
main("your_data.csv")
```

### Batch Processing
To analyze multiple files:
```python
import os
from forensic_analyzer import main

for csv_file in os.listdir("evidence_folder"):
    if csv_file.endswith(".csv"):
        main(os.path.join("evidence_folder", csv_file))
```

---

## ⚠️ Important Notes

1. **Data Privacy**: Ensure you have proper authorization before analyzing user data.
2. **Keyword Sensitivity**: The abuse keyword list is customizable and may need tuning for your use case.
3. **False Positives**: Sentiment analysis may flag legitimate negative sentiments.
4. **Performance**: Large CSV files (>100K rows) may take several minutes to process.
5. **Hash Verification**: Keep hash logs for chain-of-custody documentation.

---

## 🐛 Troubleshooting

### `ModuleNotFoundError: No module named 'textblob'`
Solution: Run `pip install -r requirements.txt`

### `LookupError: 'corpora/brown' not found`
Solution: Run `python -m textblob.download_corpora`

### `FileNotFoundError: incident_log.csv`
Solution: Ensure the CSV file exists in the project directory or provide full path

### Poor sentiment analysis results
Solution: Ensure corpora are downloaded and try adjusting sentiment thresholds

---

## 📚 Libraries Used

- **pandas**: Data manipulation and CSV handling
- **TextBlob**: Sentiment analysis and NLP
- **matplotlib**: Data visualization
- **hashlib**: Cryptographic hashing (built-in)
- **os & pathlib**: File system operations (built-in)

---

## 📜 License

This tool is provided for forensic analysis and research purposes.

---

## 💡 Suggestions for Improvement

- Add ML-based classifier for more accurate abuse detection
- Implement multi-language support
- Add database backend for large-scale analysis
- Create web UI for visualization
- Add export to PDF format
- Implement clustering analysis
- Add API endpoint for integration

---

## 📧 Support

For issues or questions, review the code comments or check the function docstrings.

---

**Created**: November 2025  
**Version**: 1.0  
**Author**: Forensic Analysis Team
