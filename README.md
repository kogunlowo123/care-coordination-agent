# Care Coordination Agent

[![CI](https://github.com/kogunlowo123/care-coordination-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/care-coordination-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Healthcare | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Care coordination agent that manages patient care plans, tracks referrals, coordinates between providers, monitors care gaps, and ensures continuity of care across settings.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `create_care_plan` | Create or update a patient care plan with goals and interventions |
| `track_referral` | Track referral status from order to completion |
| `identify_care_gaps` | Identify gaps in preventive care and chronic disease management |
| `coordinate_transition` | Coordinate care transition between settings (hospital to home) |
| `generate_summary` | Generate care coordination summary for the care team |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/care-coordination/process` | Process request |
| `POST` | `/api/v1/care-coordination/query` | Query data |
| `POST` | `/api/v1/care-coordination/validate` | Validate |
| `POST` | `/api/v1/care-coordination/report` | Generate report |
| `GET` | `/api/v1/care-coordination/audit` | Get audit trail |

## Features

- Care
- Coordination
- Compliance
- Interoperability

## Integrations

- Epic Ehr
- Cerner Ehr
- Allscripts
- Fhir Server
- Clearinghouse

## Architecture

```
care-coordination-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── care_coordination_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**EHR + Healthcare Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
