#!/usr/bin/env python
# coding: utf-8

# In[154]:


#for printing terminals, non_terminals and their entries in Parsing_table
def print_(table):
    ffs.print_rules(rules);       
    ffs.print_FFset(firstSet,True);   
    ffs.print_FFset(followSet,False); 
    terminals=set()
    for nt in rules.keys():
        terminals=terminals.union(firstSet[nt])
        terminals=terminals.union(followSet[nt])
    terminals.discard('eps')
    print("\nNon Terminals:\n",rules.keys())  
    print("\nTerminals:\n",terminals)                   
    print("\n\nTable entries are:\n")
    for row,col in table.items():
        print(row,':',col)    
    print()
    return
def get_parsing_table(firstSet,followSet,rules):
    parsing_table=defaultdict()
    table=defaultdict()   #just for printing in good way (can be done by parsing_table too)
    for key,rule in rules.items():
        for sub_rule in rule:
            symbol = sub_rule[0]
            if ffs.isNonTerminal(symbol,rules): 
                for ter in firstSet[symbol]-{'eps'}:
                    parsing_table[key,ter]={key:sub_rule}
                    table[key,ter]=key+'-> '+' '.join(i for i in sub_rule)

            elif symbol=="eps" or symbol in deepcopy(firstSet[symbol]):
                for ter in followSet[key]:
                    parsing_table[key,ter] = {key:['eps']}
                    table[key,ter]=key+'-> '+'eps'
            else:
                parsing_table[key,symbol]={key:sub_rule}
                table[key,symbol]=key+'-> '+' '.join(i for i in sub_rule)
    print_(table)  #for printing terminals, non_terminals and their entries in Parsing_table
    return parsing_table


# In[155]:


def parser(p_table,start_state):
    expr = list(map(str,input("Enter expression for prasing(Plz enter space between 2 entry)\n").split())) 
    if expr[-1] != '$':
        print("\nPlease add '$' at the end of expression. Try again")
        return
    print("\nyour expression is",expr)
    stack=['$'];stack.append(start_state)
    inp=0
    while(stack and expr[inp]):
        popped = stack.pop()
        while (popped=='eps'):  #when popped is epsilon then again pop
            popped = stack.pop()
        if popped != expr[inp]:
            if p_table.get((popped,expr[inp])): #for checking, this entry is in table or not ?
                rule = p_table.get((popped,expr[inp])).get(popped)  # 2D dict table is again 1D dict with that rule
                for x in range(len(rule)):   
                    stack.append(rule[-x-1])     # minus for reversing 
            else:
                print("\nError, the expression is wrong. Try again")
                return
        else:
            inp+=1
        if stack[0]==expr[inp]:
            flag=True
            break
            
    if flag:
        print("\nExpression accepted")
    else:
        print("\nExpression rejected, it can't be generated from this grammar")
    return


# In[156]:


import First_Follow_sets as ffs  
from collections import defaultdict
from copy import deepcopy
if __name__=="__main__":
    
    rules,start_state=ffs.get_rules()
    firstSet = ffs.get_first_set(rules)
    followSet = ffs.get_follow_set(rules,deepcopy(firstSet),start_state)
    parsing_table = get_parsing_table(deepcopy(firstSet),deepcopy(followSet),rules)
    parser(parsing_table,start_state)
#     print(parsing_table)


# In[157]:


parser(parsing_table,start_state)


# In[159]:


parser(parsing_table,start_state)


# In[161]:


parser(parsing_table,start_state)


# In[162]:


parser(parsing_table,start_state)


# In[163]:


parser(parsing_table,start_state)


# In[ ]:




