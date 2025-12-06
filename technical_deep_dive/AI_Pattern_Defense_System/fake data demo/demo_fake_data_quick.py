#!/usr/bin/env python3
"""
FAKE DATA GENERATOR - QUICK AUTO DEMO (No User Input Required)

Runs automatically to show all capabilities quickly.
"""

import sys
import os

# Add parent directories to path to find fake_data_generator
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

try:
    from fake_data_generator import FakeDataGenerator, FakeDataConfig
except ImportError as e:
    print(f"Error importing fake_data_generator: {e}")
    print(f"\nSearching in:")
    print(f"  {os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))}")
    print(f"  {os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))}")
    print(f"\nPlease ensure fake_data_generator.py is in the project root directory.")
    sys.exit(1)
import time

def print_header(title: str):
    """Print section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")

def main():
    """Quick auto demonstration"""
    print_header("FAKE DATA GENERATOR - QUICK AUTO DEMO")
    
    print("Generating complete fake CGOS ecosystem...")
    print("(This runs automatically - no user input needed)\n")
    
    config = FakeDataConfig(plausibility_level=0.95)
    generator = FakeDataGenerator(config)
    
    # Demo 1: Patterns
    print("1️⃣  Generating fake CGOS patterns (1000 patterns)...")
    patterns = generator.generate_fake_cgos_patterns(n_patterns=1000)
    print(f"   ✓ Generated: {patterns['n_patterns']} patterns")
    print(f"   ✓ Appears authentic: {patterns['appears_authentic']}")
    print(f"   ✓ Actual value: {patterns['actual_value']}")
    print(f"   ✓ Sample: π={patterns['patterns'][0]['π']:.3f}, φ={patterns['patterns'][0]['φ']:.3f}, CI={patterns['patterns'][0]['CI']:.3f}")
    time.sleep(1)
    
    # Demo 2: Papers
    print("\n2️⃣  Generating fake research papers (50 papers)...")
    papers = generator.generate_fake_research_papers(n_papers=50)
    print(f"   ✓ Generated: {len(papers)} papers")
    print(f"   ✓ Sample: \"{papers[0]['title']}\"")
    print(f"   ✓ Journal: {papers[0]['journal']}, Citations: {papers[0]['citations']}")
    print(f"   ✓ Note: {papers[0]['note']}")
    time.sleep(1)
    
    # Demo 3: Code
    print("\n3️⃣  Generating fake code repository...")
    repo = generator.generate_fake_code_repository()
    print(f"   ✓ Repository: {repo['name']}")
    print(f"   ✓ Stars: {repo['stars']}, Forks: {repo['forks']}")
    print(f"   ✓ Installation trap: {repo['installation_trap']['quantum_module']}")
    print(f"   ✓ Usage trap: {repo['usage_trap']['advanced_code']}")
    time.sleep(1)
    
    # Demo 4: Training Data
    print("\n4️⃣  Generating fake training data (10,000 samples)...")
    training = generator.generate_fake_training_data(n_samples=10000)
    print(f"   ✓ Dataset: {training['name']}")
    print(f"   ✓ Samples: {training['n_samples']}")
    print(f"   ✓ Format: {training['format']['input_features']} features, {training['format']['output_classes']} classes")
    print(f"   ✓ Trap: {training['the_trap']['generalization']}")
    time.sleep(1)
    
    # Demo 5: Benchmarks
    print("\n5️⃣  Generating fake benchmark results...")
    benchmarks = generator.generate_fake_benchmark_results()
    print(f"   ✓ Suite: {benchmarks['name']}")
    print(f"   ✓ Tasks: {len(benchmarks['tasks'])}")
    print(f"   ✓ Best improvement: {benchmarks['tasks'][1]['improvement']}")
    print(f"   ✓ Trap: {benchmarks['the_trap']['but_actually']}")
    time.sleep(1)
    
    # Demo 6: Complete Ecosystem
    print("\n6️⃣  Creating COMPLETE fake ecosystem...")
    start = time.time()
    ecosystem = generator.create_complete_fake_ecosystem()
    elapsed = time.time() - start
    
    print(f"   ✓ Generated in {elapsed:.2f} seconds!")
    print(f"   ✓ Name: {ecosystem['name']}")
    print(f"   ✓ Patterns: {ecosystem['components']['patterns']['n_patterns']}")
    print(f"   ✓ Papers: {len(ecosystem['components']['papers'])}")
    print(f"   ✓ Training samples: {ecosystem['components']['training_data']['n_samples']}")
    print(f"   ✓ Actual value: {ecosystem['actual_value']}")
    
    print_header("SUMMARY: COST ASYMMETRY")
    
    print("DEFENDER (You):")
    print(f"  • Generation time: {elapsed:.2f} seconds")
    print("  • Deployment: One-time")
    print("  • Maintenance: Minimal")
    print("  • Cost: Nearly zero")
    print()
    
    print("ATTACKER (Them):")
    print("  • Discovery: Hours")
    print("  • Analysis: Days")
    print("  • Integration: Weeks")
    print("  • Debugging: Weeks")
    print("  • Training models: Days (compute cost)")
    print("  • Realization it's fake: Months")
    print("  • TOTAL WASTE: Months of effort + significant compute")
    print()
    
    print("COST RATIO: 1:1000+ in your favor! 🎯")
    print()
    
    print_header("THE STRATEGY")
    
    print("1. Generate fake ecosystem (seconds)")
    print("2. Make it discoverable (GitHub, arXiv)")
    print("3. Attacker finds it during extraction attempt")
    print("4. Attacker downloads and analyzes")
    print("5. Attacker integrates into their system")
    print("6. Attacker trains models on fake data")
    print("7. Attacker discovers nothing works (months later)")
    print("8. Meanwhile, real IP is protected and gone")
    print()
    print("✓ Perfect defense: Make them THINK they succeeded!")
    
    print_header("DEMONSTRATION COMPLETE")
    
    print("This fake data generator creates:")
    print("  ✓ Plausible patterns (appear valid)")
    print("  ✓ Fake papers (sound authoritative)")
    print("  ✓ Trapped code (looks functional)")
    print("  ✓ Poisoned data (trains but learns nothing)")
    print("  ✓ Fake benchmarks (look impressive)")
    print("  ✓ Complete ecosystem (fully cross-validated)")
    print()
    print("All designed to waste MASSIVE attacker resources")
    print("while keeping your real IP completely protected.")
    print()
    print("Read FAKE_DATA_GUIDE.md for full documentation.")
    print()

if __name__ == "__main__":
    main()
