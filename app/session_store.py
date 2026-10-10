from collections import defaultdict
from threading import Lock
_lock=Lock();_history=defaultdict(list)
def append(user,session,role,text):
 if not user or not session:raise ValueError("Owner required")
 with _lock:
  key=(user,session);_history[key].append({"role":role,"text":text})
  _history[key]=_history[key][-12:]
  return [dict(x) for x in _history[key]]
def read(user,session):
 with _lock:return [dict(x) for x in _history.get((user,session),[])]
