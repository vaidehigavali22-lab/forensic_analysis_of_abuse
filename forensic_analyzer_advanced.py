"""
Advanced Forensic Analysis Tool - Configuration-Based Version
Imports settings from config.py for easy customization

This version allows you to modify config.py without touching the main script
"""

import os
import sys
import hashlib
import csv
from datetime import datetime
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from textblob import TextBlob

# Import configuration
try:
    from config import *
except ImportError:
    print("❌ Error: config.py not found. Please ensure config.py is in the same directory.")
    sys.exit(1)


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def ensure_output_directory():
    """Create output directory if it doesn't exist."""
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    if VERBOSE_OUTPUT:
        print(f"✓ Output directory ensured: {OUTPUT_DIR}")


def compute_hash(file_path, algorithm=HASH_ALGORITHM):
    """
    Compute hash of a file for integrity verification.
    
    Args:
        file_path (str): Path to the file to hash
        algorithm (str): Hashing algorithm (from config)
    
    Returns:
        str: Hexadecimal hash value or None
    """
    hash_obj = hashlib.new(algorithm)
    
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(HASH_CHUNK_SIZE), b""):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        if SHOW_WARNINGS:
            print(f"❌ Error: File not found - {file_path}")
        return None
    except Exception as e:
        if SHOW_WARNINGS:
            print(f"❌ Error computing hash: {e}")
        return None


def log_file_integrity(file_path, hash_value):
    """Log file integrity information."""
    try:
        with open(HASHES_LOG, "a") as f:
            timestamp = datetime.now().isoformat() if LOG_TIMESTAMPS else ""
            f.write(f"{timestamp} | {file_path} | {hash_value}\n")
    except Exception as e:
        if SHOW_WARNINGS:
            print(f"⚠ Warning: Could not log integrity - {e}")


# ============================================================================
# ANALYSIS FUNCTIONS
# ============================================================================

def contains_abuse(text, keyword_set=None):
    """
    Check if text contains abusive keywords.
    
    Args:
        text (str): Text to analyze
        keyword_set (set): Keywords to search for (uses default if None)
    
    Returns:
        bool: True if abusive keywords found
    """
    if not isinstance(text, str):
        return False
    
    if keyword_set is None:
        keyword_set = ABUSIVE_KEYWORDS
    
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in keyword_set)


def analyze_sentiment(text):
    """
    Perform sentiment analysis using TextBlob.
    
    Args:
        text (str): Text to analyze
    
    Returns:
        tuple: (polarity, subjectivity)
    """
    if not isinstance(text, str) or not text.strip():
        return 0.0, 0.0
    
    try:
        blob = TextBlob(text)
        return blob.sentiment.polarity, blob.sentiment.subjectivity
    except Exception as e:
        if SHOW_WARNINGS:
            print(f"⚠ Warning: Sentiment analysis failed - {e}")
        return 0.0, 0.0


def classify_sentiment(polarity):
    """Classify sentiment based on polarity score."""
    if polarity < NEGATIVE_THRESHOLD:
        return "Negative"
    elif polarity > POSITIVE_THRESHOLD:
        return "Positive"
    else:
        return "Neutral"


def analyze_abuse(input_file, keyword_preset="general"):
    """
    Main analysis function to detect abusive messages and analyze sentiment.
    
    Args:
        input_file (str): Path to input CSV file
        keyword_preset (str): Which keyword set to use from KEYWORD_SETS
    
    Returns:
        pd.DataFrame: Enhanced dataframe with analysis columns
    """
    if VERBOSE_OUTPUT:
        print(f"\n📂 Loading data from: {input_file}")
    
    try:
        df = pd.read_csv(input_file, encoding=CSV_ENCODING)
        if VERBOSE_OUTPUT:
            print(f"✓ Loaded {len(df)} records")
    except FileNotFoundError:
        print(f"❌ Error: Input file not found - {input_file}")
        return None
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return None
    
    # Verify required columns
    if not all(col in df.columns for col in CSV_REQUIRED_COLUMNS):
        print(f"❌ Error: CSV must contain columns: {CSV_REQUIRED_COLUMNS}")
        return None
    
    # Get keyword set
    keywords = KEYWORD_SETS.get(keyword_preset, ABUSIVE_KEYWORDS)
    
    if VERBOSE_OUTPUT:
        print(f"\n🔍 Analyzing messages (using '{keyword_preset}' keyword set)...")
    
    # Perform analysis
    df["is_abusive"] = df["short_text"].apply(lambda x: contains_abuse(x, keywords))
    df["sentiment_polarity"], df["sentiment_subjectivity"] = zip(
        *df["short_text"].apply(analyze_sentiment)
    )
    df["sentiment_class"] = df["sentiment_polarity"].apply(classify_sentiment)
    
    return df


