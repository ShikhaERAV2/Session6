# PART 1 :- Back Propagation using the EXCEL

## Back Propagation Snapshot
![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/40d12f5c-d1a4-4229-9a4f-35df271aa78a)

## Neural Network Diagram used for the Back Propagation
- 2 Input Neurons(i1,i2)-> 1 Hidden Layer with 2 Neurons(h1,h2)-> Activation function (out_h1,out_h2)-> output Layer with 2 Neurons(o1,o2)-> Activation Funtion (out_o1,out_o2)->Error(E1,E2)->Total Error (E_Total)
- Weights input to hidden layer ( w1-w4)
- weights hidden layer ->output (w5-w8)

## Back Propagtion Mathematical Calculations

![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/0e6d3fef-f12c-46a0-a362-25f6554558e5)

	
![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/38d531c2-96d1-4187-9b35-8d3994fe960e)

				
![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/ef896db5-4dd8-4197-a0d0-e197f3c15ab6)

				
![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/1ade547d-224e-4408-97f8-4d2675f0ac88)					
				

![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/ca6ea995-a726-4173-8fda-16b52602b504)

					
![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/6f2dbef7-c3f9-47c9-8b46-690a5838eca4)

											
![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/ade6cb29-d894-4276-8d8e-c93dd555691d)

## Back Propagation Loss Plot based on Change in Learning Rate

![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/c05164b7-d410-4bc2-89b0-296e51a0d44a)


# PART 2 :- CNN for Image Classification on MNIST Dataset
This CNN is created to classify the handwritten images of digits 0-9 in the MNIST dataset. The neural network is defined to identify the handwritten digits into 10 classes. 
I/P :- MNIST dataset. 
O/P :- 10 classes.

## MNIST dataset 
MNIST is a dataset of handwritten digits from 0-9.


![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/ca4b764d-2776-4776-bf7c-67fe1f9163ff)

## Model Description
This is a Multiple  convolution layers in Convolutional Neural Network for digits identification trained on MNIST dataset. Added dropout and batch normalization to improve the accuracy of the model.
Batch normalization is added after couple of convolution layers and Dropout is added away from the last layer

## Code Structure 
- `S6_Final.ipynb`: The main Jupyter Notebook contains the code to load data in train and test datasets -> transform data-> load model (defined in model.py)-> train  model -> test the model -> Check the accuracy of the model thus trained. 
- `model.py`: This file contains the definition of the model. Basic architecture of the model is defined with multiple convolution layers and fully connected layers. 
- `utils.py`: This file contains the utility functions like display of the sample data images and plotting the accuracy and loss during training. 

## Requirements
- Pytorch
- Matplotlib

## Model Accuracy
- Test Accuracy = 99.23%
- Average loss = 0.0237
  
- Training accuracy =  99.75%
- Average Loss = 0.0019
- epochs = 19

![image](https://github.com/ShikhaERAV2/Session6/assets/160948226/f256495d-fc4a-401d-82c5-83d3589764da)



 

