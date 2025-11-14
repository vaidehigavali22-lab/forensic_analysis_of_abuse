# 📑 PROJECT INDEX & GUIDE

## 🎯 QUICK NAVIGATION

**First Time?** → Start with `START_HERE.txt`  
**Want Quick Setup?** → Use `QUICKSTART.md`  
**Need Details?** → Read `README.md`  
**File Explanations?** → Check `FILE_STRUCTURE.md`  
**Verify Everything?** → Follow `CHECKLIST.md`  

---

## 📂 PROJECT CONTENTS

### 14 Total Files Organized By Purpose

> Tip: For a concise, numbered execution order see `STEPWISE_FILE_ARRANGEMENT.md` (newly added).

---

## 🚀 START HERE (READ FIRST)

### `START_HERE.txt` ⭐ READ THIS FIRST!
- **Type**: Text file  
- **Time**: 2 minutes  
- **What**: Overview and quick start guide  
- **When**: Your very first time using this project  
- **Contains**:
  - What's in the project
  - 3-step quick start
  - Common tasks
  - Tips & troubleshooting

---

## 🔧 SETUP & INSTALLATION

### `setup.ps1` (PowerShell Setup Script)
- **Type**: PowerShell script  
- **Platform**: Windows PowerShell  
- **Time**: 3-5 minutes  
- **What**: Automatic environment setup  
- **Run**: `.\setup.ps1`  
- **Does**:
  - Checks Python installation
  - Creates virtual environment
  - Installs dependencies
  - Downloads TextBlob corpora

### `setup.bat` (Command Prompt Setup Script)
- **Type**: Batch script  
- **Platform**: Windows Command Prompt  
- **Time**: 3-5 minutes  
- **What**: Automatic environment setup  
- **Run**: `setup.bat`  
- **Does**: Same as setup.ps1 but for CMD

### `requirements.txt` (Python Dependencies)
- **Type**: Text file  
- **What**: Lists required Python packages  
- **Packages**:
  - pandas (data handling)
  - textblob (sentiment analysis)
  - matplotlib (visualization)

---

## 🐍 MAIN PYTHON SCRIPTS

### `forensic_analyzer.py` ⭐ MAIN TOOL
- **Type**: Python script  
- **Lines**: 750+  
- **Dependencies**: None (standalone)  
- **Time**: ~5-10 seconds for sample data  
- **Purpose**: Main forensic analysis tool  
- **Features**:
  - ✅ Abuse detection
  - ✅ Sentiment analysis
  - ✅ File integrity hashing
  - ✅ Professional reporting
  - ✅ Data visualization

**Run**:
```bash
python forensic_analyzer.py incident_log.csv
```

**Output**: 4 files in results/ folder

---

### `forensic_analyzer_advanced.py` (Configuration-Based)
- **Type**: Python script  
- **Lines**: 650+  
- **Dependencies**: Requires config.py  
- **Purpose**: Advanced version with configuration  
- **Features**:
  - All features from main tool
  - Uses config.py settings
  - Multiple keyword presets
  - Easy customization

**Run**:
```bash
python forensic_analyzer_advanced.py data.csv general
python forensic_analyzer_advanced.py data.csv harassment
python forensic_analyzer_advanced.py data.csv cyberbullying
```

**Presets**:
- `general` - Basic abusive keywords
- `harassment` - Harassment-specific
- `cyberbullying` - Cyberbullying keywords
- `combined` - All keywords combined

---

### `config.py` (Configuration File)
- **Type**: Python configuration  
- **Lines**: 150+  
- **Purpose**: Centralized settings  
- **Customize**:
  - Abusive keywords
  - Sentiment thresholds
  - Output directory
  - Visualization colors
  - Multiple keyword sets

**Use**: Edit this file to customize behavior

---

### `examples.py` (Usage Examples)
- **Type**: Python script  
- **Lines**: 300+  
- **Examples**: 7 complete examples  
- **Time**: ~30 seconds to run all  
- **Purpose**: Demonstrate all features  

**Examples Included**:
1. Basic analysis
2. Custom output files
3. Programmatic filtering
4. Custom statistics
5. Sentiment breakdown
6. Create test data
7. Compare datasets

**Run**:
```bash
python examples.py
```

---

## 📚 DOCUMENTATION (READ AS NEEDED)

