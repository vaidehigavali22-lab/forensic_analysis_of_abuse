# 📂 PROJECT FILE STRUCTURE & DESCRIPTIONS

```
forensic_analysis/
│
├── 🐍 MAIN SCRIPTS
│   ├── forensic_analyzer.py              ← Main standalone tool (700+ lines)
│   ├── forensic_analyzer_advanced.py     ← Config-based version (650+ lines)
│   ├── config.py                         ← Configuration file (150+ lines)
│   └── examples.py                       ← Usage examples (300+ lines)
│
├── 📚 DOCUMENTATION
│   ├── README.md                         ← Complete reference guide
│   ├── QUICKSTART.md                     ← 5-minute quick start
│   ├── PROJECT_SUMMARY.md                ← Project overview
│   ├── CHECKLIST.md                      ← Verification checklist
│   └── FILE_STRUCTURE.md                 ← This file
│
├── 🛠️ SETUP & UTILITIES
│   ├── setup.ps1                         ← PowerShell setup script
│   ├── setup.bat                         ← Batch setup script
│   └── requirements.txt                  ← Python dependencies
│
├── 📊 DATA & SAMPLES
│   └── incident_log.csv                  ← Sample test dataset
│
└── 📁 OUTPUT FOLDER (created on first run)
    └── results/
        ├── analysis_results.csv          ← Full analysis with columns
        ├── forensic_report.txt           ← Professional text report
        ├── sentiment_analysis.png        ← 4-panel visualization
        └── integrity_hashes.txt          ← SHA256 hash log
```

---

## 📄 FILE DESCRIPTIONS

### 🐍 Core Python Scripts

#### `forensic_analyzer.py` (Main Tool)
**Type**: Standalone Python Script  
**Lines**: 750+  
**Purpose**: Main forensic analysis tool that doesn't require config.py

**Key Functions**:
- `compute_hash()` - SHA256 file hashing
- `contains_abuse()` - Abusive keyword detection
- `analyze_sentiment()` - TextBlob sentiment analysis
- `classify_sentiment()` - Sentiment classification
- `analyze_abuse()` - Main analysis orchestrator
- `generate_summary()` - Statistics generation
- `print_summary()` - Console output
- `save_results_csv()` - CSV export
- `save_forensic_report()` - Text report generation
- `visualize_sentiment()` - Chart creation
- `main()` - Entry point

**Usage**:
```bash
python forensic_analyzer.py incident_log.csv
python forensic_analyzer.py custom_data.csv
```

---

#### `forensic_analyzer_advanced.py` (Config-Based)
**Type**: Python Script (imports config.py)  
**Lines**: 650+  
**Purpose**: Advanced version using centralized configuration

**Key Differences from Main**:
- Imports all settings from config.py
- Supports multiple keyword presets
- Easy customization without code changes
- Same functions, enhanced flexibility

**Usage**:
```bash
python forensic_analyzer_advanced.py data.csv general
python forensic_analyzer_advanced.py data.csv harassment
python forensic_analyzer_advanced.py data.csv cyberbullying
```

---

#### `config.py` (Configuration)
**Type**: Configuration File (Python)  
**Lines**: 150+  
**Purpose**: Centralized settings for easy customization

**Main Sections**:
1. `ABUSIVE_KEYWORDS` - List of keywords to detect
2. `NEGATIVE_THRESHOLD` - Polarity cutoff for negative
3. `POSITIVE_THRESHOLD` - Polarity cutoff for positive
4. `OUTPUT_DIR` - Where to save results
5. `VISUALIZATION_CONFIG` - Chart settings
6. `KEYWORD_SETS` - Multiple preset keyword collections

**What You Can Customize**:
- Add/remove abusive keywords
- Adjust sentiment thresholds
- Change output directory
- Modify visualization colors
- Define custom keyword sets

---

#### `examples.py` (Usage Examples)
**Type**: Python Script  
**Lines**: 300+  
**Purpose**: Demonstrates all tool features

**Included Examples**:
1. **Example 1**: Basic analysis with default settings
2. **Example 2**: Custom output file locations
3. **Example 3**: Programmatic filtering of results
4. **Example 4**: Generate custom statistics
5. **Example 5**: Detailed sentiment breakdown
6. **Example 6**: Create sample test data
7. **Example 7**: Compare multiple datasets

**Usage**:
```bash
python examples.py
```

---

### 📚 Documentation Files

