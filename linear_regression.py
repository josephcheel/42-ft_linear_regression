import numpy as np
import matplotlib.pyplot as plt
import argparse
import sys
import signal

LEARNING_RATE = 0.01
MINIMUM_STEP_SIZE = 0.0001
MAXIMUM_NUMBER_OF_STEPS = 1000
STARTING_THETA0 = 0
STARTING_THETA1 = 0

error_list = []
def handle_interrupt(signal, frame):
    print("Ctrl+C detected! Closing the figure.")
    plt.close('all')
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

def linear_regression_window(original_x, original_y, theta0, theta1):
    plt.figure(figsize=(10, 6))
    plt.grid()
    plt.title(TITLEPLT)
    plt.gcf().canvas.manager.set_window_title('ft_linear_regression')
    plt.xlabel(LABELX)
    plt.ylabel(LABELY)
    plt.scatter(original_x, original_y, color='red', label='Data')

    # Plot regression line
    x_sorted = np.sort(original_x)
    y_predicted = theta0 + theta1 * x_sorted
    plt.plot(x_sorted, y_predicted, color='blue', label=f"y = {theta1:.3f}…x + {theta0:.3f}…")

    plt.legend()
    plt.show()

def error_window(error_list):
    plt.figure(figsize=(10, 6))
    plt.grid()
    plt.title('Error vs. Steps')
    plt.gcf().canvas.manager.set_window_title('ft_linear_regression errors')
    plt.xlabel('Steps/Iterations')
    plt.ylabel('Error')
    plt.plot(range(len(error_list)), error_list, color='red', label='Error')
    plt.legend()
    plt.show()

def mean_bias_error(observed_x, observed_y, intercept, slope):
    
    m = len(observed_x)
    predicted_values = intercept + slope * observed_x

    errors = predicted_values - observed_y

    gradient_intercept = (1 / m) * np.sum(errors)
    gradient_slope = (1 / m) * np.sum(errors * observed_x)

    new_intercept = intercept - LEARNING_RATE * gradient_intercept
    new_slope = slope - LEARNING_RATE * gradient_slope
    
    return new_intercept, new_slope, errors

def ft_gradient_descend(theta0, theta1, observed_y, observed_x, errors):

    for step in range(MAXIMUM_NUMBER_OF_STEPS):
        new_theta0, new_theta1, error = mean_bias_error(observed_x, observed_y, theta0, theta1)
        if errors:
            error_list.append(np.mean(error**2))
    
        if abs(new_theta0 - theta0) < MINIMUM_STEP_SIZE and abs(new_theta1 - theta1) < MINIMUM_STEP_SIZE:
            print(f"Converged at step {step}")
            break

        theta0, theta1 = new_theta0, new_theta1

    return theta0, theta1

def standardization(data):
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    return (data - mean) / std, mean, std

def ft_linear_regression(data, errors):
    
    # Standardize the data
    data, mean_x, std_x = standardization(data)
    standarized_x = data[:, 0]
    standarized_y = data[:, 1]

    theta0, theta1 = ft_gradient_descend(STARTING_THETA0, STARTING_THETA1, standarized_y, standarized_x, errors)

    # Reverse the standardization
    theta1 = theta1 * (std_x[1] / std_x[0])
    theta0 = theta0 * std_x[1] + mean_x[1] - theta1 * mean_x[0]
    
    return theta0, theta1


def parse_dataset(file_path, delimiter=',', skip_header=True):
    try:
        data = np.genfromtxt(file_path, delimiter=delimiter, skip_header=skip_header)
    except FileNotFoundError:
        print(f"File {file_path} not found. Please specify a valid path with option --dataset or -d", file=sys.stderr)
        exit(1)
    except PermissionError:
        print(f"Permission denied to access file {file_path}. Please check the permissions.", file=sys.stderr)
        exit(1)
    except Exception as e:
        print(f"An error occurred while parsing the dataset: {e}", file=sys.stderr)
        exit(1)
    return data

def output_result(theta0, theta1, output_file):
    try:
        open(output_file, "w").write(f"{{\"theta0\": {theta0}, \"theta1\": {theta1}}}")
        print(f"Results successfully saved to {output_file}")
    except PermissionError:
        print(f"Permission denied to write to file {output_file}. Please check the permissions.", file=sys.stderr)

# theta0 = intercept
# theta1 = slope

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(
        description="Computes a Linear Regression using the Gradient Descent Algorithm with the specified dataset.")

    # Dataset-related arguments
    dataset_group = argparser.add_argument_group('Dataset Options')
    dataset_group.add_argument('--dataset', "-d", type=str, default='./data.csv', help="Path to the dataset.")
    dataset_group.add_argument('--delimiter', "-del", type=str, default=',', help="Delimiter for the dataset.")
    dataset_group.add_argument('--skip_header', action="store_false", help="Skip header of the dataset.")

    # Plotting options
    plot_group = argparser.add_argument_group('Plotting Options')
    plot_group.add_argument('--graphical', "-g", action="store_true", help="Show graphical representation of the dataset.")
    plot_group.add_argument('--errors', "-e", action="store_true", help="Show error graph.")
    plot_group.add_argument('--labelx', "-lx", type=str, default='X values', help="X-axis label.")
    plot_group.add_argument('--labely', "-ly", type=str, default='Y values', help="Y-axis label.")
    plot_group.add_argument('--title', "-t", type=str, default='Linear Regression Plot', help="Title of the plot.")

    # Algorithm options
    algo_group = argparser.add_argument_group('Algorithm Options')
    algo_group.add_argument('--learning_rate', "-lr", type=float, default=0.01, help="Learning rate for the Gradient Descent algorithm.")

    # Output options
    output_group = argparser.add_argument_group('Output Options')
    output_group.add_argument('--output', "-o", nargs='?', const='result.json', type=str, default='', help="Output file for the results as JSON. (default: result.json)")

    # Parse arguments
    args = argparser.parse_args()
    delimiter = args.delimiter
    dataset_path = args.dataset
    LABELX = args.labelx
    LABELY = args.labely
    TITLEPLT = args.title
    LEARNING_RATE = args.learning_rate
    skip_header = args.skip_header

    data = parse_dataset(dataset_path, delimiter=delimiter, skip_header=skip_header)

    
    if data is None or data.size == 0 or len(data.shape) != 2 or data.shape[1] != 2 or data.shape[0] < 2:
        print("Error: CSV file has an incorrect format. Possible issues include too many columns, too few rows, or mismatched data. Exiting...")
        exit(1)

    valid_rows = ~np.isnan(data).any(axis=1)
    cleaned_data = data[valid_rows]

    if cleaned_data is None or cleaned_data.size == 0 or len(cleaned_data.shape) != 2 or cleaned_data.shape[1] != 2 or cleaned_data.shape[0] < 2:
        print("Error: CSV file has an incorrect format. Possible issues include too many columns, too few rows, or mismatched data. Exiting...")
        exit(1)
    
    print(cleaned_data.shape, len(cleaned_data.shape))
    original_x = cleaned_data[:, 0].copy()
    original_y = cleaned_data[:, 1].copy()

    theta0, theta1 = ft_linear_regression(cleaned_data, args.errors)

    print(f"Theta0: {theta0}, Theta1: {theta1}")
    if args.output:
        output_result(theta0, theta1, args.output)
    if args.errors:
        if error_list:
            print(f"Last Error: {error_list[-1]}")

    if args.graphical:
        linear_regression_window(original_x, original_y, theta0, theta1)

    if args.errors:
        error_window(error_list)
