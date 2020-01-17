# defining function

def loan_el_amt(salary,bonus,fd):
    'to calc loan amount'
    if salary>=20000:
        loan=salary*6
    else:
        loan=salary*4
    if bonus>=10000:
        loan+=bonus*3
    else:
        loan+=bonus*2
    loan+=fd*0.5
    return loan

# required arguments(positional order)

amt=loan_el_amt(25000,9000,70000)
print("Loan Amount %0.2f Rs" %amt)

# keyword argument/name of parameters
amt=loan_el_amt(bonus=12000,fd=40000,salary=16000)
print("loan upto %0.2f Rs"%amt)


# variable name argument

def game_score(team,*score):
    'to calc game score and centuries'
    sum=0
    century=0
    for run in score:
        sum+=run
        if run>=100:
            century+=1
    else:
        print("Score of %s is %d runs with %d centuries"%(team,sum,century))

# calling function

game_score("IND",65,110,55,105,45,50)
game_score("PAK",25,15,12)
game_score("ENG",45,24,65,115)

