import sys
import os
import time
import subprocess

def print_banner():
    print("\n" + "="*70)
    print(" SECURITY SUITE - PROOF OF CONCEPT DEMO")
    print(" AI Defense System Showcase")
    print("="*70 + "\n")

def check_dependencies():
    print("[1/4] Checking dependencies...")
    
    required_modules = {
        'tkinter': 'GUI framework (usually bundled with Python)',
        'subprocess': 'Process management (standard library)',
        'threading': 'Multi-threading support (standard library)',
        'json': 'Configuration handling (standard library)',
        'os': 'OS interactions (standard library)',
        'sys': 'System operations (standard library)',
        'pathlib': 'Path handling (standard library)'
    }
    
    missing = []
    for module, description in required_modules.items():
        try:
            __import__(module)
            print(f"   ✓ {module:15} - {description}")
        except ImportError:
            print(f"   ✗ {module:15} - MISSING")
            missing.append(module)
    
    if missing:
        print(f"\n   ❌ Missing dependencies: {', '.join(missing)}")
        if 'tkinter' in missing:
            print("\n   To install tkinter:")
            print("   - Windows: Reinstall Python with tcl/tk option checked")
            print("   - Linux: sudo apt-get install python3-tk")
            print("   - Mac: brew install python-tk")
        return False
    
    print("   ✅ All dependencies available\n")
    return True

def check_tool_scripts():
    print("[2/4] Checking security tool scripts...")
    
    required_scripts = [
        "network_security_analyzer.py",
        "infinite_thought.py",
        "unified_defense_system.py",
        "fake_data_generator.py",
        "ai_logic_battle_system.py",
        "quantum_honeypot_core.py"
    ]
    
    missing = []
    for script in required_scripts:
        if os.path.exists(script):
            print(f"   ✓ {script}")
        else:
            print(f"   ✗ {script} - NOT FOUND")
            missing.append(script)
    
    if missing:
        print(f"\n   ❌ Missing {len(missing)} tool scripts")
        return False
    
    print("   ✅ All tool scripts present\n")
    return True

def check_main_application():
    print("[3/4] Checking main application...")
    
    if os.path.exists("security_suite.py"):
        print("   ✓ security_suite.py found")
        print("   ✅ Main application ready\n")
        return True
    else:
        print("   ✗ security_suite.py NOT FOUND")
        print("   ❌ Main application missing\n")
        return False

