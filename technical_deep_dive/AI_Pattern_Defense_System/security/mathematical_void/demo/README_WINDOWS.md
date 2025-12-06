# 🛡️ Void Protection Demo - Windows Edition

## ⚡ Super Quick Start (3 Steps)

### Step 1: Start Server
Double-click **`START_SERVER.bat`**

Wait for this message:
```
[✓] Server running on http://localhost:8000
```

**Keep this window open!**

### Step 2: Run Demo
In a **NEW** window, double-click **`RUN_COMPARISON.bat`**

You'll see:
```
👤 CREATOR:  Risk Score: 0.9186 (REAL)
💀 ATTACKER: Risk Score: 0.9700 (DECOY)
✓ DIFFERENT MODELS CONFIRMED
```

### Step 3: Success!
Void protection is working! ✓

---

## 📂 Windows Files (Just Double-Click!)

| Double-Click This | What It Does |
|-------------------|--------------|
| **RUN_DEMO.bat** | Main menu - shows all options |
| **START_SERVER.bat** | Starts the server (do this first!) |
| **RUN_COMPARISON.bat** | **BEST DEMO** - Shows proof! |
| **RUN_ATTACKER.bat** | Shows attack detection |
| **RUN_CREATOR.bat** | Shows normal usage |
| **RUN_TESTS.bat** | Validates everything works |
| **TEST_CONNECTION.bat** | Quick check if server is running |

---

## 🎯 Best Demo Sequence

### Window 1: Server
```
START_SERVER.bat
```
Leave this running!

### Window 2: Comparison (PROOF!)
```
RUN_COMPARISON.bat
```
This shows that creator and attacker get different models!

### Window 3: Attacker (DETECTION!)
```
RUN_ATTACKER.bat
```
Watch the server window for `[✗ BLOCKED]` messages!

### Browser: Dashboard
```
http://localhost:8000
```
See live statistics!

---

## 🚨 Troubleshooting

### "python is not recognized"

Install Python from [python.org](https://python.org)  
✅ Check "Add Python to PATH" during installation

### "No module named 'requests'"

Open Command Prompt and run:
```cmd
pip install requests
```

### "Address already in use"

A server is already running. Close the server window or press Ctrl+C in it.

### Server won't start

1. Check Python is installed: `python --version`
2. Check port 8000 is free
3. Run as administrator if needed

### "Connection refused"

Make sure server is running first (START_SERVER.bat)!

---

## 💡 What You'll See

### Server Window
```
[✓ CREATOR] 127.0.0.1 → Real model
[✗ BLOCKED] 127.0.0.1 → Decoy (Threat: high)
    Indicators: High frequency: 15 req/min
```

### Comparison Demo
```
TEST CASE: Moderate Risk
Input: Vol=0.5, Corr=0.3, Liq=1.0

👤 CREATOR:  0.9186 (REAL algorithm)
💀 ATTACKER: 0.9700 (DECOY algorithm)

✓ DIFFERENT MODELS CONFIRMED
```

### Dashboard (Browser)
```
Total Requests:        127
Creator Requests:       42 ✓
Extraction Attempts:    12 ⚠
Decoys Served:          85 ✗
```

---

## ✅ Quick Validation

### 1. Server Check
```
TEST_CONNECTION.bat
```
Should say: "✓ Server is RUNNING!"

### 2. Full Test
```
RUN_TESTS.bat
```
Should say: "✓ ALL TESTS PASSED"

### 3. Proof
```
RUN_COMPARISON.bat
```
Should show different scores for creator vs attacker

---

## 📖 More Information

- **WINDOWS_GUIDE.md** - Complete Windows guide
- **START_HERE.md** - Detailed instructions
- **DEMO_README.md** - Full technical documentation

---

## 🎉 That's It!

**Your void protection system is working on Windows!**

Next steps:
- ✅ Run all demos
- ✅ Read the code
- ✅ Modify and experiment
- ✅ Integrate with your systems

---

**Questions? Check WINDOWS_GUIDE.md for detailed help!**
