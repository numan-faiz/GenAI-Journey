# ANN---neural network training process


# ==================================================================================
# WHAT DOES TRAINING MEAN?
# ==================================================================================
# Training ANN = teaching model to minimize error
# Feed data into the network
# Compare predictions vs actual labels
# Adjust weights to reduce loss
# Repeat many iterations (epochs)


# ==================================================================================
# Training Pipeline
# ==================================================================================
# Initialize weights & biases
# Forward pass (calculate prediction)
# Compute loss
# Backpropagation (compute gradients)
# Step 1: Forward Pass
# z = x * w + b = 2 * 1 + 0 = 2
# Repeat -> epochs



# ==================================================================================
# ANN TRAINING, TUNING, AND EVALUATION - COMPLETE NOTES
# ==================================================================================

# ----------------------------------------------------------------------------------
# Train / Test Split
# ----------------------------------------------------------------------------------
# Training: Learn weights
# Validation: Tune hyperparameters
# Testing: Final performance check

# Rule of Thumb:
# 60% Train / 20% Validation / 20% Test


# ----------------------------------------------------------------------------------
# Epochs & Batches
# ----------------------------------------------------------------------------------
# Epoch = one full pass through the dataset
# Batch = subset of training data
# Mini-batch training = best for stability + speed

# Example:
# Dataset: 1000 samples, Batch size = 100 -> 10 batches per epoch


# ----------------------------------------------------------------------------------
# Understanding Learning Rate
# ----------------------------------------------------------------------------------
# Learning Rate (η) controls update step size: W = W - η * (dL / dW)
# Too high -> unstable training, diverges
# Too low -> very slow learning

# Tip:
# start small (e.g., 0.001, 0.01)

# Learning Rate Example:
# Learning Rate | Behavior
# 0.1           | overshoots, unstable
# 0.01          | fast learning
# 0.0001        | very slow


# ----------------------------------------------------------------------------------
# Evaluating ANN
# ----------------------------------------------------------------------------------
# Common metrics:
# For Classification: Accuracy, Precision, Recall, F1-score
# For Regression: MSE, MAE, RMSE

# Confusion matrix helps visualize classification results
# Evaluation ensures model performs well on unseen data


# ----------------------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------------------
# ANN training = forward pass + backprop + weight update
# Train / Validate / Test for generalization
# Learning rate is critical: controls how fast the model learns
# Evaluate with accuracy/loss plots & metrics


# ==================================================================================
# BINARY CROSS ENTROPY & CATEGORICAL CROSS ENTROPY FORMULAS
# ==================================================================================
# Binary Cross Entropy
# BCE = -1/N * Σ [y_i * log(p_i) + (1 - y_i) * log(1 - p_i)]

# Categorical Cross Entropy
# L = -log(y_hat_true)

# Goal
# Minimize loss


# ==================================================================================
# THE CHAIN RULE & WEIGHT/BIAS UPDATE FORMULAS
# ==================================================================================
# W = W - η * (dL / dW)

# η = learning rate
# dL / dW = gradient

# b = b - η * (dL / db)


# ==================================================================================
# INTUITION EXAMPLE: LEARNING BEHAVIOR OF ANN
# ==================================================================================
# If ANN predicts: 9
# Actual value: 10
# Error = 1
# So weights are slightly increased

# If ANN predicts: 2
# Actual value: 10
# Error = 8
# Weights adjust more strongly

# Learning Behavior:
# Big mistakes -> Big correction
# Small mistakes -> Small correction


# ==================================================================================
# COMMON CHALLENGES IN TRAINING ANN
# ==================================================================================
# Vanishing Gradients
# Description: gradients become too small -> slow learning

# Exploding Gradients
# Description: gradients too large -> unstable training

# Learning rate issues
# Description: too high -> diverges; too low -> slow training


# ==================================================================================
# KEY TAKEAWAY
# ==================================================================================
# Finding the right learning rate = fast + stable learning


