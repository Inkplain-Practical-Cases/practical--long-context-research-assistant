from app.evidence import passages,retrieve
def test_retrieval():
 r=retrieve("citation",passages("d","citation evidence\nno match"))
 assert r[0]["id"]=="d:0"
