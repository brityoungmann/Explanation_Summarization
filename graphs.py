import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import Utils

import case_study


def atts(att, time, bf,et, r=None):
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)


    plt.plot(att, time, marker='o', markersize=10, linestyle='-', color='#332288', label='CauSumX', linewidth=4.5)
    # plt.plot(att, ids, marker='+', linestyle='-', color='r', label='IDS', linewidth=2.5)
    if et:
        plt.plot(att, et, marker='^', markersize=10, linestyle='-', color='#CC6677', label='Explanation Table',
                 linewidth=4.5)
    plt.plot(att, bf, marker='p', markersize=10, linestyle='-', color='#1177AA', label='Brute Force', linewidth=4.5)

    # Add labels and title
    #plt.xlabel('number of attributes',fontweight='bold', fontsize=28)
    plt.ylabel('time (s)', fontweight='bold', fontsize=28)
    if r:
        att = r#(3, 45, 5)
    plt.xticks(att)
    plt.legend()
    #plt.title('Time vs. attributes')

    # Show the graph
    #plt.tight_layout()
    plt.show()

def variants_in_depth_cov():
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)

    att = [1,2,3,4,5,6,7,8,9,10]
    cpe = [0.3, 0.7, 0.8, 1, 1, 1, 1, 1, 1, 1]
    greedy = [0.2, 0.3, 0.5, 0.6, 0.7, 0.9, 0.95, 0.98, 1, 1]

    # Create the line graph

    plt.plot(att, cpe, marker='o',markersize=10, linestyle='-', color='#332288', label='CauSumX', linewidth=4.5)
    # plt.plot(att, ids, marker='+', linestyle='-', color='r', label='IDS', linewidth=2.5)

    plt.plot(att, greedy, marker='^',markersize=10, linestyle='-', color='#CC6677', label='Greedy-Last-Step', linewidth=4.5)

    # Add labels and title
    plt.xlabel('Solution size',fontweight='bold', fontsize=24)
    plt.ylabel('Coverage', fontweight='bold', fontsize=28)
    plt.xticks(att)
    plt.axhline(y=0.75, color='black', linestyle='--', linewidth=2)  # Add horizontal line at 6.6
    plt.legend()
    #plt.tight_layout()
    #plt.title('Time vs. attributes')

    # Show the graph
    plt.show()


def variants_in_depth():
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)

    att = [1,2,3,4,5,6,7,8,9,10]
    cpe = [3.3, 6.7, 8.3, 10.2, 16.8, 19.8, 22.3, 26.7, 29.8, 31.1]
    greedy = [3.4, 7.3, 10.3, 14.7, 17.6, 21.7, 25.4, 29.8, 32.9, 34.0]


    # Create the line graph
    plt.plot(att, cpe, marker='o',markersize=10, linestyle='-', color='#332288', label = 'CauSumX', linewidth=4.5)
    # plt.plot(att, ids, marker='+', linestyle='-', color='r', label='IDS', linewidth=2.5)

    plt.plot(att, greedy, marker='^',markersize=10, linestyle='-', color= '#CC6677', label='Greedy-Last-Step', linewidth=4.5)

    # Add labels and title
    plt.xlabel('Solution size',fontweight='bold', fontsize=24)
    plt.ylabel('Overall explainability', fontweight='bold', fontsize=28)
    plt.xticks(att)
    plt.legend()
    #plt.tight_layout()
    #plt.title('Time vs. attributes')

    # Show the graph
    plt.show()

def bins(att, time, bf,et):
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)

    # Create the line graph
    plt.plot(att, time, marker='o', markersize=10, linestyle='-', color='#332288', label='CauSumX', linewidth=4.5)
    # plt.plot(att, ids, marker='+', linestyle='-', color='r', label='IDS', linewidth=2.5)
    if et:
        plt.plot(att, et, marker='^', markersize=10, linestyle='-', color='#CC6677', label='Explanation Table',
                 linewidth=4.5)
    plt.plot(att, bf, marker='p', markersize=10, linestyle='-', color='#1177AA', label='Brute Force', linewidth=4.5)

    # plt.plot(att, time, marker='o', linestyle='-', color='b', label = 'CPE', linewidth=4.5)
    # # plt.plot(att, ids, marker='+', linestyle='-', color='r', label='IDS', linewidth=2.5)
    # if et:
    #     plt.plot(att, et, marker='^', linestyle='-', color='m', label='Explanation Table', linewidth=4.5)
    # plt.plot(att, bf, marker='p', linestyle='-', color='g', label='Brute Force', linewidth=4.5)

    # Add labels and title
    plt.xlabel('number of treatment patterns',fontweight='bold', fontsize=24)
    plt.ylabel('time (s)', fontweight='bold', fontsize=28)
    plt.xticks(att)
    plt.legend()
    #plt.tight_layout()
    #plt.title('Time vs. attributes')

    # Show the graph
    plt.show()

