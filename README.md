# Requeriments
##### Version
- Python version >= 3.6
##### Modules
- Matplotlib
- Numpy
- Math

##### Optional
Follow the instructions that are in the next link to add text rendering support with LaTeX:

http://matplotlib.org/users/usetex.html

# Guide
## Example 1
* This guide uses experimental data *

| Distance              | Time                       |
|-----------------------|----------------------------|
| x<sub>1</sub> = 0.1 m | t<sub>1</sub> = 0.7805 s   |
| x<sub>2</sub> = 0.2 m | t<sub>2</sub> = 1.099 s    |
| x<sub>3</sub> = 0.3 m | t<sub>3</sub> = 1.3265 s   |
| x<sub>4</sub> = 0.4 m | t<sub>4</sub> = 1.51775 s  |
| x<sub>5</sub> = 0.5 m | t<sub>5</sub> = 1.7185 s   |
| x<sub>6</sub> = 0.6 m | t<sub>6</sub> = 1.8835 s   |
| x<sub>7</sub> = 0.7 m | t<sub>7</sub> = 2.048 s    |
| x<sub>8</sub> = 0.8 m | t<sub>8</sub> = 2.18775 s  |
| x<sub>9</sub> = 0.9 m | t<sub>9</sub> = 2.32175 s  |
| x<sub>10</sub> = 1 m  | t<sub>10</sub> = 2.44975 s |

1.- Execute the script using one of the following commands:

`python main.py`

or:

`ipython main.py`

or:

Give execute permission to the main.py file

`chmod +x main.py`

and execute it with:

`./main.py`

It's recommended to add the data in a .csv file, where a row is the data of a variable, like you can see in the following image:

<img src="https://raw.github.com/index-0/Regresion/master/Images/csv.png" alt=".csv file example" width="550" height="94">

To execute the script with the .csv file:

`python main.py datafile.csv`

2.- Choice the regression method

Input '1' for power regression or input '2' for linear regression.

3.- Input the names of the variables

If you want to use 't' in the x axis then input 't' in the first prompt.

If you want to use 'x' in the y axis then input 'x' in the second prompt.

3.1.- In case that a .csv file wasn't given, you will need to input the data manually

4.- Input the unit of the variables

If the unit of the first variable (x axis) are seconds then input 's' or 'seconds' or: '\textnormal{seconds}' in case LaTeX is enabled and the same goes for the y axis.

5.- Graph of the given data (Optional)

![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/figure_1.png)

6.- Choice the equation y(x) or x(y)

If you want to compute the equation y(x) then input '1' or if you want to compute the equation x(y) then input '2'.

7.- Graph of the equation (Optional)

![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/figure_2.png)

8.- Graph of the comparison (Optional)

![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/figure_3.png)

9.- A .csv file will be saved in the script dir
![ScreenShot](https://raw.github.com/index-0/Regresion/master/Images/saved_csv_file.png)