#### `README.md` (Complete Reference)
**Size**: ~400 lines  
**Purpose**: Comprehensive documentation

**Sections**:
- Installation instructions
- Usage guide
- Input CSV format
- Output file descriptions
- Analysis details
- Customization guide
- Function reference
- Troubleshooting
- Library information
- Suggestions for improvement

---

#### `QUICKSTART.md` (Quick Setup)
**Size**: ~150 lines  
**Purpose**: Get started in 5 minutes

**Sections**:
- Installation (3 options)
- Running the analysis
- Input file format
- Output files
- Example output
- Customization tips
- Troubleshooting
- Project structure

---

#### `PROJECT_SUMMARY.md` (Overview)
**Size**: ~200 lines  
**Purpose**: High-level project overview

**Sections**:
- What you have (list of files)
- Key features
- Quick start (3 steps)
- Output structure
- Technical stack
- File descriptions
- Analysis workflow
- Customization options
- Use cases
- Performance characteristics

---

#### `CHECKLIST.md` (Verification)
**Size**: ~350 lines  
**Purpose**: Verify installation and functionality

**Sections**:
- Installation checklist
- Verification steps
- Feature testing
- Documentation check
- Functionality tests
- Performance verification
- Customization tests
- Error handling verification
- Go-live readiness

---

#### `FILE_STRUCTURE.md` (This File)
**Purpose**: Explain each file in the project

---

### 🛠️ Setup & Utility Files

#### `setup.ps1` (PowerShell Setup)
**Language**: PowerShell Script  
**Purpose**: Automatic environment setup for Windows PowerShell

**What It Does**:
1. Checks if Python is installed
2. Creates virtual environment
3. Activates virtual environment
4. Installs required packages
5. Downloads TextBlob corpora
6. Displays setup completion message

**Usage**:
```powershell
.\setup.ps1
```

---

#### `setup.bat` (Batch Setup)
**Language**: Batch Script  
**Purpose**: Automatic environment setup for Command Prompt

**What It Does**:
1. Checks if Python is installed
2. Creates virtual environment
3. Activates virtual environment
4. Installs required packages
5. Downloads TextBlob corpora
6. Displays setup completion message

**Usage**:
```cmd
setup.bat
```

---

#### `requirements.txt` (Dependencies)
**Format**: Python requirements file  
**Purpose**: Lists all required Python packages

**Content**:
```
pandas>=1.3.0
textblob>=0.17.1
matplotlib>=3.4.0
```

**Usage**:
```bash
pip install -r requirements.txt
```

---

### 📊 Data Files

#### `incident_log.csv` (Sample Data)
**Format**: CSV (Comma-Separated Values)  
**Rows**: 20 test messages  
**Purpose**: Sample data for testing the tool

**Columns**:
- `id` - Message ID (1-20)
- `datetime_utc` - Timestamp
- `platform` - Social media platform
- `url` - Link to message
- `short_text` - Message content (analyzed)
- `victim_follows_abuser` - Relationship flag

**Sample Rows**:
```csv
1,2025-11-10T08:15:23Z,Twitter,https://...,You are worthless and stupid,False
2,2025-11-10T08:20:45Z,Facebook,https://...,I hope you have a great day,True
```

---

### 📁 Output Folder (Generated)

#### `results/` Directory
**Created**: On first run of any script  
**Purpose**: Stores all analysis outputs

#### `results/analysis_results.csv`
**Format**: CSV  
**Purpose**: Full dataset with analysis columns

**Columns Added**:
- `is_abusive` (boolean) - Contains abusive keywords?
- `sentiment_polarity` (float) - Sentiment score (-1 to +1)
- `sentiment_subjectivity` (float) - Subjectivity score (0 to 1)
- `sentiment_class` (string) - Negative/Neutral/Positive

---

#### `results/forensic_report.txt`
**Format**: Text file  
**Purpose**: Professional forensic analysis report

**Sections**:
- Evidence information (file, hash, date)
- Abuse detection results
- Sentiment analysis statistics
- Detailed findings (message-by-message)

---

#### `results/sentiment_analysis.png`
**Format**: PNG image (300 DPI)  
**Purpose**: Visual representation of analysis

**Chart Contains**:
1. Pie chart - Sentiment class distribution
2. Bar chart - Abuse detection results
3. Histogram - Polarity distribution
4. Histogram - Subjectivity distribution

---

