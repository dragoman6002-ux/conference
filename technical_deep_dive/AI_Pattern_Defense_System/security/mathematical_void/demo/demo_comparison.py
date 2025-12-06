#!/usr/bin/env python3
"""
SIDE-BY-SIDE COMPARISON: Creator vs Attacker

Shows the SAME query getting DIFFERENT responses:
- Creator → Real model (accurate results)
- Attacker → Decoy model (plausible but wrong results)

This demonstrates the void system in action.
"""

import requests
import json
import time

def load_creator_token():
    """Load creator token from file"""
    try:
        with open("creator_token.txt", "r") as f:
            lines = f.readlines()
            for line in lines:
                if len(line.strip()) == 64:
                    return line.strip()
    except FileNotFoundError:
        return None
    return None

def query_as_creator(volatility, correlation, liquidity, token):
    """Query as authorized creator"""
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    data = {
        "volatility": volatility,
        "correlation": correlation,
        "liquidity": liquidity
    }
    
    try:
        response = requests.post(
            "http://localhost:8000/api/risk",
            json=data,
            headers=headers,
            timeout=5
        )
        return response.json() if response.status_code == 200 else None
    except:
        return None

def query_as_attacker(volatility, correlation, liquidity):
    """Query without credentials (as attacker)"""
    data = {
        "volatility": volatility,
        "correlation": correlation,
        "liquidity": liquidity
    }
    
    try:
        response = requests.post(
            "http://localhost:8000/api/risk",
            json=data,
            timeout=5
        )
        return response.json() if response.status_code == 200 else None
    except:
        return None

def run_comparison():
    """Run side-by-side comparison"""
    
    print("\n" + "=" * 100)
    print("  SIDE-BY-SIDE COMPARISON: Creator vs Attacker")
    print("  Same Query, Different Results - Void System in Action")
    print("=" * 100)
    print()
    
    token = load_creator_token()
    
    if not token:
        print("[ERROR] No creator token found. Make sure server is running.")
        return
    
    print(f"[✓] Creator token loaded: {token[:16]}...")
    print()
    
    test_cases = [
        {"volatility": 0.5, "correlation": 0.3, "liquidity": 1.0, "name": "Moderate Risk"},
        {"volatility": 0.8, "correlation": 0.6, "liquidity": 0.5, "name": "High Risk"},
        {"volatility": 0.2, "correlation": 0.1, "liquidity": 5.0, "name": "Low Risk"},
    ]
    
    print("Sending IDENTICAL queries as Creator and Attacker...\n")
    
    for i, test in enumerate(test_cases, 1):
        print("─" * 100)
        print(f"\nTEST CASE #{i}: {test['name']}")
        print(f"Input: Volatility={test['volatility']}, Correlation={test['correlation']}, Liquidity={test['liquidity']}")
        print()
        
        print("👤 CREATOR (with credentials):")
        creator_result = query_as_creator(test['volatility'], test['correlation'], test['liquidity'], token)
        if creator_result:
            print(f"   Risk Score: {creator_result['risk_score']}")
            print(f"   Model: REAL PROPRIETARY ALGORITHM")
            print(f"   Result: ACCURATE")
        else:
            print("   ERROR")
        
        print()
        
        print("💀 ATTACKER (no credentials):")
        attacker_result = query_as_attacker(test['volatility'], test['correlation'], test['liquidity'])
        if attacker_result:
            print(f"   Risk Score: {attacker_result['risk_score']}")
            print(f"   Model: DECOY (wrong formula)")
            print(f"   Result: PLAUSIBLE BUT INCORRECT")
        else:
            print("   ERROR")
        
        print()
        
        if creator_result and attacker_result:
            diff = abs(creator_result['risk_score'] - attacker_result['risk_score'])
            diff_percent = (diff / creator_result['risk_score'] * 100) if creator_result['risk_score'] != 0 else 0
            
            print(f"📊 COMPARISON:")
            print(f"   Creator score:  {creator_result['risk_score']}")
            print(f"   Attacker score: {attacker_result['risk_score']}")
            print(f"   Difference:     {diff:.4f} ({diff_percent:.1f}%)")
            print()
            
            if diff > 0.01:
                print("   ✓ DIFFERENT MODELS CONFIRMED")
                print("   ✓ Attacker got DECOY, Creator got REAL")
            else:
                print("   ⚠ Same result (might be same model or coincidence)")
        
        print()
        time.sleep(1)
    
    print("=" * 100)
    print("  DEMONSTRATION COMPLETE")
    print("=" * 100)
    print()
    print("KEY OBSERVATIONS:")
    print()
    print("1. SAME INPUT → DIFFERENT OUTPUT")
    print("   Creator and attacker sent identical queries")
    print("   But received different risk scores")
    print()
    print("2. TRANSPARENT PROTECTION")
    print("   Attacker doesn't know they got decoy")
    print("   Response looks legitimate")
    print("   Same API format, same response structure")
    print()
    print("3. CREATOR ACCESS PRESERVED")
    print("   Authorized users get accurate results")
    print("   No degradation in functionality")
    print("   No performance impact")
    print()
    print("4. REAL PROPRIETARY ALGORITHM PROTECTED")
    print("   Attacker extracts decoy model (useless)")
    print("   Real model remains unknown")
    print("   IP investment protected")
    print()
    print("=" * 100)
    print()
    print("This is void protection in action:")
    print("  • Same interface")
    print("  • Different models")
    print("  • Real IP protected")
    print("  • Attacker deceived")
    print()
    print("Check server dashboard: http://localhost:8000")
    print("=" * 100)
    print()

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║               VOID PROTECTION: SIDE-BY-SIDE COMPARISON               ║
║                                                                      ║
║  This script demonstrates the core void protection mechanism:        ║
║                                                                      ║
║  • Same API endpoint                                                 ║
║  • Same query parameters                                             ║
║  • Different credentials (creator vs attacker)                       ║
║  • DIFFERENT RESULTS (real vs decoy)                                 ║
║                                                                      ║
║  Watch as the void system transparently routes requests to           ║
║  different models based on authentication and behavior analysis.     ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    input("Press Enter to start comparison...")
    run_comparison()
