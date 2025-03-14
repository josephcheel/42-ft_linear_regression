<!--HEADER-->
<h1 align="center"> Linear Regression | 
 <picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://cdn.simpleicons.org/42/white">
  <img alt="42" width=40 align="center" src="https://cdn.simpleicons.org/42/Black">
 </picture>
 Advanced 
  <!-- <img alt="Complete" src="https://raw.githubusercontent.com/Mqxx/GitHub-Markdown/main/blockquotes/badge/dark-theme/complete.svg"> -->
</h1>
<!--FINISH HEADER-->

<!--MINI DESCRIPTION-->
> This project implements linear regression using a dataset to predict a dependent variable based on an independent variable. It involves data preprocessing, making predictions, and visualizing results using matplotlib. The final output is a scatter plot with a fitted regression line, showcasing the model’s accuracy.

![Linear regression window of the program](https://github.com/josephcheel/42-ft_linear_regression/blob/5318703d32b434d7ee0b5d9420e4b6d942582c26/readme/ft_linear_regression.webp)

> [!IMPORTANT]  
> When refering in the project about theta0($\theta_0$) and theta1($\theta_1$) in the project:
> * theta0($\theta_0$) is the intercept, and can be used interchangeably with the term "intercept." It represents the value of 𝑦 when 𝑥=0.
> * theta1($\theta_1$) is the slope, and can be used interchangeably with the term "slope." It represents how much 𝑦 changes for each unit increase in 𝑥.

### Install Dependencies
```bash
. ./install.sh
```
### Linear Regression Program
Computes a Linear Regression using Gradient Descend Algorithm with the dataset specified.
* use --dataset or -d to specify a dataset
* use --graphical or -g to open a graph window with the result
* use --output or -o to save the result in a json format file 
##### for more information about options use:
```bash
python3 linear_regression.py -h
```
Try:
```bash
python3 linear_regression.py --dataset datasets/data.csv --graphical
```
### Linear Predictor Program
This program calculates the predicted value of Y based on a given X value using a simple linear equation \( Y = $theta_0$ + $theta_1$ · X \)

* use --theta0 or -t0 to specify the theta0 or intercept
* use --theta1 or -t1 to specify the theta1 or slope
* use --json or -j for input a json with theta0 and theta1 result from the previous program
##### for more information about options use:
```bash
python3 linear_predictor.py -h
```
Try:
```bash
python3 linear_predictor.py --theta0 8474.34137591075 --theta1 -0.021199045602042395
```
