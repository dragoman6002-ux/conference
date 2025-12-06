#!/usr/bin/env python3
"""
REAL NETWORK DEMONSTRATION: Void-Protected API Server

This is a REAL server with ACTUAL network communication demonstrating:
1. Real proprietary data (financial model)
2. Real extraction attempts
3. Real void protection routing to decoys
4. Real creator navigation to actual data

Run this to see void security in action with real network traffic.
"""

import socket
import json
import hashlib
import secrets
import time
import threading
from datetime import datetime
from typing import Dict, List, Optional
import http.server
import socketserver
from urllib.parse import urlparse, parse_qs

class ProprietaryFinancialModel:
    """
    REAL proprietary algorithm - This is what we're protecting
    This represents millions in R&D investment
    """
    def __init__(self):
        self.secret_parameters = {
            "risk_weight_alpha": 0.23847,
            "beta_correlation": 1.8392,
            "gamma_adjustment": 0.00391,
            "proprietary_factor": 2.71828,
            "market_sensitivity": 0.618034,
        }
        
        self.secret_formula = """
        Risk Score = (alpha * volatility^2) + (beta * correlation) 
                    - (gamma * liquidity) * proprietary_factor
        """
    
    def calculate_risk_score(self, data: Dict) -> float:
        """Real proprietary risk calculation"""
        volatility = data.get("volatility", 0)
        correlation = data.get("correlation", 0)
        liquidity = data.get("liquidity", 1)
        
        score = (
            self.secret_parameters["risk_weight_alpha"] * (volatility ** 2) +
            self.secret_parameters["beta_correlation"] * correlation -
            self.secret_parameters["gamma_adjustment"] * liquidity
        ) * self.secret_parameters["proprietary_factor"]
        
        return round(score, 4)

class DecoyFinancialModel:
    """
    Plausible but WRONG model - This is what attackers get
    Looks real, but uses incorrect formulas
    """
    def __init__(self):
        self.parameters = {
            "risk_weight_alpha": 0.15,
            "beta_correlation": 1.2,
            "gamma_adjustment": 0.05,
            "standard_factor": 2.0,
            "market_sensitivity": 0.5,
        }
    
    def calculate_risk_score(self, data: Dict) -> float:
        """Decoy calculation - wrong but plausible"""
        volatility = data.get("volatility", 0)
        correlation = data.get("correlation", 0)
        liquidity = data.get("liquidity", 1)
        
        score = (
            self.parameters["risk_weight_alpha"] * volatility +
            self.parameters["beta_correlation"] * correlation +
            self.parameters["gamma_adjustment"] / liquidity
        ) * self.parameters["standard_factor"]
        
        return round(score, 4)

