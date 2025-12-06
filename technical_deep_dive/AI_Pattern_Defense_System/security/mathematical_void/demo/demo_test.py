#!/usr/bin/env python3
"""
AUTOMATED TEST SUITE: Void Protection System

Validates all functionality:
1. Server responds correctly
2. Creator authentication works
3. Attacker detection works
4. Routing works correctly
5. Dashboard accessible
6. Statistics accurate
"""

import requests
import time
import subprocess
import sys
import os
from typing import Dict, Tuple

class VoidSystemTester:
    """Automated testing of void protection system"""
    
    def __init__(self, server_url: str = "http://localhost:8000"):
        self.server_url = server_url
        self.token = None
        self.tests_passed = 0
        self.tests_failed = 0
    
    def print_test(self, name: str):
        """Print test name"""
        print(f"\n{'─' * 80}")
        print(f"TEST: {name}")
        print(f"{'─' * 80}")
    
    def print_result(self, passed: bool, message: str):
        """Print test result"""
        if passed:
            print(f"✓ PASS: {message}")
            self.tests_passed += 1
        else:
            print(f"✗ FAIL: {message}")
            self.tests_failed += 1
    
    def load_token(self) -> bool:
        """Load creator token"""
        try:
            with open("creator_token.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if len(line.strip()) == 64:
                        self.token = line.strip()
                        return True
        except FileNotFoundError:
            pass
        return False
    
    def test_server_running(self) -> bool:
        """Test 1: Server is running and responding"""
        self.print_test("Server Running")
        
        try:
            response = requests.get(self.server_url, timeout=5)
            if response.status_code == 200:
                self.print_result(True, "Server responding on port 8000")
                return True
            else:
                self.print_result(False, f"Server returned status {response.status_code}")
                return False
        except Exception as e:
            self.print_result(False, f"Cannot connect to server: {e}")
            return False
    
    def test_token_created(self) -> bool:
        """Test 2: Creator token was created"""
        self.print_test("Creator Token Created")
        
        if self.load_token():
            self.print_result(True, f"Token found: {self.token[:16]}...")
            return True
        else:
            self.print_result(False, "No creator token found")
            return False
    
    def test_api_endpoint(self) -> bool:
        """Test 3: API endpoint responds"""
        self.print_test("API Endpoint")
        
        try:
            response = requests.get(
                f"{self.server_url}/api/risk?volatility=0.5&correlation=0.3&liquidity=1.0",
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                if "risk_score" in data:
                    self.print_result(True, f"API responding, risk_score={data['risk_score']}")
                    return True
                else:
                    self.print_result(False, "API response missing risk_score")
                    return False
            else:
                self.print_result(False, f"API returned status {response.status_code}")
                return False
        
        except Exception as e:
            self.print_result(False, f"API error: {e}")
            return False
    
    def test_creator_authentication(self) -> bool:
        """Test 4: Creator authentication works"""
        self.print_test("Creator Authentication")
        
        if not self.token:
            self.print_result(False, "No token available")
            return False
        
        try:
            headers = {"Authorization": f"Bearer {self.token}"}
            
            response = requests.post(
                f"{self.server_url}/api/risk",
                json={"volatility": 0.5, "correlation": 0.3, "liquidity": 1.0},
                headers=headers,
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                self.print_result(True, f"Creator authenticated, risk_score={data['risk_score']}")
                return True
            else:
                self.print_result(False, f"Authentication failed with status {response.status_code}")
                return False
        
        except Exception as e:
            self.print_result(False, f"Authentication error: {e}")
            return False
    
    def test_different_models(self) -> Tuple[bool, float, float]:
        """Test 5: Creator and attacker get different models"""
        self.print_test("Model Routing (Creator vs Attacker)")
        
        if not self.token:
            self.print_result(False, "No token available")
            return False, 0, 0
        
        try:
            test_data = {"volatility": 0.5, "correlation": 0.3, "liquidity": 1.0}
            
            headers_creator = {"Authorization": f"Bearer {self.token}"}
            response_creator = requests.post(
                f"{self.server_url}/api/risk",
                json=test_data,
                headers=headers_creator,
                timeout=5
            )
            
            creator_score = response_creator.json()["risk_score"]
            
            time.sleep(0.2)
            
            for _ in range(15):
                requests.post(
                    f"{self.server_url}/api/risk",
                    json={"volatility": 0.5 + _ * 0.01, "correlation": 0.3, "liquidity": 1.0},
                    timeout=5
                )
                time.sleep(0.05)
            
            response_attacker = requests.post(
                f"{self.server_url}/api/risk",
                json=test_data,
                timeout=5
            )
            
            attacker_score = response_attacker.json()["risk_score"]
            
            diff = abs(creator_score - attacker_score)
            
            if diff > 0.01:
                self.print_result(True, f"Different models confirmed")
                print(f"   Creator score: {creator_score}")
                print(f"   Attacker score: {attacker_score}")
                print(f"   Difference: {diff:.4f}")
                return True, creator_score, attacker_score
            else:
                self.print_result(False, f"Same model (difference: {diff:.4f})")
                return False, creator_score, attacker_score
        
        except Exception as e:
            self.print_result(False, f"Routing test error: {e}")
            return False, 0, 0
    
    def test_extraction_detection(self) -> bool:
        """Test 6: Extraction attempts are detected"""
        self.print_test("Extraction Detection")
        
        try:
            initial_stats = requests.get(f"{self.server_url}/stats", timeout=5).json()
            initial_detections = initial_stats.get("extraction_attempts_detected", 0)
            
            for i in range(20):
                requests.post(
                    f"{self.server_url}/api/risk",
                    json={"volatility": 0.1 + i * 0.05, "correlation": 0.3, "liquidity": 1.0},
                    timeout=5
                )
                time.sleep(0.05)
            
            time.sleep(0.5)
            
            final_stats = requests.get(f"{self.server_url}/stats", timeout=5).json()
            final_detections = final_stats.get("extraction_attempts_detected", 0)
            
            new_detections = final_detections - initial_detections
            
            if new_detections > 0:
                self.print_result(True, f"Detected {new_detections} extraction attempt(s)")
                return True
            else:
                self.print_result(False, "No extraction attempts detected")
                return False
        
        except Exception as e:
            self.print_result(False, f"Detection test error: {e}")
            return False
    
    def test_dashboard(self) -> bool:
        """Test 7: Dashboard is accessible"""
        self.print_test("Dashboard Accessibility")
        
        try:
            response = requests.get(self.server_url, timeout=5)
            
            if response.status_code == 200 and "Void-Protected API Server" in response.text:
                self.print_result(True, "Dashboard accessible at http://localhost:8000")
                return True
            else:
                self.print_result(False, "Dashboard not accessible")
                return False
        
        except Exception as e:
            self.print_result(False, f"Dashboard error: {e}")
            return False
    
    def test_statistics(self) -> bool:
        """Test 8: Statistics endpoint works"""
        self.print_test("Statistics Endpoint")
        
        try:
            response = requests.get(f"{self.server_url}/stats", timeout=5)
            
            if response.status_code == 200:
                stats = response.json()
                required_fields = [
                    "total_requests",
                    "creator_requests",
                    "extraction_attempts_detected",
                    "decoys_served"
                ]
                
                if all(field in stats for field in required_fields):
                    self.print_result(True, "Statistics endpoint working")
                    print(f"   Total requests: {stats['total_requests']}")
                    print(f"   Creator requests: {stats['creator_requests']}")
                    print(f"   Extraction attempts: {stats['extraction_attempts_detected']}")
                    print(f"   Decoys served: {stats['decoys_served']}")
                    return True
                else:
                    self.print_result(False, "Statistics missing required fields")
                    return False
            else:
                self.print_result(False, f"Stats returned status {response.status_code}")
                return False
        
        except Exception as e:
            self.print_result(False, f"Statistics error: {e}")
            return False
    
    def run_all_tests(self):
        """Run complete test suite"""
        print("=" * 80)
        print("  VOID PROTECTION SYSTEM - AUTOMATED TEST SUITE")
        print("=" * 80)
        print()
        print("Testing real network communication and void protection...")
        print()
        
        if not self.test_server_running():
            print("\n[ERROR] Server not running. Start server first:")
            print("  python demo_server.py")
            return
        
        self.test_token_created()
        self.test_api_endpoint()
        self.test_creator_authentication()
        self.test_different_models()
        self.test_extraction_detection()
        self.test_dashboard()
        self.test_statistics()
        
        print("\n" + "=" * 80)
        print("  TEST RESULTS")
        print("=" * 80)
        print()
        print(f"Tests passed: {self.tests_passed}")
        print(f"Tests failed: {self.tests_failed}")
        print(f"Success rate: {self.tests_passed / (self.tests_passed + self.tests_failed) * 100:.1f}%")
        print()
        
        if self.tests_failed == 0:
            print("✓ ALL TESTS PASSED")
            print()
            print("Void protection system is working correctly:")
            print("  ✓ Server operational")
            print("  ✓ Authentication working")
            print("  ✓ Model routing functional")
            print("  ✓ Extraction detection active")
            print("  ✓ Dashboard accessible")
            print("  ✓ Statistics tracking")
            print()
            print("System is READY for demonstration.")
        else:
            print(f"✗ {self.tests_failed} TEST(S) FAILED")
            print()
            print("Check server logs and ensure:")
            print("  - Server is running on port 8000")
            print("  - No firewall blocking connections")
            print("  - Creator token file exists")
        
        print()
        print("=" * 80)

if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║                 VOID PROTECTION SYSTEM - TEST SUITE                  ║
║                                                                      ║
║  This script validates all components of the void protection        ║
║  demonstration system.                                               ║
║                                                                      ║
║  Prerequisites:                                                      ║
║    • Server running (python demo_server.py)                          ║
║    • Port 8000 accessible                                            ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
    """)
    
    input("Press Enter to start tests (make sure server is running)...")
    
    tester = VoidSystemTester()
    tester.run_all_tests()
