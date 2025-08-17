#!/usr/bin/env python3
"""
Kind API - Random Compliment Service
Serves random compliments from a YAML file via REST API
"""

import os
import yaml
import random
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

# Configuration
YAML_FILE = "kind_response.yaml"
API_VERSION = "v1"

# Load compliments from YAML


def load_compliments():
    """Load compliments from YAML file with error handling"""
    try:
        with open(YAML_FILE, "r") as f:
            return yaml.safe_load(f)["compliments"]
    except FileNotFoundError:
        abort(404, f"Compliment file not found: {YAML_FILE}")
    except yaml.YAMLError as e:
        abort(500, f"YAML error: {e}")
    except Exception as e:
        abort(500, f"Unexpected error loading compliments: {e}")


# Main API endpoint


@app.route(f"/api/{API_VERSION}/compliment", methods=["GET"])
def get_compliment():
    """Get a random compliment"""
    compliments = load_compliments()

    if not compliments:
        abort(404, "No compliments available")

    return jsonify(
        {
            "api_version": API_VERSION,
            "compliment": random.choice(compliments),
            "status": "success",
        }
    )


# Health check endpoint


@app.route("/api/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify(
        {"status": "ok", "message": "Kind API is running", "version": "1.0.0"}
    )


if __name__ == "__main__":
    # Run in production mode (with proper port handling)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, threaded=True)
