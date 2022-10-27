#include <iostream>
#include <cmath>
using namespace std;

double Simpson(double a, double b, int N, double func(double x)){
	double s = 0.0;
	double h = (b-a)/N;
	s+=func(a) + func(b);
	for(int i = 1; i < N; i++){
		if(i%2 == 0){
			s += 4 * func(a + i*h);
		}
		else{
			s += 2 * func(a + double(i)*h);
		}
	}
	return s*h/3.0;
}
	
	
int main(){
	
	double a, b;
	int n;
    cout << "This program calculate integral of function sin(x), cos(x), x^3, using Simpson method\n";
    cout << "Enter 3 numbers: from, to, amount of dots\n";
	cin >> a >> b >> n;

	cout << Simpson(a,b,n, sin) << "\n";
	cout << Simpson(a,b,n, cos) << "\n";
	cout << Simpson(a,b,n, [](double x){return x*x*x;});

	system("pause");
	
}