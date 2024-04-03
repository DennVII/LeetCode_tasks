#include <iostream>
#include <vector>
#include <string>

const std::string DESCRIPTION = "Given an m x n matrix, return true if the matrix is Toeplitz. \
Otherwise, return false. A matrix is Toeplitz if every diagonal from top-left \
to bottom-right has the same elements.";

class Solution {
public:
    bool isToeplitzMatrix(std::vector<std::vector<int>>&);
};


bool Solution::isToeplitzMatrix(std::vector<std::vector<int>>& matrix){
    for (size_t i {0}; i != matrix.size(); ++i){
        for(size_t j {0}; j != matrix[i].size(); ++j){
            if( i != 0 && j != 0){
                if (matrix[i][j] != matrix[i-1][j-1]){
                    return false;
                }
            }
        }
    }
    return true;
}