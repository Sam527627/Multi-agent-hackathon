# Multi-Agent AI Business Process Automation

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.1+-orange.svg)](https://langchain.com)
[![CI](https://github.com/Sam527627/Multi-agent-hackathon/actions/workflows/ci.yml/badge.svg)](https://github.com/Sam527627/Multi-agent-hackathon/actions)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Multi-agent AI system that automates complex business workflows. Orchestrator decomposes tasks into specialised sub-agents (data retrieval, analysis, report generation) with human-in-the-loop checkpoints. 71% fully automated completion on 50 benchmark tasks.

## Architecture
```
User Task → Orchestrator Agent (LangGraph)
    ├── Data Agent (PostgreSQL, REST APIs)
    ├── Analysis Agent (Python execution, calculations)
    ├── Search Agent (web research, fact verification)
    └── Report Agent (structured output, formatting)
            ↓
Human checkpoint (low-confidence decisions)
            ↓
Output + full audit trail (every decision logged)
```

## Benchmark Results (50 Business Tasks)
- Fully automated: **71%**
- Correctly escalated to human: **24%**
- False completion: **5%**
- Average task duration: **34 seconds**

## Tech Stack
`Python` `LangGraph` `LangChain` `OpenAI GPT-4o` `Ollama (local)` `FastAPI` `PostgreSQL` `Redis` `Docker`

## Quick Start
```bash
git clone https://github.com/Sam527627/Multi-agent-hackathon
cd Multi-agent-hackathon
cp .env.example .env  # Add OPENAI_API_KEY or set OLLAMA_HOST
docker-compose up --build
```

## Author
**Sambhav Kapoor** — [LinkedIn](https://linkedin.com/in/sambhav-kapoorr)
