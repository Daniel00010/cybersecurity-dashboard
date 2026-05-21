from flask import Flask, render_template, jsonify
import requests
import pandas as pd
from datetime import datetime

app = Flask(__name__)

def get_threat_data():
    # Using AbuseIPDB free public threat data
    # We'll use a sample of known malicious IPs for demo
    sample_threats = [
        {"ip": "185.220.101.45", "country": "DE", "abuse_score": 100, "type": "TOR Exit Node", "reports": 847, "last_seen": "2026-05-20"},
        {"ip": "45.155.205.233", "country": "RU", "abuse_score": 98, "type": "SSH Brute Force", "reports": 632, "last_seen": "2026-05-20"},
        {"ip": "192.42.116.16", "country": "NL", "abuse_score": 97, "type": "TOR Exit Node", "reports": 521, "last_seen": "2026-05-19"},
        {"ip": "198.235.24.156", "country": "US", "abuse_score": 95, "type": "DDoS Attack", "reports": 489, "last_seen": "2026-05-19"},
        {"ip": "89.234.157.254", "country": "FR", "abuse_score": 94, "type": "Port Scan", "reports": 412, "last_seen": "2026-05-18"},
        {"ip": "171.25.193.77", "country": "SE", "abuse_score": 93, "type": "TOR Exit Node", "reports": 398, "last_seen": "2026-05-18"},
        {"ip": "62.102.148.68", "country": "CH", "abuse_score": 91, "type": "SSH Brute Force", "reports": 356, "last_seen": "2026-05-17"},
        {"ip": "91.108.4.168", "country": "NL", "abuse_score": 89, "type": "Malware", "reports": 334, "last_seen": "2026-05-17"},
        {"ip": "5.188.86.172", "country": "RU", "abuse_score": 88, "type": "SSH Brute Force", "reports": 298, "last_seen": "2026-05-16"},
        {"ip": "80.82.77.139", "country": "NL", "abuse_score": 86, "type": "Port Scan", "reports": 276, "last_seen": "2026-05-16"},
    ]
    return sample_threats

def get_stats(threats):
    df = pd.DataFrame(threats)
    
    # Count by country
    country_counts = df['country'].value_counts().to_dict()
    
    # Count by threat type
    type_counts = df['type'].value_counts().to_dict()
    
    # Average abuse score
    avg_score = round(df['abuse_score'].mean(), 1)
    
    # Total reports
    total_reports = int(df['reports'].sum())
    
    return {
        "country_counts": country_counts,
        "type_counts": type_counts,
        "avg_score": avg_score,
        "total_reports": total_reports
    }

@app.route('/')
def index():
    threats = get_threat_data()
    stats = get_stats(threats)
    return render_template('index.html', threats=threats, stats=stats)

@app.route('/api/threats')
def api_threats():
    threats = get_threat_data()
    stats = get_stats(threats)
    return jsonify({"threats": threats, "stats": stats})

if __name__ == '__main__':
    app.run(debug=True)