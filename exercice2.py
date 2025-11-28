import numpy as np

# Création d'un tableau en initialisant les valeurs à 0 et en type bouléen
grid = np.zeros((1000,1000), dtype=int)


# execution des exercices
grid[887:959+1,9:629+1] +=1
grid[454:844+1,398:448+1] += 1
grid[539:559+1,243:965+1] -= 1
grid[grid < 0] = 0
grid[370:676+1,819:868+1] -= 1
grid[grid < 0] = 0
grid[145:370+1,40:997+1] -= 1
grid[grid < 0] = 0
grid[301:808+1,3:453+1] -= 1
grid[grid < 0] = 0
grid[351:951+1,678:908+1] +=1
# Changer le true en false ou inversement
grid[720:897+1,196:994+1] +=2
grid[831:904+1,394:860+1] +=2
total = np.sum(grid)
print(total)

