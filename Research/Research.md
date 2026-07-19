# Before Getting Started

I decided to structure this document around four fundamental questions:

* When will the model change?
* How will the model change?
* How will the model know when to change?
* How will the AI determine whether a change improved its performance?

This document will be continuously evolving as research progresses. Each category will be updated independently as new ideas, experiments, and discoveries are introduced.

Artificial intelligence tools may be used to assist with organizing, analyzing, and developing ideas. The specific AI used is not important for this process, as the differences between available tools are minimal for the purpose of organizing and developing these concepts :>

for the current leader board 7/13/2026 claude is ontop so ill stick with that

![7/13/2026](../Data/images/development/PublicModelsRanking7/13/2026.png)



## When will the model change a node?  (very input causes a node change)  Sensitivity ∝ 1 / complexity
- Prediction error (difference between expected and observed outcome)
- High usage (how often the node is activated)
- Depth (deeper nodes are more specific and easier to modify)

Few nodes:
    high sensitivity
    fast learning
    less stable

Many nodes:
    low sensitivity
    slower learning
    more stable

## How will the model change a node?
- Split nodes
- Merge nodes
- Adjust node values
- Create new nodes
- Move nodes


## Node Change Priority
1. Depth
   - Determines node stability and change sensitivity

2. Change trigger
   - Determines when modification is allowed

3. Modification tools
   - Algorithms attached to node constructors

4. Optimization
   - Learns which modification tool produces the best results


## How will the model know a change improved itself?
- Create evaluation score based on node history and data
- Save previous tree state
- Compare before and after states
- Revert unsuccessful changes

