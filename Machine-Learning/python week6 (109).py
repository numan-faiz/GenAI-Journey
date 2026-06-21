# introduction to random forest:
# "Random Forest boht saare Decision Trees (darakhton) ka ek jangal (Forest) hota hai. Ye Ensemble 
#  ki technique par kaam karta hai."
# ensemble learning-->bht saray weak clasifier ko mila ke ek strong classifier banaty

# random forest is an ensemble learning method that combines multiple decison trees to improve predictive performance
# instead of relying on a single tree, random forest builds many trees and aggregates their predictions to reduce overfitting


# application of random forest
# spam detection
# medical diagnosis(classification)
# house price predictions
# stock forecasting (regression)

# Advantages of random forest
# reduce overfitting using multipl decision tree
# imporve accuracy
# robustness-->error negligible
# handle large/hight duimentional dataset


# how random forest work
# bootstrap sampling-->
# "Original dataset me se rows ko random tareeqe se chunna, jisme ek hi row baar baar"
# " (with replacement) bhi select ho sakti hai, taake har Decision Tree ko ek alag aur naya sub-dataset mile."

# 🛠️ Example se Samjho:
# Agar original data me 4 rows hain: [A, B, C, D]
# To Bootstrap sample random tareeqe se aisy banenge:

# Tree 1 ka data: [A, B, B, D] (B do dafa aa gaya, C miss ho gaya)

# Tree 2 ka data: [C, A, D, C] (C do dafa aa gaya, B miss ho gaya)

# Is random sampling ka faida ye hota hai ke saare Decision Trees bilkul aik jaisa ratta nahi 
# maarte, jis se model me Overfitting khatam ho jati hai.

# random feature selection

# "Decision Tree banate hue, har split (node) par saare columns (features) check karne ke bajaye, sirf kuch"
# " random columns ko chunna aur unme se best column par data ko split karna."

# 🛠️ Example se Samjho:
# Farz karo tumhare data me total 10 columns hain.

# Normal Decision Tree kya karta hai: Wo har node par khara ho kar saare 10 ke 10 columns check karta 
# hai ke sabse behtar split kaun dega. Isse har dafa wahi dominant column select hota hai aur saare trees 
# ek jaise banne lagte hain.

# Random Forest (Random Feature Selection) kya karta hai: Wo har split par hukum deta hai ke "In 10 "
# "me se koi bhi 3 columns randomly uthao (jaise Column 2, 5, 8)". Ab tree majbooran sirf unhi 3 columns 
# me se best chun kar split karega. Agle node par 3 naye random columns select honge!

# 🎯 Iska Asli Faida Kya Hai?
# De-correlation (Trees ko alag banana): Agar data me koi ek column boht strong hai, to normal 
# tree hamesha usi ko use karega. Random feature selection se baqi kamzor columns ko bhi mauqa milta 
# hai, jisse har tree bilkul alag dimaag ka banta hai.

# Overfitting Khatam: Jab boht saare alag alag dimaag wale trees mil kar vote karte hain, to overfitting
# bilkul tabah ho jati hai.


# multiple treesgrwon independently , and predictions are aggregated


# advnatgaes-->
# high accuracy-->aggregation of multiple trees improve predictive power
# robustness-->resistant to t overfitting due to averaging accross trees
# can handle missing data and provide into feature importance
# woek for both classification and regression task:bar char can visulaize improtance  