### `README.md` ⭐ COMPLETE REFERENCE
- **Type**: Markdown  
- **Pages**: ~15 screens  
- **Time**: 15-30 minutes  
- **Purpose**: Comprehensive documentation  
- **Sections**:
  - Features overview
  - Installation guide
  - Usage instructions
  - Input/Output formats
  - Analysis details
  - Customization guide
  - Function reference
  - Troubleshooting
  - Library information

**When to Read**: When you need detailed information

---

### `QUICKSTART.md` (Quick Setup Guide)
- **Type**: Markdown  
- **Pages**: ~5 screens  
- **Time**: 5-10 minutes  
- **Purpose**: Get started quickly  
- **Sections**:
  - Installation options
  - Running the tool
  - Input file format
  - Output files
  - Example output
  - Customization tips
  - Troubleshooting

**When to Read**: When you want to start immediately

---

### `PROJECT_SUMMARY.md` (Overview)
- **Type**: Markdown  
- **Pages**: ~8 screens  
- **Time**: 10 minutes  
- **Purpose**: High-level project overview  
- **Sections**:
  - What you have
  - Key features
  - Quick start (3 steps)
  - Output structure
  - Technical stack
  - File descriptions
  - Analysis workflow
  - Use cases
  - Performance metrics

**When to Read**: To understand the overall project

---

### `FILE_STRUCTURE.md` (File Descriptions)
- **Type**: Markdown  
- **Pages**: ~10 screens  
- **Time**: 15-20 minutes  
- **Purpose**: Explain each file in detail  
- **Sections**:
  - Visual file tree
  - Detailed descriptions
  - File statistics
  - Dependencies map
  - Getting started
  - Organization tips

**When to Read**: When you want to understand each file

---

### `CHECKLIST.md` (Verification Guide)
- **Type**: Markdown  
- **Pages**: ~12 screens  
- **Time**: 10-15 minutes (to follow)  
- **Purpose**: Verify everything works  
- **Checklists**:
  - Installation checklist
  - Verification steps
  - Feature testing
  - Functionality tests
  - Performance verification
  - Customization tests
  - Go-live readiness

**When to Use**: To verify setup and functionality

---

### `START_HERE.txt` (Entry Point)
- **Type**: Text file  
- **Pages**: 1-2 screens  
- **Time**: 2 minutes  
- **Purpose**: First thing to read  
- **Contains**:
  - Welcome message
  - Quick overview
  - 3-step quick start
  - Navigation guide
  - Tips

**When to Read**: Your very first time

---

## 📊 DATA & SAMPLES

### `incident_log.csv` (Sample Dataset)
- **Type**: CSV file  
- **Rows**: 20 test messages  
- **Columns**: 6 (id, datetime_utc, platform, url, short_text, victim_follows_abuser)  
- **Purpose**: Test data for examples  
- **Use**: Run tool on this file first to understand output  

**Run**:
```bash
python forensic_analyzer.py incident_log.csv
```

---

## 🗂️ OUTPUT FILES (Generated)

When you run the tool, it creates a `results/` folder with:

### `results/analysis_results.csv`
- Full dataset with analysis columns
- Includes: is_abusive, sentiment_polarity, sentiment_subjectivity, sentiment_class

### `results/forensic_report.txt`
- Professional text-based forensic report
- Includes: metadata, statistics, detailed findings

### `results/sentiment_analysis.png`
- 4-panel visualization (300 DPI)
- 4 charts: pie, bar, 2 histograms

### `results/integrity_hashes.txt`
- Log of file hashes (SHA256)
- For chain-of-custody verification

---

## 📋 READING GUIDE BY SCENARIO

### Scenario 1: "I want to start RIGHT NOW"
1. Open: `START_HERE.txt` (2 min)
2. Run: `.\setup.ps1` (5 min)
3. Run: `python forensic_analyzer.py incident_log.csv` (done!)

### Scenario 2: "I need complete setup instructions"
1. Read: `QUICKSTART.md`
2. Follow steps 1-3
3. Done!

### Scenario 3: "I want to understand everything"
1. Read: `START_HERE.txt` (overview)
2. Read: `README.md` (complete guide)
3. Read: `FILE_STRUCTURE.md` (file details)
4. Run: `examples.py` (see it work)

### Scenario 4: "I want to customize the tool"
1. Read: `README.md` "Customization" section
2. Edit: `config.py`
3. Run: `python forensic_analyzer_advanced.py`

### Scenario 5: "I need to verify everything works"
1. Follow: `CHECKLIST.md`
2. Check each section
3. Verify all outputs