def tuples(att, time, bf,et):
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)


    # Create the line graph
    plt.plot(att, time, marker='o',markersize=10, linestyle='-', color='#332288', label = 'CauSumX', linewidth=4.5)
    # plt.plot(att, ids, marker='+', linestyle='-', color='r', label='IDS', linewidth=2.5)
    if et:
        plt.plot(att, et, marker='^',markersize=10, linestyle='-', color='#CC6677', label='Explanation Table', linewidth=4.5)
    plt.plot(att, bf, marker='p', markersize=10,linestyle='-', color= '#1177AA', label='Brute Force', linewidth=4.5)

    # Add labels and title
    plt.xlabel('number of tuples',fontweight='bold', fontsize=28)
    plt.ylabel('time (s)', fontweight='bold', fontsize=28)
    plt.xticks(att, rotation = 25)
    plt.legend()
    #plt.tight_layout()
    #plt.title('Time vs. attributes')

    # Show the graph
    plt.show()

def phases():
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 20}
    plt.rc('font', **font)
    datasets = ['Adult', 'Stack Overflow', 'IMPUS-CPS', 'Accidents']
    phase1_times = [4.5, 26.0, 3.5, 25.7]  # Runtime for phase 1 (in seconds)
    phase2_times = [13.7, 28.3, 107.1, 141.5]  # Runtime for phase 2 (in seconds)
    phase3_times = [3, 1, 2, 3]  # Runtime for phase 3 (in seconds)

    # Plotting
    x = np.arange(len(datasets))
    width = 0.35

    fig, ax = plt.subplots()

    # Stacked bar plot
    p1 = ax.bar(x, phase1_times, width, label='Mining Grouping Patterns')
    p2 = ax.bar(x, phase2_times, width, bottom=phase1_times, label='Detecting Treatment Patterns')
    p3 = ax.bar(x, phase3_times, width, bottom=np.add(phase1_times, phase2_times), label='Obtaining a Solution')

    # Labels and ticks
    ax.set_ylabel('time (s)',fontweight='bold', fontsize=20)
    ax.set_xlabel('Datasets',fontweight='bold', fontsize=20)
    #ax.set_title('Runtime of Algorithm Phases')
    ax.set_xticks(x)
    ax.set_xticklabels(datasets)
    ax.legend()

    # Display the plot
    plt.show()
    #plt.savefig('plot.pdf', bbox_inches='tight', pad_inches=0)
    #plt.savefig('runtime_plot.pdf', format='pdf')


def cates(att, time,time2,time3,time4,time5):
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)

    # Create the line graph
    plt.plot(att, time, marker='o',markersize = 10, linestyle='-', color='b', linewidth=4.5)
    plt.plot(att, time2, marker='p',markersize = 10, linestyle='-', color='m', linewidth=4.5)
    plt.plot(att, time3, marker='v',markersize = 10, linestyle='-', color='c', linewidth=4.5)
    plt.plot(att, time4, marker='*',markersize = 10, linestyle='-', color='g', linewidth=4.5)
    plt.plot(att, time5, marker='^',markersize = 10, linestyle='-', color='r', linewidth=4.5)

    # Add labels and title
    plt.xlabel('number of tuples', fontweight='bold', fontsize=28)
    plt.ylabel('CATE value', fontweight='bold', fontsize=28)
    plt.xticks(att, rotation=25)
    #plt.legend()
    # plt.tight_layout()
    # plt.title('Time vs. attributes')

    # Show the graph
    plt.show()


