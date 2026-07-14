# ANN--feedforward neural networks
# ANN kam kerta hy feed fowrad neural network usool pe
# woo ye hy :
# a nueral network where data flows only in one direction 
# input-->hidden layer--input ye direction hy is tarf in sy output ke trf
# no loops,no feddback connection
# aslo called multilayer perceptron(MLP )
# MLP simplest form hy ANN ka sabsy pehly ye banaye gye

# how data moves:
# input feature enter the network
# each layer computes: 
# z=wx+b      
# a=σ(z)

# flow example:
# (input)feature-->hidden layer-->output-->phr hm external word ko dekhaty oky
# key characteristics:
# signal moves forward only
# uses activation functions(ReLu,Sigmoid,Tanh)
# learn weights+bias via trainning
# best for tabular,simple image tasks and text feature
# no good for :time series task(LSTM,RNN instead)

# Archetecture example:
# input(x)--hidden layer-->output (y)
# example:predicting car price  example of regression hy 
# input:mileage, age,engine size
# output:price estimate

# numerica example by feed fowrad formula:
# z=wx+b   
# input-->hidden layer--output
# input x=2
# weight w=1
# bias b=0
# step1:forwad pass
# z=x.w+b=2*1+0=2
# step2: activation ReLu
# opositive ke liye psoitive hi hge ReLu kuch nahi kerta phr usi ko consider kerta agr value positive hu tu 

# takeaways:
# feed forward-->no loops
# data moves input-->output
# foundation of all deep learning model

# ==================================================================================
# ANN: FEEDFORWARD NEURAL NETWORKS (MLP) - COMPLETE NOTE
# ==================================================================================

# ----------------------------------------------------------------------------------
# POINT 1: Feedforward Ka Usool (Core Concept)
# "a neural network where data flows only in one direction: input -> hidden -> output. 
# No loops, no feedback connection. Also called Multilayer Perceptron (MLP)"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Feedforward ka matlab hai "sirf aage bhejna". Is network me data hamesha seedha 
# input se shuru hota hai, hidden layers se guzarta hai aur output par khatam hota hai. 
# Isme koi chakkar (loops) nahi hote aur data kabhi lout kar peeche nahi aata. 
# Yeh ANN ki sabse purani aur aasan shakal hai jise Multilayer Perceptron (MLP) kehte hain.


# ----------------------------------------------------------------------------------
# POINT 2: Data Kaise Chalta Hai? (How Data Moves)
# "input feature enter -> each layer computes: z = wx + b -> a = σ(z)"
# "flow example: (input)feature -> hidden layer -> output -> external world"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Har ek layer ke andar do kaam hote hain:
# 1. z = wx + b : Inputs ko weights se multiply karke bias jama kiya jata hai.
# 2. a = σ(z) : Us 'z' ko activation function ke filter se guzar kar 'a' (activation) nikaala jata hai.
# Yeh 'a' agli layer ke liye naya input ban jata hai, aur aakhir me output bahar ki dunya ko dikha di jati hai.


# ----------------------------------------------------------------------------------
# POINT 3: Khubiyan Aur Istemal (Characteristics & Use Cases)
# "signal moves forward only, uses activation functions, learn weights+bias. 
# Best for tabular data. Not good for time series tasks."
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Faide: Yeh seedha tabular data (excel sheets), aasan images aur text features ke liye best hai.
# - Nuqsan: Yeh purani baatein yaad nahi rakh sakta, isiliye Time Series (jaise kal mausam kaisa hoga) ke liye acha nahi hai.
#  Wahan hum RNN ya LSTM use karte hain.


# ----------------------------------------------------------------------------------
# POINT 4: Architecture & Real Life Misaal
# "example: predicting car price (Regression). Input: mileage, age, engine size -> Output: price"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# Agar humein gaari ki keemat maloom karni ho:
# - Input Layer: Gaari kitni chali hai (mileage), kitni purani hai (age), aur engine kitna bada hai.
# - Hidden Layers: In sab baaton ko aapas me tolengi (weights lagayengi).
# - Output Layer: Gaari ki final estimated keemat batayegi (Regression Task).


# ----------------------------------------------------------------------------------
# POINT 5: Aapki Math Wali Numerical Misaal (Step-by-Step Calculation)
# "input x=2, weight w=1, bias b=0"
# ----------------------------------------------------------------------------------
# EXPLANATION:
# - Step 1 (Forward Pass): Sabse pehle formula laga: z = (x * w) + b = (2 * 1) + 0 = 2.
# - Step 2 (ReLU Activation): Ab is 'z=2' par ReLU function laga: f(x) = max(0, x). 
#   Kyunki 2 ek positive number hai, toh ReLU ne usay bilkul nahi chheda aur waisa hi 2 
#   baher bhej diya. Agar yeh minus me hota, toh ReLU usay 0 kar deta. Jawab aaya = 2.


# ----------------------------------------------------------------------------------
# TAKEAWAYS (Aakhiri Nichor)
# - Feed Forward = No Loops (Koi chakkar nahi).
# - Data hamesha Input se Output ki taraf jata hai.
# - Yeh dunya ke saare deep learning models ki asli buniyaad (foundation) hai.
# ==================================================================================