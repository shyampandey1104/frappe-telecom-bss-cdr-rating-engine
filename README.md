# Frappe Telecom BSS CDR Rating & Postpaid Billing Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Telecom](https://img.shields.io/badge/Telecom-BSS%20%2F%20OSS-blueviolet.svg)](https://trai.gov.in)

High-throughput Call Detail Record (CDR) ingestion and rating engine designed for telecom service providers, MVNOs, and VoIP trunk billing.

## Features
- **Multi-Service Rating:** Rates voice minutes, cellular data (MB/GB), SMS, and value-added services.
- **Roaming Surcharges:** Dynamic peak/off-peak and inter-circle national roaming tariff multipliers.
- **Taxation Breakdown:** Telecom GST 18% calculation with invoice generation.

## Tests
```bash
python3 -m unittest discover tests
```
