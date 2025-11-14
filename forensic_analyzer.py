"""
🧩 FORENSIC ANALYSIS TOOL FOR ONLINE ABUSE
===========================================

A Python-based forensic analysis tool that detects abusive or harassing messages 
from a dataset (CSV file) and performs digital evidence integrity checks using hashing.

Author: Forensic Analysis Team
Date: 2025
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


# ============================================================================
# CONFIGURATION & CONSTANTS
# ============================================================================

# Abusive keywords to detect
ABUSIVE_KEYWORDS = {
    "worthless",
    "hate",
    "kill",
    "stupid",
    "idiot",
    "disgusting",
    "pathetic",
    "loser",
    "trash",
    "scum",
    "waste",
    "deserve",
    "die",
    "cancer",
    "plague",
    "evil",
    "demonic",
    "horrible",
    "despicable",
}

# Sentiment thresholds
NEGATIVE_THRESHOLD = -0.1
POSITIVE_THRESHOLD = 0.1

# Output configuration
OUTPUT_DIR = "results"
RESULTS_CSV = os.path.join(OUTPUT_DIR, "analysis_results.csv")
REPORT_TXT = os.path.join(OUTPUT_DIR, "forensic_report.txt")
VISUALIZATION = os.path.join(OUTPUT_DIR, "sentiment_analysis.png")
HASHES_LOG = os.path.join(OUTPUT_DIR, "integrity_hashes.txt")


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def ensure_output_directory():
    """Create output directory if it doesn't exist."""
    Path(OUTPUT_DIR).mkdir(exist_ok=True)
    print(f"✓ Output directory ensured: {OUTPUT_DIR}")


def compute_hash(file_path, algorithm="sha256"):
    """
    Compute SHA256 hash of a file for integrity verification.
    
    Args:
        file_path (str): Path to the file to hash
        algorithm (str): Hashing algorithm (default: sha256)
    
    Returns:
        str: Hexadecimal hash value
    """
    hash_obj = hashlib.new(algorithm)
    
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        print(f"❌ Error: File not found - {file_path}")
        return None
    except Exception as e:
        print(f"❌ Error computing hash: {e}")
        return None


def log_file_integrity(file_path, hash_value):
    """Log file integrity information to a dedicated file."""
    try:
        with open(HASHES_LOG, "a") as f:
            timestamp = datetime.now().isoformat()
            f.write(f"{timestamp} | {file_path} | {hash_value}\n")
    except Exception as e:
        print(f"⚠ Warning: Could not log integrity - {e}")


# ============================================================================
# ANALYSIS FUNCTIONS
# ============================================================================

def contains_abuse(text):
    """
    Check if text contains abusive keywords.
    
    Args:
        text (str): Text to analyze
    
    Returns:
        bool: True if abusive keywords found, False otherwise
    """
    if not isinstance(text, str):
        return False
    
    text_lower = text.lower()
    return any(keyword in text_lower for keyword in ABUSIVE_KEYWORDS)


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
        print(f"⚠ Warning: Sentiment analysis failed for text - {e}")
        return 0.0, 0.0


def classify_sentiment(polarity):
    """
    Classify sentiment based on polarity score.
    
    Args:
        polarity (float): Sentiment polarity (-1 to 1)
    
    Returns:
        str: Sentiment classification (Negative, Neutral, Positive)
    """
    if polarity < NEGATIVE_THRESHOLD:
        return "Negative"
    elif polarity > POSITIVE_THRESHOLD:
        return "Positive"
    else:
        return "Neutral"


def analyze_abuse(input_file):
    """
    Main analysis function to detect abusive messages and analyze sentiment.
    
    Args:
        input_file (str): Path to input CSV file
    
    Returns:
        pd.DataFrame: Enhanced dataframe with analysis columns
    """
    print(f"\n📂 Loading data from: {input_file}")
    
    try:
        df = pd.read_csv(input_file)
        print(f"✓ Loaded {len(df)} records")
    except FileNotFoundError:
        print(f"❌ Error: Input file not found - {input_file}")
        return None
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return None
    
    # Verify required columns
    required_columns = ["short_text"]
    if not all(col in df.columns for col in required_columns):
        print(f"❌ Error: CSV must contain column 'short_text'")
        return None
    
    print("\n🔍 Analyzing messages...")
    
    # Perform analysis
    df["is_abusive"] = df["short_text"].apply(contains_abuse)
    df["sentiment_polarity"], df["sentiment_subjectivity"] = zip(
        *df["short_text"].apply(analyze_sentiment)
    )
    df["sentiment_class"] = df["sentiment_polarity"].apply(classify_sentiment)
    
    return df


def generate_summary(df):
    """
    Generate a comprehensive summary of the analysis.
    
    Args:
        df (pd.DataFrame): Analyzed dataframe
    
    Returns:
        dict: Summary statistics
    """
    total_messages = len(df)
    abusive_count = df["is_abusive"].sum()
    abusive_percentage = (abusive_count / total_messages * 100) if total_messages > 0 else 0
    
    sentiment_counts = df["sentiment_class"].value_counts().to_dict()
    avg_polarity = df["sentiment_polarity"].mean()
    avg_subjectivity = df["sentiment_subjectivity"].mean()
    
    summary = {
        "total_messages": total_messages,
        "abusive_count": abusive_count,
        "abusive_percentage": abusive_percentage,
        "sentiment_counts": sentiment_counts,
        "avg_polarity": avg_polarity,
        "avg_subjectivity": avg_subjectivity,
    }
    
    return summary


