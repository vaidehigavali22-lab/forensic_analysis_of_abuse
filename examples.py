"""
Example & Test Script for Forensic Analysis Tool
Demonstrates how to use the analyzer programmatically
"""

from forensic_analyzer import (
    compute_hash,
    analyze_abuse,
    generate_summary,
    print_summary,
    save_results_csv,
    save_forensic_report,
    visualize_sentiment,
    ensure_output_directory,
)

import pandas as pd


def example_1_basic_analysis():
    """Example 1: Basic analysis with default settings"""
    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Analysis")
    print("="*70)
    
    ensure_output_directory()
    
    input_file = "incident_log.csv"
    file_hash = compute_hash(input_file)
    print(f"File hash: {file_hash}")
    
    df = analyze_abuse(input_file)
    summary = generate_summary(df)
    print_summary(summary, input_file, file_hash)


def example_2_custom_output():
    """Example 2: Analyze with custom output files"""
    print("\n" + "="*70)
    print("EXAMPLE 2: Custom Output")
    print("="*70)
    
    ensure_output_directory()
    
    input_file = "incident_log.csv"
    output_csv = "results/custom_analysis.csv"
    output_report = "results/custom_report.txt"
    output_viz = "results/custom_visualization.png"
    
    # Analyze
    df = analyze_abuse(input_file)
    summary = generate_summary(df)
    file_hash = compute_hash(input_file)
    
    # Save to custom locations
    save_results_csv(df, output_csv)
    save_forensic_report(df, summary, input_file, file_hash, output_report)
    visualize_sentiment(df, output_viz)
    
    print(f"✓ Results saved to custom locations")
    print(f"  CSV: {output_csv}")
    print(f"  Report: {output_report}")
    print(f"  Visualization: {output_viz}")


def example_3_programmatic_filtering():
    """Example 3: Analyze and filter results programmatically"""
    print("\n" + "="*70)
    print("EXAMPLE 3: Programmatic Filtering")
    print("="*70)
    
    df = analyze_abuse("incident_log.csv")
    
    # Filter abusive messages
    abusive_messages = df[df['is_abusive'] == True]
    print(f"\n🚨 Found {len(abusive_messages)} abusive messages:")
    print(abusive_messages[['id', 'short_text', 'sentiment_polarity']])
    
    # Filter highly negative messages
    negative_messages = df[df['sentiment_polarity'] < -0.5]
    print(f"\n😠 Found {len(negative_messages)} highly negative messages:")
    print(negative_messages[['id', 'short_text', 'sentiment_polarity']])
    
    # Combined filter: abusive AND negative
    severe = df[(df['is_abusive'] == True) & (df['sentiment_polarity'] < -0.3)]
    print(f"\n⚠️  Found {len(severe)} severe cases (abusive + negative):")
    print(severe[['id', 'short_text', 'is_abusive', 'sentiment_polarity']])


def example_4_statistics():
    """Example 4: Generate custom statistics"""
    print("\n" + "="*70)
    print("EXAMPLE 4: Custom Statistics")
    print("="*70)
    
    df = analyze_abuse("incident_log.csv")
    
    print("\n📊 Statistics by Platform:")
    if 'platform' in df.columns:
        platform_stats = df.groupby('platform').agg({
            'is_abusive': ['count', 'sum'],
            'sentiment_polarity': ['mean', 'min', 'max']
        })
        print(platform_stats)
    
    print("\n📊 Abusive Message Statistics:")
    abusive = df[df['is_abusive'] == True]
    print(f"  Count: {len(abusive)}")
    print(f"  Avg Polarity: {abusive['sentiment_polarity'].mean():.4f}")
    print(f"  Avg Subjectivity: {abusive['sentiment_subjectivity'].mean():.4f}")
    
    print("\n📊 Non-Abusive Message Statistics:")
    safe = df[df['is_abusive'] == False]
    print(f"  Count: {len(safe)}")
    print(f"  Avg Polarity: {safe['sentiment_polarity'].mean():.4f}")
    print(f"  Avg Subjectivity: {safe['sentiment_subjectivity'].mean():.4f}")


def example_5_sentiment_breakdown():
    """Example 5: Detailed sentiment breakdown"""
    print("\n" + "="*70)
    print("EXAMPLE 5: Sentiment Breakdown")
    print("="*70)
    
    df = analyze_abuse("incident_log.csv")
    
    for sentiment in ['Negative', 'Neutral', 'Positive']:
        messages = df[df['sentiment_class'] == sentiment]
        print(f"\n{sentiment.upper()} Messages ({len(messages)}):")
        if len(messages) > 0:
            print(messages[['short_text', 'sentiment_polarity']].head(3).to_string())


def example_6_create_custom_csv():
    """Example 6: Create a sample CSV for testing"""
    print("\n" + "="*70)
    print("EXAMPLE 6: Create Custom Test Data")
    print("="*70)
    
    custom_data = {
        'id': range(1, 6),
        'datetime_utc': ['2025-11-12T10:00:00Z'] * 5,
        'platform': ['Twitter', 'Facebook', 'Instagram', 'Discord', 'Twitter'],
        'url': ['https://example.com'] * 5,
        'short_text': [
            'You are stupid and worthless',
            'Beautiful sunny day!',
            'I hate everything',
            'Thanks for the support!',
            'You deserve to die',
        ],
        'victim_follows_abuser': [False, True, False, True, False]
    }
    
    df = pd.DataFrame(custom_data)
    df.to_csv('results/test_data.csv', index=False)
    print("✓ Created test_data.csv with 5 sample messages")
    print(df.to_string(index=False))


def example_7_compare_datasets():
    """Example 7: Compare two datasets"""
    print("\n" + "="*70)
    print("EXAMPLE 7: Compare Datasets")
    print("="*70)
    
    print("\n📊 Comparing multiple analysis runs:")
    
    # First analysis
    df1 = analyze_abuse("incident_log.csv")
    sum1 = generate_summary(df1)
    
    print(f"\nDataset 1 (incident_log.csv):")
    print(f"  Total: {sum1['total_messages']}")
    print(f"  Abusive: {sum1['abusive_count']} ({sum1['abusive_percentage']:.1f}%)")
    print(f"  Avg Polarity: {sum1['avg_polarity']:.4f}")


def run_all_examples():
    """Run all examples"""
    print("\n🧪 RUNNING FORENSIC ANALYSIS TOOL EXAMPLES\n")
    
    try:
        example_1_basic_analysis()
        example_2_custom_output()
        example_3_programmatic_filtering()
        example_4_statistics()
        example_5_sentiment_breakdown()
        example_6_create_custom_csv()
        example_7_compare_datasets()
        
        print("\n" + "="*70)
        print("✅ ALL EXAMPLES COMPLETED SUCCESSFULLY")
        print("="*70)
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    print("\n" + "🔬 "*20)
    print("FORENSIC ANALYSIS TOOL - EXAMPLES & TESTS")
    print("🔬 "*20)
    
    run_all_examples()
    
    print("\n💡 Try modifying these examples to suit your needs!")
    print("💡 Import functions from forensic_analyzer.py in your own scripts\n")