def generate_summary(df):
    """Generate comprehensive summary statistics."""
    total_messages = len(df)
    abusive_count = df["is_abusive"].sum()
    abusive_percentage = (abusive_count / total_messages * 100) if total_messages > 0 else 0
    
    sentiment_counts = df["sentiment_class"].value_counts().to_dict()
    avg_polarity = df["sentiment_polarity"].mean()
    avg_subjectivity = df["sentiment_subjectivity"].mean()
    
    return {
        "total_messages": total_messages,
        "abusive_count": abusive_count,
        "abusive_percentage": abusive_percentage,
        "sentiment_counts": sentiment_counts,
        "avg_polarity": avg_polarity,
        "avg_subjectivity": avg_subjectivity,
    }


def print_summary(summary, input_file, file_hash):
    """Print analysis summary to console."""
    print("\n" + "="*70)
    print("📊 FORENSIC ANALYSIS SUMMARY")
    print("="*70)
    print(f"File: {input_file}")
    print(f"Hash ({HASH_ALGORITHM.upper()}): {file_hash}")
    print(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-"*70)
    print(f"Total Messages: {summary['total_messages']}")
    print(f"Abusive Messages: {summary['abusive_count']} ({summary['abusive_percentage']:.2f}%)")
    print(f"Average Polarity: {summary['avg_polarity']:.4f}")
    print(f"Average Subjectivity: {summary['avg_subjectivity']:.4f}")
    print("\nSentiment Distribution:")
    for sentiment, count in summary['sentiment_counts'].items():
        percentage = (count / summary['total_messages'] * 100) if summary['total_messages'] > 0 else 0
        print(f"  - {sentiment}: {count} ({percentage:.2f}%)")
    print("="*70 + "\n")


# ============================================================================
# OUTPUT & REPORTING FUNCTIONS
# ============================================================================

def save_results_csv(df, output_file):
    """Save analysis results to CSV."""
    try:
        df.to_csv(output_file, index=False)
        if VERBOSE_OUTPUT:
            print(f"✓ Results saved to: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Error saving CSV: {e}")
        return False


def save_forensic_report(df, summary, input_file, file_hash, output_file):
    """Save detailed forensic report as text file."""
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("="*80 + "\n")
            f.write("DIGITAL FORENSIC ANALYSIS REPORT - ONLINE ABUSE DETECTION\n")
            f.write("="*80 + "\n\n")
            
            f.write("[EVIDENCE INFORMATION]\n")
            f.write(f"Source File: {input_file}\n")
            f.write(f"{HASH_ALGORITHM.upper()} Hash: {file_hash}\n")
            f.write(f"Analysis Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
            f.write(f"Total Records: {summary['total_messages']}\n\n")
            
            f.write("[ABUSE DETECTION RESULTS]\n")
            f.write(f"Abusive Messages Found: {summary['abusive_count']}\n")
            f.write(f"Abuse Percentage: {summary['abusive_percentage']:.2f}%\n")
            f.write(f"Abusive Keywords Used: {', '.join(sorted(ABUSIVE_KEYWORDS))}\n\n")
            
            f.write("[SENTIMENT ANALYSIS]\n")
            f.write(f"Average Polarity: {summary['avg_polarity']:.4f}\n")
            f.write(f"Average Subjectivity: {summary['avg_subjectivity']:.4f}\n")
            f.write("Sentiment Distribution:\n")
            for sentiment, count in summary['sentiment_counts'].items():
                percentage = (count / summary['total_messages'] * 100) if summary['total_messages'] > 0 else 0
                f.write(f"  {sentiment}: {count} ({percentage:.2f}%)\n")
            f.write("\n")
            
            if INCLUDE_DETAILED_FINDINGS:
                f.write("[DETAILED FINDINGS]\n")
                f.write(f"{'ID':<10} {'Platform':<15} {'Abusive':<10} {'Polarity':<12} {'Sentiment':<12}\n")
                f.write("-"*80 + "\n")
                
                for idx, row in df.iterrows():
                    if idx >= MAX_DETAILED_FINDINGS:
                        f.write(f"... ({len(df) - idx} more records)\n")
                        break
                    
                    record_id = str(row.get('id', idx))[:10]
                    platform = str(row.get('platform', 'N/A'))[:15]
                    is_abusive = "YES" if row['is_abusive'] else "NO"
                    polarity = f"{row['sentiment_polarity']:.4f}"
                    sentiment = row['sentiment_class']
                    
                    f.write(f"{record_id:<10} {platform:<15} {is_abusive:<10} {polarity:<12} {sentiment:<12}\n")
            
            f.write("\n" + "="*80 + "\n")
            f.write("END OF REPORT\n")
            f.write("="*80 + "\n")
        
        if VERBOSE_OUTPUT:
            print(f"✓ Forensic report saved to: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Error saving report: {e}")
        return False


# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def visualize_sentiment(df, output_file):
    """Generate visualization of sentiment polarity distribution."""
    try:
        fig, axes = plt.subplots(2, 2, figsize=VISUALIZATION_SIZE, dpi=VISUALIZATION_DPI)
        fig.suptitle("Sentiment Analysis Visualization - Forensic Report", fontsize=16, fontweight='bold')
        
        # 1. Sentiment Class Distribution
        sentiment_counts = df['sentiment_class'].value_counts()
        colors = [COLOR_NEGATIVE, COLOR_NEUTRAL, COLOR_POSITIVE]
        axes[0, 0].pie(
            sentiment_counts.values,
            labels=sentiment_counts.index,
            autopct='%1.1f%%',
            colors=colors[:len(sentiment_counts)],
            startangle=90
        )
        axes[0, 0].set_title("Sentiment Class Distribution", fontweight='bold')
        
        # 2. Abusive vs Non-Abusive
        abuse_counts = df['is_abusive'].value_counts()
        abuse_labels = ['Non-Abusive', 'Abusive']
        abuse_values = [abuse_counts.get(False, 0), abuse_counts.get(True, 0)]
        axes[0, 1].bar(abuse_labels, abuse_values, color=[COLOR_SAFE, COLOR_ABUSIVE])
        axes[0, 1].set_title("Abuse Detection Results", fontweight='bold')
        axes[0, 1].set_ylabel("Count")
        for i, v in enumerate(abuse_values):
            axes[0, 1].text(i, v + 0.5, str(v), ha='center', fontweight='bold')
        
        # 3. Polarity Distribution
        axes[1, 0].hist(df['sentiment_polarity'], bins=30, color='#3498db', edgecolor='black', alpha=0.7)
        axes[1, 0].set_title("Sentiment Polarity Distribution", fontweight='bold')
        axes[1, 0].set_xlabel("Polarity Score")
        axes[1, 0].set_ylabel("Frequency")
        mean_polarity = df['sentiment_polarity'].mean()
        axes[1, 0].axvline(mean_polarity, color='red', linestyle='--', linewidth=2, 
                          label=f"Mean: {mean_polarity:.3f}")
        axes[1, 0].legend()
        
        # 4. Subjectivity Distribution
        axes[1, 1].hist(df['sentiment_subjectivity'], bins=30, color='#f39c12', edgecolor='black', alpha=0.7)
        axes[1, 1].set_title("Sentiment Subjectivity Distribution", fontweight='bold')
        axes[1, 1].set_xlabel("Subjectivity Score")
        axes[1, 1].set_ylabel("Frequency")
        mean_subjectivity = df['sentiment_subjectivity'].mean()
        axes[1, 1].axvline(mean_subjectivity, color='red', linestyle='--', linewidth=2,
                          label=f"Mean: {mean_subjectivity:.3f}")
        axes[1, 1].legend()
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=VISUALIZATION_DPI, bbox_inches='tight')
        if VERBOSE_OUTPUT:
            print(f"✓ Visualization saved to: {output_file}")
        plt.close()
    except Exception as e:
        print(f"❌ Error creating visualization: {e}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main(input_file="incident_log.csv", keyword_preset="general"):
    """
    Main orchestration function.
    
    Args:
        input_file (str): Path to input CSV file
        keyword_preset (str): Keyword set to use ('general', 'harassment', 'cyberbullying', 'combined')
    """
    print("\n" + "🔍 "*20)
    print("FORENSIC ANALYSIS TOOL - ONLINE ABUSE DETECTION (Advanced)")
    print("🔍 "*20 + "\n")
    
    # Step 1: Ensure output directory
    ensure_output_directory()
    
    # Step 2: Compute file hash
    print(f"\n🔐 Computing file integrity hash...")
    file_hash = compute_hash(input_file)
    if file_hash:
        print(f"✓ {HASH_ALGORITHM.upper()}: {file_hash}")
        log_file_integrity(input_file, file_hash)
    else:
        if CONTINUE_ON_ERROR:
            print("⚠ Continuing without integrity verification...")
            file_hash = "N/A"
        else:
            print("❌ Failed to compute hash. Exiting.")
            return
    
    # Step 3: Analyze abuse and sentiment
    df = analyze_abuse(input_file, keyword_preset)
    if df is None:
        print("❌ Analysis failed. Exiting.")
        return
    
    # Step 4: Generate summary
    summary = generate_summary(df)
    
    # Step 5: Print summary
    print_summary(summary, input_file, file_hash)
    
    # Step 6: Save results
    save_results_csv(df, RESULTS_CSV)
    save_forensic_report(df, summary, input_file, file_hash, REPORT_TXT)
    visualize_sentiment(df, VISUALIZATION)
    
    print("\n" + "✅ "*20)
    print("ANALYSIS COMPLETE")
    print("✅ "*20)
    print(f"\n📁 Results folder: {os.path.abspath(OUTPUT_DIR)}")
    print(f"📄 CSV Report: {RESULTS_CSV}")
    print(f"📊 Visualization: {VISUALIZATION}")
    print(f"📋 Detailed Report: {REPORT_TXT}")
    print(f"🔐 Integrity Log: {HASHES_LOG}\n")


if __name__ == "__main__":
    keyword_set = "general"  # Change to 'harassment', 'cyberbullying', or 'combined'
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "incident_log.csv"
    
    if len(sys.argv) > 2:
        keyword_set = sys.argv[2]
    
    main(input_file, keyword_set)
