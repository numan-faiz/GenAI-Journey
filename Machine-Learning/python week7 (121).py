# K-NN---Distance Metrics


# k-nn heavily relies on proximity to neighbors for predictions prefferd neoghbors

# how to calculate knn value:
# Euclidean distance:

# Sir, Euclidean Distance darasul KNN (K-Nearest Neighbors) ka "Asli Dimaag" hai. Isi formula ki 
# wajah se KNN ko pata chalta hai ke kaunsa padosi  (data point) paas hai aur kaunsa door hai.
# sensitive to scale so we have normalize the data
# use--case:continous numerical features like heigh weigh test score.

#                     n  l  l
# formula=d(i,j) = √ ∑ (x - x)² 
#                    l=1 i   j

# Short Meaning of Each Term:
# ---------------------------------------------------------------------
# d(i,j)      -> New point 'i' aur Old point 'j' ke beech ka total fasla.
# √           -> Square Root (Sab kuch plus karne ke baad aakhri underroot).
# ∑ (l=1 to n)-> Summation (Pehle feature se lekar n-th feature tak sabko jama karna).
# x_il        -> Point 'i' ka l-th feature (column).
# x_jl        -> Point 'j' ka l-th feature (column).
# ²           -> Square (Minus sign khatam karne aur bade farq ko highlight karne ke liye).



# manhattan distnace:
# 🎯 Manhattan Distance Kya Hai? (Taxi/Grid Distance)
# Euclidean distance me hum do points ke beech me bilkul seedhi line (Shortest Path) khinch kar fasla napte 
# hain. Lekin Manhattan distance me seedhi line lagane ki ijazat nahi hoti!

# Isko "Taxi Cab Distance" bhi kehte hain. Farz karein aap ek sheher (jaise New York ya Manhattan) me
# hain jahan boht saari imaratein aur blocks bane hue hain. Ek taxi seedha 
# imaraton ke upar se urr kar nahi ja sakti, usay hamesha sadko par horizontal (daayein-baayein) aur 
# vertical (upar-neeche) ghoom kar hi jana padega.

# 📉 ML Graph Par Yeh Kaise Kaam Karta Hai?
# Manhattan distance me hum dono points ke features ka sirf aamne-saamne ka farq (absolute difference)
# nikal kar unhein aapas me jama (add) kar dete hain. Isme koi square ya underroot nahi hota.


# =====================================================================
# KNN---Manhattan Distance Mathematical Formula
# =====================================================================

#               n
# d(i,j) =     ∑  |x_il - x_jl|
#              l=1

# ---------------------------------------------------------------------
# Short Meaning of Each Term:
# ---------------------------------------------------------------------
# d(i,j)      -> New point 'i' aur Old point 'j' ke beech ka Manhattan distance.
# ∑ (l=1 to n)-> Summation (Pehle feature se lekar n-th feature tak sabko jama karna).
# |x_il - x_jl|-> Absolute difference (Minus ka sign khatam karke absolute farq nikalna).
#
# NOTE: Isme koi Square (²) ya Underroot (√) nahi hota!



# measure distance along axes (like taxi driving in a grid)
# less sensitive to outliers than euclidean distance;good for discrete feature


# minkowski distance:
# generalize distance metric;include euclidean and manhtaan as special cases

# Sir, Minkowski Distance darasul KNN (K-Nearest Neighbors) ka ek "Ustad Formula" (Master Formula) hai.

# Yeh koi alag se naya formula nahi hai, balki yeh ek aisa generalized formula hai jo Euclidean Distance
# aur Manhattan Distance dono ko apne andar chupa kar baitha hai. Iska matlab hai ke agar aapke paas
# Minkowski distance ka formula hai, toh aap isi ek formula se Euclidean bhi nikal sakte ho aur Manhattan bhi!

# 🌟 Minkowski Kya Hai? (Ek "Universal Remote" Wali Misal)Farz karo aapke ghar me do alag-alag companies ke
# AC lage hain—ek Dawlance ka hai aur ek Haier ka. Dono ke remotes alag-alag hain.Dawlance chalane ke liye
# aapko Dawlance ka remote uthana padta hai (Samjho yeh Manhattan Distance hai).Haier chalane ke liye aapko 
# Haier ka remote uthana padta hai (Samjho yeh Euclidean Distance hai).Ab aap market jaate ho aur wahan se
# ek Universal Remote khareed kar le aate ho. Us universal remote me ek switch (button) laga hai:Agar aap
# us switch ko 1 par set karte ho, toh woh Dawlance ka AC chala deta hai.Agar aap us switch ko 2 par set 
# karte ho, toh woh Haier ka AC chala deta hai.Minkowski Distance bas isi Universal Remote ka naam hai! Aur
# jo button remote par laga hai, usay math me "$p$" kehte hain.



# =====================================================================
# KNN---Minkowski Distance Mathematical Formula
# =====================================================================

#               n     p
# d(i,j) = p-√ [ ∑  |x_il - x_jl| ]
#              l=1


# ---------------------------------------------------------------------
# Short Meaning of Universal Remote Key (p Parameter):
# ---------------------------------------------------------------------
# - If p = 1 -> Formula becomes Manhattan Distance (Taxi Cab Distance)
# - If p = 2 -> Formula becomes Euclidean Distance (Straight-Line Distance)
# p=3 is minkowski distance

# ---------------------------------------------------------------------
# Meaning of Each Term:
# ---------------------------------------------------------------------
# d(i,j)       -> Point 'i' aur Point 'j' ke beech ka total Minkowski distance.
# p-√ (p-root) -> Sab kuch plus karne ke baad aakhri me p-th root lena.
# ∑ (l=1 to n) -> Summation (Pehle feature se lekar n-th feature tak sabko jama karna).
# |x_il - x_jl|-> Absolute difference (Minus ka sign khatam karne ke liye).
# Power p      -> Har feature ke farq ko power 'p' dena.





# coding:

# demonstration of distance metrics in k-NN

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score


# 1)create  simple dataset
x,y=make_classification(
    n_samples=1000,
    n_features=2,    #2D for easy implementaion
    n_informative=2,
    n_redundant=0,
    random_state=42
)

x_train,x_test,y_train,y_test=train_test_split(
    x,y,test_size=0.25,random_state=42
)

# train KNN with different distance metrics
metrics={
    "Euclidean":KNeighborsClassifier(n_neighbors=5,metric="euclidean"),
    "Manhattan":KNeighborsClassifier(n_neighbors=5,metric="manhattan"),
    "Minkowski":KNeighborsClassifier(n_neighbors=5,metric="minkowski",p=3)
}


for name,model in metrics.items():
    model.fit(x_train,y_train)
    y_pred=model.predict(x_test)
    acc=accuracy_score(y_test,y_pred)
    print(f"{name} accuracy: {acc:.3f}")




# show numeric example of distance for two points
x1=np.array([2,3])
x2=np.array([5,7])

euclidean=np.linalg.norm(x1-x2)
manhattan=np.sum(np.abs(x1-x2))
minkowski_p3=(np.sum(np.abs(x1-x2)**3))**(1/3)







print("Distance example between",x1, "and", x2)
print("euclidean:",round(euclidean,3))
print("manhattan:",round(manhattan,3))
print("minkowski (p=3):",round(minkowski_p3,3))