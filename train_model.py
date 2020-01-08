import csv

# def gradient (x1, x2, y1 , y2) :
#     return ((y1 -y2)/(x1 - x2))


def cost_function(theta0, theta1, data):
    error = 0
    for i in range(0, len(data)):
        error += (data[i]['price'] - ((theta1 * data[i]['distance']) + theta0)) ** 2
        print(error)
    return (error / float(len(data)))

def format_data(data):
    for i in range(0, len(data)):
        data[i]['price'] = float(data[i]['price'])/10000
        data[i]['distance'] = float(data[i]['distance'])/10000
    return data

def derivatives(data, theta0, theta1):
    derivative_theta1 = 0
    derivative_theta0 = 0
    for i in range(0, len(data)):
        y_calc = data[i]['price'] - theta1 * data[i]['distance'] + theta0
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
    learning_rate = 0.00001
    iterations = 50
    with open('Honda CRV.csv', mode='r') as csv_file:
        dataset = list(csv.DictReader(csv_file, delimiter=';'))
    dataset = format_data(dataset)
    for i in range(0, iterations):
        (derTheta1, derTheta0) = derivatives(dataset, theta0, theta1)
        theta1 = theta1 - learning_rate * derTheta1
        theta0 = theta0 - learning_rate * derTheta0
        # print(derTheta1)
        # print(derTheta0)
    print(cost_function(theta0, theta1, dataset))
    print(theta1*2 + theta0)

if __name__ == "__main__":
    	train_model()     

#true_car_listings.csv price_in_$;mileage