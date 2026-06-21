# introduction to k-means clustering

# its unsupervised(clustering) data input avaialbe and output not
#  clustering meei bghr dekhy output data opoint taqseeem kerna yani cluster kerna ok

# unsupervised learning used for:
# customer segmentation for targeted marketting
# grouping in unsupervied learning is not labeled as right or wrong

# example :
# detect fraudelent bank trasacation

# grouping similar news articles or images

# recommendation products based on brwosing behaviour

# evaluation of unsupervised learning:
# evaluation for cluster analysis:

1# within-cluster distance--points ke bech distnace
# between-cluster distance-->distnace km utna distnace



# Algorithms in unsupervied learnning:
# k-mean is unsupervised learnning algorithm used to group data points into k cluster
# each cluster has centrioid representing the means of its data points

# goal of k-means:group similar data points into a single cluster and positio them around a centriod

# how k-means works:
# initalize k cluster cetrioids randomly
# asighn each data point to the nearest centriod (using euclidean distance)
# recalculate centroids as the mean of all points in each cluster
# repeat assighment and update steps until cluster stablize

# crtiria to finalize clusters:
# run clustering for a maximum number of iteration and output the resulting clusters
# monitor centriod movements
# if centriods shift but data points stay in their original cluster ,clustering is stable


# key characteristics of k-means clustering:
# unsupervised
# iterative refinement algorithm
# sensitive to initial centriod positions
# fast and scalable for large datasets

# ==================================================================================
# INTRODUCTION TO K-MEANS CLUSTERING: LINE-BY-LINE NICHOR
# ==================================================================================

# LINE 1:
# introduction to k-means clustering
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Hum Machine Learning ka ek naya hissa shuru kar rahe hain jise Unsupervised Learning 
# ya "Clustering" kehte hain. K-Means iska sabse pehla aur mashhoor algorithm hai.


# LINE 2 & 3:
# its unsupervised(clustering) data input available and output not
# clustering meei bghr dekhy output data opoint taqseeem kerna yani cluster kerna ok
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Supervised me hum computer ko data (X) aur answer (y) dono dete the. 
# Unsupervised me hum computer ko sirf data (X) dete hain, answer (y) YAANI LABELS NAHI DETE!
# Computer bina koi answer dekhe, khud se data points ki shakal aur unka aapas ka 
# fasla dekh kar unko alag-alag dhabon (Clusters/Groups) me taqseem karta hai.


# ==================================================================================
# UNSUPERVISED LEARNING USED FOR (Yeh kahan kaam aata hai?):
# ==================================================================================

# LINE 4:
# customer segmentation for targeted marketing
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Dukandari me customers ko alag karna. Jaise computer khud hi ameer customers ko 
# alag group me daal de aur kanjoos customers ko alag group me, taake unko unke 
# mutabiq discounts dikhaye ja skein.


# LINE 5:
# grouping in unsupervised learning is not labeled as right or wrong
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Isme koi "Sahi" ya "Ghalat" jawab nahi hota. Kyunki computer ke paas koi master key 
# (labels) nahi hoti, woh bas apni samajh se group banata hai. Aap yeh nahi keh sakte 
# ke group galat bana hai, bas woh data ki similarity par banta hai.


# LINE 6 & 7:
# example : detect fraudulent bank transaction
# grouping similar news articles or images
# recommendation products based on browsing behaviour
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Real Life Use Cases:
# 1. Fraud Detection: Dhoke wali bank transactions ko aam transactions se alag thalag karna.
# 2. News/Images: Ek jaisi khabron ya tasveeron ko aapas me jor kar ek group banana.
# 3. Recommendations: Jo cheezein aap internet par dekhte hain, unke mutabiq aapko naye 
#    products suggest karna (jaise Netflix ya YouTube karta hai).


# ==================================================================================
# EVALUATION OF CLUSTER ANALYSIS (Group sahi bana ya nahi, kaise check karein?):
# ==================================================================================

# LINE 8 & 9:
# 1# within-cluster distance--points ke bech distance (Kam hona chahiye)
# 2# between-cluster distance-->distance zyada utna acha  (Zyada hona chahiye)
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# 1. Within-Cluster Distance: Ek hi group ke andar maujood points ka aapas ka fasla. 
#    Yeh fasla KAM SE KAM hona chahiye, yaani ek group ke log aapas me bilkul jure hon.
# 2. Between-Cluster Distance: Do alag-alag groups ke beech ka fasla. 
#    Yeh fasla ZYADA SE ZYADA hona chahiye, yaani dono groups ek dusre se door door hon.


# ==================================================================================
# ALGORITHMS & GOAL OF K-MEANS (K-Means Kaise Chalta Hai?):
# ==================================================================================

# LINE 10 & 11:
# k-mean is unsupervised learning algorithm used to group data points into k cluster
# each cluster has centroid representing the means of its data points
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# K-Means me "K" ka matlab hai "Groups ki ginti" (Jaise K=3 matlab 3 groups banane hain).
# Har group ka ek Boss (Center point) hota hai jise "Centroid" kehte hain. Yeh centroid 
# us group ke saare points ka Average (Mean) hota hai.


