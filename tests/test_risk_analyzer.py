"""
Tests for risk analyzer
"""

import pytest
import asyncio
from src.analyzers import RiskAnalyzer


@pytest.fixture
def analyzer():
    return RiskAnalyzer(data_dir="/tmp/test-risk-data")


@pytest.mark.asyncio
async def test_analyze_token(analyzer):
    """Test token analysis"""
    # Use a known token (WAIFU)
    result = await analyzer.analyze_token("BGAED7f6EcBbWPamiWxcpgXqpkGm7zpYoxmx29Jh9cUp")
    
    assert "symbol" in result
    assert "score" in result
    assert "risk_level" in result
    assert "metrics" in result
    assert result["score"] >= 0
    assert result["score"] <= 100


@pytest.mark.asyncio
async def test_format_report(analyzer):
    """Test report formatting"""
    result = await analyzer.analyze_token("BGAED7f6EcBbWPamiWxcpgXqpkGm7zpYoxmx29Jh9cUp")
    report = analyzer.format_report(result)
    
    assert isinstance(report, str)
    assert len(report) > 0
    assert "$" in report  # Should contain token symbol


@pytest.mark.asyncio
async def test_token_not_found(analyzer):
    """Test handling of non-existent token"""
    result = await analyzer.analyze_token("invalid_mint_address_12345")
    
    assert "error" in result
    assert result["score"] == 0
