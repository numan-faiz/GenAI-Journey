# ANN--bckpropagation algorithm

# wha is backpropagation
# algoritm to train neural network

# backpropagation:measure error loss
# computes gradeints(partial deriatives)
# updates weights to reduce error
# repeat until convergence
# key idea of backpropagation:
# learning by adjusting weights backward from output layer
# the flow of backpropagation is reverse direction from out to input ok

# why de we need backpropagation:
# without backprop ANN cannot learn
# backprop helps the network learn patterns
# undersatnding how wrong the prediction was
# undersatnding which weights caused the error
# improving weights accordingly


# the training loop:
# forward pass-->predict output
# backward pass-->calculate gradients
# updated weights(gradeint descent)
# repeat for many epochs

# nueron output:
# z=wx+b
# y=σ(z)
# loss example (MSE):
# l=1/2(y-y)^2


# ==================================================================================
# BINARY CROSS ENTROPY & CATEGORICAL CROSS ENTROPY FORMULAS
# ==================================================================================

# 1. Binary Cross Entropy
# BCE = -1/N * Σ [y_i * log(p_i) + (1 - y_i) * log(1 - p_i)]

# 2. Categorical Cross Entropy
# L = -log(y_hat_true)

# 3. Goal
# Minimize loss

# ==================================================================================
# THE CHAIN RULE & WEIGHT/BIAS UPDATE FORMULAS
# ==================================================================================

# 1. Weight Update Formula
# W = W - η * (dL / dW)

# 2. Key Terms
# η = learning rate
# dL / dW = gradient

# 3. Bias Update Formula
# b = b - η * (dL / db)



# gradeint descnet:
# moving in direction of lowest error

# visual flow:
# forward pass:
# inputs--layers---output--loss

# backward pss:
# loss--ouput layer--hidden layers---wieghted updaetd

# ==================================================================================
# INTUITION EXAMPLE: LEARNING BEHAVIOR OF ANN
# ==================================================================================

# Case 1: Small Mistake
# If ANN predicts: 9
# Actual value: 10
# Error = 1
# So weights are slightly increased

# Case 2: Big Mistake
# If ANN predicts: 2
# Actual value: 10
# Error = 8
# Weights adjust more strongly

# Core Learning Behavior:
# Big mistakes -> Big correction
# Small mistakes -> Small correction

# OMMON CHALLENGES IN TRAINING ANN
# ==================================================================================

# Challenge 1: Vanishing Gradients
# Description: gradients become too small -> slow learning

# Challenge 2: Exploding Gradients
# Description: gradients too large -> unstable training

# Challenge 3: Learning Rate Issues
# Description: too high -> diverges; too low -> slow training


# summary:
# backprop uses chain rules to compute gradeint
# updated weights to reduce loss
# fundamental to trainning neuralnetwork
# training=forward pass+backward pass
# memory hack:forward for predic and backward to learn



# ==================================================================================
# ANN: BACKPROPAGATION ALGORITHM (COMPLETE STEP-BY-STEP EXPLANATION)
# ==================================================================================

# ----------------------------------------------------------------------------------
# POINT 1: What is Backpropagation & Key Idea
# "algorithm to train neural network, measure error loss, computes gradients (partial derivatives),
#  updates weights to reduce error, repeat until convergence. Flow is reverse direction from output 
# to input"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - ASAN LAFZON ME: Backpropagation ka seedha matlab hai "Peeche ki taraf chalna". 
# - Jab hamara network aage ki taraf (Forward) ja kar koi ghalat jawab nikaalta hai, 
#   toh hum aakhiri layer (Output) par khade ho kar nuksaan/galti (Loss) naapte hain.
# - Phir hum wahan se ulta (Reverse) chalte hain—output layer se hidden layer, aur 
#   phir input layer ki taraf—taake raste me baithe saare workers (weights) ko unki 
#   ghalti ke mutabiq theek kiya ja sake. Yeh chakkar tab tak chalta hai jab tak ghalti khatam na ho jaye.


# ----------------------------------------------------------------------------------
# POINT 2: Why Do We Need Backpropagation?
# "without backprop ANN cannot learn, understand how wrong the prediction was, 
#  understand which weights caused the error, improving weights accordingly"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Iske bina neural network bilkul andha hai. Agar backpropagation nahi hoga, toh 
#   robot ko kabhi pata hi nahi chalega ke uska jawab kitna ghalat tha, aur na hi 
#   usay yeh pata chalega ke kis worker (weight) ki wajah se yeh ghalti hui. 
# - Yeh algorithm network ko ungli pakad kar sikhata hai ke: "Beta, tumne yeh ghalti ki, 
#   ab is weight ko thoda badlo taake agli baar jawab sahi aaye."


