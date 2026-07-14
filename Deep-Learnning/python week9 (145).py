# ANN--->logistic Activation Function
# Activate function:
# decide whether a neuron should activate or not
# introduce non-linearity into  the network 
# enable neural network to learn complex patterns

# Applied after weighted  sum+bias

# why activation function are needed
# netwrok becomes a linear mode

# example: linear model-->staright line

# cannot learn comlex realtionships
# example:activation fucntion-->curves and boundaries

# logistic (Sigmoid) function:
# one of the earliest activation function
# outputs value between o and 1
# often between for binary classification
#formula:  "σ(x) = 1 / (1 + e^(-x)) -> used for binary classification. Issue: Vanishing Gradient"

# or hn agr logistic function me numerical example sy lelo: jasy:
# input                   output
# -3                     0.047
# -1                     0.269
# 0                     0.5
# 1                     0.731
 
# 3                    0.953

# agar input jitna large hu utni value 1 ke qareeb hoge ok

# logistic function in a neuron weighted sum:
# z=w1x1+w2x2+b

# activation: a=σ(z)
# a--actrivation fyunction
# σ(z)-->wighted sum


# advantages of logistic function:
# simple and intuitive
# output in probality range(0,1)
# work well for binary output
# diffrentiable (needed for backpropagation-->kam ata hy learning of wights and bias me)


# limitation of logisttic function
# vanishing gradient problem
# output not zero centered
# slower convergence for deep networks
# rarely used in hidden layers today
# when to use logistic function
# binary classification output layer
# logistic regression
# prbability estimation tasks
# usually repalced by ReLu in hidden layers


# ==================================================================================
# ANN: LOGISTIC (SIGMOID) ACTIVATION FUNCTION - COMPLETE NOTE
# ==================================================================================

# ----------------------------------------------------------------------------------
# POINT 1: Activation Function Kya Hai? (Core Role)
# "decide whether a neuron should activate or not, introduce non-linearity, 
#  enable network to learn complex patterns. Applied after weighted sum+bias"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Activation function ek gatekeeper hai jo faisla karta hai ke neuron ko "ON" (activate) 
# hona hai ya nahi. Yeh hamesha 'z = wx + b' (weighted sum + bias) nikalne ke BAAD 
# lagaya jata hai taake model me curves aur boundaries (Non-Linearity) aa sakein.


# ----------------------------------------------------------------------------------
# POINT 2: Activation Function Kyun Zaroori Hai?
# "Without it, network becomes a linear model (straight line) and cannot learn complex relationships"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Agar hum activation function nahi lagayenge, toh pure network ki math aakhir me ek 
# seedhi line (Linear Model) ban jayegi. Seedhi line se aap real-world ke mushkil 
# patterns (jaise chehre pehchanna ya curves wale data) ko kabhi nahi seekh sakte.


# ----------------------------------------------------------------------------------
# POINT 3: Logistic (Sigmoid) Function & Formula
# "one of the earliest activation function, outputs value between 0 and 1. 
#  Formula: σ(z) = 1 / (1 + e^(-z))"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Yeh dunya ke sabse purane activation functions me se ek hai. Iska kaam har chote-bade 
# number ko pakad kar 0 aur 1 ke beech me band (squeeze) kar dena hai.


# ----------------------------------------------------------------------------------
# POINT 4: Aapki Math Wali Numerical Misaal (Input vs Output)
# "agar input jitna large hu utni value 1 ke qareeb hoge"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Agar hum formula me alal-alag inputs dalen, toh dekhein yeh numbers ko kaise badalta hai:
# - Input (-3) --> Output: 0.047  (Minus me bada number 0 ke bilkul qareeb hai)
# - Input (-1) --> Output: 0.269
# - Input (0)  --> Output: 0.500  (Bilkul center/darmiyan)
# - Input (1)  --> Output: 0.731
# - Input (3)  --> Output: 0.953  (Plus me bada number 1 ke bilkul qareeb hai)
# RULE: Input jitna bada (positive) hota jayega, output utna hi 1 ke qareeb bhagega.


# ----------------------------------------------------------------------------------
# POINT 5: Neuron Me Iska Istemal (In a Neuron Weighted Sum)
# "z = w1x1 + w2x2 + b  -->  a = σ(z)"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - z = Weighted Sum (Inputs ko weights se multiply kiya aur bias jama kiya).
# - a = Final Activation (Us 'z' ko Sigmoid ke formula me daal kar probability nikaali).


# ----------------------------------------------------------------------------------
# POINT 6: Faide (Advantages)
# "simple, output in probability range (0,1), differentiable (needed for backpropagation)"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Iska jawab 0 aur 1 ke beech aata hai, isiliye yeh Probability batane ke liye best hai.
# - Diffrentiable: Iska calculus/derivative aasan hai, jo 'Backpropagation' me computer 
#   ko weights aur bias sahi se seekhne (learn karne) me madad deta hai.


# ----------------------------------------------------------------------------------
# POINT 7: Nuqsan / Limitations
# "vanishing gradient, output not zero centered, slower convergence, rarely used in hidden layers"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Vanishing Gradient: Agar input boht bada ya boht chota ho jaye, toh graph flat ho 
#   jata hai, jisse learning speed bilkul mar jati hai (gradient zero ho jata hai).
# - Not Zero Centered: Iska center 0.5 hai, 0 nahi. Is wajah se training slow ho jati hai.
# - Aaj kal isay beech wali (Hidden) layers me koi nahi poochta, wahan ReLU chalta hai.


# ----------------------------------------------------------------------------------
# POINT 8: Kab Use Karna Hai? (When to Use)
# "binary classification output layer, logistic regression, probability estimation tasks"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Isko sirf aur sirf network ki **Aakhiri Layer (Output Layer)** me use karte hain jab 
# jawab "Haan" ya "Naa" (Binary Classification) me chahiye ho, ya direct probability 
# nikaalni ho.
# ==================================================================================