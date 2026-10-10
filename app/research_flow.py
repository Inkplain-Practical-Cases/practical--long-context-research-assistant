from app.evidence import passages
from app.answer import answer
from app.session_store import append
def research(user,session,question,documents,budget=120):
 if not user or not session:raise PermissionError("Owner required")
 if not question.strip():raise ValueError("Question required")
 all_passages=[p for doc,text in documents.items() for p in passages(doc,text)]
 append(user,session,"user",question)
 result=answer(question,all_passages,budget)
 append(user,session,"assistant",result["answer"])
 return {"session_id":session,**result}
