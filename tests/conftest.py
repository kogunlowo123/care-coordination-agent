"""Test configuration for Care Coordination Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "care-coordination-agent", "category": "Healthcare"}
