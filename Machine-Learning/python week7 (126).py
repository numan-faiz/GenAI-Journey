# Naive-Bayes--- types of model(Gaussian,multinomial,bernoulli)

# gaussian naive bayes:use for continous feature  and real numbers
# assunes feature follow a normal (gaussian) distribution


# =====================================================================
# Naive-Bayes--- Types of Models (Short & Simple Notes)
# =====================================================================

# 1. GaussianNB  alogirthm   -> For Continuous Data (Numbers/Decimals like Age, Salary)
#    Matlab: Data points decimal me hain aur Bell Curve banate hain.

# ==================================================================================
# GAUSSIAN NAIVE BAYES ASSUMPTION: LINE-BY-LINE NICHOR
# ==================================================================================

# LINE 1:
# gaussian naive bayes: use for continuous feature and real numbers
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Yeh model tab use hota hai jab aapka data point yaani decimals me ho. 
# Jaise: Blood Pressure (120.5), Temperature (37.2), ya Tumor Size (14.23). 
# Agar data text (words) nahi hai aur continuous numbers hain, toh Gaussian lagega.


# LINE 2:
# assumes feature follow a normal (gaussian) distribution
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Yeh algorithm dimaag me pehle se farz (assume) kar leta hai ke aapka data ek 
# khaas shape me bikhra hua hai, jise hum "Bell Curve" (Normal Distribution) kehte hain.
# Is curve ka ek beech ka center hota hai jise Mean (nb.theta_) kehte hain, aur 
# dono taraf data barabar phaila hota hai jise Variance (nb.var_) kehte hain.


# ----------------------------------------------------------------------------------
# THE MATHEMATICAL FORMULA (Piche chalne wali asli math):
# ----------------------------------------------------------------------------------
# P(xi | y) = (1 / sqrt(2 * pi * var)) * exp( -(x - mu)^2 / (2 * var) )
#
# -> mu  (Mean)     = Bell curve ka bilkul beech wala hissa (nb.theta_).
# -> var (Variance) = Bell curve ki chaudai ya bikhrao (nb.var_).
# -> x   (Sawaal)   = Woh naya number jo hum check kar rahe hain.
# ==================================================================================





# 2. MultinomialNB algorithm-> For Discrete Data (Word Counts/Frequencies in Text)
#    Matlab: Lafz kitni dafa (count) aaya hai, uspar faisla karna.
# used for discrete count features
# common in text classification and sentiment analysis
# suitable for baf-of-words and TF-IDF feature represenataion

# ==================================================================================
# MULTINOMIAL NAIVE BAYES: LINE-BY-LINE NICHOR & FORMULA
# ==================================================================================

# LINE 1 & 2:
# 2. MultinomialNB algorithm-> For Discrete Data (Word Counts/Frequencies in Text)
#    Matlab: Lafz kitni dafa (count) aaya hai, uspar faisla karna.
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# "Discrete Data" ka matlab hai ginti wale numbers (jaise 0, 1, 2, 5, 10). 
# Yeh model decimals (point wale numbers) par kaam nahi karta. Iska poora faisla 
# is baat par hota hai ke ek lafz pure document ya email me kitni dafa (count) aaya hai.


# LINE 3 & 4:
# used for discrete count features
# common in text classification and sentiment analysis
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Jab bhi aapko text par kaam karna ho—jaise email ko "Spam ya Ham" pehchanna ho, 
# ya kisi customer ke review ko parh kar "Sentiment Analysis" karna ho ke woh khush 
# hai (Positive) ya gussa hai (Negative)—toh wahan MultinomialNB sabse best hota hai.


# LINE 5:
# suitable for bag-of-words and TF-IDF feature representation
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Computer ko direct text (words) samajh nahi aate. Isliye hum text ko numbers me 
# badalte hain. 
# 1. Bag-of-Words (CountVectorizer): Yeh har lafz ki simple ginti (counts) likhta hai.
# 2. TF-IDF: Yeh lafz ki ginti ke sath-sath uski ahmiyat (importance) ka score likhta hai.
# Kyunki yeh dono methods hume ginti ya frequencies dete hain, isliye yeh Multinomial 
# ke liye bilkul perfect fit hain.


# ----------------------------------------------------------------------------------
# THE MATHEMATICAL FORMULA (Piche chalne wali asli math):
# ----------------------------------------------------------------------------------
#                N_yi + alpha
#   P(xi | y) = -----------------
#                N_y + alpha * n
#
# LaTeX Style: P(x_i \mid y) = \frac{N_{yi} + \alpha}{N_y + \alpha n}
#
# -> P(xi | y) : Kisi khaas class 'y' (jaise Spam) me lafz 'xi' ke aane ka chance.
# -> N_yi      : Class 'y' ke saare data me yeh lafz 'xi' total kitni dafa aaya hai.
# -> N_y       : Class 'y' ke andar maujood saare lafzon ki kul ginti (Total words).
# -> alpha     : Laplace Smoothing (Hamesha 1.0 rakhte hain) taake agar koi naya lafz 
#                aaye toh probability 0 na ho jaye, warna poora formula multiply hokar 0 ho jayega.
# -> n         : Pure dataset me total unique (alag-alag) lafzon ki ginti.
# ==================================================================================




# 3. BernoulliNB   algorithm-> For Binary Data (Yes/No, 1/0, Presence/Absence)
#    Matlab: Lafz kitni dafa aaya farq nahi parta, bas lafz "hai ya nahi".
#  used for binary features(presence or absence)

#  example:whether a word appear(1) or not in an email


# model selection in naive bayes:
# continous data--->Gaussian NB
# count data--->multinomial NB
# binary data--->bernouli NB


# demonstration of three naive bayes model
from sklearn.datasets import load_breast_cancer,make_classification
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB,MultinomialNB,BernoulliNB
from sklearn.metrics import accuracy_score



# 1--Gaussian naive bayes---continuos data

x_g,y_g=load_breast_cancer(return_X_y=True)
x_tr,x_te,y_tr,y_te=train_test_split(
    x_g,y_g,test_size=0.25,random_state=42
)

g_nb=GaussianNB()
g_nb.fit(x_tr,y_tr)
acc_g=accuracy_score(y_te,g_nb.predict(x_te))
print(acc_g)


# 2)multinomial naive bayes-->text/count data:
texts=[
    "buy cheap medicine for free",
    "win a free prize",
    "meeting sceduled confrimed",
    "project deadline tommorrow,we must do this",
    "limited time offer to win a prize",
    "let us discuss the report at your free schedule"
]

labels=[1,1,0,0,1,0]   #1=spam 0=not spam

vectorizer=CountVectorizer()
x_text=vectorizer.fit_transform(texts)
x_tr,x_te,y_tr,y_te=train_test_split(
    x_text,labels,test_size=0.33,random_state=42
)

m_nb=MultinomialNB()
m_nb.fit(x_tr,y_tr)
acc_m=accuracy_score(y_te,m_nb.predict(x_te))
print(acc_m)



# bernauli naive bayes-->binary features
x_b,y_b=make_classification(
    n_samples=200,n_features=10,n_informative=5,n_redundant=0,random_state=42
)
x_tr,x_te,y_tr,y_te=train_test_split(
    x_g,y_g,test_size=0.25,random_state=42
)

b_nb=BernoulliNB()
b_nb.fit(x_tr,y_tr)
acc_b=accuracy_score(y_te,b_nb.predict(x_te))



# results

print("model performance")
print(f"Gaussian NB accuracy:{acc_g:.3f}")
print(f"multinomial NB accuracy:{acc_m:.3f}")
print(f"Bernoulli NB accuracy:{acc_b:.3f}")