# ==================================================================================
# WHAT DOES TRAINING MEAN?
# ==================================================================================
# Training ANN = teaching model to minimize error
# Feed data into the network
# Compare predictions vs actual labels
# Adjust weights to reduce loss
# Repeat many iterations (epochs)
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Training ka seedha matlab hai model ko uski ghaltiyan (Error) kam se kam karna sikhana.
# - Hum network me data daalte hain (Feed data), model apna ek tuka marta hai, phir hum check karte 
#   hain ke model ka tuka asli jawab (Actual label) se kitna door hai.
# - Is ghalti ko dekh kar computer raste ke workers (Weights) ko badalta hai taake ghalti kam ho jaye, 
#   aur yeh chakkar hazaron baar (Epochs) chalta rehta hai jab tak model perfect na ho jaye.


# ==================================================================================
# Training Pipeline & Step 1: Forward Pass
# ==================================================================================
# Initialize weights & biases
# Forward pass (calculate prediction)
# Compute loss
# Backpropagation (compute gradients)
# z = x * w + b = 2 * 1 + 0 = 2
# Repeat -> epochs
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Pipeline ka matlab hai training ke steps ka order:
#   1. Initialize: Shuru me computer blind tuke marne ke liye weights aur biases ko koi bhi 
# random number de deta hai.
#   2. Forward Pass: Data aage jata hai aur answer nikalta hai.
#   3. Compute Loss: Ghalti ka hissab lagaya jata hai.
#   4. Backpropagation: Ghalti ko piche le ja kar sahi kiya jata hai.
# - MATH WALI MISAAL: Agar aapka input x=2 hai, weight w=1 hai, aur bias b=0 hai, toh pehla hissab (z) 
#   kya banega? z = 2 * 1 + 0 = 2. Yeh line batati hai ke neuron shuru me simple maths kaise karta hai.


# ==================================================================================
# Train / Test Split
# ==================================================================================
# Training: Learn weights
# Validation: Tune hyperparameters
# Testing: Final performance check
# Rule of Thumb: 60% Train / 20% Validation / 20% Test
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Hum apne poore data ko ek sath model ke samne nahi phenkte, balke 3 hisson me baant-te hain:
# 1. Training Data (60%): Is data par model din-raat sabaq seekhta hai aur weights ko adjust karta hai.
# 2. Validation Data (20%): Is par model ka "Mock Test" hota hai taake hum uski setting/speed
#  (Hyperparameters) theek kar sakein.
# 3. Testing Data (20%): Yeh model ke liye bilkul "Unseen/Anjan" data hota hai, is par aakhiri 
# board ka imtihan hota hai ke model real world me pass hoga ya fail.

# ==================================================================================
# Epochs & Batches
# ==================================================================================
# Epoch = one full pass through the dataset
# Batch = subset of training data
# Mini-batch training = best for stability + speed
# Example: Dataset: 1000 samples, Batch size = 100 -> 10 batches per epoch
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Epoch: Jab model poori ki poori kitaab (saara dataset) ek baar shuru se aakhir tak parh le, toh use 1 
# Epoch kehte hain.
# - Batch: Agar kitaab me 1000 sawal (Samples) hain, toh computer ek sath saare sawal dimaag me nahi daal
#  sakta. Woh 100-100 sawalon ke chote chote tukre (Batches) banata hai.
# - Mini-batch: Iska faida yeh hai ke computer na toh heavy hota hai aur na hi slow, speed aur accuracy
#  dono top level rehti hain. 1000/100 = 10 chakar me 1 Epoch poora hoga!


# ==================================================================================
# Understanding Learning Rate
# ==================================================================================
# Learning Rate (η) controls update step size: W = W - η * (dL / dW)
# Too high -> unstable training, diverges | Too low -> very slow learning
# Learning Rate Example: 0.1 (overshoots) | 0.01 (fast learning) | 0.0001 (very slow)
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Learning rate (η - Eta) model ke seekhne ki raftaar (Step Size) hai:
# - Agar learning rate boht zyada (0.1) rakh di, toh model lambe lambe jumps marega aur sahi jawab ke
#  upar se nikal jayega (Overshoot/Diverge).
# - Agar boht choti (0.0001) rakh di, toh model itna chota kadam uthayega ke sabaq seekhte seekhte 
# barson lag jayenge (Very slow learning).
# - TIP: Isiliye darmayani speed (jaise 0.01) se shuru karna sabse best hota hai.


