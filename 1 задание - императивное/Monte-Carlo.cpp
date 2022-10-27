#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <cmath>

using namespace std;

int main(){
	cout << "This program calculates the volume of the sphere according to the method Monte-Carlo \n";
	cout << "Enter the radius of sphere: ";
	int R;
	cin >> R;
	cout << "Enter the count of dots: ";
	int N;
	cin >> N;
	int n = 0;
	srand(time(0));
	for(int i = 0; i < N; i++){		
		double x = rand() % (2*R+1) - R;
		double y = rand() % (2*R+1) - R;
		double z = rand() % (2*R+1) - R;
		
		double xf = rand() % 10000 / 10000.0;
		double yf = rand() % 10000 / 10000.0;
		double zf = rand() % 10000 / 10000.0;
		
		if(x+xf < -R || x+xf > R) x -= xf; else x+=xf;
		if(y+yf < -R || y+yf > R) y -= yf; else y+=yf;
		if(z+zf < -R || z+zf > R) z -= zf; else z+=zf;
		
		if (sqrt(double(x*x+y*y+z*z)) <= R){
			n++;	
		}
	}
	long double response = double(8*R*R*R)*(n/double(N));
	long double answer = 4./3.*3.14159*R*R*R;
	
	cout << "Response: " << response << endl;
	cout << "Answer: " << answer << endl;
	cout << "Deviation: " << abs(100 - (response / (answer/100.))) << "\n";
	
	system("pause");
	return 0;
}