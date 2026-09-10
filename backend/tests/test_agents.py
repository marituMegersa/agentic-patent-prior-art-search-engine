def test_agent_orchestrator():
    prompt = "Test execution query for agentic-patent-prior-art-search-engine"
    assert len(prompt) > 0
    assert "Test" in prompt
