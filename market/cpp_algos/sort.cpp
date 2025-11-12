#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

struct Farmer {
    string name;
    string crop;
    string region;
    int price;
};

int main() {
    int choice, order;

    // Read inputs from stdin (sent by Django)
    cin >> choice >> order;

    vector<Farmer> farmers = {
        {"Ali Khan", "Wheat", "Punjab", 120},
        {"Ahmed Raza", "Wheat", "Sindh", 115},
        {"Sana", "Rice", "Balochistan", 150}
    };

    auto cmp = [&](Farmer &a, Farmer &b) {
        bool res = false;
        if (choice == 1) res = a.price < b.price;
        else if (choice == 2) res = a.crop < b.crop;
        else if (choice == 3) res = a.region < b.region;
        return order == 1 ? res : !res;
    };

    sort(farmers.begin(), farmers.end(), cmp);

    for (auto &f : farmers)
        cout << f.name << "," << f.crop << "," << f.region << "," << f.price << endl;

    return 0;
}
