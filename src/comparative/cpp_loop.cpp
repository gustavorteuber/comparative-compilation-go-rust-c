#include <iostream>
#include <chrono>

int main() {
    auto start = std::chrono::high_resolution_clock::now();
    for (int i = 0; i <= 10000; ++i) {
        // Do nothing, just loop
    }
    auto finish = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = finish - start;
    std::cout << "C++ Time: " << elapsed.count() << " seconds\n";
    return 0;
}
