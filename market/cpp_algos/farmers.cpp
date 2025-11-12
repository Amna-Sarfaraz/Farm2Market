#include <bits/stdc++.h>
using namespace std;

class Farmer {
public:
    string name, city, produce;
    float price;
    int quantity;

    Farmer(string n, string c, string p, float pr, int q)
        : name(n), city(c), produce(p), price(pr), quantity(q) {}
};

class Buyer {
public:
    string name, city, need;
    int quantity;

    Buyer(string n, string c, string need, int q)
        : name(n), city(c), need(need), quantity(q) {}
};

int main() {
    vector<Farmer> farmers;
    int n;
    cout << "Enter number of farmers: ";
    cin >> n;
    for (int i = 0; i < n; i++) {
        string name, city, produce;
        float price;
        int qty;
        cout << "Enter name, city, produce, price, quantity:\n";
        cin >> name >> city >> produce >> price >> qty;
        farmers.push_back(Farmer(name, city, produce, price, qty));
    }

    cout << "\n--- Farmers Added ---\n";
    for (auto &f : farmers) {
        cout << f.name << " | " << f.city << " | " << f.produce
             << " | " << f.price << " | " << f.quantity << "\n";
    }
    return 0;
}
