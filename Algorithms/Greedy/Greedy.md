_________________ 

### Greedy method

#### Mechanism
- Divide the problem in successive sub-problems P1, P2, ...Pn
- Progress to the final solution by selecting at each step the best decision

#### Strategy
- Successively incorporate elements that realize the local optimum
- No second thoughts are allowed on already made decisions

Required elements:

- A candidate set (from which a solution is created)
- A selection function (selects the best candidate to be added to the solution)
- A feasibility function (determines if a candidate can be used in a solution)
- An objective function (assigns a value to a solution, or a partial solution)
- A solution function (checks if a complete solution has been found)

#### Complexity 
- Polynomial run time (for some k > 0, its running time on inputs of size n is O(n^k). This includes linear, quadratic, cubic and more)

#### Advantages
- Can reach the optimal solution
- Builds the solution step by step (finds the solution in an incremental way)
- Offers a single solution (unlike backtracking)

#### Disadvantages
- Short-sighted
- Non-recoverable

#### When to use
- For optimization
- Solution is the result of a successive selections of local optima
- Problems with solution represented by subsets or cartesian products that
achieve a certain optimum (minimum or maximum) of an objective function

#### Examples
#### Coins problem
##### Problem:
Find a way to pay a sum of money using a minimum number
of coins (different values of coins are available).

Input: Sum = 80, Coins = [1, 5, 10, 25, 50] | Output: 80 = 50 + 25 + 5

Input: Sum = 10, Coins = [1, 2, 3, 4] | Output: 10 = 4 + 3 + 2 + 1

Input: Sum = 10, Coins = [2, 3, 4, 5] | Output: 10 = 5 + 3 + 2


##### Solution:

L - list of available coins

isSolution(sol)
 - If the sum of coins selected in sol is equal to the desired sum

selectMostPromising(L)
 - Select the highest value coin in L

acceptable(el,sol)
- If the sum of coins in sol + el is not over the desired sum


```python
def sum(l):
    s = 0
    for el in l:
        s = s + el
    return s

def is_solution(solution, limit):
    return sum(solution) == limit

def select_most_promising(candidates):
    return max(candidates)

def acceptable(element, solution, limit):
    return sum(solution) + element <= limit

def greedy_coins(coins, given_sum):
    sol = []
    while (not is_solution(sol, given_sum)) and (coins != []):
        el = select_most_promising(coins)
        coins.remove(el)
        if acceptable(el, sol, given_sum):
            sol.append(el)
    if is_solution(sol, given_sum):
        return sol
    else:
        return None


def test_greedy_coins():
    assert greedy_coins([1, 5, 10, 25, 50], 80) == [50, 25, 5]
    assert greedy_coins([1, 2, 3, 4], 10) == [4, 3, 2, 1]
    #assert greedy_coins([1, 2, 3, 4, 5], 10) == [5, 3, 2]
    assert greedy_coins([2, 3, 4, 5], 10) == None


print(test_greedy_coins())
```

#### Knapsack problem
##### Problem:
We have a list of objects, each with a value (v) and a weight
(w). The objective is to place objects in a knapsack of capacity W such that the total value
of objects is maximum and the total weight does not exceed W. 

##### Solution:
```python
class Item:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt
  
    def __lt__(self, other):
        return self.cost < other.cost


def greedy_knapsack(wt, val, capacity):
    val_list = []
    for i in range(len(wt)):            
        val_list.append(Item(wt[i], val[i], i))
  
    # sorting items by value
    val_list.sort(reverse=True)
  
    total_value = 0
    for i in val_list:
        cur_wt = int(i.wt)
        cur_val = int(i.val)
        if capacity - cur_wt >= 0:
            capacity -= cur_wt
            total_value += cur_val
        else:
            fraction = capacity / cur_wt
            total_value += cur_val * fraction
            capacity = int(capacity - (cur_wt * fraction))
            break
    return total_value
  
  
def test_greedy_knapsack():
    wt = [10, 40, 20, 30]
    val = [60, 40, 100, 120]
    capacity = 50
    assert greedy_knapsack(wt, val, capacity) == 240


print(test_greedy_knapsack())
```


#### Stagecoach problem
#### Dynamic vs Greedy 
| Similarity                                           	| Differences                                                                                                                                                                                      	|
|------------------------------------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| Both techniques are applied in optimization problems 	| DP always provides the optimal solution<br>Greedy does not guarantee finding the optimal solution                                                                                                	|
|                                                      	| DP is applicable to problems in which the general optimum implies<br>partial optima<br>Greedy is applicable to problems for which the general optimum is<br>obtained from partial (local) optima 	|