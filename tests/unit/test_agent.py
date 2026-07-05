"""Care Coordination Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_create_care_plan():
    """Test Create or update a patient care plan with goals and interventions."""
    tools = AgentTools()
    result = await tools.create_care_plan(patient_id="test", conditions="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_track_referral():
    """Test Track referral status from order to completion."""
    tools = AgentTools()
    result = await tools.track_referral(referral_id="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_identify_care_gaps():
    """Test Identify gaps in preventive care and chronic disease management."""
    tools = AgentTools()
    result = await tools.identify_care_gaps(patient_id="test", guidelines="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_coordinate_transition():
    """Test Coordinate care transition between settings (hospital to home)."""
    tools = AgentTools()
    result = await tools.coordinate_transition(patient_id="test", from_setting="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.care_coordination_agent_agent import CareCoordinationAgentAgent
    agent = CareCoordinationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
