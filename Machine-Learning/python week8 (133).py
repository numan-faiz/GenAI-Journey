# Introduction to hierarchical cluster
# it is type of explainable AI
# hierarchical cluster is an unsupervised method that organizes data points into a hirarchy
#  of nested clusters
# does not require pre-specifying the number of clusters
# builds a tree-like structure (dendrogram) showing realtionships between points and clusters
# usefull for understanding natural in data and visualizing cluster hierarchy



# key characteritics of hierarchy
# produce a nested sequence of cluster from fine(data pure) to coarse(data impure) cluster

# two main types:
# Agglomerative(bottom-up)-->nechy sy satrt keerke root tak ana
# divisive (top-down)--->top-down-->hm rooot sy start kerty or leaf pe ajaty hy 

# efficient for small to medium size-datasets
# sensitive to distance metrics and linkage critira for manhataan diffrent tree and for euclidean dffrent tree

# Advantages of hierarchical clustering:
# does not require specifying k upfront
# provides visual represntaion via dengogram
# flexible choice of distnace and linkage method

# application of hierarchical clustering:
# gene expresiion analysis
# customer segemenation
# documents clustering--if we have huge nuber of documents and to divide it used cluster hirachical



# ==================================================================================
# HIERARCHICAL CLUSTERING: SAPSE ASAAN ROMAN URDU NICHOR
# ==================================================================================

# ----------------------------------------------------------------------------------
# 1. INTRODUCTION (Yeh Kya Bala Hai?)
# ----------------------------------------------------------------------------------
# - Unsupervised Method: K-Means ki tarah isme bhi pehle se labels ya answers nahi hote.
# - Hierarchy (Shajra-e-Nasab): Yeh data points ko ek Shajre ya Tree (Darakht) ki tarah 
#   groups ke andar naye groups bana kar jorhta hai.
# - No "K" Needed: Isme pehle se computer ko nahi batana parta ke 3 groups banao ya 4.
# - Dendrogram (Khandan ka Naksha): Yeh ek tree jaisa graph banata hai, jise Dendrogram 
#   kehte hain. Isay dekh kar saaf pata chalta hai ke kaun sa point kiske sabse kareeb hai.
# - Explainable AI: Kyunki iska graph (Dendrogram) sab kuch khol kar dikha deta hai ke 
#   groups kaise bane, isiliye isay "Explainable AI" ka hissa maana jata hai.


# ----------------------------------------------------------------------------------
# 2. TWO MAIN TYPES (Dono Qismein - Neeche se Upar ya Upar se Neeche)
# ----------------------------------------------------------------------------------
# A. Agglomerative (Bottom-Up): 
#    - Shuruat me har point apna ek alag group (cluster) hota hai.
#    - Phir computer do sabse kareeb wale points ko jorhta hai, phir unke sath teesre ko... 
#    - Aise neeche se shuru ho kar upar ki taraf aate hain aur aakhir me ek bada group (Root) ban jata hai.
#
# B. Divisive (Top-Down):
#    - Bilkul iska ulta! Shuruat me saara data ek hi bade group (Root) me hota hai.
#    - Phir computer us bade group ko torta jata hai, torta jata hai... 
#    - Aakhir me har banda (Leaf) bilkul akela alag group ban jata hai.


# ----------------------------------------------------------------------------------
# 3. ADVANTAGES & CHARACTERISTICS (Khubiyan Aur Asar)
# ----------------------------------------------------------------------------------
# - No K Upfront: K-Means ki tarah Elbow method ke chakkar me padne ki zaroorat nahi.
# - Sensitive to Distance & Linkage: Yeh is baat par boht ghaur karta hai ke aap fasla 
#   kaise naap rahe hain. Agar Manhattan distance use karenge toh alag tree banega, 
#   agar Euclidean use karenge toh alag tree banega.
# - Small Datasets: Yeh sirf chote aur medium data ke liye fit hai, boht bade data par 
#   yeh thak jata hai (slow ho jata hai).


# ----------------------------------------------------------------------------------
# 4. APPLICATIONS (Yeh Kahan Kahan Kaam Aata Hai?)
# ----------------------------------------------------------------------------------
# - Gene Expression: Biology me DNA aur genes ke khandan ka pata lagane ke liye.
# - Customer Segmentation: Ameer, garib ya medium customers ke naye groups dhoondne ke liye.
# - Document Clustering: Agar hazaron files ya documents hain, toh unko unke topic ke 
#   mutabiq alag-alag dheriyan banane ke liye.
# ==================================================================================