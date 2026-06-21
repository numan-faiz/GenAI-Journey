# introduction to Naive Bayes
# =====================================================================
# Introduction to Naive Bayes Classifier
# =====================================================================

# 1. What is it?
# --------------
# - It is a supervised learning algorithm based on Bayes' Theorem.
# - Chiefly used for text classification (e.g., Spam Detection, Sentiment Analysis).

# 2. Why is it called 'NAIVE'?
# ----------------------------
# - Because it assumes that all features (columns) are completely 
#   independent of each other. (Features ka aapas me koi talluq nahi hai).

# 3. Mathematical Formula (Bayes' Theorem):
# ----------------------------------------
#   P(A|B) = [ P(B|A) * P(A) ] / P(B)
#
#   - P(A|B) -> Posterior Probability (Chance of event A happening given B has occurred)
#   - P(B|A) -> Likelihood (Chance of predictor B given class A)
#   - P(A)   -> Prior Probability of class A
#   - P(B)   -> Prior Probability of predictor B


# example:
# A=class label  (e.g)=spam or not spam
# B=observed features (e.g),=words in an email

# P(A)--->prior probability
# P(B|A)-->likelihood
# P(B)-->evidance
# the class with the highest posterioer probablity is predicted



# 4. Main Use-Cases:
# ------------------
# - Email Spam Filtering (Spam vs Ham)
# - Sentiment Analysis (Positive vs Negative reviews)
# - Document Classification

# =====================================================================
# Naive Bayes Classifier (Sabse Asan Notes)
# =====================================================================

# 1. BAYES (Probability/Record):
#    Purane data ka record dekh kar naye aane wale event ka andaza lagana.
#    Example: Agar email me 'Lottery' hai, toh purane record ke mutabiq 
#             yeh 90% Spam hogi.


# 2. NAIVE (Bholapan):
#    Yeh farz karta hai ke data ke saare features (words/columns) azaad hain.
#    Unka aapas me koi lena-dena ya rishta nahi hai.

# 3. Best Use-Case:
#    Text Classification (Spam vs Ham, Positive vs Negative Reviews).


# naive bayes is a probablistics classsification alogorithm base on bayes theorm
# it predicts the probablity that a  give instance belongs to a specific class or jiske probablity 
# zyada hoge usko consider kerlety hy 

# called "naive" bacuase ye kehta hy ke tama feature ju b input me hy wo ek dosry pe independent hy lekin hm kehty 
# kuch na kuch relate hta but ye kehta hy ke nahi hta bilkul
 
# commonly used in text classification,spam detection and sentiment analysis

# Advantages of Naive bayes:
# fast and efficient for large datasets
# perform well with small amount of data
# handles categorical and text dataq effectively


# limitaion of Naive bayes
# independence assumption is often unrealistic
# poor performnace with higly correlated features





