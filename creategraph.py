import matplotlib.pyplot as plt

def graph(data):
    plt.switch_backend('Agg')
    plt.plot([50,100,150,200,250], data)
    plt.xlabel('Number of Jumping Jacks')
    plt.ylabel('Heat Rate (BPM)')
    plt.title("Heart Rate as Workouts Get Harder")
    plt.savefig('static/graph.png', bbox_inches='tight')
    return 
