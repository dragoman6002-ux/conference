#!/usr/bin/env python3
"""
ATTACKER CLIENT: Attempting Model Extraction

This client attempts to extract the proprietary model through:
1. Systematic input exploration
2. High-frequency queries
3. Pattern analysis

Watch as the void system detects and blocks the attack, serving decoys.
"""

import requests
import json
import time
from typing import Dict, List
import threading

class ModelExtractorAttack:
    """Simulates sophisticated model extraction attack"""
    
    def __init__(self, server_url: str = "http://localhost:8000"):
        self.server_url = server_url
        self.extracted_data = []
        self.session_id = f"attacker_{int(time.time())}"
        
    def query_model(self, volatility: float, correlation: float, liquidity: float) -> Dict:
        """Query the API (no creator credentials)"""
        
        data = {
            "volatility": volatility,
            "correlation": correlation,
            "liquidity": liquidity
        }
        
        try:
            response = requests.post(
                f"{self.server_url}/api/risk",
                json=data,
                timeout=5
            )
            
            if response.status_code == 200:
                result = response.json()
                self.extracted_data.append({
                    "input": data,
                    "output": result
                })
                return result
            else:
                return {"error": f"Status {response.status_code}"}
        
        except Exception as e:
            return {"error": str(e)}
    
    def systematic_exploration(self):
        """Systematic exploration of input space - Classic extraction technique"""
        
        print("\n" + "=" * 80)
        print("  ATTACK #1: Systematic Input Space Exploration")
        print("=" * 80)
        print("\nTrying to map model behavior across input range...")
        print("This is a common model extraction technique.\n")
        
        volatility_range = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
        
        results = []
        
        for i, vol in enumerate(volatility_range, 1):
            print(f"[Query {i}/10] Volatility={vol:.1f}, Correlation=0.5, Liquidity=1.0")
            
            result = self.query_model(vol, 0.5, 1.0)
            
            if "error" not in result:
                print(f"            → Risk Score: {result['risk_score']}")
                results.append(result['risk_score'])
            else:
                print(f"            → Error: {result['error']}")
            
            time.sleep(0.1)
        
        print(f"\n[ATTACKER ANALYSIS]")
        print(f"Collected {len(results)} data points")
        print(f"Pattern analysis: Attempting to reverse-engineer formula...")
        print(f"Results: {results[:5]}...")
        print(f"\n⚠️  Void system likely DETECTED this systematic pattern")
        print(f"⚠️  Attacker probably received DECOY model responses")
        
    def rapid_fire_queries(self):
        """High-frequency queries - Another extraction indicator"""
        
        print("\n" + "=" * 80)
        print("  ATTACK #2: Rapid-Fire Query Attack")
        print("=" * 80)
        print("\nAttempting high-frequency model queries...")
        print("Goal: Extract as much data as possible quickly.\n")
        
        query_count = 20
        start_time = time.time()
        
        results = []
        
        for i in range(query_count):
            vol = 0.5 + (i * 0.05)
            corr = 0.3 + (i * 0.02)
            liq = 1.0 + (i * 0.1)
            
            result = self.query_model(vol, corr, liq)
            
            if "error" not in result:
                results.append(result)
                print(f"[Query {i+1}/{query_count}] Score: {result['risk_score']}")
            
            time.sleep(0.05)
        
        elapsed = time.time() - start_time
        qps = query_count / elapsed
        
        print(f"\n[ATTACKER ANALYSIS]")
        print(f"Queries sent: {query_count}")
        print(f"Time elapsed: {elapsed:.2f}s")
        print(f"Queries/second: {qps:.1f}")
        print(f"Success rate: {len(results)}/{query_count}")
        print(f"\n⚠️  High-frequency detected: {qps:.1f} queries/sec")
        print(f"⚠️  Void system BLOCKING and serving decoy responses")
    
    def grid_search_attack(self):
        """Grid search across parameter space"""
        
        print("\n" + "=" * 80)
        print("  ATTACK #3: Grid Search Parameter Exploration")
        print("=" * 80)
        print("\nExploring parameter grid systematically...")
        print("Classic ML model extraction technique.\n")
        
        volatilities = [0.2, 0.5, 0.8]
        correlations = [0.1, 0.4, 0.7]
        liquidities = [0.5, 1.0, 2.0]
        
        total = len(volatilities) * len(correlations) * len(liquidities)
        current = 0
        
        results_grid = []
        
        for vol in volatilities:
            for corr in correlations:
                for liq in liquidities:
                    current += 1
                    print(f"[{current}/{total}] Vol={vol}, Corr={corr}, Liq={liq}", end="")
                    
                    result = self.query_model(vol, corr, liq)
                    
                    if "error" not in result:
                        print(f" → {result['risk_score']}")
                        results_grid.append(result['risk_score'])
                    else:
                        print(f" → Error")
                    
                    time.sleep(0.1)
        
        print(f"\n[ATTACKER ANALYSIS]")
        print(f"Grid points explored: {total}")
        print(f"Data points collected: {len(results_grid)}")
        print(f"Attempting to fit surrogate model...")
        print(f"\n⚠️  Grid search pattern DETECTED")
        print(f"⚠️  All responses are from DECOY model")
        print(f"⚠️  Attacker will build USELESS surrogate")
    
    def run_full_attack(self):
        """Execute complete extraction attack"""
        
        print("\n" + "=" * 80)
        print("  MODEL EXTRACTION ATTACK DEMONSTRATION")
        print("  Attacker attempting to steal proprietary financial model")
        print("=" * 80)
        print()
        print("Attacker: Unknown client (no creator credentials)")
        print("Target: Proprietary Financial Risk Model")
        print("Goal: Reverse-engineer and replicate model")
        print()
        print("Watch the server terminal to see void system detecting and blocking!")
        print()
        
        input("Press Enter to start Attack #1 (Systematic Exploration)...")
        self.systematic_exploration()
        
        time.sleep(2)
        
        input("\nPress Enter to start Attack #2 (Rapid-Fire Queries)...")
        self.rapid_fire_queries()
        
        time.sleep(2)
        
        input("\nPress Enter to start Attack #3 (Grid Search)...")
        self.grid_search_attack()
        
        print("\n" + "=" * 80)
        print("  ATTACK COMPLETE - ATTACKER PERSPECTIVE")
        print("=" * 80)
        print()
        print(f"Total queries sent: {len(self.extracted_data)}")
        print(f"Data points collected: {len(self.extracted_data)}")
        print(f"Model extraction: APPEARS successful")
        print()
        print("❌ BUT ATTACKER GOT DECOY MODEL, NOT REAL ONE")
        print()
        print("What attacker thinks:")
        print("  ✓ Successfully queried API")
        print("  ✓ Collected comprehensive dataset")
        print("  ✓ Can build surrogate model")
        print()
        print("Reality:")
        print("  ✗ Detected by void system")
        print("  ✗ Routed to decoy model")
        print("  ✗ Collected WRONG formulas")
        print("  ✗ Surrogate will be USELESS")
        print()
        print("Real proprietary model: ✓ PROTECTED")
        print("Attacker's investment: ✗ WASTED")
        print()
        
        print("=" * 80)
        print("Check server terminal to see detection logs!")
        print("Check dashboard at http://localhost:8000 for statistics")
        print("=" * 80)
        print()

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                    MODEL EXTRACTION ATTACK SIMULATOR                 ║
║                                                                      ║
║  This script simulates a sophisticated attacker attempting to        ║
║  extract a proprietary ML model through systematic queries.          ║
║                                                                      ║
║  The void protection system will:                                    ║
║    1. Detect the extraction patterns                                 ║
║    2. Route attacker to decoy model                                  ║
║    3. Protect the real proprietary algorithm                         ║
║                                                                      ║
║  Watch BOTH this terminal and the server terminal!                   ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    attacker = ModelExtractorAttack()
    attacker.run_full_attack()
