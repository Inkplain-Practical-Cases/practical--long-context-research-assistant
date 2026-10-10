from app.context_budget import pack_context
def test_budget():
 r=pack_context([{'id':'a','text':'one two'},{'id':'b','text':'three four'}],2)
 assert r['used']==2 and r['omitted']==['b']
