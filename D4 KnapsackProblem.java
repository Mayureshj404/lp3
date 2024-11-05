// Write a program to solve a 0-1 Knapsack problem using dynamic programming or branch and bound strategy.
import java.util.Scanner;

public class KnapsackProblem {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the knapsack capacity: ");
        int capacity = scanner.nextInt();

        System.out.print("Enter the number of items: ");
        int items = scanner.nextInt();

        int[] price = new int[items + 1];
        int[] wt = new int[items + 1];

        System.out.println("Enter the details for each item:");
        for (int i = 1; i <= items; i++) {
            System.out.print("Item " + i + " - Weight: ");
            wt[i] = scanner.nextInt();
            System.out.print("Item " + i + " - Price: ");
            price[i] = scanner.nextInt();
        }

        int[][] dp = new int[items + 1][capacity + 1];

        for (int i = 0; i <= items; i++) {
            for (int j = 0; j <= capacity; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if (wt[i] <= j) {
                    dp[i][j] = Math.max(dp[i - 1][j], price[i] + dp[i - 1][j - wt[i]]);
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        System.out.println("Maximum Profit Earned: " + dp[items][capacity]);
    }
}


/*
Output :
Enter the knapsack capacity: 10
Enter the number of items: 4
Enter the details for each item:
Item 1 - Weight: 2
Item 1 - Price: 3
Item 2 - Weight: 2
Item 2 - Price: 7
Item 3 - Weight: 4
Item 3 - Price: 2
Item 4 - Weight: 5
Item 4 - Price: 9
Maximum Profit Earned: 19
0/1 Knapsack :
Time Complexity: O(N*W). 
where ‘N’ is the number of weight element and ‘W’ is capacity. As for every weight element we traverse through all weight capacities 1<=w<=W.
Auxiliary Space: O(N*W). 
The use of 2-D array of size ‘N*W’.
*/

#include <iostream>
using namespace std;

// Function to solve the 0-1 Knapsack problem using Dynamic Programming
int knapsack(int capacity, int weights[], int values[], int n) {
    // DP table to store the maximum values for given capacity and items
    int dp[n + 1][capacity + 1];

    // Initialize the DP table with 0s for base cases (no items or 0 capacity)
    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= capacity; w++) {
            if (i == 0 || w == 0) {
                dp[i][w] = 0;
            } else if (weights[i - 1] <= w) {
                // Max value by either taking or not taking the current item
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]]);
            } else {
                dp[i][w] = dp[i - 1][w];
            }
        }
    }

    // The last cell will have the maximum value for the given capacity
    return dp[n][capacity];
}

int main() {
    int capacity; // Maximum weight capacity of the knapsack
    int n;        // Number of items

    cout << "Enter number of items: ";
    cin >> n;

    int weights[n], values[n]; // Arrays to store weights and values of items

    cout << "Enter weights of items: ";
    for (int i = 0; i < n; i++) {
        cin >> weights[i];
    }

    cout << "Enter values of items: ";
    for (int i = 0; i < n; i++) {
        cin >> values[i];
    }

    cout << "Enter the maximum capacity of the knapsack: ";
    cin >> capacity;

    int max_value = knapsack(capacity, weights, values, n);
    cout << "The maximum value that can be achieved is: " << max_value << endl;

    return 0;
}
