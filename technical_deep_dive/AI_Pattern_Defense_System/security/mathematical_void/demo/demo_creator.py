#!/usr/bin/env python3
"""
LEGITIMATE CLIENT: Creator with proper credentials

This client has the creator token and accesses the REAL model.
Demonstrates proper navigation through void system.
"""

import requests
import json
import time
from typing import Dict

class LegitimateClient:
    """Authorized client with creator credentials"""
    
    def __init__(self, server_url: str = "http://localhost:8000"):
        self.server_url = server_url
        self.creator_token = self._load_creator_token()
        
        if not self.creator_token:
            print("[ERROR] No creator token found!")
            print("Make sure the server is running and created creator_token.txt")
            return
        
        print(f"[✓] Loaded creator token: {self.creator_token[:16]}...")
    
    def _load_creator_token(self) -> str:
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
    
    def calculate_risk(self, volatility: float, correlation: float, liquidity: float) -> Dict:
        """Query the risk model as authorized creator"""
        
        headers = {
            "Authorization": f"Bearer {self.creator_token}",
            "Content-Type": "application/json"
        }
        
        data = {
            "volatility": volatility,
            "correlation": correlation,
            "liquidity": liquidity
        }
        
        try:
            response = requests.post(
                f"{self.server_url}/api/risk",
                json=data,
                headers=headers,
                timeout=5
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Status {response.status_code}"}
        
        except Exception as e:
            return {"error": str(e)}
    
    def run_demo(self):
        """Run legitimate usage demonstration"""
        
        print("\n" + "=" * 80)
        print("  LEGITIMATE CLIENT (CREATOR) - Accessing Real Model")
        print("=" * 80)
        print()
        
        if not self.creator_token:
            print("[ERROR] Cannot proceed without creator token")
            return
        
        test_cases = [
            {"name": "Low Risk Portfolio", "volatility": 0.2, "correlation": 0.1, "liquidity": 10.0},
            {"name": "Medium Risk Portfolio", "volatility": 0.5, "correlation": 0.3, "liquidity": 5.0},
            {"name": "High Risk Portfolio", "volatility": 0.9, "correlation": 0.7, "liquidity": 1.0},
            {"name": "Volatile Market", "volatility": 1.2, "correlation": 0.5, "liquidity": 3.0},
        ]
        
        print("Running legitimate risk calculations...\n")
        
        results = []
        
        for i, test in enumerate(test_cases, 1):
            print(f"[{i}/4] {test['name']}")
            print(f"      Input: Vol={test['volatility']}, Corr={test['correlation']}, Liq={test['liquidity']}")
            
            result = self.calculate_risk(
                test['volatility'],
                test['correlation'],
                test['liquidity']
            )
            
            if "error" not in result:
                print(f"      ✓ Risk Score: {result['risk_score']}")
                print(f"      Timestamp: {result['timestamp']}")
                results.append(result)
            else:
                print(f"      ✗ Error: {result['error']}")
            
            print()
            time.sleep(0.5)
        
        print("=" * 80)
        print("SUMMARY")
        print("=" * 80)
        print(f"Total queries: {len(test_cases)}")
        print(f"Successful: {len(results)}")
        print(f"As creator: ALL requests routed to REAL model")
        print(f"Model access: PROPRIETARY ALGORITHM")
        print()
        print("✓ Creator authentication successful")
        print("✓ Accessing real proprietary model")
        print("✓ Getting accurate risk calculations")
        print()

if __name__ == "__main__":
    client = LegitimateClient()
    client.run_demo()
