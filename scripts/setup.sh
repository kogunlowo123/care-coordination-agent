#!/bin/bash
set -euo pipefail
echo "Setting up Care Coordination Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