### Scenario 6: "I'm having problems"
1. Check: `README.md` "Troubleshooting" section
2. Follow: `QUICKSTART.md` "Troubleshooting"
3. Review: `CHECKLIST.md` "Error Handling"

---

## 🎯 FILE DEPENDENCY CHART

```
User
  ↓
START_HERE.txt ──────→ Main entry point
  ↓
setup.ps1/setup.bat ──→ Sets up environment
  ↓
requirements.txt ─────→ Installs dependencies
  ↓
incident_log.csv ─────→ Sample test data
  ↓
forensic_analyzer.py ─→ Main tool (standalone)
  OR
forensic_analyzer_advanced.py ──→ + config.py (customizable)
  ↓
results/ ─────────────→ Output files
```

---

## 📖 DOCUMENTATION HIERARCHY

```
Level 1 (START HERE)
  └─ START_HERE.txt

Level 2 (QUICK START - 5 minutes)
  ├─ QUICKSTART.md
  └─ setup.ps1/setup.bat

Level 3 (OPERATIONAL - 30 minutes)
  ├─ README.md
  └─ examples.py

Level 4 (REFERENCE - As needed)
  ├─ FILE_STRUCTURE.md
  ├─ PROJECT_SUMMARY.md
  └─ config.py

Level 5 (VERIFICATION - Optional)
  └─ CHECKLIST.md
```

---

## ⏱️ TIME COMMITMENTS

| Task | Time | File |
|------|------|------|
| Initial read | 2 min | START_HERE.txt |
| Setup | 5 min | setup.ps1 or setup.bat |
| First run | <1 min | Run: forensic_analyzer.py |
| Check results | 2 min | results/ folder |
| Quick start full | 10 min | QUICKSTART.md |
| Complete learning | 45 min | All docs |
| Deep dive | 2 hrs | All files + examples |

---

## 🔍 FINDING SPECIFIC INFORMATION

| Looking for... | Check file... |
|---|---|
| Quick start | START_HERE.txt or QUICKSTART.md |
| Installation help | QUICKSTART.md or README.md |
| How to use | README.md Usage section |
| Input file format | README.md or FILE_STRUCTURE.md |
| Output description | README.md Output section |
| Customization | README.md or config.py |
| Troubleshooting | README.md Troubleshooting |
| Examples | examples.py |
| File descriptions | FILE_STRUCTURE.md |
| Project overview | PROJECT_SUMMARY.md |
| Verification | CHECKLIST.md |
| All keywords | config.py |

---

## ✅ VERIFICATION CHECKLIST

- [ ] All 14 files present
- [ ] START_HERE.txt accessible
- [ ] setup.ps1 or setup.bat ready
- [ ] forensic_analyzer.py in directory
- [ ] incident_log.csv has data
- [ ] README.md is readable
- [ ] examples.py is complete
- [ ] config.py has settings

---

## 🚀 READY TO START?

**Just run this:**

```powershell
.\setup.ps1
python forensic_analyzer.py incident_log.csv
```

**Then check:** `results/` folder

---

## 📞 HELP RESOURCES

1. **Quick Questions**: See START_HERE.txt
2. **Setup Issues**: See QUICKSTART.md "Troubleshooting"
3. **Usage Questions**: See README.md
4. **Feature Questions**: See examples.py
5. **Customization**: See config.py comments
6. **Verification**: See CHECKLIST.md

---

## 🎓 LEARNING PATH

```
Day 1: Get Started
  ✓ Read START_HERE.txt
  ✓ Run setup.ps1
  ✓ Run first analysis
  ✓ Check results

Day 2: Explore
  ✓ Read QUICKSTART.md
  ✓ Run examples.py
  ✓ Try custom CSV

Day 3: Master
  ✓ Read README.md fully
  ✓ Customize config.py
  ✓ Run advanced version
  ✓ Create custom examples
```

---

## 📊 PROJECT STATISTICS

- **Total Files**: 14
- **Documentation Files**: 6
- **Python Scripts**: 4
- **Configuration/Data**: 2
- **Setup Scripts**: 2
- **Total Lines of Code**: ~1,400
- **Total Documentation Lines**: ~2,100
- **Total Size**: ~150 KB
- **Features**: 12+
- **Examples**: 7
- **Output Formats**: 4

---

**Welcome to the Forensic Analysis Tool! 🔍**

**Next Step**: Open `START_HERE.txt` NOW
