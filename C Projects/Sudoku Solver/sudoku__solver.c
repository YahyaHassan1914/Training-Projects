#include <stdio.h>
#include <stdbool.h>
#include <time.h>  // Include time.h for timing functions

#define N 9
int counter = 0;

// Function to print the Sudoku grid
void printGrid(int grid[N][N]) {
    for (int row = 0; row < N; row++) {
        for (int col = 0; col < N; col++)
            printf("%2d", grid[row][col]);
        printf("\n");
    }
}

// Function to find an empty location in the grid
bool findEmptyLocation(int grid[N][N], int *row, int *col) {
    for (*row = 0; *row < N; (*row)++) {
        for (*col = 0; *col < N; (*col)++) {
            if (grid[*row][*col] == 0)
                return true;
        }
    }
    return false;
}

// Function to check if placing num at grid[row][col] is valid
bool isSafe(int grid[N][N], int row, int col, int num) {
    // Check row
    for (int x = 0; x < N; x++) {
        if (grid[row][x] == num)
            return false;
    }

    // Check column
    for (int x = 0; x < N; x++) {
        if (grid[x][col] == num)
            return false;
    }

    // Check subgrid
    int startRow = row - row % 3, startCol = col - col % 3;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (grid[i + startRow][j + startCol] == num)
                return false;
        }
    }

    return true;
}

// Main solver function using backtracking
bool solveSudoku(int grid[N][N]) {
    int row, col;

    // If no empty space is left, we are done
    if (!findEmptyLocation(grid, &row, &col))
        return true;

    // Consider digits 1 to 9
    for (int num = 1; num <= 9; num++) {
        // If looks promising
        if (isSafe(grid, row, col, num)) {
            // Make tentative assignment
            grid[row][col] = num;

            // printf("\n Step %d \n", counter);
            // counter++;
            // printGrid(grid);
            // printf("\n");
            // getchar();

            // Return if success
            if (solveSudoku(grid))
                return true;

            // Failure, undo and try again
            grid[row][col] = 0;
        }
    }

    // Trigger backtracking
    return false;
}

int main() {
    int grid[N][N] = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };

    // Record start time
    clock_t start = clock();

    if (solveSudoku(grid) == true)
        printGrid(grid);
    else
        printf("No solution exists");

    // Record end time
    clock_t end = clock();

    // Calculate elapsed time in seconds
    double elapsed_time = (double)(end - start) / CLOCKS_PER_SEC;
    printf("\nElapsed time: %.6f seconds\n", elapsed_time);

    return 0;
}