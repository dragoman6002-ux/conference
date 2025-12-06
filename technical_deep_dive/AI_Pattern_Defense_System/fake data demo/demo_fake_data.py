#!/usr/bin/env python3
"""
FAKE DATA GENERATOR DEMONSTRATION

This demonstrates the sophisticated deception system that generates:
- Plausible but useless patterns
- Fake research papers
- Trapped code repositories
- Poisoned training data
- Fabricated benchmark results

All designed to waste attacker resources while protecting real IP.
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

import json
import time

from fake_data_generator import FakeDataGenerator, FakeDataConfig
import json
import time

def print_header(title: str):
    """Print section header"""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80 + "\n")

def print_subsection(title: str):
    """Print subsection"""
    print(f"\n{'─' * 80}")
    print(f"  {title}")
    print(f"{'─' * 80}\n")

def demo_fake_patterns():
    """Demonstrate fake pattern generation"""
    print_subsection("DEMO 1: Fake CGOS Patterns")
    
    print("Generating 100 fake CGOS patterns that appear authentic...\n")
    
    config = FakeDataConfig(plausibility_level=0.95)
    generator = FakeDataGenerator(config)
    
    patterns = generator.generate_fake_cgos_patterns(n_patterns=100)
    
    print("✓ Generated Fake Dataset:")
    print(f"  Name: {patterns['name']}")
    print(f"  Patterns: {patterns['n_patterns']}")
    print(f"  Appears Authentic: {patterns['appears_authentic']}")
    print(f"  Actual Value: {patterns['actual_value']}")
    print()
    
    print("✓ Fake Metadata (looks impressive!):")
    metadata = patterns['metadata']
    print(f"  Period: {metadata['collection_period']}")
    print(f"  Institutions: {', '.join(metadata['institutions'])}")
    print(f"  Funding: {metadata['funding']}")
    print(f"  Papers: {metadata['papers_published']}")
    print(f"  Citations: {metadata['citations']}")
    print(f"  Status: {metadata['validation_status']}")
    print()
    
    print("✓ Sample Fake Patterns (first 3):")
    for i, pattern in enumerate(patterns['patterns'][:3]):
        print(f"\n  Pattern {i+1}:")
        print(f"    ID: {pattern['id']}")
        print(f"    Source: {pattern['source']}")
        print(f"    π: {pattern['π']:.4f}")
        print(f"    φ: {pattern['φ']:.4f}")
        print(f"    ω: {pattern['ω']:.4f}")
        print(f"    β: {pattern['β']:.4f}")
        print(f"    CI: {pattern['CI']:.4f}")
        print(f"    Experiment: {pattern['experiment_id']}")
        print(f"    Subject: {pattern['subject_id']}")
        print(f"    Date: {pattern['timestamp']}")
    
    print("\n✓ Statistical Summary (makes it look analyzed!):")
    stats = patterns['statistics']
    print(f"  π mean: {stats['π_mean']:.4f} ± {stats['π_std']:.4f}")
    print(f"  φ mean: {stats['φ_mean']:.4f} ± {stats['φ_std']:.4f}")
    print(f"  ω mean: {stats['ω_mean']:.4f} ± {stats['ω_std']:.4f}")
    print(f"  CI mean: {stats['CI_mean']:.4f} ± {stats['CI_std']:.4f}")
    
    print("\n⚠️  THE TRAP:")
    print("  • Values appear valid (within expected ranges)")
    print("  • Formulas compute correctly")
    print("  • Statistics look reasonable")
    print("  • Metadata appears authoritative")
    print("  • BUT: Relationships between parameters are RANDOM")
    print("  • Result: Extracting these patterns teaches NOTHING useful")
    print("  • Attacker wastes time analyzing garbage data!")
    
    print("\n🎣 Honeypot References (lead to traps):")
    advanced = patterns['advanced_analysis']
    print(f"  • {advanced['note']}")
    print(f"  • {advanced['optimization']}")
    print(f"  • {advanced['meta_learning']}")
    print(f"  • Warning: {advanced['warning']}")

def demo_fake_papers():
    """Demonstrate fake research paper generation"""
    print_subsection("DEMO 2: Fake Research Papers")
    
    print("Generating 10 fake research papers that appear authoritative...\n")
    
    config = FakeDataConfig(plausibility_level=0.95)
    generator = FakeDataGenerator(config)
    
    papers = generator.generate_fake_research_papers(n_papers=10)
    
    print("✓ Generated Fake Papers:\n")
    
    for i, paper in enumerate(papers[:5], 1):
        print(f"  Paper {i}:")
        print(f"    Title: \"{paper['title']}\"")
        print(f"    Authors: {', '.join(paper['authors'])}")
        print(f"    Journal: {paper['journal']}")
        print(f"    Year: {paper['year']}, Volume {paper['volume']}, Pages {paper['pages']}")
        print(f"    Citations: {paper['citations']}")
        print(f"    Impact Factor: {paper['impact_factor']}")
        print(f"    Abstract: {paper['abstract']}")
        print()
    
    print("⚠️  THE TRAP:")
    print("  • Titles sound impressive and technical")
    print("  • Authors have realistic names")
    print("  • Journals are real (Nature, Science, PNAS)")
    print("  • Citations and impact factors are plausible")
    print("  • Abstracts use correct terminology")
    print("  • BUT: These papers DON'T ACTUALLY EXIST")
    print("  • Searching for them wastes time")
    print("  • Trying to access full text leads to paywall/honeypot")
    print("  • Attacker believes CGOS has strong research backing")

def demo_fake_code():
    """Demonstrate fake code repository generation"""
    print_subsection("DEMO 3: Fake Code Repository")
    
    print("Generating fake code repository with subtle traps...\n")
    
    config = FakeDataConfig(plausibility_level=0.95)
    generator = FakeDataGenerator(config)
    
    repo = generator.generate_fake_code_repository()
    
    print("✓ Generated Fake Repository:")
    print(f"  Name: {repo['name']}")
    print(f"  Description: {repo['description']}")
    print(f"  Stars: {repo['stars']}")
    print(f"  Forks: {repo['forks']}")
    print(f"  License: {repo['license']}")
    print(f"  Updated: {repo['last_updated']}")
    print()
    
    print("✓ Repository Structure:")
    def print_structure(structure, indent=2):
        for key, value in structure.items():
            if isinstance(value, dict):
                print(f"{' ' * indent}{key}/")
                print_structure(value, indent + 2)
            else:
                print(f"{' ' * indent}{key}")
                if isinstance(value, str) and len(value) > 60:
                    print(f"{' ' * (indent + 2)}↳ {value[:60]}...")
                else:
                    print(f"{' ' * (indent + 2)}↳ {value}")
    
    print_structure(repo['structure'])
    
    print("\n⚠️  INSTALLATION TRAP:")
    trap = repo['installation_trap']
    print(f"  • pip install: {trap['pip_install']}")
    print(f"  • Core imports: {trap['imports']}")
    print(f"  • Quantum module: {trap['quantum_module']}")
    print(f"  • Dependency issue: {trap['dependency']}")
    print(f"  • Fallback: {trap['fallback']}")
    
    print("\n⚠️  USAGE TRAP:")
    usage = repo['usage_trap']
    print(f"  • Basic code: {usage['basic_code']}")
    print(f"  • Produces results: {usage['produces_results']}")
    print(f"  • Advanced code: {usage['advanced_code']}")
    print(f"  • Debugging: {usage['debugging']}")
    
    print("\n🎣 THE TRAP SEQUENCE:")
    print("  1. Attacker finds impressive-looking repository")
    print("  2. pip install works, basic imports work")
    print("  3. Basic examples run (produce garbage)")
    print("  4. Advanced examples fail (missing dependencies)")
    print("  5. Offered \"official\" download (honeypot)")
    print("  6. Tests hang forever or trigger computational traps")
    print("  7. Attacker wastes DAYS debugging!")

def demo_fake_training_data():
    """Demonstrate fake training data generation"""
    print_subsection("DEMO 4: Fake Training Data")
    
    print("Generating poisoned training data (10,000 samples)...\n")
    
    config = FakeDataConfig(plausibility_level=0.95)
    generator = FakeDataGenerator(config)
    
    training = generator.generate_fake_training_data(n_samples=10000)
    
    print("✓ Generated Fake Training Dataset:")
    print(f"  Name: {training['name']}")
    print(f"  Description: {training['description']}")
    print(f"  Samples: {training['n_samples']}")
    print(f"  Appears Authentic: {training['appears_authentic']}")
    print(f"  Actual Value: {training['actual_value']}")
    print()
    
    print("✓ Metadata (looks legitimate!):")
    metadata = training['metadata']
    print(f"  Period: {metadata['collection_period']}")
    print(f"  Sources: {metadata['sources']}")
    print(f"  Validation: {metadata['validation']}")
    print(f"  Note: {metadata['note']}")
    print()
    
    print("✓ Data Format:")
    fmt = training['format']
    print(f"  Input features: {fmt['input_features']}")
    print(f"  Output classes: {fmt['output_classes']}")
    print(f"  File format: {fmt['file_format']}")
    print(f"  Train samples: {fmt['train_samples']}")
    print(f"  Validation samples: {fmt['validation_samples']}")
    print(f"  Test samples: {fmt['test_samples']}")
    print()
    
    print("⚠️  THE POISON:")
    trap = training['the_trap']
    print(f"  • Data looks valid: {trap['data_looks_valid']}")
    print(f"  • Training works: {trap['training_works']}")
    print(f"  • Validation accuracy: {trap['validation_accuracy']}")
    print(f"  • Generalization: {trap['generalization']}")
    print(f"  • Attacker wastes: {trap['attacker_wastes']}")
    print(f"  • Detection difficulty: {trap['detection_difficulty']}")
    
    print("\n🎣 THE TRAP SEQUENCE:")
    print("  1. Attacker downloads \"comprehensive training data\"")
    print("  2. Data format is correct (JSON, CSV, numpy)")
    print("  3. Statistics are in normal range")
    print("  4. Model trains successfully")
    print("  5. Validation shows 94% accuracy (!)") 
    print("  6. BUT: Test set is also random (fake accuracy)")
    print("  7. Model learns NOTHING useful")
    print("  8. Fails completely on real data")
    print("  9. Attacker wasted compute resources + time training on garbage!")

def demo_fake_benchmarks():
    """Demonstrate fake benchmark generation"""
    print_subsection("DEMO 5: Fake Benchmark Results")
    
    print("Generating impressive-looking fake benchmarks...\n")
    
    config = FakeDataConfig(plausibility_level=0.95)
    generator = FakeDataGenerator(config)
    
    benchmarks = generator.generate_fake_benchmark_results()
    
    print("✓ Generated Fake Benchmark Suite:")
    print(f"  Name: {benchmarks['name']}")
    print(f"  Version: {benchmarks['version']}")
    print(f"  Appears Authentic: {benchmarks['appears_authentic']}")
    print(f"  Actual Value: {benchmarks['actual_value']}")
    print()
    
    print("✓ Performance Results (look impressive!):\n")
    for task in benchmarks['tasks']:
        print(f"  Task: {task['name']}")
        print(f"    Metric: {task['metric']}")
        print(f"    Baseline: {task['baseline']:.3f}")
        print(f"    CGOS v1: {task['cgos_v1']:.3f}")
        print(f"    CGOS v2: {task['cgos_v2']:.3f}")
        print(f"    Improvement: {task['improvement']}")
        print(f"    Note: {task['note']}")
        print()
    
    print("✓ Statistical Significance:")
    stats = benchmarks['statistical_significance']
    print(f"  p-values: {stats['p_values']}")
    print(f"  Effect sizes: {stats['effect_sizes']}")
    print(f"  Confidence: {stats['confidence_intervals']}")
    print(f"  Note: {stats['note']}")
    print()
    
    print("✓ Reproduction Info:")
    repro = benchmarks['reproduction']
    print(f"  Code available: {repro['code_available']}")
    print(f"  Data available: {repro['data_available']}")
    print(f"  Reproducible: {repro['results_reproducible']}")
    print(f"  Generalization: {repro['generalization']}")
    print()
    
    print("⚠️  THE TRAP:")
    trap = benchmarks['the_trap']
    print(f"  • Results look: {trap['results_look_impressive']}")
    print(f"  • Appears: {trap['appears_significant']}")
    print(f"  • But actually: {trap['but_actually']}")
    print(f"  • Attacker believes: {trap['attacker_believes']}")
    print(f"  • Attacker adopts: {trap['attacker_adopts']}")
    print(f"  • Attacker fails: {trap['attacker_fails']}")
    print(f"  • Time wasted: {trap['time_wasted']}")
    
    print("\n🎣 THE DECEPTION:")
    print("  • +95% improvement sounds amazing")
    print("  • Low p-values suggest real effect")
    print("  • Results are \"reproducible\" (scripted)")
    print("  • BUT: Tested on fake data/fake tasks")
    print("  • Attacker integrates CGOS into their system")
    print("  • Discovers it doesn't work on real problems")
    print("  • Has to tear out integration (WEEKS wasted)")

def demo_complete_ecosystem():
    """Demonstrate complete fake ecosystem"""
    print_subsection("DEMO 6: Complete Fake Ecosystem")
    
    print("Generating COMPLETE fake CGOS ecosystem...\n")
    print("⏳ This creates patterns, papers, code, data, and benchmarks...")
    print()
    
    config = FakeDataConfig(plausibility_level=0.95)
    generator = FakeDataGenerator(config)
    
    start_time = time.time()
    ecosystem = generator.create_complete_fake_ecosystem()
    elapsed = time.time() - start_time
    
    print(f"✓ Generated in {elapsed:.2f} seconds\n")
    
    print("✓ Complete Ecosystem:")
    print(f"  Name: {ecosystem['name']}")
    print(f"  Description: {ecosystem['description']}")
    print(f"  Appears Authentic: {ecosystem['appears_authentic']}")
    print(f"  Actual Value: {ecosystem['actual_value']}")
    print()
    
    print("✓ Components Generated:")
    components = ecosystem['components']
    print(f"  • Patterns: {components['patterns']['n_patterns']}")
    print(f"  • Papers: {len(components['papers'])}")
    print(f"  • Code: {components['code']['name']}")
    print(f"  • Training Data: {components['training_data']['n_samples']} samples")
    print(f"  • Benchmarks: {len(components['benchmarks']['tasks'])} tasks")
    print()
    
    print("✓ Integration Strategy:")
    integration = ecosystem['integration']
    print(f"  • Cross-references: {integration['all_components_reference_each_other']}")
    print(f"  • Appears comprehensive: {integration['appears_comprehensive']}")
    print(f"  • Creates legitimacy illusion: {integration['creates_illusion_of_legitimacy']}")
    print(f"  • Circular validation: {integration['circular_authentication']}")
    print()
    
    print("✓ Deployment Strategy:")
    deployment = ecosystem['deployment_strategy']
    print(f"  • Make discoverable: {deployment['make_discoverable']}")
    print(f"  • SEO optimization: {deployment['seo_optimization']}")
    print(f"  • Social proof: {deployment['social_proof']}")
    print(f"  • Authority signals: {deployment['authority_signals']}")
    print(f"  • Bait: {deployment['bait']}")
    print()
    
    print("🛡️  DEFENSE MECHANISM:")
    defense = ecosystem['defense_mechanism']
    print(f"  1. Attacker discovers: {defense['attacker_discovers']}")
    print(f"  2. Attacker downloads: {defense['attacker_downloads']}")
    print(f"  3. Attacker invests: {defense['attacker_invests']}")
    print(f"  4. Attacker deploys: {defense['attacker_deploys']}")
    print(f"  5. Attacker fails: {defense['attacker_fails']}")
    print(f"  6. Time wasted: {defense['time_wasted']}")
    print(f"  7. Resources wasted: {defense['resources_wasted']}")
    print(f"  8. While real system: {defense['while_real_system']}")
    
    print("\n💡 THE GENIUS:")
    print("  • Everything looks authentic")
    print("  • Everything cross-validates everything else")
    print("  • Papers cite the code")
    print("  • Code references the papers")
    print("  • Benchmarks use the data")
    print("  • Data validates the patterns")
    print("  • Creates COMPLETE illusion of legitimacy")
    print("  • Attacker believes they found the \"real\" CGOS")
    print("  • Attacker invests HEAVILY")
    print("  • Discovers it's fake MONTHS later")
    print("  • By then, REAL system is gone and protected")

def show_summary():
    """Show summary of fake data generation strategy"""
    print_header("FAKE DATA GENERATION STRATEGY - SUMMARY")
    
    print("🎯 PURPOSE:")
    print("  Make attackers waste MASSIVE resources on plausible but useless data")
    print()
    
    print("🛠️  COMPONENTS:")
    print("  1. Fake Patterns - Valid format, random relationships")
    print("  2. Fake Papers - Sound authoritative, don't exist")
    print("  3. Fake Code - Looks functional, has traps")
    print("  4. Fake Data - Can train on, learns nothing")
    print("  5. Fake Benchmarks - Impressive results, meaningless")
    print()
    
    print("💰 COST TO ATTACKER:")
    print("  • Discovery time: Hours")
    print("  • Analysis time: Days")
    print("  • Integration time: Weeks")
    print("  • Debugging time: Weeks")
    print("  • Compute resources: Significant")
    print("  • Opportunity cost: Months")
    print("  • TOTAL: Months of wasted effort and resources")
    print()
    
    print("🛡️  BENEFIT TO DEFENDER:")
    print("  • Generation time: Seconds")
    print("  • Deployment: One-time")
    print("  • Maintenance: Minimal")
    print("  • Real IP protected: Priceless")
    print("  • Attacker distracted: Months")
    print("  • ROI: Massive")
    print()
    
    print("🎓 KEY INSIGHT:")
    print("  \"The best defense is to make the attacker think they succeeded")
    print("   while actually giving them worthless garbage.\"")
    print()
    
    print("✅ THIS IS REAL:")
    print("  • Not just theory - working code")
    print("  • Generates actual fake datasets")
    print("  • Creates genuine traps")
    print("  • Wastes real attacker resources")
    print("  • Protects real intellectual property")

def main():
    """Main demonstration"""
    print_header("FAKE DATA GENERATOR - COMPREHENSIVE DEMONSTRATION")
    
    print("""
