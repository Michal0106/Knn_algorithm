def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            line = line.replace(',','.').split()
            attributes = list(map(float, line[:-1]))
            decision_attribute = line[-1]
            data.append([attributes, decision_attribute])
    return data

def count_euclidean_distance(val1,val2):
    sum = 0
    for i in range(len(val1)):
        sum += (val2[i] - val1[i]) ** 2
    return sum ** 0.5

def knn_algorithm(train_data, test_instance, k):
    distances = []
    for data_instance in train_data:
        distances.append([data_instance, count_euclidean_distance(test_instance[0], data_instance[0])])

    sorted_distances = sorted(distances, key=lambda x: x[1])
    most_common = {}
    for i in sorted_distances[:k]:
        if most_common.get(i[0][1]) is None:
            most_common[i[0][1]] = 1
        else:
            most_common[i[0][1]] += 1
    sorted_most_common = sorted(most_common.items(), key=lambda x: (-x[1], next((idx for idx, item in enumerate(sorted_distances) if item[0][1] == x[0]), None)))
    most_common_value = sorted_most_common[0][0]
    return most_common_value


def main():
    training_data = read_file("iris_training.txt")
    test_data = read_file("iris_test.txt")

    while True:
        try:
            k = int(input("Type in k value:"))
            if k > 0: break
            else: raise ValueError
        except ValueError:
            print("Wrong value, type k one more time")

    positive_test = 0
    all_tests = len(test_data)
    for test_instance in test_data:
        expected_value = test_instance[1]
        real_value = knn_algorithm(training_data,test_instance,k)
        positive_test += (1 if expected_value == real_value else 0)
        print("for k value =",k,"expected value was:",expected_value,",real value is",real_value,'\n')
    print("number of positive tests =",positive_test, ",out of",all_tests)
    print("test correctness = ",round(positive_test/all_tests,3),'%')
    while True:
        try :
            attributes_input = input("Enter attributes separated by white space (e.g., 5.1 3.5 1.4 0.2): ").replace(',','.')
            if len(attributes_input.split()) == 0 : raise ValueError
            attributes = list(map(float, attributes_input.split()))
            predicted_label = knn_algorithm(training_data, (attributes, ''), k)
            print("Predicted label:", predicted_label.upper())
            continue_input = input("Do you want to continue (y/n)? ").strip().lower()
            if continue_input != 'y':
                break
            k_changing = input("Do you want to change k (y/n)?")
            if k_changing == 'y':
                k = int(input("Type in k value:"))
        except ValueError:
            print("You typed wrong values")


main()
