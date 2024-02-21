import pandas as pd
import sys
import matplotlib.pyplot as plt
import os

class DataProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.df = self.read_csv_file()

    def read_csv_file(self):
        extension = os.path.splitext(self.filename)
        if extension[1] != ".csv":
            raise FileNotFoundError("Please check the file name and extension (e.g. filename.csv)")
        df = pd.read_csv(self.filename)
        df = df.set_index(df.columns[0])
        
        df = self.fill_na_values(df)
        return df

    @staticmethod
    def fill_na_values(df):
        int_float_cols = df.select_dtypes(include=['int', 'float']).columns
        df[int_float_cols] = df[int_float_cols].fillna(value=0)
        object_cols = df.select_dtypes(include="object").columns
        df[object_cols] = df[object_cols].fillna(value="-")
        return df

    def filter_data(self, columns):
        self.df = self.df[columns]

    def get_summary_stats(self):
        print("\nSummary statistics table")
        print(self.df.describe(include='all'))

    def plot(self, attr):
        try:    
            self.df.plot(kind=attr[0], title=attr[1], xlabel=attr[2], ylabel=attr[3], use_index=True)
        except:
            print("Please enter valid attributes")

    def save_processed_data(self):
        self.df.to_csv(f'Processed_{self.filename}', index=False)

def process_data(filename):
    data_processor = DataProcessor(filename)
    print(data_processor.df)
    
    filter = input("\nDo you want to filter the data? (Yes or no)\n")
    if filter.lower() == "yes":
        columns = input("Enter the column/s to filter by: (Separate by comma if more than one)\n").split(",")
        data_processor.filter_data(columns)        
        print("\nFiltered data\n", data_processor.df)
        data_processor.save_processed_data()
        
    data_processor.get_summary_stats()
    
    plots = input("\nDo you want to make a plot? (Yes or no)\n")
    if plots.lower() == "yes":
        attributes = input("\nEnter the following in comma-separated form:\n"
                    +"  Kind: \'line or bar or hist(histogram)\'\n"
                    +"  Title: \'Title of the plot\'\n"
                    +"  X-Label: \'X-Label of the plot\'\n"
                    +"  Y-Label: \'Y-Label of the plot\'\n\n")
        
        data_processor.plot(attributes.split(","))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        filename = input("Enter the filename :\n")
    else:
        filename = sys.argv[1]
    process_data(filename)
    plt.show()