class VoidProtectionSystem:
    """
    REAL void protection system for the API
    Routes extraction attempts to decoys, creators to real system
    """
    def __init__(self):
        self.real_model = ProprietaryFinancialModel()
        self.decoy_models = {}
        self.request_history = {}
        self.creator_tokens = set()
        self.blocked_ips = set()
        
        self._generate_creator_token()
        self.stats = {
            "total_requests": 0,
            "creator_requests": 0,
            "extraction_attempts_detected": 0,
            "extraction_attempts_blocked": 0,
            "decoys_served": 0
        }
    
    def _generate_creator_token(self) -> str:
        """Generate secure creator token"""
        token = secrets.token_hex(32)
        self.creator_tokens.add(token)
        
        with open("creator_token.txt", "w") as f:
            f.write(f"CREATOR TOKEN (keep secret):\n{token}\n")
            f.write(f"\nUse this in requests: Authorization: Bearer {token}\n")
        
        print(f"[SETUP] Creator token saved to creator_token.txt")
        return token
    
    def analyze_request(self, client_ip: str, request_data: Dict, headers: Dict) -> Dict:
        """
        REAL threat analysis - Detect extraction attempts
        """
        self.stats["total_requests"] += 1
        
        current_time = time.time()
        
        if client_ip not in self.request_history:
            self.request_history[client_ip] = {
                "requests": [],
                "first_seen": current_time,
                "patterns": []
            }
        
        history = self.request_history[client_ip]
        history["requests"].append({
            "time": current_time,
            "data": request_data
        })
        
        recent_requests = [r for r in history["requests"] if current_time - r["time"] < 60]
        history["requests"] = recent_requests
        
        auth_header = headers.get("authorization", "")
        is_creator = any(token in auth_header for token in self.creator_tokens)
        
        request_frequency = len(recent_requests)
        
        is_systematic = self._detect_systematic_pattern(recent_requests)
        
        threat_score = 0
        threat_indicators = []
        
        if request_frequency > 10:
            threat_score += 0.4
            threat_indicators.append(f"High frequency: {request_frequency} req/min")
        
        if is_systematic:
            threat_score += 0.5
            threat_indicators.append("Systematic exploration detected")
        
        if not is_creator and request_frequency > 5:
            threat_score += 0.3
            threat_indicators.append("Non-creator with elevated activity")
        
        if client_ip in self.blocked_ips:
            threat_score = 1.0
            threat_indicators.append("Previously blocked IP")
        
        threat_level = "none"
        if threat_score > 0.7:
            threat_level = "critical"
            self.stats["extraction_attempts_detected"] += 1
        elif threat_score > 0.4:
            threat_level = "high"
        elif threat_score > 0.2:
            threat_level = "medium"
        
        return {
            "is_creator": is_creator,
            "threat_level": threat_level,
            "threat_score": threat_score,
            "indicators": threat_indicators,
            "client_ip": client_ip,
            "request_count": request_frequency
        }
    
    def _detect_systematic_pattern(self, requests: List[Dict]) -> bool:
        """Detect if requests show systematic exploration pattern"""
        if len(requests) < 5:
            return False
        
        values = []
        for req in requests[-10:]:
            if "data" in req and "volatility" in req["data"]:
                values.append(req["data"]["volatility"])
        
        if len(values) < 5:
            return False
        
        diffs = [values[i+1] - values[i] for i in range(len(values)-1)]
        
        if len(set(diffs)) <= 2:
            return True
        
        if all(d > 0 for d in diffs) or all(d < 0 for d in diffs):
            return True
        
        return False
    
    def get_decoy_model(self, client_ip: str) -> DecoyFinancialModel:
        """Get consistent decoy for this client"""
        if client_ip not in self.decoy_models:
            self.decoy_models[client_ip] = DecoyFinancialModel()
        return self.decoy_models[client_ip]
    
    def process_request(self, client_ip: str, request_data: Dict, headers: Dict) -> Dict:
        """
        MAIN ROUTING LOGIC
        Creator → Real model
        Attacker → Decoy model
        """
        analysis = self.analyze_request(client_ip, request_data, headers)
        
        if analysis["is_creator"]:
            self.stats["creator_requests"] += 1
            model = self.real_model
            model_type = "REAL"
            print(f"[✓ CREATOR] {client_ip} → Real model")
        
        elif analysis["threat_level"] in ["critical", "high"]:
            self.stats["extraction_attempts_blocked"] += 1
            self.stats["decoys_served"] += 1
            model = self.get_decoy_model(client_ip)
            model_type = "DECOY"
            print(f"[✗ BLOCKED] {client_ip} → Decoy (Threat: {analysis['threat_level']})")
            print(f"    Indicators: {', '.join(analysis['indicators'])}")
            
            if analysis["threat_level"] == "critical":
                self.blocked_ips.add(client_ip)
        
        else:
            if len(self.request_history.get(client_ip, {}).get("requests", [])) > 3:
                self.stats["decoys_served"] += 1
                model = self.get_decoy_model(client_ip)
                model_type = "DECOY"
                print(f"[⚠ SUSPICIOUS] {client_ip} → Decoy (monitoring)")
            else:
                self.stats["creator_requests"] += 1
                model = self.real_model
                model_type = "REAL"
                print(f"[? UNKNOWN] {client_ip} → Real model (low activity)")
        
        result = model.calculate_risk_score(request_data)
        
        return {
            "risk_score": result,
            "timestamp": datetime.now().isoformat(),
            "model_version": "v2.1.4",
            "status": "success",
            "_internal_model_type": model_type,
            "_internal_threat_analysis": analysis
        }

