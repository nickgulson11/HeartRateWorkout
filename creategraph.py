import matplotlib.pyplot as plt

def graph(data):
    plt.switch_backend('Agg')
    data_int = [int(data[0]),int(data[1]),int(data[2]),int(data[3]),int(data[4])]
    plt.plot([50,100,150,200,250], data_int)
    plt.xlabel('Number of Jumping Jacks')
    plt.ylabel('Heat Rate (BPM)')
    plt.title("Heart Rate as Workouts Get Harder")
    plt.savefig('static/graph.png', bbox_inches='tight')
    return 
