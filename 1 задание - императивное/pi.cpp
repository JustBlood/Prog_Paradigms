#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

int main(){
    int N;
    long double pi=3.1415926535897932384626433832795028841971693993751, calc_pi=0.;
    cout << "This program calculates the number pi to a certain precision (N) after the decimal point using Leibniz's Series.\nEnter N not exceeding 50: ";
    cin >> N;
    pi = round(pi*pow(10,N))/pow(10,N);
    int i=0, j=1;
    while(bool(double(abs(pi - calc_pi)) >= double(1/pow(10,N+1)))){
        if(i%2==0){
            calc_pi += 4/double(j);
        }
        else{
            calc_pi -= 4/double(j);
        }
        i+=1;
        j+=2;
    }  

    cout << "calculated value: ";
    cout << fixed << setprecision(N) << calc_pi << "\n";
    cout << "right value: ";
    cout << fixed << setprecision(N) << pi;
    system("pause");
    return 0;

}