def print_summary(summary, input_file, file_hash):
    """Print analysis summary to console."""
    print("\n" + "="*70)
    print("📊 FORENSIC ANALYSIS SUMMARY")
    print("="*70)
    print(f"File: {input_file}")
    print(f"Hash (SHA256): {file_hash}")
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
            f.write(f"SHA256 Hash: {file_hash}\n")
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
            
            f.write("[DETAILED FINDINGS]\n")
            f.write(f"{'ID':<10} {'Platform':<15} {'Abusive':<10} {'Polarity':<12} {'Sentiment':<12}\n")
            f.write("-"*80 + "\n")
            
            for idx, row in df.iterrows():
                if pd.isna(row.get('id')):
                    record_id = str(idx)
                else:
                    record_id = str(row['id'])
                
                platform = str(row.get('platform', 'N/A'))[:15]
                is_abusive = "YES" if row['is_abusive'] else "NO"
                polarity = f"{row['sentiment_polarity']:.4f}"
                sentiment = row['sentiment_class']
                
                f.write(f"{record_id:<10} {platform:<15} {is_abusive:<10} {polarity:<12} {sentiment:<12}\n")
            
            f.write("\n" + "="*80 + "\n")
            f.write("END OF REPORT\n")
            f.write("="*80 + "\n")
        
        print(f"✓ Forensic report saved to: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Error saving report: {e}")
        return False


# ============================================================================
# VISUALIZATION FUNCTIONS
# ============================================================================

def visualize_sentiment(df, output_file):
    """
    Generate visualization of sentiment polarity distribution.
    
    Args:
        df (pd.DataFrame): Analyzed dataframe
        output_file (str): Path to save visualization
    """
    try:
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle("Sentiment Analysis Visualization - Forensic Report", fontsize=16, fontweight='bold')
        
        # 1. Sentiment Class Distribution
        sentiment_counts = df['sentiment_class'].value_counts()
        colors = ['#e74c3c', '#95a5a6', '#2ecc71']
        axes[0, 0].pie(
            sentiment_counts.values,
            labels=sentiment_counts.index,
            autopct='%1.1f%%',
            colors=colors,
            startangle=90
        )
        axes[0, 0].set_title("Sentiment Class Distribution", fontweight='bold')
        
        # 2. Abusive vs Non-Abusive Messages
        abuse_counts = df['is_abusive'].value_counts()
        abuse_labels = ['Non-Abusive', 'Abusive']
        abuse_values = [abuse_counts.get(False, 0), abuse_counts.get(True, 0)]
        axes[0, 1].bar(abuse_labels, abuse_values, color=['#2ecc71', '#e74c3c'])
        axes[0, 1].set_title("Abuse Detection Results", fontweight='bold')
        axes[0, 1].set_ylabel("Count")
        for i, v in enumerate(abuse_values):
            axes[0, 1].text(i, v + 0.5, str(v), ha='center', fontweight='bold')
        
        # 3. Polarity Distribution Histogram
        axes[1, 0].hist(df['sentiment_polarity'], bins=30, color='#3498db', edgecolor='black', alpha=0.7)
        axes[1, 0].set_title("Sentiment Polarity Distribution", fontweight='bold')
        axes[1, 0].set_xlabel("Polarity Score")
        axes[1, 0].set_ylabel("Frequency")
        axes[1, 0].axvline(df['sentiment_polarity'].mean(), color='red', linestyle='--', linewidth=2, label=f"Mean: {df['sentiment_polarity'].mean():.3f}")
        axes[1, 0].legend()
        
        # 4. Subjectivity Distribution Histogram
        axes[1, 1].hist(df['sentiment_subjectivity'], bins=30, color='#f39c12', edgecolor='black', alpha=0.7)
        axes[1, 1].set_title("Sentiment Subjectivity Distribution", fontweight='bold')
        axes[1, 1].set_xlabel("Subjectivity Score")
        axes[1, 1].set_ylabel("Frequency")
        axes[1, 1].axvline(df['sentiment_subjectivity'].mean(), color='red', linestyle='--', linewidth=2, label=f"Mean: {df['sentiment_subjectivity'].mean():.3f}")
        axes[1, 1].legend()
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight')
        print(f"✓ Visualization saved to: {output_file}")
        plt.close()
    except Exception as e:
        print(f"❌ Error creating visualization: {e}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main(input_file="incident_log.csv"):
    """
    Main orchestration function.
    
    Args:
        input_file (str): Path to input CSV file
    """
    print("\n" + "🔍 "*20)
    print("FORENSIC ANALYSIS TOOL - ONLINE ABUSE DETECTION")
    print("🔍 "*20 + "\n")
    
    # Step 1: Ensure output directory
    ensure_output_directory()
    
    # Step 2: Compute file hash for integrity
    print(f"\n🔐 Computing file integrity hash...")
    file_hash = compute_hash(input_file)
    if file_hash:
        print(f"✓ SHA256: {file_hash}")
        log_file_integrity(input_file, file_hash)
    else:
        print("❌ Failed to compute hash. Continuing without integrity verification...")
        file_hash = "N/A"
    
    # Step 3: Analyze abuse and sentiment
    df = analyze_abuse(input_file)
    if df is None:
        print("❌ Analysis failed. Exiting.")
        return
    
    # Step 4: Generate summary
    summary = generate_summary(df)
    
    # Step 5: Print summary to console
    print_summary(summary, input_file, file_hash)
    
    # Step 6: Save results to CSV
    save_results_csv(df, RESULTS_CSV)
    
    # Step 7: Save forensic report
    save_forensic_report(df, summary, input_file, file_hash, REPORT_TXT)
    
    # Step 8: Generate visualization
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
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "incident_log.csv"
    
    main(input_file)
