import numpy
import numpy as np
import math

def normalizar(x,xmin,xmax):
    return (x-xmin)/(xmax-xmin)
def mapeo_normalizar(x,xmin,xmax):
     return (x*(xmax-xmin)) +xmin

def lineal(data_x,dec=False,tool='mpl'):
    x_min =min(data_x)
    x_max =max(data_x)
    if tool=='mpl' and dec==False:
        y = [round((x-x_min)/(x_max-x_min),3) for x in data_x]
        return y
    elif tool=='mpl' and dec==True:
        y = [round((x_max-x)/(x_max-x_min),3) for x in data_x]
        return y
    elif tool =='gcalc' and dec==False:
        expression = f'numpy.round(((A - {x_min})/({x_max} - {x_min})),3)'
        return expression
    elif tool =='gcalc' and dec==True:
        expression = f'numpy.round((({x_max} - A)/({x_max} - {x_min})),3)'
        return expression 


def logistica(x_data,xc,xmin,xmax,alpha,dec=False,tool='mpl'):
    if alpha==0.0:
            alpha =0.01
    X_l =np.array(lineal(x_data))
    X_c= normalizar(xc,xmin,xmax)
    B = (100*(X_l-X_c))/alpha
    if tool=='mpl'and dec==False:
        y_ = [round((1/(1+math.exp(-b_i))),3) for b_i in B]
        y =  [round((y_i-min(y_))/(max(y_)-min(y_)),3) for y_i in y_]  
        return y
    elif tool=='mpl'and dec==True:
        y_ = [round(1-(1/(1+math.exp(-b_i))),3) for b_i in B]
        y =  [round((y_i-min(y_))/(max(y_)-min(y_)),3) for y_i in y_]  
        return y
    elif tool =='gcalc' and dec==False:
        expression = f'numpy.round(1/(1+exp(-((100/{alpha})*( ((A-{xmin})/({xmax}-{xmin}))-{X_c}) ))),3)'
        return expression
    elif tool =='gcalc' and dec==True:
        expression = f'numpy.round(1-(1/(1+exp(-((100/{alpha})*( ((A - {xmin})/({xmax} - {xmin}))-{X_c}) )))),3)'
        return expression 
    
def concava(x_data,xmin,xmax,gamma,dec=False,tool='mpl'):
    if gamma==0:
            gamma =0.01
    X_l =np.array(lineal(x_data))
   
    if tool=='mpl'and dec==False:
        X_gamma = (1-X_l)*gamma
        y_ = [round(1-((math.exp(b_i)-1)/(math.exp(gamma)-1)),3) for b_i in X_gamma]
        y =  [round((y_i-min(y_))/(max(y_)-min(y_)),3) for y_i in y_]  
        return y
    elif tool=='mpl'and dec==True:

        X_gamma = X_l*gamma
        y_ = [round(1-((math.exp(b_i)-1)/(math.exp(gamma)-1)),3) for b_i in X_gamma]
        y =  [round((y_i-min(y_))/(max(y_)-min(y_)),3) for y_i in y_]  
        return y
    elif tool =='gcalc' and dec==False:
        A_ec =f'(1-((A-{xmin})/({xmax}-{xmin})))*{gamma}'
        expression = f'numpy.round(1-((exp({A_ec})-1) /(exp({gamma})-1)) ,3)'
        return expression
    elif tool =='gcalc' and dec==True:
        expression = f'numpy.round(1-((exp((((A-{xmin})/({xmax}-{xmin}))*{gamma})-1)/(exp({gamma})-1))),3)'
        return expression 
def convexa(x_data,xmin,xmax,gamma,dec=False,tool='mpl'):
    if gamma==0:
            gamma =0.01
    X_l =np.array(lineal(x_data))
   
    if tool=='mpl'and dec==False:
        X_gamma = X_l*gamma
        y_ = [round(((math.exp(b_i)-1)/(math.exp(gamma)-1)),3) for b_i in X_gamma]
        y =  [round((y_i-min(y_))/(max(y_)-min(y_)),3) for y_i in y_]  
        return y
    elif tool=='mpl'and dec==True:
        X_gamma = (1-X_l)*gamma
        y_ = [round(((math.exp(b_i)-1)/(math.exp(gamma)-1)),3) for b_i in X_gamma]
        y =  [round((y_i-min(y_))/(max(y_)-min(y_)),3) for y_i in y_]  
        return y
    elif tool =='gcalc' and dec==False:
        expression = f'numpy.round((exp(((A-{xmin})/({xmax}-{xmin}))*{gamma})-1)/(exp({gamma})-1),3)'
        return expression
    elif tool =='gcalc' and dec==True:
        expression = f'numpy.round((exp((1-((A-{xmin})/({xmax}-{xmin})))*{gamma})-1)/(exp({gamma})-1),3)'
        return expression 

def campana(x_data,xc,xmin,xmax,alpha,dec=False,tool='mpl'):
    if alpha==0:
            alpha =0.01
    X_l =np.array(lineal(x_data))
    X_c= normalizar(xc,xmin,xmax)
    B = (100*(X_l-X_c))/alpha
    BB = B**2
    if tool=='mpl'and dec==False:
        y_ = [round(math.exp(-b_i),3) for b_i in BB]
        y =  [round((y_i-min(y_))/(max(y_)-min(y_)),3) for y_i in y_]  
        return y
    elif tool=='mpl'and dec==True:
        y_ = [round(1-math.exp(-b_i),3) for b_i in BB]
        y =  [round((y_i-min(y_))/(max(y_)-min(y_)),3) for y_i in y_]  
        return y
    elif tool =='gcalc' and dec==False: ## entra la capa raster normalizada linealmente
        expression = f'numpy.round(exp(-(numpy.power((100*(((A-{xmin})/({xmax}-{xmin}))-{X_c}))/{alpha},2))),3)'
        return expression
    elif tool =='gcalc' and dec==True:
        expression = f'numpy.round(1- exp(-(numpy.power((100*(((A-{xmin})/({xmax}-{xmin}))-{X_c}))/{alpha},2))),3)'
        return expression 