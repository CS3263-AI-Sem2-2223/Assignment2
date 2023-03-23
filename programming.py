from mylogic4e import *

# ====== Question 2.1 ======

clauses = []
clauses.append(expr("(Rover(x) & Sovenir(y) & Gives(x, y, z) & Nice(z)) ==> Legend(x)"))
clauses.append(expr("Friend(Green, Percey)"))
clauses.append(expr("Owns(Green, S1)"))
clauses.append(expr("Souvenir(S1)"))

'''---your codes start here---'''


'''----your codes end here----'''

print(clauses)

# ====== Question 2.2 ======

mars_kb = FolKB(clauses)

'''---your codes start here---'''


'''----your codes end here----'''