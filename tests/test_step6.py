from app.research_flow import research
def test_research():
 result=research("a","s","citations",{"doc":"We preserve citations."},40)
 assert result["grounded"] and result["citations"]
