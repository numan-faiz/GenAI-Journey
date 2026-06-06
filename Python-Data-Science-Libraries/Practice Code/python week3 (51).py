# creating arrays in numpy
# how to make arrays let see babe
import numpy as np
arr=np.array([1,2,3])
print(arr)
print(np.zeros((2,3)))
print(np.ones((2,3)))
print(np.full((2,3),7))
print(np.arange(0,10,2))
print(np.linspace(0,1,5))

# make identity matrix
print(np.eye(3))

# diagonal matrix by selected value in diognal
print(np.diag([1,2,3]))

print(np.array([1,2,3], dtype=float))

arr=np.array([1.5,2.5,3.9])
print(arr.astype(int))

# undersdtanding--->


# Chalo yar, in sab ko ek ek karke bilkul asaan aur desi misalon se samajhte hain.
# Imagine karo aap ek AI model ki "building" khari kar rahe ho, to ye sab aapke tools
# hain:
#
# ### 1. `np.array([1,2,3])`
# Ye sab se basic cheez hai. Python ki simple list ko NumPy ke **"Super Array"**
# mein badalna.
# *   **Asaan lafzon mein:** Ek purani lakri ki siri (list) ko mazboot lohay ki
# siri (array) mein badal dena taake computer is par tezi se charh sakay.
#
# ### 2. `np.zeros((2,3))`
# Ye aapko ek khali (zero se bhara hua) table bana kar deta hai jis mein **2 rows** aur
# **3 columns** hain.
# *   **Gen AI Use:** Jab AI ko koi nayi tasveer banani hoti hai, to wo shuru mein aik
# "kaali screen" (zero pixels) se start karta hai.
#
# ### 3. `np.ones((2,3))`
# Bilkul `zeros` ki tarah, lekin is mein har jagah **1** likha hota hai.
# *   **Gen AI Use:** AI mein jab humein kisi cheez ki "Masking" karni ho (yani kisi
# hissay ko highlight karna ho), to wahan 1 use hota hai.
#
# ### 4. `np.full((2,3), 7)`
# Agar aap chahte hain ke table zero ya ek se nahi, balki kisi **khaas number**
# (maslan 7) se bhara ho.
# *   **Asaan lafzon mein:** Ek aisa paper mangwana jis par pehle se hi har jagah
# '7' likha hua ho.
#
# ### 5. `np.arange(0, 10, 2)`
# Ye ek range banata hai. (Start, Stop, Step).
# *   **Matlab:** 0 se shuru karo, 10 par ruk jao (10 shamil nahi hoga), aur **2,
# 2 ka gap** rakho.
# *   **Result:** `[0, 2, 4, 6, 8]`
#
# ### 6. `np.linspace(0, 1, 5)`
# Ye bohat "smart" function hai. Aap kehte ho: "Bhai 0 se 1 tak jao aur mujhe
# barabar faslay par **5 numbers** nikaal kar do."
# *   **Result:** `[0. , 0.25, 0.5 , 0.75, 1. ]`
# *   **AI Logic:** Jab AI ek cheez se doosri cheez mein dheere dheere badalta hai
# (Morphing), to ye function use hota hai.
#
# ---
#
# ### 7. `np.eye(3)` (Identity Matrix)
# Ye ek aisa square table banata hai jis mein diagonal (tirchi line) mein **1**
# hota hai aur baaki sab **0**.
# *   **AI Logic:** Ye AI ka **"Mirror" (Aaina)** hai. Kisi bhi image ko is matrix
# se multiply karo to wo waisi ki waisi hi rehti hai. Ye transformations ko reset
# karne ke kaam aata hai.
#
# ### 8. `np.diag([1,2,3])`
# Agar aap apni marzi ke numbers diagonal mein rakhna chahte hain.
# *   **Asaan lafzon mein:** Ek khali ground mein sirf tirchi line mein khambe
# (poles) kharay karna.
#
# ---
#
# ### 9. `dtype=float` aur `astype(int)` (Data Types)
# AI mein numbers ki "shakal" bohat matter karti hai.
#
# *   **`dtype=float`:** Ye `[1, 2, 3]` ko `[1.0, 2.0, 3.0]` bana deta hai.
# AI zyadatar points wale numbers (floats) hi samajhta hai kyunke calculations
# accurate hoti hain.
# *   **`astype(int)`:** Ye points wale numbers ko khatam kar ke unhein "seedha"
# kar deta hai. Maslan `3.9` ko ye `3` bana dega (ye round nahi karta, bas point ke
# baad wala hissa kaat deta hai).
# *   **Gen AI Use:** Jab AI output deta hai to wo floats mein hota hai, lekin jab
# humne photo dikhani hoti hai to hum usay `int` (integers) mein convert karte hain.
#
# ---
#
# **Summary Tip:**
# *   `zeros`, `ones`, `full` = **Shuruat** (Initial setup).
# *   `arange`, `linspace` = **Ginti aur Fasla** (Counting).
# *   `eye`, `diag` = **Khaas Shapes** (Special structures).
# *   `astype` = **Shakal badalna** (Data conversion).
#
# In mein se koi aisa function hai jo abhi bhi tang kar raha hai?