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
    string keyword;
    int search_type;

    // Read inputs from stdin (sent by Django)
    cin >> keyword >> search_type;

    vector<Farmer> farmers = {
        {"Ali Khan", "Wheat", "Punjab", 120},
        {"Ahmed Raza", "Wheat", "Sindh", 115},
        {"Sana", "Rice", "Balochistan", 150},
        {"Zara", "Rice", "Punjab", 130}
    };

    bool found = false;
    for (auto &f : farmers) {
        if (f.name == keyword || f.crop == keyword || f.region == keyword) {
            cout << f.name << "," << f.crop << "," << f.region << "," << f.price << endl;
            found = true;
            if (search_type == 1) break;  // linear search stops at first match
        }
    }

    if (!found)
        cout << "NoMatch" << endl;

    return 0;
}
