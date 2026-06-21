# introduction to principal componenet analysis (PCA)

# PCA is a dimetionality reduction technique
# its reduce dimentionality but remain constant variance
# help simlify dataset
# reduced computational cost
# remove noise

# how PCA works:
# transform the original features into a new set pf orthogonal axes called principal componenents

# working steps of PCA:
# project data onto directions(principal componenets) where variance is maximized 
# first principal component -->directions of maximum variance

# second princiapl component:orthogonal to the first,with next highest variance
# subsequent components follow the same rule

# xample agar koi data me 30  feature hy or hemin 15 kernanhy tu hm uska variance nikalengy sab ka or 
# or phr usko descending order me likh dengy or top ke 15 feature lelengy ye uska PCA hgya 

# example of PCA:
# 2d dataset of exam scores (math,pyhsics)-->PCA identifies a new axis caturing most variation
# reduces corelated featureinto a single component while retainning most information
# facilities visualization of high dimensional data in 2D or 3D

# Advantages of PCA:
# reduce dimetionality-->faster computation
# remove corelated and reduntant features
# facilties visualization of high dimentional data 
# disadvantages of PCA:
# principal components are linear combinations-->less interpretable
# some information loss is inevitable 
# sensitive to faeature scaling



# ==================================================================================
# COMPLETE PCA NICHOR: ALL YOUR POINTS IN EASY ROMAN URDU (COPY-PASTE READY)
# ==================================================================================

# ----------------------------------------------------------------------------------
# 1. PCA KYA HAI? (Introduction)
# ----------------------------------------------------------------------------------
# - Dimensionality Reduction: Yeh data ke columns (features) ko kam karne ki technique hai.
# - Maintain Variance: Yeh columns ko aise kam karta hai ke data ki asli maloomat 
#   (variance) zaya na ho, balki woh barqarar (constant) rahe.
# - Simplify Dataset: Mushkil aur bade data ko aasan aur chota bana deta hai.
# - Reduce Cost & Noise: Isse computer par load kam parta hai (fast computation) aur 
#   data ke andar ka fuzool kachra (noise) saaf ho jata hai.


# ----------------------------------------------------------------------------------
# 2. PCA KAAM KAISE KARTA HAI? (How PCA Works)
# ----------------------------------------------------------------------------------
# - Orthogonal Axes: PCA purane columns ko delete nahi karta. Yeh unko mix karke naye 
#   raste (axes) banata hai jise hum "Principal Components (PCs)" kehte hain.
# - 90-Degree (Orthogonal): Saare naye PCs aapas me 90-degree ke angle par hote hain, 
#   yaani ek dusre se bilkul azaad hote hain.


# ----------------------------------------------------------------------------------
# 3. WORKING STEPS (PCA Ke Qadam)
# ----------------------------------------------------------------------------------
# - Step 1 (Project Data): PCA data ko un raston par phenkta hai jahan sabse zyada 
#   bikhrao (maximum variance) nazar aaye.
# - Step 2 (PC1): Pehla naya column (First Principal Component) woh hota hai jahan 
#   sabse zyada variance/maloomat hoti hain.
# - Step 3 (PC2): Dusra column (Second Principal Component) PC1 ke sath 90-degree par 
#   hota hai, aur isme bachi-kuchi sabse zyada maloomat hoti hain.
# - Step 4 (Subsequent): Baqi saare PCs bhi isi tarah ek dusre se 90-degree par bante jate hain.


# ----------------------------------------------------------------------------------
# 4. CORRECT EXAMPLE (30 Features Se 15 Features Ki Asli Haqeeqat)
# ----------------------------------------------------------------------------------
# - Ghalat Soch: Purane 30 columns me se top 15 ko select karna aur 15 ko delete karna (Yeh PCA nahi hai).
# - Sahi Soch (PCA): PCA purane 30 columns ka juice nikaal kar unko aapas me MIX karega, 
#   aur unse 15 NAYE jadooi columns (PC1 se PC15) bana dega. Is tarah purane 30 columns 
#   ka mawaad bhi zaya nahi hota aur columns bhi 15 reh jate hain!


# ----------------------------------------------------------------------------------
# 5. EXAMS SCORES WALI MISAAL (Math & Physics)
# ----------------------------------------------------------------------------------
# - Agar aapke paas 2D data hai (Math aur Physics ke marks), toh dono columns aapas me 
#   mile hue (correlated) hote hain kyunki hoshiar bacha dono me ache marks leta hai.
# - PCA in dono ko jorh kar ek naya single axis bana deta hai (Jaise "Smartness"), jo 
#   dono ka kaam akele karta hai. Is tarah high-dimensional data ko 2D ya 3D graph par 
#   dekhna (visualize) aasan ho jata hai.


# ----------------------------------------------------------------------------------
# 6. FAIDE AUR NUQSAN (Advantages & Disadvantages)
# ----------------------------------------------------------------------------------
# - FAIDE (Advantages):
#   1. Columns kam hone se model super-fast chalta hai.
#   2. Mile-jule (correlated/redundant) columns ka jhanjhat khatam ho jata hai.
#   3. Bare data ko graph par dekhna (visualization) aasan ho jata hai.
# 
# - NUQSAN (Disadvantages):
#   1. Less Interpretable: Naye columns (PC1, PC2) ka koi asli matlab samajh nahi aata 
#      ke yeh 'Age' hai ya 'Salary'. Yeh bas linear combination hote hain.
#   2. Information Loss: Thodi boht maloomat ka nuqsan (loss) lazmi hota hai.
#   3. Scaling Sensitive: Agar data ko pehle scale na kiya jaye, toh PCA ghalat kaam karta hai.
# ==================================================================================