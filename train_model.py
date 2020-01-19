import csv
import matplotlib.pyplot as plt
import numpy as np

# def gradient (x1, x2, y1 , y2) :
#     return ((y1 -y2)/(x1 - x2))


def cost_function(theta0, theta1, data):
    error = 0
    print(len(data))
    for i in range(0, len(data)):
        error += (data[i]['price'] - ((theta1 * data[i]['distance']) + theta0)) ** 2
        # print(error)
    return (error / float(len(data)))

def format_data(data):
    dataset = []
    for i in range(0, len(data)):
        data[i]['price'] = float(data[i]['price'])/10000
        data[i]['distance'] = float(data[i]['distance'])/10000
        dataset.append(data[i])
    return dataset

def derivatives(data, theta0, theta1):
    derivative_theta1 = 0
    derivative_theta0 = 0
    for i in range(0, len(data)):
        y_calc = data[i]['price'] - (theta1 * data[i]['distance'] + theta0)
        # print(y_calc)
        derivative_theta1 += (y_calc *  data[i]['distance'])
        derivative_theta0 += y_calc
    # print(derivative_theta0)
    derivative_theta0 = (-2/len(data)) * derivative_theta0
    derivative_theta1 = (-2/len(data)) * derivative_theta1
    return (derivative_theta1, derivative_theta0)

def train_model():
    dataset = []
    theta1 = 0
    theta0 = 0
    learning_rate = 0.000016
    iterations = 5000
    with open('mazda_used_car_dataset.csv', mode='r') as csv_file:
        dataset = list(csv.DictReader(csv_file, delimiter='\t'))
    dataset = format_data(dataset)
    for i in range(0, iterations):
        (derTheta1, derTheta0) = derivatives(dataset, theta0, theta1)
        theta1 = theta1 - learning_rate * derTheta1
        theta0 = theta0 - learning_rate * derTheta0
        # print(derTheta1)
        # print(derTheta0)
    print(cost_function(theta0, theta1, dataset))
    print(theta1)
    print(theta0)
    x = []
    y =[]
    for i in range(0, len(dataset)):
        x.append(dataset[i]['distance'])
        y.append(dataset[i]['price'])
    colors = (0,0,0)
    area = np.pi*3
    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    x1 = np.linspace(40,0,100)
    y2 = theta1*x1+theta0
    plt.plot(x1, y2, 'r', label='y')
    plt.title('Graph of mileage vs price_usd')
    plt.legend(loc='upper left')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

if __name__ == "__main__":
    	train_model()     

#true_car_listings.csv price_in_$;mileage