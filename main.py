import pandas as pd
import matplotlib.pyplot as plt

class Iris:
    # Read the CSV file into a Pandas DataFrame
    data = pd.read_csv("iris.data", header=None,
                       names=['sepal length', 'sepal width', 'petal length', 'petal width', 'iris_class'])

    def basic_data_manip(self):
        # Accessing individual columns
        sepal_length = self.data['sepal length']
        sepal_width = self.data['sepal width']
        petal_length = self.data['petal length']
        petal_width = self.data['petal width']
        iris_class = self.data['iris_class']

        # Create subsets based on specific conditions
        subset_setosa = self.data[self.data['iris_class'] == 'Iris-setosa']
        subset_long = self.data[self.data['petal length'] > 5.0]

        # Calculate descriptive statistics for individual columns
        sepal_length_stats = sepal_length.describe()
        sepal_width_stats = sepal_width.describe()
        petal_length_stats = petal_length.describe()
        petal_width_stats = petal_width.describe()

        return petal_length_stats

    def data_viz(self):
        # Bar plot for all dimensions
        dimensions = ['sepal length', 'sepal width', 'petal length', 'petal width']
        # Calculate descriptive statistics for each dimension
        stats = [self.data[column].describe() for column in dimensions]

        # Extract mean and standard deviation from statistics
        mean_lengths = [stat['mean'] for stat in stats]
        std_lengths = [stat['std'] for stat in stats]

        # Create a bar plot with error bars
        fig, ax = plt.subplots()
        ax.bar(dimensions, mean_lengths, yerr=std_lengths, capsize=5)
        ax.set_ylabel('Mean Dimensions')
        ax.set_title('Bar Plot for Mean Dimensions')

        plt.show()

    def filter_even_numbers(self, numbers):
        even_numbers = []
        # Filter even numbers from the input list
        for num in numbers:
            if num % 2 == 0:
                even_numbers.append(num)
        return even_numbers

    def create_squares_list(self, start, end):
        squares_list = []
        # Create a list of squares for numbers from start to end
        for num in range(start, end + 1):
            squares_list.append(num ** 2)
        return squares_list

    def unique(self):
        # Get unique values in the 'iris_class' column
        unique_values_set = set(self.data['iris_class'])
        return unique_values_set

    def corr(self):
        # Calculate the correlation between 'sepal length' and 'sepal width'
        correlation = self.data['sepal length'].corr(self.data['sepal width'])
        return correlation

def main():
    iris_instance = Iris()  # Create an instance of the Iris class
    result = iris_instance.basic_data_manip()
    print(result)

    graph = iris_instance.data_viz()
    print(graph)

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = iris_instance.filter_even_numbers(numbers)
    print("Even Numbers:", even_numbers)

    squares_list = iris_instance.create_squares_list(1, 10)
    print("Squares List:", squares_list)

    unq = iris_instance.unique()
    print("Unique values in the 'iris_class' column:", unq)

    corr = iris_instance.corr()
    print(f"Correlation between 'sepal length' and 'sepal width': {corr}")

if __name__ == '__main__':
    main()
