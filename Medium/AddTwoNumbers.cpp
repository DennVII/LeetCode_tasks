#include <iostream>
#include <string>


const std::string DECSRIPTION = "You are given two non-empty linked lists representing two non-negative integers. \
The digits are stored in reverse order, and each of their nodes contains a single digit. \
Add the two numbers and return the sum as a linked list. \
You may assume the two numbers do not contain any leading zero, except the number 0 itself.";

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};



class Solution {
public:
    ListNode* addTwoNumbers(ListNode*, ListNode*);
    ListNode* createListNode(int*, size_t);
    void printListNode(const ListNode*);
};


ListNode* Solution::createListNode(int* nums, size_t n){
    ListNode* res = nullptr;
    ListNode* iter = nullptr;
    for(size_t i {0}; i != n; ++i){
        if (iter == nullptr){
            iter = new ListNode(nums[i]);
            res = iter;
        }
        else{
            iter->next = new ListNode(nums[i]);
            iter = iter->next;
        }
    }
    return res;
}


void Solution::printListNode(const ListNode* ln){
    const ListNode* temp = ln;
    while(temp != nullptr){
        std::cout << temp->val << ' ';  
        temp = temp->next;
    }
    std::cout<< "\n";
}


ListNode* Solution::addTwoNumbers(ListNode* l1, ListNode* l2){
    int remainder = 0;
    ListNode* result = nullptr;
    ListNode* iterator = nullptr;

    while(l1 != nullptr and l2 != nullptr){
        if (iterator == nullptr){
            iterator = new ListNode();
            result = iterator;
        }
        else{
            iterator->next = new ListNode();
            iterator = iterator->next;
        }


        iterator->val = (l1->val + l2->val + remainder) % 10;
        remainder = (l1->val + l2->val + remainder) / 10;

        l1 = l1->next;
        l2 = l2->next;
    }

    while(l1 != nullptr){
        iterator->next = new ListNode();
        iterator = iterator->next;

        iterator->val = (l1->val + remainder) % 10;
        remainder = (l1->val + remainder) / 10;

        l1 = l1->next;
    }

    while(l2 != nullptr){
        iterator->next = new ListNode();
        iterator = iterator->next;

        iterator->val = (l2->val + remainder) % 10;
        remainder = (l2->val + remainder) / 10;

        l2 = l2->next;
    }

    if (remainder){
        iterator->next = new ListNode();
        iterator = iterator->next;

        iterator->val = remainder;
    }

    return result;
}