# ==================================================================================
# Evaluating ANN
# ==================================================================================
# For Classification: Accuracy, Precision, Recall, F1-score
# For Regression: MSE, MAE, RMSE
# Confusion matrix helps visualize classification results
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Model pass hua ya fail, yeh check karne ke liye do alag tareeqe hain:
# - Classification (Jaise: Cat vs Dog): Yahan hum dekhte hain accuracy kitni hai, Precision aur 
# Recall kitna perfect hai, aur F1-score kya hai. "Confusion Matrix" ek table hota hai jo saaf
#  dikha deta hai ke model ne kitni billiyon ko ghalti se kutta bol diya.
# - Regression (Jaise: Ghar ki keemat nikaalna): Yahan hum ghalti ka size naapte hain MSE, MAE,
#  ya RMSE ke zariye (Jitni kam value, utna behtar model).


# ==================================================================================
# BINARY CROSS ENTROPY & CATEGORICAL CROSS ENTROPY FORMULAS
# ==================================================================================
# BCE = -1/N * Σ [y_i * log(p_i) + (1 - y_i) * log(1 - p_i)]
# L = -log(y_hat_true)
# Goal: Minimize loss
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Yeh ghalti (Loss) nikaalne ke do bade mathematical scales hain:
# - Binary Cross Entropy (BCE): Yeh tab use hota hai jab jawab "Yes/No" ya "0 ya 1" me ho
#  (Binary Classification). Yeh formula prediction aur asli target ke beech ke gap ko log 
# function se naapta hai.
# - Categorical Cross Entropy (CCE): Yeh tab lagta hai jab options do se zyada hon (Multiclass). 
# Iska kaam sirf asli sahi class ki prediction par focus kar ke loss nikaalna hai.
# - GOAL: In formulas ka maqsad computer ko ek number dena hai jise computer ne har haal me kam 
# (Minimize) karna hai.


# ==================================================================================
# THE CHAIN RULE & WEIGHT/BIAS UPDATE FORMULAS
# ==================================================================================
# W = W - η * (dL / dW) | b = b - η * (dL / db)
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Yeh woh asli jadu hai jisse network ke andar ki tabdeeli hoti hai. 
# - dL/dW batata hai ke 'W' (Weight) badalne se Loss par kya farq padega.
# - Naya Weight = Purana Weight - (Speed * Gradient). Hum purane weight me se ghalti ka asar 
# minus karte hain taake agla tuka asli jawab ke qareeb lage. Same yahi kaam Bias (b) ke sath hota hai.


# ==================================================================================
# INTUITION EXAMPLE: LEARNING BEHAVIOR OF ANN
# ==================================================================================
# Predict: 9, Actual: 10 -> Error = 1 (Weights slightly increased)
# Predict: 2, Actual: 10 -> Error = 8 (Weights adjust more strongly)
# Core Learning Behavior: Big mistakes -> Big correction | Small mistakes -> Small correction
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Neural network bilkul insaan ki tarah behave karta hai:
# - Agar ghalti choti hai (Error = 1), toh computer sabaq seekhte waqt weights ko boht 
# thoda sa hilayega (Slightly change).
# - Agar ghalti boht bhayanak hai (Predict kiya 2 jabke hona chahiye tha 10, Error = 8),
#  toh computer ko jhatka lagta hai aur woh weights ko boht zor se badalta hai (Big correction).


# ==================================================================================
# COMMON CHALLENGES IN TRAINING ANN
# ==================================================================================
# Vanishing Gradients: gradients become too small -> slow learning
# Exploding Gradients: gradients too large -> unstable training
# Learning rate issues: too high -> diverges; too low -> slow training
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Training ke dauran teen sabse bade dushman aate hain:
# 1. Vanishing Gradients: Pichli layers tak aate aate ghalti ka ishara itna chota ho jata hai
#  ke shuru wale weights bilkul seekhna band kar dete hain.
# 2. Exploding Gradients: Ghalti ka number itna bada ho jata hai ke weights control se bahr ho
#  kar pagal ho jaate hain aur training crash ho jati hai.
# 3. Learning Rate Issues: Speed fast toh model unstable, speed slow toh model sadiyon tak seekhta rahega.


# keytakeawayas:
# find the right learning rate 
# fast and stable laerning