#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Farmer {
    string name;
    string crop;
    string region;
    int price;
};

// Comparator function
bool compareFarmers(const Farmer &a, const Farmer &b, int choice, int order) {
    bool res = false;
    if (choice == 1) res = a.price < b.price;       // Sort by price
    else if (choice == 2) res = a.crop < b.crop;    // Sort by crop
    else if (choice == 3) res = a.region < b.region; // Sort by region
    return (order == 1) ? res : !res; // Ascending or descending
}

// Merge two halves
void merge(vector<Farmer> &farmers, int left, int mid, int right, int choice, int order) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<Farmer> L(n1), R(n2);

    for (int i = 0; i < n1; i++)
        L[i] = farmers[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = farmers[mid + 1 + j];

    int i = 0, j = 0, k = left;

    while (i < n1 && j < n2) {
        if (compareFarmers(L[i], R[j], choice, order))
            farmers[k++] = L[i++];
        else
            farmers[k++] = R[j++];
    }

    while (i < n1)
        farmers[k++] = L[i++];
    while (j < n2)
        farmers[k++] = R[j++];
}

// Merge Sort algorithm
void mergeSort(vector<Farmer> &farmers, int left, int right, int choice, int order) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(farmers, left, mid, choice, order);
        mergeSort(farmers, mid + 1, right, choice, order);
        merge(farmers, left, mid, right, choice, order);
    }
}

int main() {
    int choice, order;

    // Read inputs from Django
    cin >> choice >> order;

    vector<Farmer> farmers = {
        {"Ali Khan", "Wheat", "Punjab", 120},
        {"Ahmed Raza", "Wheat", "Sindh", 115},
        {"Sana", "Rice", "Balochistan", 150}
    };

    // Perform merge sort
    mergeSort(farmers, 0, farmers.size() - 1, choice, order);

    // Output result for Django
    for (auto &f : farmers)
        cout << f.name << "," << f.crop << "," << f.region << "," << f.price << endl;

    return 0;
}