#### `results/integrity_hashes.txt`
**Format**: Text log  
**Purpose**: Track file integrity over time

**Content**:
```
2025-11-12T10:30:45.123456 | incident_log.csv | a3b45f9e8c12d7f4...
2025-11-12T10:35:12.654321 | evidence.csv | d7f4a3b45f9e8c12d...
```

---

## 📊 File Statistics

| File | Type | Size | Purpose |
|------|------|------|---------|
| forensic_analyzer.py | Python | 750 lines | Main tool |
| forensic_analyzer_advanced.py | Python | 650 lines | Config version |
| config.py | Python | 150 lines | Settings |
| examples.py | Python | 300 lines | Examples |
| README.md | Markdown | 400 lines | Guide |
| QUICKSTART.md | Markdown | 150 lines | Quick setup |
| PROJECT_SUMMARY.md | Markdown | 200 lines | Overview |
| CHECKLIST.md | Markdown | 350 lines | Verification |
| FILE_STRUCTURE.md | Markdown | 400 lines | This file |
| setup.ps1 | PowerShell | 40 lines | Setup |
| setup.bat | Batch | 35 lines | Setup |
| requirements.txt | Text | 3 lines | Dependencies |
| incident_log.csv | CSV | 20 rows | Sample data |

**Total**: ~3,500 lines of code + documentation

---

## 🔄 File Dependencies

```
forensic_analyzer.py (standalone)
    ├─ imports: pandas, textblob, matplotlib, hashlib, os
    └─ no dependencies on other project files

forensic_analyzer_advanced.py
    ├─ imports: config.py (required)
    ├─ imports: pandas, textblob, matplotlib, hashlib, os
    └─ can reuse: functions from forensic_analyzer.py

config.py
    └─ no dependencies
    └─ imported by: forensic_analyzer_advanced.py

examples.py
    ├─ imports: forensic_analyzer.py (required)
    └─ imports: pandas

setup.ps1 / setup.bat
    └─ creates: venv/ (virtual environment)
    └─ installs: requirements.txt packages

incident_log.csv
    └─ used by: forensic_analyzer.py, examples.py
```

---

## 🚀 Getting Started

### Step 1: Initial Setup
```bash
# Choose one:
.\setup.ps1        # PowerShell
setup.bat          # Command Prompt
```

### Step 2: First Run
```bash
python forensic_analyzer.py incident_log.csv
```

### Step 3: Check Results
```bash
Get-ChildItem results/
# Output should show 4 files
```

---

## 📝 File Organization Tips

### Keep organized:
- ✅ Keep all files in the same directory
- ✅ Don't move individual files around
- ✅ Keep `config.py` near `forensic_analyzer_advanced.py`
- ✅ Let results/ folder be created automatically

### Customization workflow:
1. Edit `config.py` (keywords, thresholds)
2. Run `python forensic_analyzer_advanced.py`
3. Review outputs in `results/`

### Development workflow:
1. Modify `forensic_analyzer.py` or `forensic_analyzer_advanced.py`
2. Test with `python examples.py`
3. Check outputs in `results/`

---

## 🔐 Important Files to Backup

- `config.py` - Your customizations
- `incident_log.csv` - Your original data
- `results/` - Analysis outputs (keep for records)

---

## 📖 Where to Find Information

| Question | File |
|----------|------|
| How do I install? | QUICKSTART.md |
| How do I use it? | README.md |
| What does each file do? | This file (FILE_STRUCTURE.md) |
| What are the examples? | examples.py |
| How do I customize? | config.py, README.md |
| Is everything working? | CHECKLIST.md |
| What's in this project? | PROJECT_SUMMARY.md |

---

## ✅ File Checklist

- [ ] forensic_analyzer.py (main tool)
- [ ] forensic_analyzer_advanced.py (advanced version)
- [ ] config.py (configuration)
- [ ] examples.py (examples)
- [ ] README.md (reference guide)
- [ ] QUICKSTART.md (quick start)
- [ ] PROJECT_SUMMARY.md (overview)
- [ ] CHECKLIST.md (verification)
- [ ] FILE_STRUCTURE.md (this file)
- [ ] setup.ps1 (setup script)
- [ ] setup.bat (setup script)
- [ ] requirements.txt (dependencies)
- [ ] incident_log.csv (sample data)

**All files present? You're ready to go!** 🎉

---

**Next Step**: Read QUICKSTART.md to get started in 5 minutes!
