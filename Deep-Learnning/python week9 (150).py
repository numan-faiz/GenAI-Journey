# ANN--model validatiion:

# why model validation:
# model genarlize well to unseen data
# avoids overfitting and underfitting
# reliable comparison between models

# goal:
# trustworthy performance estimation


# hmry mind me hta ke hmny kahi bias data mtlb ek taraha
# ka data trainingor ek taraha ka data testing me nhi daldeya kahi isko door kerny ke liye hm use 
# kerty cross validation technique ok


# cross validation:
# training multiple models  on diffrent data splits
# provides more stable and reliable performance measure
# uses data efficeintly especially when limited

# K-fold cross-validation:
# dataset split into K equal parts
# train on k-1 folds
# test on 1 fold
# repeat K times
# average acuuracy

# signifinace testing:
# used to judge if model improvement is statistically meaningfull or not random chance
# two models may differ slighlty in accuracy
# we test whether diffrence is statiscally significant


# common tests:
# paired t-test
# wilcoxon signed-rank test
# mcnemar,s test (for classification outputs)

# paired t-test:
# datatype: continuos (interval or ratio)
# requirements: the difference between pairs must follow a normal distribution
# usage:comparing means before/after treatment (e.h. blood presuure)


# wilcoxon signed-rank test:(non parametric)
# datatype: ordinal or non-normal continuous data
# requirements: does not assume normality; uses ranks of differences
# usage: comparing medians of paired skewed data or ranked scores



# mcnemar,s test (for classification outputs)(non parametric):
# datatype:
# binary(categorical) data (e.g yes no,pass fail)

# requirements:
# specifically tests for changes in proportions in 2*2 contigency tables:
# usage:
# comparing proportions in paired ,categorical or longitudinal studies

# example:
# model A acuuracy:91.2%
# model B accuracy:92.0%

# small diffrence is b really better?
# perform t-test on fold-wise accuracies
# if p-value<0.05-->difference likely due to chance
# if less then significnat

# idea:
# sum of sqaured distance is called inertia

# keytakaways:
# cross validation prevents misleading evaluation
# k-fold cv=standard method for model robustness
# reliable comparison between models

# remeber:better validation=better AI models


# ==================================================================================
# ANN--MODEL VALIDATION: COMPLETE NOTES WITH LINE-BY-LINE EXPLANATIONS
# ==================================================================================

# ----------------------------------------------------------------------------------
# Why Model Validation?
# ----------------------------------------------------------------------------------
# - Model generalize well to unseen data
# ----------------------------------------------------------------------------------
# EXPLANATION: Validation ka asal maqsad yeh check karna hai ke model naye anjan data 
# (unseen data) par sahi perform kar pa raha hai ya nahi (Generalization).
# ----------------------------------------------------------------------------------
# - Avoids overfitting and underfitting
# ----------------------------------------------------------------------------------
# EXPLANATION: Yeh check karta hai ke kahin model ne ratta toh nahi mara (Overfitting) 
# ya kahin model bilkul nalaik toh nahi reh gaya (Underfitting).
# ----------------------------------------------------------------------------------
# - Reliable comparison between models
# ----------------------------------------------------------------------------------
# EXPLANATION: Iski madad se hum do ya do se zyada alag models ke darmiyan ek sacha 
# aur bharosay-mand muqabla (comparison) kar sakte hain.


# ----------------------------------------------------------------------------------
# Goal: Trustworthy performance estimation
# ----------------------------------------------------------------------------------
# EXPLANATION: Asal target yeh hai ke model ka jo bhi accuracy score aaye, us par hum 
# aankhein band kar ke bharosa (trust) kar sakein.


# ----------------------------------------------------------------------------------
# URDU CONCEPT BLOCK: Bias Data Problem
# ----------------------------------------------------------------------------------
# "Hamare dimaag me aata hai ke kahin humne bias data (matlab ek tarah ka data) 
# training me aur doosri tarah ka data testing me toh nahi daal diya? Is maslay ko 
# door karne ke liye hum Cross Validation technique use karte hain."
# ----------------------------------------------------------------------------------
# EXPLANATION: Agar sara aasan data training me chala jaye aur mushkil data testing me, 
# toh evaluation kharab ho jayegi. Cross Validation data ko har tarah se ghuma-phira 
# kar check karti hai taake yeh bias khatam ho jaye.


# ----------------------------------------------------------------------------------
# Cross Validation
# ----------------------------------------------------------------------------------
# - Training multiple models on different data splits
# ----------------------------------------------------------------------------------
# EXPLANATION: Hum data ke alag alag tukre (splits) karte hain aur baar baar naye 
# tareeqe se models ko train kar ke check karte hain.
# ----------------------------------------------------------------------------------
# - Provides more stable and reliable performance measure
# ----------------------------------------------------------------------------------
# EXPLANATION: Isse milne wala accuracy score zyada pakka (stable) aur sach batane 
# wala hota hai.
# ----------------------------------------------------------------------------------
# - Uses data efficiently especially when limited
# ----------------------------------------------------------------------------------
# EXPLANATION: Agar aapke paas dataset chota (limited) hai, toh yeh technique poore 
# data ka ek ek qatra sahi tarah se istemal (efficient use) kar leti hai.

