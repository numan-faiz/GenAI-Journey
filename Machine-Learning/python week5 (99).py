# linear regression-gradient descent optimization
# Gradient Descent ek optimization algorithm hai jiska kaam Cost Function (MSE) ko kam se kam (minimize) 
# karna hota hai taake model ki predictions sab se behtar ho sakein.
# 
# gradient descent optimization is used to minimize the errors

# what is gradeint?
# a gradeint is a fucntion that increase or decrease its value gradually
# what is descent?
# mean to move downward

# what gradient decent mean?
# gradually moving downward at varying speeds to minmize a function

# gradeint decent is an optimization method used to minmize the cost function



# how it works
# start with random values for m & b
# update step by step
# m=m - learnining rate*gradeint

# repeat until the cost function minimized

# urdu me


# Yeh Kaam Kaise Karta Hai? (Step-by-Step):
# 1.Random Start: Algorithm line ke weights (\(m\)) aur bias (\(c\)) ki koi bhi random value chun kar kaam shuru karta hai.
# 2.Calculate Gradient: Yeh check karta hai ke slope (gradient) kis taraf neeche ja raha hai (yaani error
#  kis taraf kam ho raha hai).
# 3.Take a Step: Yeh error ko kam karne ke liye sahi taraf ek chota kadam (step) leta hai. Is step ke size ko Learning Rate
#  (\(\alpha \)) kehte hain.
# 4.Repeat: Yeh tab tak chote chote kadam leta rehta hai jab tak yeh sab se neeche yaani Global Minima (zero ya sab se kam error) 
# par na pahonch jaye.


# too small learning rate-> slow learning result will be best but too much time consume
# too large learning --> overshooting may not converge
# maintain optiomal learning rate
# use adaptive learning rate if needed
# Adaptive learning rate linear regression me aik aisi technique hai jahan model training ke doran error ke mutabiq
#  apna learning rate khud hi chota ya bara karta rehta hai taake
#  optimal solution jaldi aur sahi mil sakay.


