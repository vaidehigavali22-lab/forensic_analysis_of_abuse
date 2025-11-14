"""
Configuration file for Forensic Analysis Tool
Modify these settings to customize the analysis behavior
"""

# ============================================================================
# ABUSE KEYWORDS CONFIGURATION
# ============================================================================
# Add or remove keywords to customize abuse detection
# Keywords are case-insensitive

ABUSIVE_KEYWORDS = {
    # Derogatory terms
    "worthless",
    "stupid",
    "idiot",
    "loser",
    "trash",
    "scum",
    "waste",
    
    # Violent language
    "hate",
    "kill",
    "die",
    "die",
    
    # Gross/disgusting language
    "disgusting",
    "pathetic",
    "horrible",
    "despicable",
    "evil",
    "demonic",
    
    # Negative qualifiers
    "deserve",
    "cancer",
    "plague",
}

# ============================================================================
# SENTIMENT ANALYSIS CONFIGURATION
# ============================================================================

# Sentiment thresholds for classification
# Polarity range: -1 (very negative) to +1 (very positive)
NEGATIVE_THRESHOLD = -0.1  # Below this = Negative
POSITIVE_THRESHOLD = 0.1   # Above this = Positive
# Between thresholds = Neutral

# ============================================================================
# OUTPUT CONFIGURATION
# ============================================================================

OUTPUT_DIR = "results"
RESULTS_CSV = f"{OUTPUT_DIR}/analysis_results.csv"
REPORT_TXT = f"{OUTPUT_DIR}/forensic_report.txt"
VISUALIZATION = f"{OUTPUT_DIR}/sentiment_analysis.png"
HASHES_LOG = f"{OUTPUT_DIR}/integrity_hashes.txt"

# ============================================================================
# VISUALIZATION CONFIGURATION
# ============================================================================

VISUALIZATION_DPI = 300
VISUALIZATION_SIZE = (14, 10)

# Colors for charts
COLOR_NEGATIVE = '#e74c3c'  # Red
COLOR_NEUTRAL = '#95a5a6'   # Gray
COLOR_POSITIVE = '#2ecc71'  # Green
COLOR_ABUSIVE = '#e74c3c'   # Red
COLOR_SAFE = '#2ecc71'      # Green

# ============================================================================
# PROCESSING CONFIGURATION
# ============================================================================

# CSV reading options
CSV_ENCODING = 'utf-8'
CSV_REQUIRED_COLUMNS = ['short_text']

# Hash algorithm
HASH_ALGORITHM = 'sha256'

# File chunk size for hashing (in bytes)
HASH_CHUNK_SIZE = 4096

# ============================================================================
# REPORT CONFIGURATION
# ============================================================================

# Include detailed message list in forensic report
INCLUDE_DETAILED_FINDINGS = True

# Maximum messages to include in detailed findings
MAX_DETAILED_FINDINGS = 10000

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

# Enable console output
VERBOSE_OUTPUT = True

# Log timestamps
LOG_TIMESTAMPS = True

# ============================================================================
# ADVANCED OPTIONS
# ============================================================================

# Show warnings for invalid data
SHOW_WARNINGS = True

# Continue processing on errors
CONTINUE_ON_ERROR = True

# Create backups of existing output files
CREATE_BACKUPS = True

# ============================================================================
# CUSTOM KEYWORD SETS
# ============================================================================
# Define additional keyword groups for different contexts

HARASSMENT_KEYWORDS = {
    "threatening",
    "intimidating",
    "bullying",
    "harassment",
    "stalking",
    "doxxing",
}

SLUR_KEYWORDS = {
    # Note: These are placeholder concepts
    # Add actual slur terms relevant to your analysis
    "offensive_term_1",
    "offensive_term_2",
}

CYBERBULLYING_KEYWORDS = {
    "loser",
    "ugly",
    "fat",
    "weak",
    "pathetic",
    "failure",
    "ridiculous",
}

# ============================================================================
# PRESET KEYWORD SETS
# ============================================================================

KEYWORD_SETS = {
    "general": ABUSIVE_KEYWORDS,
    "harassment": HARASSMENT_KEYWORDS,
    "cyberbullying": CYBERBULLYING_KEYWORDS,
    "combined": ABUSIVE_KEYWORDS | HARASSMENT_KEYWORDS | CYBERBULLYING_KEYWORDS,
}
