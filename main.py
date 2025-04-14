import pandas as pd
import data_loader as dl
import data_processor as dp
import data_visualizer as dv

def main():
    path = "population.csv"
    #load data
    data = dl.load_dataset(path)
    
    #Process data
    pd = dp.process_data(data)

    #visualize data
    dv.plot_pop(pd)
    dv.plot_scatter(pd)

if __name__ == "__main__":
    main()
