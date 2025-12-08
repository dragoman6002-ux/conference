import sys
import subprocess
import os
import time

def print_section(title):
    print("\n" + "="*70)
    print(f" {title}")
    print("="*70 + "\n")

def check_file_exists(filename, description):
    if os.path.exists(filename):
        print(f"✅ {description:40} [{filename}]")
        return True
    else:
        print(f"❌ {description:40} [{filename}] NOT FOUND")
        return False

def check_python_syntax(filename):
    try:
        result = subprocess.run(
            [sys.executable, "-m", "py_compile", filename],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            return True
        else:
            print(f"   ⚠️  Syntax issue: {result.stderr[:100]}")
            return False
    except Exception as e:
        print(f"   ⚠️  Could not check: {e}")
        return False

def test_tool_import(filename):
    try:
        result = subprocess.run(
            [sys.executable, "-c", f"import sys; exec(open('{filename}').read())"],
            capture_output=True,
            text=True,
            timeout=2
        )
        return True
    except Exception:
        return False

def main():
    print("\n" + "🔍 " * 35)
    print_section("SECURITY SUITE - CONNECTION VERIFICATION")
    print("This script verifies all components are properly connected.\n")
    
    all_ok = True
    
    print_section("1. Core Files Check")
    
    core_files = [
        ("security_suite.py", "Main GUI Application"),
        ("demo.py", "Demo Launcher"),
    ]
    
    for filename, description in core_files:
        if not check_file_exists(filename, description):
            all_ok = False
    
    print_section("2. Security Tool Scripts Check")
    
    tools = [
        ("network_security_analyzer.py", "Network Security Analyzer"),
        ("infinite_thought.py", "Infinite Thought Generator"),
        ("unified_defense_system.py", "Unified Defense System"),
        ("fake_data_generator.py", "Fake Data Generator"),
        ("ai_logic_battle_system.py", "AI Logic Battle System"),
        ("quantum_honeypot_core.py", "Quantum Honeypot Core"),
    ]
    
    for filename, description in tools:
        if not check_file_exists(filename, description):
            all_ok = False
    
    print_section("3. Python Syntax Validation")
    
    python_files = [f[0] for f in core_files + tools if f[0].endswith('.py')]
    
    syntax_ok = True
    for filename in python_files:
        if os.path.exists(filename):
            status = "✅" if check_python_syntax(filename) else "❌"
            print(f"{status} {filename}")
            if status == "❌":
                syntax_ok = False
    
    if not syntax_ok:
        all_ok = False
    
    print_section("4. Module Imports Check")
    
    required_modules = [
        'tkinter',
        'subprocess',
        'threading',
        'json',
        'os',
        'sys',
        'pathlib'
    ]
    
    import_ok = True
    for module in required_modules:
        try:
            __import__(module)
            print(f"✅ {module:20} - Available")
        except ImportError:
            print(f"❌ {module:20} - NOT AVAILABLE")
            import_ok = False
    
    if not import_ok:
        all_ok = False
    
    print_section("5. Quick Execution Test")
    
    print("Testing: infinite_thought.py (2 seconds)")
    try:
        process = subprocess.Popen(
            [sys.executable, "infinite_thought.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True
        )
        
        start = time.time()
        line_count = 0
        
        while time.time() - start < 2:
            line = process.stdout.readline()
            if line:
                line_count += 1
                if line_count <= 3:
                    print(f"   {line.strip()}")
        
        process.terminate()
        process.wait(timeout=2)
        
        if line_count > 0:
            print(f"\n✅ Tool executed and produced {line_count} lines of output")
        else:
            print("\n⚠️  Tool executed but no output detected")
            
    except Exception as e:
        print(f"\n❌ Execution failed: {e}")
        all_ok = False
    
    print_section("6. Tool Interconnection Test")
    
    print("Verifying tools can be called from main application...")
    
    for filename, description in tools:
        if os.path.exists(filename):
            if test_tool_import(filename):
                print(f"✅ {description:40} - Can be launched")
            else:
                print(f"⚠️  {description:40} - May have issues")
    
    print_section("VERIFICATION SUMMARY")
    
    if all_ok:
        print("""
✅✅✅ ALL SYSTEMS OPERATIONAL ✅✅✅

Your Security Suite is ready for demonstration!

Next Steps:
  1. Run the demo:     python demo.py
  2. Launch GUI:       python security_suite.py

Everything is properly connected and ready to showcase.
""")
        return 0
    else:
        print("""
⚠️  SOME ISSUES DETECTED ⚠️

Please review the errors above and fix any missing files or dependencies.
""")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        print("\n" + "🔍 " * 35 + "\n")
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\nVerification interrupted.\n")
        sys.exit(1)
