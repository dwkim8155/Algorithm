import re

def solution(new_id):
    #1단계
    new_id = new_id.lower()
    
    #2단계
    new_id = "".join(re.findall("[a-z0-9\-\_\.]", new_id))
    
    #3단계
    new_id = re.sub('\.{2,}', '.', new_id)
    
    #4단계
    if new_id.startswith("."):
        new_id = new_id[1:]
    if new_id.endswith("."):
        new_di = new_id[:-1]
    
    #5단계
    if not new_id:
        new_id+="a"
    
    #6단계
    new_id = new_id[:15]
    if new_id.endswith("."):
        new_id = new_id[:-1]
    
    #7단계
    if len(new_id) <= 2:
        new_id = new_id+new_id[-1]*(3-len(new_id))
  
    return new_id