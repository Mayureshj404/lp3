#include <iostream>
using namespace std;

// Structure to represent an item
struct Item {
    float weight;
    float value;
};

// Function to calculate the maximum value for the knapsack
float fractionalKnapsack(int W, Item items[], int n) {
    // Sorting items based on value/weight ratio
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if ((items[j].value / items[j].weight) < (items[j + 1].value / items[j + 1].weight)) {
                Item temp = items[j];
                items[j] = items[j + 1];
                items[j + 1] = temp;
            }
        }
    }

    float totalValue = 0.0; // Total value in the knapsack
    float remainingWeight = W; // Remaining capacity of the knapsack

    for (int i = 0; i < n && remainingWeight > 0; i++) {
        if (items[i].weight <= remainingWeight) {
            // If the entire item can be taken
            totalValue += items[i].value;
            remainingWeight -= items[i].weight;
        } else {
            // If only a fraction of the item can be taken
            totalValue += items[i].value * (remainingWeight / items[i].weight);
            remainingWeight = 0;
        }
    }

    return totalValue;
}

int main() {
    int n, W;

    cout << "Enter the number of items: ";
    cin >> n;
    
    Item items[n];

    cout << "Enter the maximum weight of the knapsack: ";
    cin >> W;

    for (int i = 0; i < n; i++) {
        cout << "Enter weight and value of item " << i + 1 << ": ";
        cin >> items[i].weight >> items[i].value;
    }

    float maxValue = fractionalKnapsack(W, items, n);

    cout << "Maximum value in Knapsack = " << maxValue << endl;

    return 0;
}
