"""Budget passages before placing them in a model context."""
def pack_context(passages:list[dict],limit:int=120)->dict:
    if limit<1:raise ValueError("Positive budget required")
    chosen=[];used=0;omitted=[]
    for passage in passages:
        size=len(passage["text"].split())
        if used+size<=limit:
            chosen.append(dict(passage));used+=size
        else:omitted.append(passage["id"])
    return {"passages":chosen,"used":used,"limit":limit,"omitted":omitted}
