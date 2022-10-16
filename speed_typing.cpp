#include <iostream>
#include <string>
using namespace std;

int main()
{
    int t{};
    cin >> t;
    for (int i = 0; i < t; i++){
        string I{};
        string P{};
        cin >> I >> P;

        int k{0};
        string S{};

        for (auto &c: P){
            if (c == I[k]){
                S += c;
                k++;
            }
        }

        if (S == I){
            cout << "Case #" << i+1 << ": " << P.size() - I.size() << endl;
        } else {
            cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
        }
    }
    return 0;
}