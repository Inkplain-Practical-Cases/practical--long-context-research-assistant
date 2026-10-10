from app.session_store import append,read
def test_isolation():
 append("a","s","user","secret")
 assert read("b","s")==[]
