#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Liam McMonies
# Email: lm384@hw.ac.uk
# Date: 02/12/2020


# Imports
#from matplotlib import pyplot as plt
#from graphviz import Digraph


# Reference: [1]
# Bar Chart: Takes Data And Displays It In A Bar Chart.
def barChart(data, xlab, ylab, ttl):
    plt.style.use('fivethirtyeight')
    plt.bar(range(len(data)), list(data.values()), align='center')
    plt.xticks(range(len(data)), list(data.keys()))
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(ttl)
    plt.tight_layout()
    plt.show()


# Graph Diagram: Takes Data And Formats It Into A Graph.
# Reference: [12]
def graphDiagram(data, documentId, visitorId):
    dot = Digraph(comment='Also Likes')

    # Creates Box Node Based On Key In Dictionary
    dot.attr('node', shape='box')
    for key, val in data.items():
        if key == visitorId:
            dot.node(str(key)[-4:], style="filled", color=".3.9.7")
        else:
            dot.node(str(key)[-4:])

    # Creates Circle Node Based On Value In Dictionary
    dot.attr('node', shape='circle')
    for key, val in data.items():
        for j in val:
            if documentId == j:
                dot.node(str(j)[-4:], style="filled", color=".3.9.7")
            else:
                dot.node(str(j)[-4:])

    # Creates Arrows Based On Keys And Values.
    for key, val in data.items():
        for j in val:
            dot.edge(str(key)[-4:], str(j)[-4:])

    dot.render('graph.ps', view=True)
