# Linear-and-Logistic-Regression-Models

These are various Linear and logistic regression models that I have created on my own over the course of mastering the basics of Artificial Intelligence and Machine Learning. I have attached the datasets followed by my algorithms, but the location of these must be manually copy-pasted onto the "with open" statement if any user wishes to test them. Additionally, users must manually enter data onto the list "test" at the bottom if they wish to test the model on certain values.

The csv file "Size vs Price data" is a dataset on houses in a particular area. The columns are as follows: Taxes, Bedrooms, Bathrooms, Total Size, Lot, Price 

The Linear regression programs will predict the price of a house if you enter the parameters in the test variable in the following order: Taxes, Bedrooms, Bathrooms, Total Size, Lot
It will first ask you the number of iterations that it must be trained for (The larger the number, the more accurate it gets in prediction!). It then commences training and prints the values of the parameters at each iteration of gradient descent along with the cost function. As you will see, the cost function will decrease over a number of iterations as the algorithm gets more accurate. At the end, it will predict the price of the house on the basis of the data you entered in the Test variable.

The Logistic regression program simply sets accurate parameters based on the very small dataset provided within the program.