def dagorder():
    font = {'family': 'sans-serif', 'weight': 'bold', 'size': 28}
    plt.rc('font', **font)

    # Define the datasets and their corresponding baseline values
    datasets = ['German', 'Adult']
    baselines = ['PC', 'FCI', 'LiNGAM']
    values = np.array([[0.81, 0.84, 0.87], [0.85, 0.62, 0.65]])
    colors = ['#DDCC77', '#CC6677', '#332288']
    fill_patterns = ['||', '**', '//']

    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Set the width of each bar
    bar_width = 0.2

    # Set the positions of the bars on the x-axis
    x = np.arange(len(datasets))

    # Define the colors for each baseline
    #colors = ['tab:orange', 'tab:green', 'tab:red']
    bars = []
    # Plot the bars for each baseline
    for i, baseline in enumerate(baselines):
        bar = ax.bar(x + (i * bar_width), values[:, i], width=bar_width, label=baseline, color=colors[i])
        bars.append(bar)

    unique_colors = set(colors)
    for color in unique_colors:
        pattern = fill_patterns[list(unique_colors).index(color) % len(fill_patterns)]
        same_color_bars = [bar[idx] for bar, c in zip(bars, colors) for idx in range(len(bar)) if c == color]
        for bar in same_color_bars:
            bar.set_hatch(pattern)

    # Calculate the middle position for the x-axis ticks and labels
    middle_position = x + ((len(baselines) - 1) * bar_width) / 2

    # Set the x-axis ticks and labels at the middle position
    ax.set_xticks(middle_position)
    ax.set_xticklabels(datasets)
    ax.set_ylabel("Kendall's tau", fontweight='bold', fontsize=28)

    # Add a legend
    ax.legend()

    # Show the plot
    plt.show()


def order(data,values):
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)
    # Example data
    categories = data

    # Create the bar plot
    #plt.bar(categories, values)
    plt.plot(categories, values, marker='o', markersize=10, linestyle='-', color='b', linewidth=4.5)

    # # Add labels to the bars
    # for i, value in enumerate(values):
    #     plt.text(i, value, str(value), ha='center', va='bottom')

    # Customize the plot
    plt.xlabel('data size', fontweight='bold', fontsize=28)
    plt.ylabel('Kendall\'s Tau', fontweight='bold', fontsize=28)
    plt.ylim(0, 1)
    # Display the plot
    plt.show()

def aprioriExp(threshold,expso,expadult, expacc):
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)

    # Create the line graph

    plt.plot(threshold, expso, marker='o', markersize=10, linestyle='-', color='#004c6d', label='German', linewidth=4.5)
    # plt.plot(att, ids, marker='+', linestyle='-', color='r', label='IDS', linewidth=2.5)
    plt.plot(threshold, expacc, marker='^', markersize=10, linestyle='-', color='#ffa700', label='Accidents',
             linewidth=4.5)
    plt.plot(threshold, expadult, marker='p', markersize=10, linestyle='-', color='#bc5090', label='Adult',
             linewidth=4.5)

    # Add labels and title
    plt.xlabel('Apriori Threshold', fontweight='bold', fontsize=24)
    plt.ylabel('Explainability', fontweight='bold', fontsize=28)
    plt.xticks(threshold)
    plt.axhline(y=6.6, color='#004c6d', linestyle='--', linewidth=4.5)  # Add horizontal line at 6.6
    plt.axhline(y=2.4, color='#bc5090', linestyle='--', linewidth=4.5)  # Add horizontal line at 2.4
    plt.axhline(y=3.8, color='#ffa700', linestyle='--', linewidth=4.5)  # Add horizontal line at 2.4
    plt.legend()
    # plt.tight_layout()
    # plt.title('Time vs. attributes')

    # Show the graph
    plt.show()

def aprioriCov(threshold,expso,expadult, expacc):
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)

    #colors = ['#004c6d', '#ffa700', '#bc5090', '#003f5c']
    # Create the line graph
    plt.plot(threshold, expso, marker='o',markersize = 10, linestyle='-', color='#004c6d', label='German', linewidth=4.5)
    # plt.plot(att, ids, marker='+', linestyle='-', color='r', label='IDS', linewidth=2.5)
    plt.plot(threshold, expacc, marker='^',markersize = 10, linestyle='-', color= '#ffa700', label='Accidents', linewidth=4.5)
    plt.plot(threshold, expadult, marker='p',markersize = 10, linestyle='-', color= '#bc5090', label='Adult', linewidth=4.5)

    # Add labels and title
    plt.xlabel('Apriori Threshold', fontweight='bold', fontsize=24)
    plt.ylabel('Coverage', fontweight='bold', fontsize=28)
    plt.xticks(threshold)
    # plt.axhline(y=6.6, color='r', linestyle='--', linewidth=2)  # Add horizontal line at 6.6
    # plt.axhline(y=2.4, color='r', linestyle='--', linewidth=2)  # Add horizontal line at 2.4
    plt.legend()
    # plt.tight_layout()
    # plt.title('Time vs. attributes')

    # Show the graph
    plt.show()

