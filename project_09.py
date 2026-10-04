#=============================================
# PANDAS ANALYZER & DATA VISUALIZATION PROGRAM
#=============================================

#==============================================
# Author: Hitesh CHAUDHARY
#==============================================





import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class SalesDataAnalyzer:

    def __init__(self):
        self.df = None
        self.last_figure = None

    def get_column(self, name):

        name = str(name).strip().lower()

        for col in self.df.columns:

            clean_col = str(col).strip().lower()

            if clean_col == name:
                return col

        return None


    def load_dataset(self):

        print("\n== Load Dataset ==")

        path = input(
            "Enter the path of the dataset (CSV file): "
        ).strip()

        try:

            self.df = pd.read_csv(path)

            # Remove unwanted spaces from column names
            self.df.columns = (
                self.df.columns
                .astype(str)
                .str.strip()
            )

            print("Dataset loaded successfully!")

            print("\nColumns available:")

            print(list(self.df.columns))

        except FileNotFoundError:

            print("File not found!")
            print("Use: data/sales_data.csv")

        except Exception as e:

            print("Error loading dataset:", e)


    def explore_data(self):

        if self.df is None:

            print("Please load the dataset first!")
            return

        print("\n== Explore Data ==")

        print("1. Display the first 5 rows")
        print("2. Display the last 5 rows")
        print("3. Display column names")
        print("4. Display data types")
        print("5. Display basic info")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            print(self.df.head())

        elif choice == "2":

            print(self.df.tail())

        elif choice == "3":

            print(list(self.df.columns))

        elif choice == "4":

            print(self.df.dtypes)

        elif choice == "5":

            self.df.info()

        else:

            print("Invalid choice!")


    def dataframe_operations(self):

        if self.df is None:

            print("Please load the dataset first!")
            return

        print("\n== DataFrame Operations ==")

        print("1. Sort Data")
        print("2. Filter Data")
        print("3. Add Calculated Column")
        print("4. Group Data")
        print("5. Rename Column")
        print("6. Drop Column")

        choice = input("Enter your choice: ").strip()


        if choice == "1":

            print("\nAvailable columns:")
            print(list(self.df.columns))

            name = input(
                "Enter column name to sort by: "
            )

            column = self.get_column(name)

            if column is None:

                print("Column not found!")
                return

            order = input(
                "Enter order (asc/desc): "
            ).strip().lower()

            if order == "desc":

                self.df = self.df.sort_values(
                    by=column,
                    ascending=False
                )

            else:

                self.df = self.df.sort_values(
                    by=column
                )

            print("\nData sorted successfully!")
            print(self.df)


        elif choice == "2":

            print("\nAvailable columns:")
            print(list(self.df.columns))

            name = input(
                "Enter column name to filter: "
            )

            column = self.get_column(name)

            if column is None:

                print("Column not found!")
                return

            value = input(
                "Enter value: "
            ).strip()

            result = self.df[
                self.df[column].astype(str).str.strip().str.lower()
                == value.lower()
            ]

            print("\nFiltered Data:")

            if result.empty:

                print("No matching records found.")

            else:

                print(result)


        elif choice == "3":

            print("\nNumeric columns:")

            numeric = self.df.select_dtypes(
                include=np.number
            ).columns

            print(list(numeric))

            name = input(
                "Enter numeric column name: "
            )

            column = self.get_column(name)

            if column is None or column not in numeric:

                print("Invalid numeric column!")
                return

            new_column = input(
                "Enter new column name: "
            ).strip()

            self.df[new_column] = self.df[column] * 2

            print(
                "Calculated column added successfully!"
            )

            print(self.df)


        elif choice == "4":

            print("\nAvailable columns:")
            print(list(self.df.columns))

            name = input(
                "Enter column to group by: "
            )

            column = self.get_column(name)

            if column is None:

                print("Column not found!")
                return

            print("1. Sum")
            print("2. Mean")
            print("3. Count")

            operation = input(
                "Enter operation: "
            ).strip()

            numeric = self.df.select_dtypes(
                include=np.number
            ).columns

            if operation == "1":

                print(
                    self.df.groupby(column)[
                        numeric
                    ].sum()
                )

            elif operation == "2":

                print(
                    self.df.groupby(column)[
                        numeric
                    ].mean()
                )

            elif operation == "3":

                print(
                    self.df.groupby(column).size()
                )

            else:

                print("Invalid operation!")


        elif choice == "5":

            print("\nAvailable columns:")
            print(list(self.df.columns))

            old_name = input(
                "Enter old column name: "
            )

            old_column = self.get_column(old_name)

            if old_column is None:

                print("Column not found!")
                return

            new_name = input(
                "Enter new column name: "
            ).strip()

            self.df.rename(
                columns={
                    old_column: new_name
                },
                inplace=True
            )

            print(
                "Column renamed successfully!"
            )


        elif choice == "6":

            print("\nAvailable columns:")
            print(list(self.df.columns))

            name = input(
                "Enter column name to drop: "
            )

            column = self.get_column(name)

            if column is None:

                print("Column not found!")
                return

            self.df.drop(
                columns=[column],
                inplace=True
            )

            print(
                "Column dropped successfully!"
            )

        else:

            print("Invalid choice!")


    def handle_missing_data(self):

        if self.df is None:

            print("Please load the dataset first!")
            return

        print("\n== Handle Missing Data ==")

        print("1. Display rows with missing values")
        print("2. Fill missing values with mean")
        print("3. Drop rows with missing values")
        print("4. Replace missing values with a specific value")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            rows = self.df[
                self.df.isnull().any(axis=1)
            ]

            if rows.empty:

                print(
                    "No missing values found in the dataset!"
                )

            else:

                print(rows)

        elif choice == "2":

            numeric = self.df.select_dtypes(
                include=np.number
            ).columns

            for column in numeric:

                self.df[column] = self.df[column].fillna(
                    self.df[column].mean()
                )

            print(
                "Missing numeric values filled with mean!"
            )

        elif choice == "3":

            self.df.dropna(
                inplace=True
            )

            print(
                "Rows with missing values dropped!"
            )

        elif choice == "4":

            value = input(
                "Enter value to replace missing values: "
            )

            self.df.fillna(
                value,
                inplace=True
            )

            print(
                "Missing values replaced successfully!"
            )

        else:

            print("Invalid choice!")


    def descriptive_statistics(self):

        if self.df is None:

            print("Please load the dataset first!")
            return

        print("\n== Descriptive Statistics ==")

        numeric = self.df.select_dtypes(
            include=np.number
        )

        print("\n", numeric.describe())

        print("\nMean:")
        print(numeric.mean())

        print("\nMedian:")
        print(numeric.median())

        print("\nStandard Deviation:")
        print(numeric.std())

        print("\nMinimum:")
        print(numeric.min())

        print("\nMaximum:")
        print(numeric.max())


    def data_visualization(self):

        if self.df is None:

            print("Please load the dataset first!")
            return

        while True:

            print("\n== Data Visualization ==")

            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Back")

            choice = input(
                "Enter your choice: "
            ).strip()


            if choice == "1":

                print("\n== Bar Plot ==")

                print(
                    "Available columns:",
                    list(self.df.columns)
                )

                x_name = input(
                    "Enter x-axis column name: "
                )

                y_name = input(
                    "Enter y-axis column name: "
                )

                x = self.get_column(x_name)
                y = self.get_column(y_name)

                if x is None or y is None:

                    print(
                        "Invalid column name!"
                    )
                    continue

                print(
                    "Generating bar plot..."
                )

                fig, ax = plt.subplots(
                    figsize=(8, 5)
                )

                ax.bar(
                    self.df[x].astype(str),
                    self.df[y]
                )

                ax.set_xlabel(x)
                ax.set_ylabel(y)
                ax.set_title("Bar Plot")

                plt.xticks(rotation=30)
                plt.tight_layout()

                self.last_figure = fig

                plt.show()

                print(
                    "Bar plot displayed successfully!"
                )

            

            elif choice == "2":

                print("\n== Line Plot ==")

                print(
                    "Available columns:",
                    list(self.df.columns)
                )

                x_name = input(
                    "Enter x-axis column name: "
                )

                y_name = input(
                    "Enter y-axis column name: "
                )

                x = self.get_column(x_name)
                y = self.get_column(y_name)

                if x is None or y is None:

                    print(
                        "Invalid column name!"
                    )
                    continue

                print(
                    "Generating line plot..."
                )

                fig, ax = plt.subplots(
                    figsize=(8, 5)
                )

                ax.plot(
                    self.df[x],
                    self.df[y],
                    marker="o"
                )

                ax.set_xlabel(x)
                ax.set_ylabel(y)
                ax.set_title("Line Plot")

                plt.tight_layout()

                self.last_figure = fig

                plt.show()

                print(
                    "Line plot displayed successfully!"
                )


            elif choice == "3":

                print("\n== Scatter Plot ==")

                print(
                    "Available columns:",
                    list(self.df.columns)
                )

                x_name = input(
                    "Enter x-axis column name: "
                )

                y_name = input(
                    "Enter y-axis column name: "
                )

                x = self.get_column(x_name)
                y = self.get_column(y_name)

                if x is None or y is None:

                    print(
                        "Invalid column name!"
                    )
                    continue

                print(
                    "Generating scatter plot..."
                )

                fig, ax = plt.subplots(
                    figsize=(8, 5)
                )

                ax.scatter(
                    self.df[x],
                    self.df[y],
                    s=80
                )

                ax.set_xlabel(x)
                ax.set_ylabel(y)
                ax.set_title("Scatter Plot")

                plt.tight_layout()

                self.last_figure = fig

                plt.show()

                print(
                    "Scatter plot displayed successfully!"
                )


            elif choice == "4":

                print("\n== Pie Chart ==")

                print(
                    "Available columns:",
                    list(self.df.columns)
                )

                name = input(
                    "Enter column for pie chart: "
                )

                column = self.get_column(name)

                if column is None:

                    print(
                        "Invalid column name!"
                    )
                    continue

                print(
                    "Generating pie chart..."
                )

                counts = self.df[
                    column
                ].value_counts()

                fig, ax = plt.subplots(
                    figsize=(7, 7)
                )

                ax.pie(
                    counts.values,
                    labels=counts.index,
                    autopct="%1.1f%%"
                )

                ax.set_title(
                    "Pie Chart"
                )

                self.last_figure = fig

                plt.show()

                print(
                    "Pie chart displayed successfully!"
                )


            elif choice == "5":

                print("\n== Histogram ==")

                print(
                    "Numeric columns:",
                    list(
                        self.df.select_dtypes(
                            include=np.number
                        ).columns
                    )
                )

                name = input(
                    "Enter column for histogram: "
                )

                column = self.get_column(name)

                numeric = self.df.select_dtypes(
                    include=np.number
                ).columns

                if (
                    column is None
                    or
                    column not in numeric
                ):

                    print(
                        "Please enter a numeric column!"
                    )
                    continue

                print(
                    "Generating histogram..."
                )

                fig, ax = plt.subplots(
                    figsize=(8, 5)
                )

                ax.hist(
                    self.df[column],
                    bins=10
                )

                ax.set_xlabel(column)
                ax.set_ylabel("Frequency")
                ax.set_title("Histogram")

                plt.tight_layout()

                self.last_figure = fig

                plt.show()

                print(
                    "Histogram displayed successfully!"
                )


            elif choice == "6":

                print("\n== Stack Plot ==")

                numeric = list(
                    self.df.select_dtypes(
                        include=np.number
                    ).columns
                )

                print(
                    "Numeric columns:",
                    numeric
                )

                names = input(
                    "Enter numeric columns separated by comma: "
                )

                columns = []

                for name in names.split(","):

                    column = self.get_column(name)

                    if (
                        column is not None
                        and
                        column in numeric
                    ):

                        columns.append(column)

                if len(columns) < 2:

                    print(
                        "Please enter at least 2 valid numeric columns!"
                    )

                    print(
                        "Example: Sales,Year"
                    )

                    continue

                print(
                    "Generating stack plot..."
                )

                x = np.arange(
                    len(self.df)
                )

                data = [
                    self.df[column].values
                    for column in columns
                ]

                fig, ax = plt.subplots(
                    figsize=(8, 5)
                )

                ax.stackplot(
                    x,
                    data,
                    labels=columns
                )

                ax.set_xlabel(
                    "Records"
                )

                ax.set_ylabel(
                    "Values"
                )

                ax.set_title(
                    "Stack Plot"
                )

                ax.legend()

                plt.tight_layout()

                self.last_figure = fig

                plt.show()

                print(
                    "Stack plot displayed successfully!"
                )

            elif choice == "7":

                break

            else:

                print(
                    "Invalid choice!"
                )

    def save_visualization(self):

        print("\n== Save Visualization ==")

        if self.last_figure is None:

            print(
                "Please generate a visualization first!"
            )

            return

        filename = input(
            "Enter file name to save the plot "
            "(e.g., scatter_plot.png): "
        ).strip()

        if not filename:

            print(
                "File name cannot be empty!"
            )

            return

        try:

            self.last_figure.savefig(
                filename,
                dpi=300,
                bbox_inches="tight"
            )

            print(
                "Visualization saved successfully!"
            )

            print(
                "Saved at:",
                os.path.abspath(filename)
            )

        except Exception as e:

            print(
                "Error saving visualization:",
                e
            )

    def run(self):

        while True:

            print(
                "\n========== Data Analysis & Visualization Program =========="
            )

            print(
                "Please select an option:"
            )

            print(
                "1. Load Dataset"
            )

            print(
                "2. Explore Data"
            )

            print(
                "3. Perform DataFrame Operations"
            )

            print(
                "4. Handle Missing Data"
            )

            print(
                "5. Generate Descriptive Statistics"
            )

            print(
                "6. Data Visualization"
            )

            print(
                "7. Save Visualization"
            )

            print(
                "8. Exit"
            )

            print(
                "=========================================================="
            )

            choice = input(
                "\nEnter your choice: "
            ).strip()

            if choice == "1":

                self.load_dataset()

            elif choice == "2":

                self.explore_data()

            elif choice == "3":

                self.dataframe_operations()

            elif choice == "4":

                self.handle_missing_data()

            elif choice == "5":

                self.descriptive_statistics()

            elif choice == "6":

                self.data_visualization()

            elif choice == "7":

                self.save_visualization()

            elif choice == "8":

                print(
                    "Exiting the program. Goodbye!"
                )

                break

            else:

                print(
                    "Invalid choice! Please select 1-8."
                )




if __name__ == "__main__":

    analyzer = SalesDataAnalyzer()

    analyzer.run()