# ----------------------------------------------------------------------------------
# POINT 3: The Training Loop & Memory Hack
# "forward pass -> predict output | backward pass -> calculate gradients | update weights
#  (gradient descent)
#  Memory hack: forward for predict and backward to learn"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Ek AI model ki training bilkul ek bache ki padhai ki tarah hoti hai jo 4 steps me ghumti hai:
# 1. Forward Pass: Model ne apna tuka mara ya guess kiya (Prediction).
# 2. Loss Calculation: Teacher ne test check kiya aur bataya ke kitne numbers katay (Loss).
# 3. Backward Pass: Bache ne paper ko ulta dekhna shuru kiya ke kahan kahan ghalti hui (Gradients).
# 4. Weight Update: Bache ne apni ghalti sudhari taake agle test (Epoch) me behtar perform kare.
# - SHORTCUT: Forward ka kaam hai sirf jawab nikaalna, Backward ka kaam hai asli sabaq seekhna.


# ----------------------------------------------------------------------------------
# POINT 4: Loss Functions (MSE, BCE, CCE)
# "Loss example (MSE): l = 1/2(y - y_hat)^2
#  BCE: used for binary classification | CCE: L = -log(y_hat_true) | Goal: Minimize loss"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Loss function ka matlab hai "Ghalti naapne ka scale".
# - MSE (Mean Squared Error): Yeh regression (numbers/keemat nikaalne) me kaam aata hai. Asli value 
# aur predicted value ke farq ka square nikaalta hai.
# - BCE (Binary Cross Entropy): Jab jawab sirf do options me se ek ho (Jaise: Kutta ya Billi).
# - CCE (Categorical Cross Entropy): Jab options do se zyada hon (Jaise: Gaari, Truck, Cycle, Jahaz).
# - ASLI MAQSAD: Hamara aakhiri maqsad hamesha is Loss (ghalti) ko zero (Minimize) karna hota hai.
# ----------------------------------------------------------------------------------
# POINT 5: The Chain Rule & Weight/Bias Update Formulas
# "W = W - η * (dL / dW) | b = b - η * (dL / db) | η = learning rate, dL/dW = gradient"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Chain Rule: Kyunki network me boht saari layers aapas me judi hoti hain, toh aakhiri layer 
#   ki ghalti ka asar pehli layer par nikaalne ke liye math ka 'Chain Rule' (multiplication) use hota hai.
# - dL / dW (Gradient): Yeh batata hai ke agar main weight ko thoda sa hilaon, toh loss par kitna asar padega.
# - η (Learning Rate): Yeh model ke seekhne ki raftaar (speed) hai. 
# - ASLI MATH: Naya Weight = Purana Weight - (Speed * Ghalti). Hum purane weight me se ghalti ko 
#   minus karte hain taake hum sahi raste par chal sakein. Same yahi kaam Bias (b) ke sath hota hai.


# ----------------------------------------------------------------------------------
# POINT 6: Gradient Descent
# "moving in direction of lowest error"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Farz karein aap ek pahad ki choti par khade hain aur andhera hai, aapko neeche wadi (lowest error) 
# me jaana hai. Aap har kadam us taraf badhayenge jahan dhalaan neeche ja rahi hogi. Gradient Descent 
# bhi weights ko hamesha us taraf dhakelata hai jahan ghalti (error) sabse kam ho.


# ----------------------------------------------------------------------------------
# POINT 7: Intuition Example (Big vs Small Mistakes)
# "Big mistakes -> Big correction | Small mistakes -> Small correction"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Case 1: Agar asli keemat 10 thi aur model ne guess kiya 9 (Choti ghalti, Error = 1), 
#   toh computer weights ko boht thoda sa badlega (Slightly increased).
# - Case 2: Agar asli keemat 10 thi aur model ne guess kiya 2 (Badi ghalti, Error = 8), 
#   toh computer ko jhatka lagega aur woh weights ko boht zor se badlega (Big correction).
# - NICHOR: Jitni badi ghalti, utna bada jhatka aur utna bada badlao!

# ----------------------------------------------------------------------------------
# POINT 8: Common Challenges (Vanishing, Exploding, Learning Rate)
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Training ke dauran 3 bade masle (challenges) aate hain:
# 1. Vanishing Gradients: Pichli layers tak aate aate ghalti ka signal itna chota (0.00001) 
#    ho jata hai ke shuru wale weights kuch seekh hi nahi paate. Training ruk jati hai.
# 2. Exploding Gradients: Ghalti ka number itna bada ho jata hai ke weights pagal ho jaate hain 
#    aur model unstable ho jata hai.
# 3. Learning Rate Issues: 
#    - Agar Speed (η) boht High rakh di: Toh model jumps marta rahega aur kabhi sahi jagah 
# nahi pahuchega (Diverges).
#    - Agar Speed (η) boht Low rakh di: Toh model itna slow seekhega ke budha ho jayega
#  par training khatam nahi hogi.
# ==================================================================================