class VoidAPIHandler(http.server.BaseHTTPRequestHandler):
    """HTTP request handler with void protection"""
    
    void_system = None
    
    def log_message(self, format, *args):
        pass
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(self._get_homepage().encode())
        
        elif self.path == "/stats":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            stats = self.void_system.stats.copy()
            stats["active_clients"] = len(self.void_system.request_history)
            stats["blocked_ips"] = len(self.void_system.blocked_ips)
            self.wfile.write(json.dumps(stats, indent=2).encode())
        
        elif self.path.startswith("/api/risk"):
            parsed = urlparse(self.path)
            params = parse_qs(parsed.query)
            
            request_data = {
                "volatility": float(params.get("volatility", [0.5])[0]),
                "correlation": float(params.get("correlation", [0.3])[0]),
                "liquidity": float(params.get("liquidity", [1.0])[0])
            }
            
            headers = {k.lower(): v for k, v in self.headers.items()}
            
            client_ip = self.client_address[0]
            
            response = self.void_system.process_request(client_ip, request_data, headers)
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            public_response = {
                "risk_score": response["risk_score"],
                "timestamp": response["timestamp"],
                "model_version": response["model_version"],
                "status": response["status"]
            }
            
            self.wfile.write(json.dumps(public_response, indent=2).encode())
        
        else:
            self.send_error(404)
    
    def do_POST(self):
        """Handle POST requests"""
        if self.path == "/api/risk":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            
            try:
                request_data = json.loads(body.decode())
            except:
                self.send_error(400, "Invalid JSON")
                return
            
            headers = {k.lower(): v for k, v in self.headers.items()}
            client_ip = self.client_address[0]
            
            response = self.void_system.process_request(client_ip, request_data, headers)
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            public_response = {
                "risk_score": response["risk_score"],
                "timestamp": response["timestamp"],
                "model_version": response["model_version"],
                "status": response["status"]
            }
            
            self.wfile.write(json.dumps(public_response, indent=2).encode())
        else:
            self.send_error(404)
    
    def _get_homepage(self) -> str:
        """Dashboard homepage"""
        stats = self.void_system.stats
        return f"""<!DOCTYPE html>
<html>
<head>
    <title>Void-Protected API Server</title>
    <meta http-equiv="refresh" content="2">
    <style>
        body {{ font-family: monospace; background: #0a0a0a; color: #00ff00; padding: 20px; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        h1 {{ color: #00ff00; border-bottom: 2px solid #00ff00; padding-bottom: 10px; }}
        .stat-box {{ background: #1a1a1a; border: 1px solid #00ff00; padding: 15px; margin: 10px 0; }}
        .stat-label {{ color: #888; }}
        .stat-value {{ color: #00ff00; font-size: 24px; font-weight: bold; }}
        .alert {{ color: #ff0000; }}
        .success {{ color: #00ff00; }}
        .warning {{ color: #ffaa00; }}
        .endpoint {{ background: #2a2a2a; padding: 10px; margin: 5px 0; border-left: 3px solid #00ff00; }}
        pre {{ background: #1a1a1a; padding: 10px; border: 1px solid #333; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🛡️ VOID-PROTECTED API SERVER - LIVE</h1>
        
        <div class="stat-box">
            <div class="stat-label">Total Requests</div>
            <div class="stat-value">{stats['total_requests']}</div>
        </div>
        
        <div class="stat-box">
            <div class="stat-label">Creator Requests (Real Model)</div>
            <div class="stat-value success">✓ {stats['creator_requests']}</div>
        </div>
        
        <div class="stat-box">
            <div class="stat-label">Extraction Attempts Detected</div>
            <div class="stat-value alert">⚠ {stats['extraction_attempts_detected']}</div>
        </div>
        
        <div class="stat-box">
            <div class="stat-label">Attacks Blocked (Decoys Served)</div>
            <div class="stat-value warning">✗ {stats['decoys_served']}</div>
        </div>
        
        <div class="stat-box">
            <div class="stat-label">Active Clients</div>
            <div class="stat-value">{len(self.void_system.request_history)}</div>
        </div>
        
        <h2>📡 API Endpoints</h2>
        
        <div class="endpoint">
            <strong>GET /api/risk</strong><br>
            Example: <code>http://localhost:8000/api/risk?volatility=0.5&correlation=0.3&liquidity=1.0</code>
        </div>
        
        <div class="endpoint">
            <strong>POST /api/risk</strong><br>
            Body: <code>{{"volatility": 0.5, "correlation": 0.3, "liquidity": 1.0}}</code>
        </div>
        
        <div class="endpoint">
            <strong>GET /stats</strong><br>
            Returns: JSON statistics
        </div>
        
        <h2>🔑 Creator Access</h2>
        <pre>Add header: Authorization: Bearer [token from creator_token.txt]</pre>
        
        <h2>🎯 Test It</h2>
        <pre>
# Normal request (might get real or decoy depending on pattern)
curl "http://localhost:8000/api/risk?volatility=0.5&correlation=0.3&liquidity=1.0"

# Creator request (gets real model)
curl -H "Authorization: Bearer YOUR_TOKEN" "http://localhost:8000/api/risk?volatility=0.5&correlation=0.3&liquidity=1.0"

# Extraction attempt (rapid systematic queries - gets decoy)
python demo_attacker.py
        </pre>
        
        <p style="margin-top: 30px; color: #666;">
        Auto-refreshing every 2 seconds | Server time: {datetime.now().strftime('%H:%M:%S')}
        </p>
    </div>
</body>
</html>"""

def start_server(port: int = 8000):
    """Start the void-protected server"""
    
    print("=" * 80)
    print("  VOID-PROTECTED API SERVER - REAL NETWORK DEMONSTRATION")
    print("=" * 80)
    print()
    print("This is a REAL server with ACTUAL network protection.")
    print("Protected asset: Proprietary Financial Risk Model")
    print()
    
    void_system = VoidProtectionSystem()
    
    VoidAPIHandler.void_system = void_system
    
    with socketserver.TCPServer(("", port), VoidAPIHandler) as httpd:
        print(f"[✓] Server running on http://localhost:{port}")
        print(f"[✓] Creator token saved to creator_token.txt")
        print()
        print("Dashboard: http://localhost:8000")
        print("API Endpoint: http://localhost:8000/api/risk")
        print("Stats: http://localhost:8000/stats")
        print()
        print("=" * 80)
        print("LIVE REQUEST LOG:")
        print("=" * 80)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n[SERVER STOPPED]")
            print("\nFinal Statistics:")
            print(f"  Total requests: {void_system.stats['total_requests']}")
            print(f"  Creator requests (real model): {void_system.stats['creator_requests']}")
            print(f"  Extraction attempts: {void_system.stats['extraction_attempts_detected']}")
            print(f"  Decoys served: {void_system.stats['decoys_served']}")
            print(f"  Protection rate: {void_system.stats['decoys_served'] / max(1, void_system.stats['total_requests']) * 100:.1f}%")

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
    start_server(port)