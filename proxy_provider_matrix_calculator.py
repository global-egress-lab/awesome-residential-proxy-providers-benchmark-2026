#!/usr/bin/env python3
"""
2026 All-Star Residential & Datacenter Proxy Providers Matrix Calculator.
Evaluates Pawns.app vs Webshare vs 9Proxy vs Decodo across traffic models.
"""
import argparse

def calculate(traffic_gb, ip_count, use_case):
    # Pawns.app: PAYG Residential ($3.00/GB or $2.50/GB >=10GB)
    pawns_cost = traffic_gb * (2.50 if traffic_gb >= 10 else 3.00)

    # Webshare: 100 Datacenter/Static ISP proxies (~$18/mo)
    webshare_cost = 18.0 if ip_count <= 100 else (ip_count * 0.16)

    # 9Proxy: Per-IP Residential ($0.20/IP, non-expiring)
    nineproxy_cost = ip_count * 0.20

    # Decodo: Enterprise Scaled Residential ($2.50/GB)
    decodo_cost = traffic_gb * 2.50

    print("=" * 70)
    print("2026 Proxy All-Star Benchmark Matrix: Cost by Architecture")
    print("=" * 70)
    print(f"Demand: {traffic_gb} GB Bandwidth | {ip_count} Clean Dedicated IPs | Use-case: {use_case}")
    print("-" * 70)
    print(f"1. Pawns.app (Budget Residential PAYG):   ${pawns_cost:.2f} (Never-expiring GB)")
    print(f"2. Webshare (Cheap Static ISP / DC):      ${webshare_cost:.2f}/mo (High concurrency)")
    print(f"3. 9Proxy (Per-IP Residential Clean Pool):${nineproxy_cost:.2f} (Pay per clean IP)")
    print(f"4. Decodo (Enterprise Heavy-Duty Pool):   ${decodo_cost:.2f} (Enterprise SLA)")
    print("=" * 70)
    return pawns_cost, webshare_cost, nineproxy_cost, decodo_cost

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Proxy Matrix Calculator")
    parser.add_argument("--traffic-gb", type=int, default=20)
    parser.add_argument("--ip-count", type=int, default=100)
    parser.add_argument("--use-case", default="general_scraping")
    args = parser.parse_args()
    calculate(args.traffic_gb, args.ip_count, args.use_case)
