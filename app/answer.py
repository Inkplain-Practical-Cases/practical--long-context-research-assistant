from app.evidence import retrieve
from app.context_budget import pack_context
def answer(query,passages,budget=120):
 ranked=retrieve(query,passages)
 selected=pack_context(ranked,budget)
 if not selected["passages"]:return {"answer":"Insufficient evidence","citations":[],"grounded":False}
 item=selected["passages"][0]
 return {"answer":item["text"],"citations":[{"id":item["id"],"source":item["source"]}],"grounded":True}
