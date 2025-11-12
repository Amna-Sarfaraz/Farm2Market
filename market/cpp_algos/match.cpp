#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Farmer {
    string name;
    string crop;
    string region;
    float price;
};

int main() {
    string crop, region;
    float budget;

    // Read inputs from stdin (sent by Django)
    cin >> crop >> region >> budget;

    vector<Farmer> farmers = {
        {"Ali Khan", "Wheat", "Punjab", 120},
        {"Ahmed Raza", "Rice", "Sindh", 110},
        {"Sana", "Wheat", "Sindh", 115},
        {"Zara", "Rice", "Punjab", 130}
    };

    bool found = false;
    for (auto &f : farmers) {
        if (f.crop == crop && f.region == region && f.price <= budget) {
            cout << f.name << "," << f.crop << "," << f.region << "," << f.price << endl;
            found = true;
        }
    }

    if (!found)
        cout << "NoMatch" << endl;

    return 0;
}
