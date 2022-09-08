import math

# The Project Euler Problem this is based on says the adjecent 13 digits instead of seven.
# I've changed it to that here, but in case you have your own answer key, I'll mark
# where you can change the loop amounts to get 7 digits instead.

a = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
aStr = str(a)

workingNums = []
products = []

for index, num in enumerate(aStr):
  selectIndex = index

  # change to: for _ in range(0, 7):
  
  for _ in range(0, 13):
    try:
      workingNums.append(int(aStr[selectIndex]))
      selectIndex += 1
    except IndexError:
      break
  products.append(math.prod(workingNums))
  workingNums.clear()

print(products)
maxProductIndex = 0
maxProduct = 0

for index, product in enumerate(products):
  if product > maxProduct:
    maxProduct = product
    maxProductIndex = index
  else:
    continue

selectIndex = maxProductIndex

# change to: for _ range(0, 13):

for _ in range(0, 13):
  workingNums.append(int(aStr[selectIndex]))
  selectIndex += 1
  
print("")

print("Max Product: " + str(maxProduct))
print("Max Product Index: " + str(maxProductIndex))
print("Max Product Numbers: " + str(workingNums))