def dagexp():
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)
    #Define the datasets and their corresponding baseline values
    # Define the datasets and their corresponding baseline values
    datasets = ['German', 'Adult']
    baselines = ['Ground Truth', 'PC', 'FCI', 'LiNGAM']
    values = np.array([[1.98, 1.55, 1.70, 1.84], [5.38, 5.62, 4.35, 4.02]])
    colors = ['#1177AA', '#DDCC77', '#CC6677', '#332288']
    fill_patterns = ['..', '||', '**', '//']

    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Set the width of each bar
    bar_width = 0.2

    # Set the positions of the bars on the x-axis
    x = np.arange(len(datasets))
    bars = []

    # Plot the bars for each baseline
    for i, baseline in enumerate(baselines):
        bar = ax.bar(x + (i * bar_width), values[:, i], width=bar_width, label=baseline, color = colors[i])
        bars.append(bar)

    unique_colors = set(colors)
    for color in unique_colors:
        pattern = fill_patterns[list(unique_colors).index(color) % len(fill_patterns)]
        same_color_bars = [bar[idx] for bar, c in zip(bars, colors) for idx in range(len(bar)) if c == color]
        for bar in same_color_bars:
            bar.set_hatch(pattern)

    # Calculate the middle position for the x-axis ticks and labels
    middle_position = x + ((len(baselines) - 1) * bar_width) / 2

    # Set the x-axis ticks and labels at the middle position
    ax.set_xticks(middle_position)
    ax.set_xticklabels(datasets)
    #ax.set_xlabel('Datasets', fontweight='bold', fontsize=28)
    ax.set_ylabel('Explainability', fontweight='bold', fontsize=28)

    # Add a legend
    ax.legend()

    # Show the plot
    plt.show()



