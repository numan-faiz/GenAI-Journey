# *****************************************DEEP LEARNING*********************************

# introduction to Artificial neural network
# now this is start deep learning
# it is supervised learning technique

# mathematical model inspired by brain
# made up of neaurons organized in layers

# it is foundation of deep learning and AI

# learn patterns from data
# used for :classification ,regresion,image recognition NLP etc



# mathmatical intution behind artificial network:
# neurons-->or it consist on human brain neuron like and all neauron organized in layers 
# weights-->input connection ko weight assighn hta phr us weigh sy decide hta ke isko kaha jana hy kaha nahi
# biases: ye input or unke sum ko mean ke around lane ke koshes kerta hy 
# activation functions:defualt behaviour ju linear hy usko non linear me convert kerny me help kerta hy 


# examples: Relu functions,sigmopid functions,tanh function

# biological neuron vs artificial neuron:
# bilogicla neuron:
# receive signals (dendrites) processes and fires (axon)
# sends signal to others

# artificail neuron"
# inputs-->multiply by wieghts-->add bias-->apply activation--->idea input-->weighted sum--->
# activation-->output

# mathematical model of neuron:
# formula:
# ==================================================================================
# 1. NEURON EQUATION
# ==================================================================================
# z = w1*x1 + w2*x2 + ... + wn*xn + b

# Where:
# x(i) = input
# w(i) = weights
# b = bias


# ==================================================================================
# 2. ACTIVATION FUNCTION
# ==================================================================================
# y(hat) = σ(z)

# Where:
# σ = activation function
# y(hat) = output


# key idea of artificial neural network:
# ANN learns values of weights and bias using training

# layers in ANN:
# input layers
# hidden layers (1-->many)
# output layers

# example architecture:
# input
# hidden (3 layers)
# output

# activation functions:if no activation function=model becmoes linear
# activation function introduces non linearity-->nuearal netwroks can learn complex patterns

# example of non linear problems:
# recognizing  faces in images 
# predicting non linear time series
# speech understanding

# ==================================================================================
# SIGMOID FUNCTION FORMULA
# ==================================================================================
# σ(x) = 1 / (1 + e^(-x))

# Where:
# σ = Sigmoid Function
# x = Input Value
# e = Euler's Number (Constant ≈ 2.718)
# used for binary clasification yes or no 


# issues in sigmoid function:
# vanishing gradient (slow learning for deep server)

# ==================================================================================
# TANH FUNCTION FORMULA & CHARACTERISTICS
# ==================================================================================
# tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x))

# Features:
# - Range: (-1, 1)
# - Centered at zero -> faster convergence than sigmoid
# - Still suffers from vanishing gradient

# Where:
# tanh = Hyperbolic Tangent Function
# x = Input Value
# e = Euler's Number (Constant ≈ 2.718)


# range(-1,1)
# centered at zwero-->faster
# convergence than sigmoid 
# still suffers from vanishing gradeient


# ReLu function(Rectified linear unit)
# f(x)=max(0,x)
# very fast trainning
# solve vanisnhing gradient issue

# draw back ReLu:
# dying relu(unit stucks at zero sometimes)


# ==================================================================================
# INTRODUCTION TO ARTIFICIAL NEURAL NETWORKS (ANN) - COMPLETE NOTE
# ==================================================================================

# ----------------------------------------------------------------------------------
# POINT 1: Introduction to ANN
# "now this is start deep learning, it is supervised learning technique, mathematical model 
# inspired by brain made up of neurons organized in layers. Foundation of deep learning and AI"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Yahan se Deep Learning ka aaghaz hota hai. ANN ek supervised learning tareeqa hai 
# jo hamare dimaag ke cells (neurons) ke nakshe par banaya gaya hai. Yeh deep learning 
# aur modern AI ki buniyaadi deewar hai.
# Usages: Iska istemal Classification, Regression, Image Recognition aur NLP me hota hai.


# ----------------------------------------------------------------------------------
# POINT 2: Mathematical Intuition Behind ANN
# "neurons (organized in layers), weights, biases, activation functions"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Neurons: Dimaag ke cells ki tarah hote hain jo alag alag partiyon (layers) me baithe hain.
# - Weights: Har input connection ki power (aukaat) hoti hai jo faisla karti hai ke data ko kahan bhejna hai.
# - Biases: Yeh total sum ko thoda shift karta hai taake model flexible rahe aur sahi se center ho sake.
# - Activation Functions: Model ka default linear behavior khatam karke usme 'Non-Linearity' laata hai.


