"""Tests for multi-agent system."""
import pytest
import sys; sys.path.insert(0,".")
from src.agents.orchestrator import Orchestrator, DataAgent, AnalysisAgent, ReportAgent

def test_data_agent_returns_json():
    a = DataAgent()
    result = a.execute("get sales data")
    import json
    data = json.loads(result)
    assert "total_revenue" in data

def test_analysis_agent_returns_text():
    a = AnalysisAgent()
    result = a.execute("analyse revenue trend")
    assert isinstance(result, str) and len(result) > 20

def test_report_agent_formats():
    a = ReportAgent()
    result = a.execute("write report", "Revenue up 12%")
    assert "Executive Summary" in result
    assert "Revenue up 12%" in result

def test_orchestrator_completes_normal_task():
    orch = Orchestrator()
    result = orch.run("Analyse Q2 sales performance")
    assert result.completed is True
    assert len(result.tasks) == 3
    assert result.final_output != ""
    assert result.total_duration_ms > 0

def test_orchestrator_flags_critical_task():
    orch = Orchestrator()
    result = orch.run("delete all customer records")
    assert result.human_checkpoint_required is True
    assert result.completed is False

def test_audit_log_populated():
    orch = Orchestrator()
    orch.run("Show revenue breakdown")
    assert len(orch.audit_log) > 0
    events = [e["event"] for e in orch.audit_log]
    assert "workflow_start" in events
    assert "workflow_complete" in events

def test_workflow_id_assigned():
    orch = Orchestrator()
    result = orch.run("Analyse customer churn", workflow_id="WF_TEST")
    assert result.workflow_id == "WF_TEST"
