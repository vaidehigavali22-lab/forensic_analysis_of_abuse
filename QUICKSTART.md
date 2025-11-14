# 🚀 QUICK START GUIDE

## Installation (5 minutes)

### Option 1: Automatic Setup (PowerShell)
```powershell
.\setup.ps1
```

### Option 2: Automatic Setup (Command Prompt)
```cmd
setup.bat
```

### Option 3: Manual Setup
```powershell
# Create virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# Install packages
pip install -r requirements.txt

# Download TextBlob corpora
python -m textblob.download_corpora
```

---

## Run the Analysis

### Basic Usage (uses incident_log.csv)
```bash
python forensic_analyzer.py
```

### Custom CSV File
```bash
python forensic_analyzer.py your_evidence.csv
```

### Advanced Version (with config)
```bash
python forensic_analyzer_advanced.py incident_log.csv general
```

**Keyword sets available:**
- `general` - Basic abusive keywords
- `harassment` - Harassment-specific terms
- `cyberbullying` - Cyberbullying keywords
- `combined` - All keywords combined

---

## Input File Format

**Required CSV columns:**
- `short_text` - The message content (REQUIRED)

**Recommended columns:**
- `id` - Unique message identifier
- `datetime_utc` - Timestamp
- `platform` - Social media platform
- `url` - Link to original message
- `victim_follows_abuser` - Relationship indicator

**Example:**
```csv
id,datetime_utc,platform,url,short_text,victim_follows_abuser
1,2025-11-10T08:15:23Z,Twitter,https://twitter.com/user/123,You are stupid,False
2,2025-11-10T08:20:45Z,Facebook,https://facebook.com/456,Great day today,True
```

---

## Output Files

Located in `results/` folder:

| File | Description |
|------|-------------|
| `analysis_results.csv` | All messages with abuse flags & sentiment scores |
| `forensic_report.txt` | Professional forensic report |
| `sentiment_analysis.png` | 4-panel visualization |
| `integrity_hashes.txt` | SHA256 hashes for chain of custody |

---

## Example Output

```
======================================================================
📊 FORENSIC ANALYSIS SUMMARY
======================================================================
File: incident_log.csv
Hash (SHA256): a3b45f9e8c12d7f4e6b2a9c1d5f8e3b7...
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

---

## Customize Analysis

Edit `config.py` to:
- Add/remove abusive keywords
- Adjust sentiment thresholds
- Change output directory
- Modify visualization colors

**Example: Add new keywords**
```python
ABUSIVE_KEYWORDS = {
    "worthless",
    "your_keyword_here",
}
```

---

## Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'pandas'`
**Solution:** Run `pip install -r requirements.txt`

### Issue: `LookupError: 'corpora/brown'`
**Solution:** Run `python -m textblob.download_corpora`

### Issue: File not found
**Solution:** Use full path or ensure CSV is in project directory

### Issue: Empty results
**Solution:** Check CSV has `short_text` column with data

---

## Project Structure

```
forensic_analysis/
├── forensic_analyzer.py           # Main standalone script
├── forensic_analyzer_advanced.py  # Configuration-based version
├── config.py                      # Customization settings
├── incident_log.csv              # Sample data
├── requirements.txt              # Dependencies
├── README.md                     # Full documentation
├── setup.ps1                     # PowerShell setup
├── setup.bat                     # Batch setup
└── results/                      # Output folder (created on first run)
    ├── analysis_results.csv
    ├── forensic_report.txt
    ├── sentiment_analysis.png
    └── integrity_hashes.txt
```

---

## Key Features

✅ **Abuse Detection** - Finds harmful language  
✅ **Sentiment Analysis** - Measures emotional tone  
✅ **File Integrity** - SHA256 hashing for evidence  
✅ **Professional Reports** - Forensic-grade output  
✅ **Visualizations** - Chart-based insights  
✅ **Modular Code** - Easy to extend & customize  

---

## Tips & Tricks

1. **Large datasets** - May take 1-5 minutes for 10K+ messages
2. **Custom keywords** - Update `config.py` for your needs
3. **Multiple files** - Run script once per file
4. **Batch processing** - Create a loop in your own script
5. **Export data** - Use `analysis_results.csv` in Excel or BI tools

---

## Next Steps

1. ✅ Run setup script
2. ✅ Prepare your CSV file
3. ✅ Run analysis: `python forensic_analyzer.py your_file.csv`
4. ✅ Check `results/` folder for outputs
5. ✅ Review forensic_report.txt for findings

---

## Support

- **Documentation**: See README.md
- **Configuration**: Edit config.py
- **Code Comments**: Check forensic_analyzer.py for detailed documentation
- **Error Messages**: Read the console output for specific issues

---

**Happy analyzing! 🔍**
