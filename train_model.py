import csv

# def gradient (x1, x2, y1 , y2) :
#     return ((y1 -y2)/(x1 - x2))


def cost_function(theta0, theta1, data):
    error = 0
    for i in range(0, len(data)):
        error += data[i]['price'] - ((theta1 * data[i]['distance']) + theta0) ** 2
    return (error / float(len(data)))

def derivatives(data, theta0, theta1):
    derivative_theta1 = 0
    derivative_theta0 = 0
    for i in range(0, len(data)):
        y_calc = theta1 * float(data[i]['distance']) + theta0
        derivative_theta1 += ((float(data[i]['price']) - y_calc) *  float(data[i]['distance']))
        derivative_theta0 += (float(data[i]['price']) - y_calc)
    derivative_theta0 = -2 * (derivative_theta0/(len(data)))
    derivative_theta1 = -2 * (derivative_theta1/(len(data)))
    return (derivative_theta1, derivative_theta0)

def train_model():
    dataset = []
    theta1 = 0
    theta0 = 0
    learning_rate = 0.000000001
    iterations = 100000
    with open('Honda CRV.csv', mode='r') as csv_file:
        dataset = list(csv.DictReader(csv_file, delimiter=';'))
    for i in range(0, iterations):
        (derTheta1, derTheta0) = derivatives(dataset, theta0, theta1)
        theta1 = theta1 - learning_rate * derTheta1
        theta0 = theta0 - learning_rate * derTheta0
        # print(theta1)
        # print(theta0)
    print(theta0*67503 + theta0)

if __name__ == "__main__":
    	train_model()     

#true_car_listings.csv price_in_$;mileage