# ----------------------------------------------------------------------------------
# K-Fold Cross-Validation (Sabse Standard Tareeqa)
# ----------------------------------------------------------------------------------
# - Dataset split into K equal parts
# ----------------------------------------------------------------------------------
# EXPLANATION: Hum poore data ko 'K' (jaise 5 ya 10) barabar hisson me baant dete hain, 
# jinhe 'Folds' kehte hain.
# ----------------------------------------------------------------------------------
# - Train on k-1 folds / Test on 1 fold
# ----------------------------------------------------------------------------------
# EXPLANATION: Agar K=5 hai, toh 4 hisson par model parhai (Train) karega aur bache 
# hue 1 hissay par imtihan (Test) dega.
# ----------------------------------------------------------------------------------
# - Repeat K times
# ----------------------------------------------------------------------------------
# EXPLANATION: Yeh process K martaba chalega, aur har dafa imtihan wala hissa badal 
# diya jayega taake har hissay par testing ho sake.
# ----------------------------------------------------------------------------------
# - Average accuracy
# ----------------------------------------------------------------------------------
# EXPLANATION: Aakhir me un saari baro (K times) ki accuracy nikaal kar unka 
# darmayana (Average) score nikal lete hain.


# ----------------------------------------------------------------------------------
# Significance Testing (Sacha Muqabla)
# ----------------------------------------------------------------------------------
# - Used to judge if model improvement is statistically meaningful or not random chance
# ----------------------------------------------------------------------------------
# EXPLANATION: Yeh check karne ke liye use hota hai ke agar ek model doosre se thoda 
# behtar hai, toh kya woh sach me powerful hai ya sirf luck/tuke (random chance) ki 
# wajah se jeet gaya.
# ----------------------------------------------------------------------------------
# - Two models may differ slightly in accuracy / Test whether difference is statistically significant
# ----------------------------------------------------------------------------------
# EXPLANATION: Do models ki accuracy me 0.5% ka farq ho sakta hai. Hum maths lagakar 
# test karte hain ke kya yeh farq sach me maani rakhta (statistically significant) 
# hai ya nahi.


# ----------------------------------------------------------------------------------
# Common Statistical Tests:
# ----------------------------------------------------------------------------------
# 1. Paired t-test:
#    - Datatype: Continuous (Interval or ratio)
#    - Requirements: The difference between pairs must follow a normal distribution
#    - Usage: Comparing means before/after treatment (e.g., blood pressure)
# ----------------------------------------------------------------------------------
# EXPLANATION: Jab data points points me hon (continuous) aur dono ka farq normal 
# bell-curve (normal distribution) banata ho. Misaal: Dawai khane se pehle aur baad 
# ka Blood Pressure naapna.
# ----------------------------------------------------------------------------------
# 2. Wilcoxon signed-rank test (Non-Parametric):
#    - Datatype: Ordinal or non-normal continuous data
#    - Requirements: Does not assume normality; uses ranks of differences
#    - Usage: Comparing medians of paired skewed data or ranked scores
# ----------------------------------------------------------------------------------
# EXPLANATION: Yeh tab lagta hai jab data normal distribution na bana raha ho (skewed ho) 
# ya data ranks (1st, 2nd, 3rd) me ho. Yeh actual values ke bajaye unke Ranks par 
# kaam karta hai.
# ----------------------------------------------------------------------------------
# 3. McNemar's test (For classification outputs) (Non-Parametric):
#    - Datatype: Binary (Categorical) data (e.g., Yes/No, Pass/Fail)
#    - Requirements: Specifically tests for changes in proportions in 2*2 contingency tables
#    - Usage: Comparing proportions in paired, categorical or longitudinal studies
# ----------------------------------------------------------------------------------
# EXPLANATION: Yeh sirf Classification models ke liye hai, jahan jawab "Sahi/Ghalat" 
# ya "0/1" (Binary) ho. Yeh ek table (2*2 Contingency table) bana kar dono models ke 
# ghalat aur sahi faislon ka direct ratio check karta hai.

# ----------------------------------------------------------------------------------
# NUMERICAL EXAMPLE ANALYSIS
# ----------------------------------------------------------------------------------
# Model A Accuracy: 91.2%
# Model B Accuracy: 92.0%
# Question: Small difference, is B really better?
# 
# Action: Perform t-test on fold-wise accuracies
# - If p-value >= 0.05 --> Difference likely due to chance (Luck / Tuka)
# - If p-value < 0.05  --> Difference is Statistically Significant (B is truly better!)
# ----------------------------------------------------------------------------------
# EXPLANATION: Dono me sirf 0.8% ka farq hai. Hum K-Fold ki har fold ki accuracy 
# par t-test lagate hain. Agar p-value 0.05 se choti aayi, toh iska matlab B kismat 
# se nahi balke apni performance ki wajah se jeeta hai.


# ----------------------------------------------------------------------------------
# Idea: Sum of squared distance is called Inertia
# ----------------------------------------------------------------------------------
# EXPLANATION: Clustering (jaise K-Means) me, points ka unke center (centroid) se 
# jo squared distance hota hai, uske kul jama (sum) ko hum Inertia kehte hain. 
# Jitna kam inertia, utne ache clusters.


# ----------------------------------------------------------------------------------
# Key Takeaways:
# ----------------------------------------------------------------------------------
# - Cross validation prevents misleading evaluation
# ----------------------------------------------------------------------------------
# EXPLANATION: Cross validation humein dhoke wali accuracy se bachati hai.
# ----------------------------------------------------------------------------------
# - K-fold cv = standard method for model robustness
# ----------------------------------------------------------------------------------
# EXPLANATION: K-Fold industry ka sabse top aur standard tareeqa hai model ki mazbooti 
# check karne ka.
# ----------------------------------------------------------------------------------
# - Reliable comparison between models / Better validation = better AI models
# ----------------------------------------------------------------------------------
# EXPLANATION: Jab validation solid hogi, toh banne wala AI model bhi real world me 
# super hit hoga.
# ==================================================================================





































































