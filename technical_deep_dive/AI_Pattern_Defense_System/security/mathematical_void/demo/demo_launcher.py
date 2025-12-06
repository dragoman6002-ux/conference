#!/usr/bin/env python3
"""
QUICK START LAUNCHER: Void Protection Demo

Easy menu-driven interface to run all demos
"""

import subprocess
import sys
import os
import time

def print_header():
    """Print demo header"""
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║              VOID PROTECTION SYSTEM - NETWORK DEMONSTRATION                ║
║                                                                            ║
║  Real server • Real network • Real protection • Real extraction attempts   ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)

def print_menu():
    """Print main menu"""
    print("\n" + "=" * 80)
    print("  MAIN MENU")
    print("=" * 80)
    print()
    print("  [1] Start Server (do this first!)")
    print("  [2] Run Legitimate Client (Creator)")
    print("  [3] Run Attacker (Model Extraction)")
    print("  [4] Run Side-by-Side Comparison")
    print("  [5] Run Automated Tests")
    print("  [6] Open Dashboard (browser)")
    print("  [7] Show Quick Start Guide")
    print("  [8] Exit")
    print()

def start_server():
    """Start the void-protected server"""
    print("\n" + "=" * 80)
    print("  Starting Void-Protected Server...")
    print("=" * 80)
    print()
    print("The server will start on http://localhost:8000")
    print()
    print("IMPORTANT:")
    print("  • Server runs in THIS terminal")
    print("  • Open NEW terminals for clients")
    print("  • Watch this terminal for request logs")
    print("  • Press Ctrl+C to stop server")
    print()
    input("Press Enter to start server...")
    
    subprocess.run([sys.executable, "demo_server.py"])

def run_creator():
    """Run legitimate client"""
    print("\n" + "=" * 80)
    print("  Running Legitimate Client (Creator)...")
    print("=" * 80)
    print()
    print("This client has creator credentials and will access the REAL model.")
    print()
    
    if not os.path.exists("creator_token.txt"):
        print("[ERROR] creator_token.txt not found!")
        print("Make sure the server is running first (option 1).")
        input("\nPress Enter to continue...")
        return
    
    input("Press Enter to run...")
    subprocess.run([sys.executable, "demo_creator.py"])
    input("\nPress Enter to continue...")

def run_attacker():
    """Run attacker simulation"""
    print("\n" + "=" * 80)
    print("  Running Attacker (Model Extraction)...")
    print("=" * 80)
    print()
    print("This simulates a sophisticated model extraction attack.")
    print()
    print("WATCH THE SERVER TERMINAL to see:")
    print("  • Detection of systematic patterns")
    print("  • Threat scoring in action")
    print("  • Requests routed to decoy")
    print()
    input("Press Enter to run...")
    subprocess.run([sys.executable, "demo_attacker.py"])
    input("\nPress Enter to continue...")

def run_comparison():
    """Run side-by-side comparison"""
    print("\n" + "=" * 80)
    print("  Running Side-by-Side Comparison...")
    print("=" * 80)
    print()
    print("This sends IDENTICAL queries as creator and attacker.")
    print("You'll see they get DIFFERENT results from the SAME endpoint.")
    print()
    
    if not os.path.exists("creator_token.txt"):
        print("[ERROR] creator_token.txt not found!")
        print("Make sure the server is running first (option 1).")
        input("\nPress Enter to continue...")
        return
    
    input("Press Enter to run...")
    subprocess.run([sys.executable, "demo_comparison.py"])
    input("\nPress Enter to continue...")

def run_tests():
    """Run automated tests"""
    print("\n" + "=" * 80)
    print("  Running Automated Tests...")
    print("=" * 80)
    print()
    print("This validates all functionality automatically.")
    print()
    print("Make sure the server is running first!")
    print()
    input("Press Enter to run...")
    subprocess.run([sys.executable, "demo_test.py"])
    input("\nPress Enter to continue...")

def open_dashboard():
    """Open dashboard in browser"""
    print("\n" + "=" * 80)
    print("  Opening Dashboard...")
    print("=" * 80)
    print()
    print("Dashboard URL: http://localhost:8000")
    print()
    print("If server is running, your browser should open automatically.")
    print("If not, manually open: http://localhost:8000")
    print()
    
    import webbrowser
    webbrowser.open("http://localhost:8000")
    
    input("\nPress Enter to continue...")

def show_guide():
    """Show quick start guide"""
    print("\n" + "=" * 80)
    print("  QUICK START GUIDE")
    print("=" * 80)
    print()
    print("Step 1: Start Server")
    print("  • Choose option [1]")
    print("  • Server starts on http://localhost:8000")
    print("  • Creates creator_token.txt")
    print("  • Logs all requests to console")
    print()
    print("Step 2: Open Dashboard")
    print("  • Choose option [6] or open http://localhost:8000")
    print("  • See live statistics")
    print("  • Auto-refreshes every 2 seconds")
    print()
    print("Step 3: Run Demos")
    print("  • Open NEW terminal windows")
    print("  • Run this script again in each terminal")
    print("  • Choose options [2], [3], or [4]")
    print()
    print("Step 4: Watch Both Terminals")
    print("  • Server terminal: See detection logs")
    print("  • Client terminal: See query results")
    print("  • Dashboard: See statistics update")
    print()
    print("What to Run:")
    print()
    print("  Option [2] - Legitimate Client")
    print("    Shows normal usage with creator credentials")
    print("    All requests routed to REAL model")
    print()
    print("  Option [3] - Attacker")
    print("    Simulates model extraction attack")
    print("    Shows detection and blocking in action")
    print("    Attacker gets DECOY model")
    print()
    print("  Option [4] - Comparison")
    print("    Sends same query as creator and attacker")
    print("    Proves they get different models")
    print("    Most powerful demonstration")
    print()
    print("  Option [5] - Tests")
    print("    Automated validation of all functionality")
    print("    Confirms system working correctly")
    print()
    print("Best Demo Sequence:")
    print()
    print("  Terminal 1: Option [1] - Start server")
    print("  Browser:    Option [6] - Open dashboard")
    print("  Terminal 2: Option [4] - Run comparison (proves routing)")
    print("  Terminal 3: Option [3] - Run attacker (shows detection)")
    print("  Terminal 4: Option [2] - Run creator (shows normal use)")
    print("  Terminal 5: Option [5] - Run tests (validates all)")
    print()
    print("=" * 80)
    input("\nPress Enter to continue...")

def main():
    """Main menu loop"""
    while True:
        print_header()
        print_menu()
        
        try:
            choice = input("Choose option [1-8]: ").strip()
            
            if choice == "1":
                start_server()
            elif choice == "2":
                run_creator()
            elif choice == "3":
                run_attacker()
            elif choice == "4":
                run_comparison()
            elif choice == "5":
                run_tests()
            elif choice == "6":
                open_dashboard()
            elif choice == "7":
                show_guide()
            elif choice == "8":
                print("\nExiting. Thank you!")
                break
            else:
                print("\n[ERROR] Invalid choice. Please choose 1-8.")
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("\n\nInterrupted. Exiting.")
            break
        except Exception as e:
            print(f"\n[ERROR] {e}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting.")