# ----------------------------------------------------------------------------------
# POINT 3: Biological Neuron vs Artificial Neuron
# "Biological: receive signals (dendrites) processes and fires (axon) -> sends signal to others
# Artificial: inputs -> multiply by weights -> add bias -> apply activation -> output"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Asli Dimaag ka Neuron: Dendrites se signal leta hai, dimaag me process karta hai, aur Axon ke zariye aage fire kar deta hai.
# - Computer ka Neuron: Inputs ko pakadta hai, unko weights se multiply karke bias jama karta hai (Weighted Sum 'z'), aur activation function ka thappa laga kar output nikaal deta hai.


# ----------------------------------------------------------------------------------
# POINT 4: Mathematical Model of Neuron
# "1. NEURON EQUATION: z = w1*x1 + w2*x2 + ... + wn*xn + b
#  2. ACTIVATION FUNCTION: y(hat) = σ(z)"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Pehle saare inputs aur weights ko multiply karke bias ke sath jama kiya jata hai (z).
# - Phir us 'z' ko activation function (σ) me daal kar final prediction (y_hat) nikaali jati hai.
# - Key Idea: ANN training ke dauran inhi Weights aur Biases ki sahi values khud seekhta hai.


# ----------------------------------------------------------------------------------
# POINT 5: Layers in ANN & Non-Linearity
# "Layers: Input, Hidden (1 to many), Output. If no activation function = model becomes linear"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Data pehle Input layer me aata hai, phir banta hai Hidden layers me (jahan asli sabaq seekha jata hai), aur aakhir me Output layer jawab deti hai.
# - Non-Linearity Kyun Zaroori Hai? Agar activation function nahi lagayenge, toh model sirf seedhi line (linear) seekh payega. Complex kaam jaise Face Recognition, Speech Understanding aur mushkil patterns bina iske namumkin hain.


# ----------------------------------------------------------------------------------
# POINT 6: Sigmoid Function
# "σ(x) = 1 / (1 + e^(-x)) -> used for binary classification. Issue: Vanishing Gradient"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Yeh output ko 0 aur 1 ke beech me band kar deta hai, isiliye Binary Classification (Haan ya Naa) ke liye best hai.
# - Nuqsan (Vanishing Gradient): Jab model boht deep hota hai, toh iska gradient (learning speed) 
# aakhir me itna chota ho jata hai ke computer boht slow seekhne lagta hai.


# ----------------------------------------------------------------------------------
# POINT 7: Tanh Function
# "tanh(x) = (e^x - e^(-x)) / (e^x + e^(-x)) -> Range: (-1, 1), Centered at zero"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Yeh Sigmoid se behtar hai kyunki iska center 0 par hota hai, jis se model thoda fast chalta hai 
# (faster convergence). 
# - Nuqsan: Isme bhi Vanishing Gradient ka masla rehta hai, yaani gehre models me slow ho jata hai.


# ----------------------------------------------------------------------------------
# POINT 8: ReLU Function (Rectified Linear Unit)
# "f(x) = max(0,x) -> very fast training, solve vanishing gradient issue"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Yeh sabse mashhoor aur fast function hai. Agar number positive hai toh waisa hi chodh dega, agar 
# negative hai toh 0 kar dega. Isne vanishing gradient ka masla hal kar diya aur training super-fast 
# kar di.


# ----------------------------------------------------------------------------------
# POINT 9: Drawback of ReLU (Dying ReLU Concept)
# "Dying ReLU: unit stucks at zero sometimes"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - ASAN LAFZON ME: Kyunki ReLU har minus (negative) number ko aankhein band karke 0 kar deta hai,
#  toh baaz auqat training ke dauran kuch neurons ke paas lagatar negative values aane lagti hain. 
# - Woh neurons hamesha ke liye 0 par atak (stuck) jaate hain, yaani woh bilkul "MURDA" (Dead) ho jaate
#  hain aur aage kuch bhi naya seekhna band kar dete hain. Isay hi "Dying ReLU" kehte hain.
# ==================================================================================