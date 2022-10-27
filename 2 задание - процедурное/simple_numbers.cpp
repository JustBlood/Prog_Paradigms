#include <iostream>
#include <iterator>
#include <numeric>

using namespace std;

// Сумма простых чисел от 1 до N

int* resheto(int N){
    // Реализует алгоритм отбора простых чисел - решето Эратосфена
    int* a = new int[N];
    for(int i = 0; i < N; i++){a[i]=i;}
    a[1] = 0;
    for(int i = 2; i <= N; i++){
        if(a[i]!=0){
            int j = i*i;
            while(j <= N){
                a[j] = 0;
                j += i;
            }
        }
        
    }
    return a;
}

int simpleSum(int N){
    // Вычисляет сумму элементов массива и возвращает её в виде числа
    int N;
    cout << "This program calculate sum of prime numbers from 1 to N\n";
    cout << "Enter N: ";
    cin >> N;
    int* a = resheto(N);
    long sum = 0;
    sum = accumulate(a, a+N, 0);
    return sum;
}

int main(){
    cout << "Answer: " << simpleSum() << "\n";

    system("pause");
    return 0;
}