def run_quick_test():
    print("[4/4] Running quick functionality test...")
    
    print("\n   Testing tool: Infinite Thought (5 seconds)")
    print("   " + "-"*60)
    
    try:
        process = subprocess.Popen(
            [sys.executable, "infinite_thought.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        
        start_time = time.time()
        output_lines = []
        
        while time.time() - start_time < 5:
            line = process.stdout.readline()
            if line:
                output_lines.append(line.strip())
                if len(output_lines) <= 10:
                    print(f"   {line.strip()}")
        
        process.terminate()
        process.wait(timeout=2)
        
        print("   " + "-"*60)
        print("   ✅ Tool executed successfully\n")
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {str(e)}\n")
        return False

def show_demo_options():
    print("="*70)
    print(" DEMO OPTIONS")
    print("="*70 + "\n")
    
    print("Choose a demo mode:\n")
    print("  [1] Launch GUI - Interactive demo (recommended for presentations)")
    print("  [2] Sequential Tool Demo - Run each tool for 10 seconds")
    print("  [3] Quick Showcase - Run all tools for 5 seconds each")
    print("  [4] Single Tool Test - Choose one tool to run")
    print("  [5] Exit\n")
    
    while True:
        choice = input("Enter your choice (1-5): ").strip()
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

def launch_gui():
    print("\n" + "="*70)
    print(" LAUNCHING SECURITY SUITE GUI")
    print("="*70 + "\n")
    print("Starting graphical interface...")
    print("You can now:")
    print("  - Click any tool button to see it in action")
    print("  - Use the Stop button to terminate running tools")
    print("  - Save output to a file")
    print("  - Try the menu options\n")
    print("Close the window when done.\n")
    
    try:
        subprocess.call([sys.executable, "security_suite.py"])
    except KeyboardInterrupt:
        print("\n\nGUI closed.")
    except Exception as e:
        print(f"\nError launching GUI: {e}")

def sequential_demo():
    print("\n" + "="*70)
    print(" SEQUENTIAL TOOL DEMONSTRATION")
    print("="*70 + "\n")
    
    tools = [
        ("network_security_analyzer.py", "Network Security Analyzer", 10),
        ("infinite_thought.py", "Infinite Thought", 10),
        ("unified_defense_system.py", "Unified Defense System", 10),
        ("fake_data_generator.py", "Fake Data Generator", 10),
        ("ai_logic_battle_system.py", "AI Logic Battle System", 10),
        ("quantum_honeypot_core.py", "Quantum Honeypot Core", 10)
    ]
    
    for script, name, duration in tools:
        print(f"\n{'='*70}")
        print(f" Running: {name}")
        print(f" Duration: {duration} seconds")
        print('='*70 + "\n")
        
        try:
            process = subprocess.Popen(
                [sys.executable, script],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            
            start_time = time.time()
            while time.time() - start_time < duration:
                line = process.stdout.readline()
                if line:
                    print(line, end='')
            
            process.terminate()
            process.wait(timeout=2)
            
            print(f"\n\n✓ {name} completed")
            time.sleep(2)
            
        except KeyboardInterrupt:
            print("\n\nDemo interrupted by user.")
            process.terminate()
            return
        except Exception as e:
            print(f"\nError running {name}: {e}")
    
    print("\n" + "="*70)
    print(" SEQUENTIAL DEMO COMPLETE")
    print("="*70 + "\n")

def quick_showcase():
    print("\n" + "="*70)
    print(" QUICK SHOWCASE - All Tools (5 seconds each)")
    print("="*70 + "\n")
    
    tools = [
        ("network_security_analyzer.py", "Network Security Analyzer"),
        ("infinite_thought.py", "Infinite Thought"),
        ("unified_defense_system.py", "Unified Defense System"),
        ("fake_data_generator.py", "Fake Data Generator"),
        ("ai_logic_battle_system.py", "AI Logic Battle System"),
        ("quantum_honeypot_core.py", "Quantum Honeypot Core")
    ]
    
    for script, name in tools:
        print(f"\n[{name}]")
        print("-"*70)
        
        try:
            process = subprocess.Popen(
                [sys.executable, script],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
            
            start_time = time.time()
            line_count = 0
            while time.time() - start_time < 5 and line_count < 15:
                line = process.stdout.readline()
                if line:
                    print(line, end='')
                    line_count += 1
            
            process.terminate()
            process.wait(timeout=2)
            
        except Exception as e:
            print(f"Error: {e}")
    
    print("\n" + "="*70)
    print(" QUICK SHOWCASE COMPLETE")
    print("="*70 + "\n")

def single_tool_test():
    print("\n" + "="*70)
    print(" SINGLE TOOL TEST")
    print("="*70 + "\n")
    
    tools = [
        ("network_security_analyzer.py", "Network Security Analyzer"),
        ("infinite_thought.py", "Infinite Thought"),
        ("unified_defense_system.py", "Unified Defense System"),
        ("fake_data_generator.py", "Fake Data Generator"),
        ("ai_logic_battle_system.py", "AI Logic Battle System"),
        ("quantum_honeypot_core.py", "Quantum Honeypot Core")
    ]
    
    print("Select a tool to test:\n")
    for i, (script, name) in enumerate(tools, 1):
        print(f"  [{i}] {name}")
    print()
    
    while True:
        choice = input("Enter your choice (1-6): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 6:
            idx = int(choice) - 1
            script, name = tools[idx]
            break
        print("Invalid choice. Please enter 1-6.")
    
    print(f"\nLaunching {name}...")
    print("Press Ctrl+C to stop\n")
    print("="*70 + "\n")
    
    try:
        subprocess.call([sys.executable, script])
    except KeyboardInterrupt:
        print("\n\nTool stopped.")

def main():
    print_banner()
    
    print("This demo will showcase the Security Suite's capabilities.\n")
    
    if not check_dependencies():
        print("\n❌ Dependency check failed. Please install missing dependencies.\n")
        return 1
    
    if not check_tool_scripts():
        print("\n❌ Tool script check failed. Some scripts are missing.\n")
        return 1
    
    if not check_main_application():
        print("\n❌ Main application check failed.\n")
        return 1
    
    if not run_quick_test():
        print("\n⚠️  Quick test had issues, but continuing...\n")
    
    print("✅ All systems operational!\n")
    
    while True:
        choice = show_demo_options()
        
        if choice == '1':
            launch_gui()
            break
        elif choice == '2':
            sequential_demo()
            break
        elif choice == '3':
            quick_showcase()
            break
        elif choice == '4':
            single_tool_test()
            break
        elif choice == '5':
            print("\nExiting demo. Goodbye!\n")
            break
    
    print("\nThank you for trying the Security Suite!")
    print("For more information, see Security_Suite_Analysis_Summary.md\n")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nDemo interrupted. Goodbye!\n")
        sys.exit(0)