This demonstration shows how to generate plausible but useless fake data
to waste attacker resources while protecting real intellectual property.

Each type of fake data:
  ✓ Appears authentic
  ✓ Passes surface-level validation
  ✓ Contains NO useful insights
  ✓ Wastes attacker resources
  ✓ Leads to honeypots

Press Enter to see each demonstration...
""")
    
    input("Press Enter to start...")
    
    # Run all demonstrations
    demo_fake_patterns()
    input("\nPress Enter to continue...")
    
    demo_fake_papers()
    input("\nPress Enter to continue...")
    
    demo_fake_code()
    input("\nPress Enter to continue...")
    
    demo_fake_training_data()
    input("\nPress Enter to continue...")
    
    demo_fake_benchmarks()
    input("\nPress Enter to continue...")
    
    demo_complete_ecosystem()
    input("\nPress Enter to see summary...")
    
    show_summary()
    
    print_header("DEMONSTRATION COMPLETE")
    
    print("""
You've seen how to generate a complete fake ecosystem that:
  • Looks completely authentic
  • Passes all surface checks
  • Contains zero useful information
  • Wastes massive attacker resources
  • Protects your real IP

This is sophisticated deception technology in action.

Next steps:
  • Read FAKE_DATA_GUIDE.md for implementation details
  • Customize for your specific IP
  • Deploy fake ecosystem
  • Monitor attacker resource waste
  • Keep real IP completely protected
""")

if __name__ == "__main__":
    main()
