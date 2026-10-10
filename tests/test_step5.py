from app.answer import answer
def test_citation():
 p=[{"id":"d:1","source":"d","text":"Context evidence is cited"}]
 assert answer("context evidence",p)["citations"][0]["id"]=="d:1"
