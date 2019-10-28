#limiting condition
coarsemin=900
coarsemax=1200
b0= coarsemax- coarsemin

agstonemin=0
agstonemax=90
b1=agstonemax-agstonemin

water_reducermin=3
water_reducermax=15
b2=water_reducermax-water_reducermin
'''膨胀剂
swellermin=0
swellermax=43
b4=swellermax-swellermin
'''
fine_aggregatemin=150
fine_aggregatemax=970
b3=fine_aggregatemax-fine_aggregatemin

flyashmin=0
flyashmax=90
b4=flyashmax-flyashmin

cementmin=160
cementmax=513
b5=cementmax-cementmin

watermin=120
watermax=176
b6=watermax-watermin

# #relational condition
# def design(a,b):
#   if a>60:
#     Fcu=1.15*a
#   if 50<=a<=60:
#     Fcu=a+1.645*6
#   if 25<=a<50:
#     Fcu=a+1.645*5
#   if a<25:
#     Fcu=a+1.645*4



