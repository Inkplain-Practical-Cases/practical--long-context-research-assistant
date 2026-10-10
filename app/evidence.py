import re
def passages(doc_id,text):
 return [{"id":f"{doc_id}:{i}","source":doc_id,"text":s.strip()} for i,s in enumerate(text.split("\n")) if s.strip()]
def retrieve(query,items,k=5):
 q=set(re.findall(r"[a-z]+",query.lower()))
 scored=[(len(q & set(re.findall(r"[a-z]+",x["text"].lower()))),x) for x in items]
 return [x for v,x in sorted(scored,key=lambda v:-v[0]) if v>0][:k]