# LINE 12:
# goal of k-means: group similar data points into a single cluster and position them around a centroid
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# K-Means ka asli maqsad yeh hai ke ek jaise saare points ko ik इकट्ठा kare aur unko 
# unke Boss (Centroid) ke gerd (charo taraf) set kar de.


# ==================================================================================
# HOW K-MEANS WORKS (Kaam karne ka tarika - Step-by-Step):
# ==================================================================================

# LINE 13:
# initialize k cluster centroids randomly
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# STEP 1: Computer shuru me nakshe par kahin bhi randomly "K" tamatar (Centroids/Bosses) 
# phenk deta hai. Agar K=3 hai, toh 3 random centers ban jayeinge.

# LINE 14:
# assign each data point to the nearest centroid (using euclidean distance)
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# STEP 2: Har data point apna sabse kareeb wala center (Boss) dhoondta hai "Euclidean Distance" 
# (seedhi line wale fasle) ke zariye, aur us group ka hissa ban jata hai.

# LINE 15:
# recalculate centroids as the mean of all points in each cluster
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# STEP 3: Jab groups ban jaate hain, toh Boss (Centroid) apni jagah badalta hai. Woh apne 
# group ke saare points ka naya center (Average/Mean) nikal kar wahan shift ho jata hai.

# LINE 16:
# repeat assignment and update steps until cluster stabilize
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# STEP 4: Yeh points ka group badalna aur Boss ka apni jagah badalna tab tak baar baar 
# chalta rehta hai jab tak sab apni sahi jagah par pakke na ho jayein.


# ==================================================================================
# CRITERIA TO FINALIZE CLUSTERS (Kaam kab khatam hota hai?):
# ==================================================================================

# LINE 17 & 18 & 19:
# run clustering for a maximum number of iteration and output the resulting clusters
# monitor centroid movements
# if centroids shift but data points stay in their original cluster, clustering is stable
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Kaam khatam hone ki 3 nishaniyan hain:
# 1. Iterations khatam ho jayein (Jaise computer ne 100 dafa chakkar poora kar liya).
# 2. Centroids (Bosses) hilna band kar dein, yaani unki jagah pakki ho jaye.
# 3. Agar Centroids thoda boht hil bhi rahe hon, par koi data point apna group chodh kar 
#    dusre group me na ja raha ho—yaani bilkul sakoon (Stability) aa jaye.
# ==================================================================================

# ==================================================================================
# KEY CHARACTERISTICS OF K-MEANS CLUSTERING: LINE-BY-LINE NICHOR
# ==================================================================================

# LINE 1:
# # unsupervised
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Isme data ke sath koi target labels ya answers (y) nahi hote. Computer bina kisi 
# ustad ya bina kisi help ke, khud hi data ke andar patterns dhoond kar unke groups banata hai.


# LINE 2:
# # iterative refinement algorithm
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# "Iterative" ka matlab hai baar baar chalna, aur "Refinement" ka matlab hai behtar hona. 
# K-Means ek hi dafa me perfect group nahi banata. Woh baar baar chakkaron (loops) me 
# chalta hai, points ko sahi group me daalta hai aur har chakkar ke sath group ki 
# quality ko pehle se zyada saf aur behtar (refine) karta jata hai.


# LINE 3:
# # sensitive to initial centroid positions
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# Yeh K-Means ki sabse badi kamzori hai! Shuru me computer randomly nakshe par jo 
# Bosses (Centroids) phenkta hai, agar woh ghalat jagah par gir jayein, toh poora 
# group ghalat ya kharab ban sakta hai. Matlab shuruati positions par iska result 
# boht zyada depend karta hai.
# (Note: Is kamzori ko door karne ke liye hum 'k-means++' use karte hain).


# LINE 4:
# # fast and scalable for large datasets
# ----------------------------------------------------------------------------------
# EASY NICHOR: 
# K-Means algorithm boht zyada tez (fast) hai. Agar aapke paas lakhon rows ka boht 
# bada data (Large Dataset) bhi ho, toh yeh dunya ke baqi clustering algorithms ke 
# muqable me boht jaldi aur makkhan ki tarah apna kaam khatam kar leta hai.
# ==================================================================================

# ==================================================================================
# K-MEANS CLUSTERING: 5 LINES SUMMARY NICHOR
# ==================================================================================

# 1. K-Means ek Unsupervised Learning algorithm hai, jisme data ke sath koi target answer ya label (y) nahi hota.
# 2. Iska asli kaam "Ek jaisi cheezon ki alag-alag dheriyan yaani Groups (Clusters) banana" hota hai.
# 3. Formula me "K" ka matlab hai Groups ki ginti, aur "Means" ka matlab hai har group ka center point (Average).
# 4. Yeh har point ka fasla (Euclidean Distance) check karke, usay sabse kareeb wale group me daalta jata hai.
# 5. Yeh aam zindagi me Customers ki pehchan (Segmentation) aur Fraud pakadne ke liye sabse tez aur mashhoor algorithm hai.
# ==================================================================================