def attsData():


    #SO
    att = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15,16,17,18,19,20]
    time = [4.445,5.333,6.4443,8.44,10.33,13.14078426361084, 19.87022352218628,
        24.10904812812805, 29.61595439910889,32.883, 35.4852466583252, 39.90481328964233,41.45325183868408,
        44.222, 48.04852318763733, 51.17861914634705, 54.1269335746765, 56.86102867126465]



    bf = [6.33,9.333, 16.222,20.333,27.210544, 56.7664756, 99.503345, 149.123455, 228.88946200,
           np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]




    et = [1.33, 2.44, 3.222, 4.33, 6.3322,10.22, 13.255, 15.224, 30.2555, 67.227,103.22,
          121.344, 189.244, 224.44, np.nan, np.nan, np.nan, np.nan]
    print(len(att), len(et))
    atts(att,time,bf,et,range(3,24,3))



    #ADULTS
    att = [3, 4, 5, 6, 7, 8 ,9,10,11,12,13]
    time = [1.443,3.555,5.32174921,
            7.98924112, 10.8178282,
            13.517076254,15.772, 16.222, 18.83446598,20.5522,21.79754138]
    bf = [5.737,9.5522,16.3322,28.99378, 36.555442,
           77.3666469, 125.915542, 223.43560533, np.nan, np.nan,np.nan]
    et = [0.223,1.0002, 1.23,2.0003,2.5,3.55, 4.533,8.737,20.44,35.554,47.2]
    atts(att, time, bf, et)

    #IMPUS
    att = [3,4,5,6,7,8,9,10]
    time = [53.555,63.7442,74.77725,81.66343,92.77553,99.77365,108.5553,114.233]
    bf = [60.5525,68.44443,132.44467,264.333355,np.nan,np.nan,np.nan,np.nan]
    et = [0.665,1.44,4.22, 7.444, 10.22, 12.33,14.222,21.22]
    atts(att, time, bf, et)

    #Accidents
    att = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,
           31,32,33,34,35,36,37,38,39,40]
    time = [30.7772,35.884, 38.995, 41.9922,
        40.662,43.885, 45.6626, 47.8885,
            50.52523, 56.8826, 60.8836, 66.88363, 74.7765, 77.883, 82.88464,
            88.97774, 93.9994, 96.883,
            98.90, 102.37,  108.14, 114.50,  119.12, 125.47, 131.24, 135.29, 137.60, 143.37,
            148.57, 149.15, 153.19, 154.34, 158.77, 161.27,163.58,  166.47, 170.51, 173.8885]
    print(len(time))
    bf = [60.5525,108.44443,204.333355,np.nan,np.nan,np.nan,np.nan,
          np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,
          np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,
          np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
    et = [1.22, 2.44, 3.44, 6.33, 12.44,17.22, 36.44, 60.5525, 108.44443, 204.333355,287.55, np.nan, np.nan, np.nan, np.nan,
          np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
          np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    print(len(et))

    atts(att, time, bf,et, range(3,45,5))


def tuplesData():


    #Adult
    data = [3256, 6512, 9768, 13024,  16280,  19537,  22793,  26049,    29305,  32561]
    data = ['3k','6k','10k','13k','16k','19k','23k','26k','29k','32k']
    time = [3.454328775405884,4.259726762771606,6.32971477508545,9.833213806152344,12.668596267700195,
            15.432836055755615,  16.55471229553223,  18.64207720756531,
            20.549094438552856,  21.549094438552856
            ]
    bf = [25.77699933, 35.66334, 63.88564, 95.3222, 158.733,
          204.6455,267.777,np.nan, np.nan,np.nan]
    et = [42.43, 45.22, 43.55, 46.222, 47.888, 48.883, 47.88, 46.882, 48.555,47.555]
    tuples(data, time, bf, et)
    #
    # #SO
    data = ['4k','7k','11k','15k','19k','23k','26k','30k','34k','38k']
    time = [17.58096957206726, 19.74780797958374, 21.552740812301636, 19.6485116481781,
            21.418529272079468, 34.59875822067261,
            32.347310066223145, 37.66509032249451,
            45.096041440963745, 56.32619905471802,
            ]
    et = None
    # ids = [np.nan] * 10
    # frl = [np.nan] * 10
    bf = [71.779933, 112.6334, 188.8334, 242.44, np.nan,np.nan,np.nan,np.nan,np.nan, np.nan]
    tuples(data, time, bf, et)
    #
    # #IMPUS
    data = ['110k','220k','330k','440k','550k','660k','770k','880k','990k','1.1m']
    time = [112.756,113.445,113.911,113.021,114.682,113.178,113.899,
            113.604,114.264,113.707]
    # ids = [np.nan] * 10
    # frl = [np.nan] * 10
    et = [20.33, 22.44, 21.444, 24.666, 22.444, 23.3444, 21.555, 20.55, 19.992, 22.33]
    bf = [198.664, 257.886, np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan,np.nan]
    tuples(data, time, bf, et)
    #
    # #accidents
    data = ['280k', '560k', '840k', '1.1m', '1.4m', '1.7m', '1.9m', '2.2m', '2.5', '2.8m']
    time = [   171.287,166.112,165.556,164.981,164.809,166.924,167.315,169.742,165.981
    ,168.473]
    # ids = [np.nan] * 10
    # frl = [np.nan] * 10
    et = None
    bf = [293.186,np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    #
    tuples(data, time, bf,et)

def binsData():


    # #Adult
    data = [25,50,75,100,125, 150]
    time = [3.4543884, 6.329714, 9.8332138, 16.223,
            20.5452856, 23.552856
            ]
    # ids = [np.nan] * 10
    # frl = [np.nan] * 10
    bf = [ 34.664, 65.884, 105.3222, 158.733, 264.77, np.nan]
    et = [6.8386,16.8254, 23.6666, 30.775, 40.6662, 47.6633]
    bins(data, time, bf, et)
    #
    # # So
    data = [50,100,150,200,250,300]
    time = [4.6675,9.8332138, 18.223,23.556,
            40.5452856, 57.552856
            ]
    bf = [27.8837,65.884, 178.733, 284.77, np.nan, np.nan]
    et = None#[np.nan] * 6
    bins(data, time, bf, et)
    #
    # # IMPUS
    data = [10, 20, 30, 40,50,60]
    time = [30.3884, 46.714, 59.2138, 76.4223,
            100.856, 120.2856
            ]
    # ids = [np.nan] * 10
    # frl = [np.nan] * 10
    bf = [55.22, 108.5733, 204.4477, np.nan, np.nan, np.nan]
    et = [0.00224,3.885,6.774,11.72553,19.3355,22.3333]
    bins(data, time, bf, et)
    #
    # # Accidents
    data = [25,50,75,100,125, 150,175]
    time = [22.6624,47.6624,59.2138, 87.14223,
             120.2856, 150.2774, 168.9937
            ]
    # ids = [np.nan] * 10
    # frl = [np.nan] * 10
    bf = [65.2332, 128.3233, 244.1177, np.nan, np.nan, np.nan, np.nan]
    et = None
    #
    #
    bins(data, time,bf, et)

def apriori():
    # #Apriori threshold
    threshold = [0,0.1,0.2,0.3,0.4,0.5]
    # #SO
    # #exp
    # expso = [243, 243, 210,190,190,162]
    # #covergae
    # covso = [1,1, 0.8, 0.6,0.5,0.5,0.3]
    #Accidents
    #exp
    expacc = [3.41, 3.41, 3.41,2.05,2.05,0]
    #covergae
    covacc = [1,1, 1,0.5,0.5,0]

    # German
    # exp
    expgerman = [6.01, 5.38, 4.71, 3.22, 1.91, 0]
    # covergae
    covgerman = [0.5, 0.5, 0.3, 0,0,0]

    # ADult
    # exp
    expadult = [2.31, 1.98, 1.98, 1.01, 1.01,0]
    # covergae
    covadult = [1, 0.86, 0.86, 0.66, 0.66, 0]
    #
    aprioriExp(threshold,expgerman,expadult, expacc)
    #aprioriCov(threshold,covgerman,covadult,covacc)

def causalDAG():


    dagexp()
    dagorder()


def cov_variants():
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)
    import numpy as np

    # Data for the bar chart
    datasets = ['German', 'Adult', 'Accidents']
    algorithms = ['Brute Force', 'Brute Force-LP', 'Greedy-Last-Step', 'CauSumX']
    colors = ['#1177AA', '#DDCC77', '#CC6677', '#332288']
    fill_patterns = ['..', '||', '**', '//']

    #data = np.random.rand(4, 4)  # Random data for demonstration purposes
    data = np.array([[0.5,0.5,0.5,0.5],[np.nan,np.nan,0.71,0.76],[np.nan,np.nan,1,1]])

    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Set the width of each bar
    bar_width = 0.2

    bars = []
    # Create the bar chart
    for j, algorithm in enumerate(algorithms):
        x = np.arange(len(datasets)) + j * bar_width
        y = data[:, j]
        bar = ax.bar(x, y, width=bar_width, label=algorithm, color = colors[j])
        bars.append(bar)

    unique_colors = set(colors)
    for color in unique_colors:
        pattern = fill_patterns[list(unique_colors).index(color) % len(fill_patterns)]
        same_color_bars = [bar[idx] for bar, c in zip(bars, colors) for idx in range(len(bar)) if c == color]
        for bar in same_color_bars:
            bar.set_hatch(pattern)


    # Set the x-axis ticks and labels
    ax.set_xticks(np.arange(len(datasets)) + bar_width * (len(algorithms) / 2))
    ax.set_xticklabels(datasets)

    # Set the y-axis label
    ax.set_ylabel('Coverage', fontweight='bold', fontsize=28)
    ax.set_yticks(np.arange(0, 1.2, 0.2))

    # Add a legend
    #ax.legend()
    ax.legend(loc='upper left')

    # Show the plot
    plt.show()

def exp_variants():
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)
    import numpy as np

    # Data for the bar chart
    datasets = ['German', 'Adult', 'Accidents']
    algorithms = ['Brute Force', 'Brute Force-LP', 'Greedy-Last-Step', 'CauSumX']
    colors = ['#1177AA', '#DDCC77', '#CC6677', '#332288']
    fill_patterns = ['..', '||', '**', '//']

    #data = np.random.rand(4, 4)  # Random data for demonstration purposes
    data = np.array([[5.9,5.88,5.8,5.7],[np.nan,np.nan,1.98,1.95],[np.nan,np.nan,3.7,3.73]])

    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Set the width of each bar
    bar_width = 0.2

    bars = []
    # Create the bar chart
    for j, algorithm in enumerate(algorithms):
        x = np.arange(len(datasets)) + j * bar_width
        y = data[:, j]
        bar = ax.bar(x, y, width=bar_width, label=algorithm, color = colors[j])
        bars.append(bar)

    unique_colors = set(colors)
    for color in unique_colors:
        pattern = fill_patterns[list(unique_colors).index(color) % len(fill_patterns)]
        same_color_bars = [bar[idx] for bar, c in zip(bars, colors) for idx in range(len(bar)) if c == color]
        for bar in same_color_bars:
            bar.set_hatch(pattern)


    # Set the x-axis ticks and labels
    ax.set_xticks(np.arange(len(datasets)) + bar_width * (len(algorithms) / 2))
    ax.set_xticklabels(datasets)

    # Set the y-axis label
    ax.set_ylabel('Overall Explainability', fontweight='bold', fontsize=28)
    ax.set_yticks(np.arange(0, 7, 1))

    # Add a legend
    ax.legend()
    #ax.legend(loc='upper center')

    # Show the plot
    plt.show()

def times_variants():
    font = {'family': 'sans-serif',
            'weight': 'bold',
            'size': 28}
    plt.rc('font', **font)
    import numpy as np

    # Data for the bar chart
    datasets = ['German', 'Adult', 'SO', 'IMPUS-CPS']
    algorithms = ['Brute Force', 'Brute Force-LP', 'Greedy-Last-Step', 'CauSumX']
    # colors = ['g','m','r', 'b']
    colors = ['#1177AA', '#DDCC77', '#CC6677', '#332288']
    fill_patterns = ['..', '||', '**', '//']

    #data = np.random.rand(4, 4)  # Random data for demonstration purposes
    data = np.array([[129,121,13,14],[np.nan,np.nan,21,23],[np.nan,np.nan,57,59],[np.nan,np.nan,114,117]])

    # Set up the figure and axes
    fig, ax = plt.subplots()

    # Set the width of each bar
    bar_width = 0.2
    bars = []
    # Create the bar chart
    for j, algorithm in enumerate(algorithms):
        x = np.arange(len(datasets)) + j * bar_width
        y = data[:, j]
        bar = ax.bar(x, y, width=bar_width, label=algorithm, color = colors[j])
        bars.append(bar)
        # bar[0].set_hatch(fill_textures[j])
    # Add fill patterns to each bar
    # # Add fill patterns to each group of bars with the same color
    unique_colors = set(colors)
    for color in unique_colors:
        pattern = fill_patterns[list(unique_colors).index(color) % len(fill_patterns)]
        same_color_bars = [bar[idx] for bar, c in zip(bars, colors) for idx in range(len(bar)) if c == color]
        for bar in same_color_bars:
            bar.set_hatch(pattern)


    # Set the x-axis ticks and labels
    ax.set_xticks(np.arange(len(datasets)) + bar_width * (len(algorithms) / 2))
    ax.set_xticklabels(datasets)

    # Set the y-axis label
    ax.set_ylabel('times (s)', fontweight='bold', fontsize=28)
    ax.set_yticks(range(0, 160, 20))

    # Add a legend
    #ax.legend()
    ax.legend(loc='upper center')

    # Show the plot
    plt.show()


if __name__ == '__main__':
    #attsData()
    #tuplesData()
    #binsData()
    #phases()

    # times_variants()
    # exp_variants()
    # cov_variants()
    variants_in_depth()
    variants_in_depth_cov()

    # data = ['280k', '560k', '840k', '1.1m', '1.4m', '1.7m', '1.9m', '2.2m', '2.5', '2.8m']
    # time = [0.38, 0.37, 0.43, 0.44, 0.45, 0.43, 0.44,0.43, 0.45, 0.44]
    # time1 = [0.39, 0.38, 0.33, 0.36, 0.35, 0.35, 0.34, 0.34, 0.35, 0.34]
    # time3 = [0.22, 0.24, 0.25, 0.26, 0.25, 0.25, 0.24, 0.24, 0.24, 0.24]
    # time4 = [0.01, 0.02, 0.05, 0.03, 0.05, 0.05, 0.04, 0.04, 0.04, 0.04]
    # time5 = [0.01, 0.01, 0.005, 0.002, 0.002, 0.002, 0.002, 0.002, 0.002, 0.001]
    # cates(data, time, time1, time3,time4,time5)
    # #
    #
    # data =['280k', '560k', '840k', '1.1m', '1.4m', '1.7m']
    # values = [0.831, 0.873, 0.905,0.947,0.950,0.951]
    # order(data, values)
    #
    #apriori()
    # #
    #
    #causalDAG()






