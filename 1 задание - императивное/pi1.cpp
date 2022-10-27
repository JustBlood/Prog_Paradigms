#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
    int N;
    long double pi=3.1415926535897932, calc_pi=sqrt(2)/2., prev = sqrt(2);
    cout << "This program calculates the number pi to a certain precision (N) after the decimal point using Viete's Series.\nEnter N not exceeding 15: ";
    cin >> N;
    if(N < 16){
        pi = round(pi*pow(10,N))/pow(10,N);
        long long i=0;
        while(bool(abs(pi - 2/calc_pi) >= double(1/pow(10,N)))){
            prev = sqrt(2+prev);
            calc_pi *= prev/2.;
            i++;

            cout << "calculated value: ";
            cout << fixed << setprecision(N+2) << 2/calc_pi - pi<< "\n";
        }  

        cout << "calculated value: ";
        cout << fixed << setprecision(N) << 2/calc_pi << "\n";
        cout << "trimmed pi: ";
        cout << fixed << setprecision(N) << pi;
        cout << "\nSum of iterations: " << i << endl;
        system("pause");
    }
    return 0;

}